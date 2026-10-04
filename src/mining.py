import time
import pandas as pd
from mlxtend.frequent_patterns import apriori, fpgrowth

def run_benchmarks(basket_matrix: pd.DataFrame, min_support: float):
    """Runs both algorithms and captures execution time metrics."""
    
    # Apriori Execution
    t0 = time.perf_counter()
    apriori_frequent = apriori(basket_matrix, min_support=min_support, use_colnames=True)
    apriori_time = time.perf_counter() - t0
    
    # FP-Growth Execution
    t0 = time.perf_counter()
    fpgrowth_frequent = fpgrowth(basket_matrix, min_support=min_support, use_colnames=True)
    fpgrowth_time = time.perf_counter() - t0
    
    metrics = {
        'Apriori Runtime (s)': apriori_time,
        'FP-Growth Runtime (s)': fpgrowth_time
    }
    
    return apriori_frequent, fpgrowth_frequent, metrics