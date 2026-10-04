# config.py
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "online_retail.csv")
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "basket_matrix.parquet")
OUTPUT_RULES_PATH = os.path.join(BASE_DIR, "outputs", "rules_summary.csv")
OUTPUT_BENCHMARK_PLOT = os.path.join(BASE_DIR, "outputs", "figures", "benchmark_comparison.png")

# Lower thresholds for tiny sample data
MIN_SUPPORT = 0.2
MIN_CONFIDENCE = 0.3
MIN_LIFT = 1.0