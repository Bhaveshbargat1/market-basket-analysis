import pandas as pd
from mlxtend.frequent_patterns import association_rules

def generate_strong_rules(frequent_itemsets: pd.DataFrame, min_confidence: float, min_lift: float) -> pd.DataFrame:
    """Derives association rules filtered by confidence and lift."""
    if frequent_itemsets.empty:
        return pd.DataFrame()
        
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)
    strong_rules = rules[rules['lift'] >= min_lift].sort_values(by='lift', ascending=False)
    return strong_rules

def query_rules_by_item(rules_df: pd.DataFrame, item_name: str, search_type: str = 'antecedent') -> pd.DataFrame:
    """
    Searches generated rules for a specific product item.
    
    Parameters:
    - rules_df: DataFrame containing the association rules.
    - item_name: Name of the product to query (e.g., 'Bread', 'Milk').
    - search_type: 
        * 'antecedent' -> Find what people buy IF they buy item_name (X => Y)
        * 'consequent' -> Find what leads people to buy item_name (Y => X)
        * 'either'     -> Find rules containing item_name anywhere
    """
    if rules_df.empty:
        print("No rules provided or rules DataFrame is empty.")
        return pd.DataFrame()

    def contains_item(itemset):
        # Convert frozenset or string representation to clean string list
        if isinstance(itemset, (set, frozenset)):
            items = [str(i).lower() for i in itemset]
        elif isinstance(itemset, str):
            items = [i.strip().lower() for i in itemset.replace("frozenset", "").replace("{", "").replace("}", "").replace("'", "").split(",")]
        else:
            return False
        return item_name.lower() in items

    if search_type == 'antecedent':
        mask = rules_df['antecedents'].apply(contains_item)
    elif search_type == 'consequent':
        mask = rules_df['consequents'].apply(contains_item)
    else:
        mask = rules_df['antecedents'].apply(contains_item) | rules_df['consequents'].apply(contains_item)

    return rules_df[mask][['antecedents', 'consequents', 'support', 'confidence', 'lift']]