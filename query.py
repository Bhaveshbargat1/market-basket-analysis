import pandas as pd
import config

def parse_itemset(itemset_str):
    """Converts frozenset string representations into clean Python sets."""
    if pd.isna(itemset_str):
        return set()
    cleaned = (
        str(itemset_str)
        .replace("frozenset(", "")
        .replace(")", "")
        .replace("{", "")
        .replace("}", "")
        .replace("'", "")
        .replace('"', "")
    )
    return {item.strip().lower() for item in cleaned.split(",") if item.strip()}

def main():
    print("--- Market Basket Query Interface ---")
    
    try:
        rules = pd.read_csv(config.OUTPUT_RULES_PATH)
    except FileNotFoundError:
        print(f"Error: Could not find {config.OUTPUT_RULES_PATH}. Please run 'python main.py' first!")
        return

    # Parse antecedents and consequents into clean sets of lowercase items
    rules['antecedent_set'] = rules['antecedents'].apply(parse_itemset)
    rules['consequent_set'] = rules['consequents'].apply(parse_itemset)

    while True:
        item = input("\nEnter product name to query (or type 'exit' to quit): ").strip().lower()
        if item == 'exit':
            break

        # Filter rules where the item is in the antecedents
        mask = rules['antecedent_set'].apply(lambda x: item in x)
        results = rules[mask]

        if not results.empty:
            print(f"\n🛒 Product Recommendations (If customer buys -> They also buy):")
            display_df = results[['antecedents', 'consequents', 'support', 'confidence', 'lift']].copy()
            # Clean up display text for readability
            display_df['antecedents'] = results['antecedent_set'].apply(lambda x: ', '.join(x).title())
            display_df['consequents'] = results['consequent_set'].apply(lambda x: ', '.join(x).title())
            print(display_df.to_string(index=False))
        else:
            print(f"\nNo rules found where '{item.title()}' is the antecedent.")
            
            # Show available items in the dataset to help the user
            all_antecedents = set().union(*rules['antecedent_set'])
            print(f"Available items you can query: {', '.join([i.title() for i in all_antecedents])}")

if __name__ == "__main__":
    main()