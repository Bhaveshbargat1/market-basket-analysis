# 🛒 Market Basket Analysis & Association Rule Mining

An end-to-end data mining and market basket analysis framework implementing **Apriori** and **FP-Growth** algorithms to uncover customer purchase patterns, calculate association metrics (Support, Confidence, Lift), and serve interactive product recommendations.

---

## 📌 Project Overview

Market Basket Analysis is a key data mining technique used by retailers to understand customer purchasing behaviors. By analyzing co-occurrence patterns in transaction datasets, businesses can optimize product placement, bundle cross-selling items, and drive recommendation engines.

This repository features:
- **Data Preprocessing & Matrix Transformation**: Converts transactional logs into sparse boolean customer baskets.
- **Algorithm Benchmarking**: Compares runtime performance of **Apriori** vs **FP-Growth** across varying minimum support thresholds.
- **Association Rule Extraction**: Extracts high-confidence, actionable rules using Support, Confidence, and Lift.
- **Interactive CLI Query Interface**: Run `query.py` to query what items customers frequently buy together.

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Data Mining & Rules:** `mlxtend` (Apriori, FP-Growth, association_rules)
- **Data Manipulation:** `pandas`, `numpy`, `pyarrow`
- **Visualization:** `matplotlib`, `seaborn`

---

## 📁 Repository Structure

```
market-basket-analysis/
├── config.py                 # Configuration parameters & file paths
├── main.py                   # Main pipeline runner (preprocessing -> mining -> rules -> benchmarking)
├── query.py                  # Interactive CLI to query recommendations for items
├── requirements.txt          # Python dependencies
├── outputs/
│   ├── figures/
│   │   └── benchmark_comparison.png # Apriori vs FP-Growth runtime benchmark
│   └── rules_summary.csv     # Extracted association rules
├── src/
│   ├── __init__.py
│   ├── data_loader.py        # Transaction cleaning and basket matrix generation
│   ├── mining.py             # Apriori & FP-Growth mining and timing benchmarks
│   ├── rules.py              # Association rule mining (support, confidence, lift)
│   └── visualization.py      # Benchmark plotting and support sweep
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Bhaveshbargat1/market-basket-analysis.git
cd market-basket-analysis
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Pipeline
Place your dataset at `data/raw/online_retail.csv` (e.g. from the UCI Machine Learning Repository Online Retail dataset) and run:
```bash
python main.py
```

### 5. Interactive Recommendation Query
Query product recommendations directly in the terminal:
```bash
python query.py
```

---

## 👨‍💻 Author

**Bhavesh Bargat**  
GitHub: [@Bhaveshbargat1](https://github.com/Bhaveshbargat1)
