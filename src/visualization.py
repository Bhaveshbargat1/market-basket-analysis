import os
import time
import matplotlib.pyplot as plt
import pandas as pd
from mlxtend.frequent_patterns import apriori, fpgrowth

def run_support_sweep(basket_matrix: pd.DataFrame, support_levels: list, output_plot_path: str):
    """Executes Apriori and FP-Growth across multiple support levels and plots performance."""
    apriori_times = []
    fpgrowth_times = []

    print("\n--- Running Benchmark Sweep ---")
    for supp in support_levels:
        # Measure Apriori
        t0 = time.perf_counter()
        apriori(basket_matrix, min_support=supp, use_colnames=True)
        t_apriori = time.perf_counter() - t0
        apriori_times.append(t_apriori)

        # Measure FP-Growth
        t0 = time.perf_counter()
        fpgrowth(basket_matrix, min_support=supp, use_colnames=True)
        t_fpgrowth = time.perf_counter() - t0
        fpgrowth_times.append(t_fpgrowth)

        print(f"Support Threshold: {supp:.2f} | Apriori: {t_apriori:.4f}s | FP-Growth: {t_fpgrowth:.4f}s")

    # Plot results
    plt.figure(figsize=(8, 5))
    plt.plot(support_levels, apriori_times, label='Apriori', marker='o', color='crimson', linewidth=2)
    plt.plot(support_levels, fpgrowth_times, label='FP-Growth', marker='s', color='forestgreen', linewidth=2)
    
    plt.xlabel('Minimum Support Threshold')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Algorithm Scalability: Apriori vs FP-Growth')
    plt.gca().invert_xaxis()  # Lower support thresholds require more computation
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    
    os.makedirs(os.path.dirname(output_plot_path), exist_ok=True)
    plt.savefig(output_plot_path, dpi=300)
    plt.close()
    print(f"\nBenchmark chart saved to: {output_plot_path}")