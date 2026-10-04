import config
from src.data_loader import load_and_clean_data, create_basket_matrix
from src.mining import run_benchmarks
from src.rules import generate_strong_rules
from src.visualization import run_support_sweep

def main():
    print("1. Loading and cleaning data...")
    df = load_and_clean_data(config.RAW_DATA_PATH)
    
    print("2. Generating Basket Matrix...")
    basket = create_basket_matrix(df)
    print(f"   Matrix created: {basket.shape[0]} transactions, {basket.shape[1]} unique items.")
    
    print(f"\n3. Running Baseline Algorithms (min_support = {config.MIN_SUPPORT})...")
    apriori_res, fpgrowth_res, metrics = run_benchmarks(basket, config.MIN_SUPPORT)
    print(f"   -> Apriori Execution Time:   {metrics['Apriori Runtime (s)']:.4f} seconds")
    print(f"   -> FP-Growth Execution Time: {metrics['FP-Growth Runtime (s)']:.4f} seconds")
    
    print("\n4. Extracting High-Confidence Rules...")
    rules = generate_strong_rules(fpgrowth_res, config.MIN_CONFIDENCE, config.MIN_LIFT)
    rules.to_csv(config.OUTPUT_RULES_PATH, index=False)
    print(f"   -> Saved {len(rules)} association rules to {config.OUTPUT_RULES_PATH}")

    # Step 5: Benchmark sweep across varying support levels
    support_thresholds = [0.4, 0.3, 0.2]
    run_support_sweep(basket, support_thresholds, config.OUTPUT_BENCHMARK_PLOT)

if __name__ == "__main__":
    main()