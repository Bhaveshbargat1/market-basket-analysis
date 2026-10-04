import pandas as pd

def load_and_clean_data(file_path: str) -> pd.DataFrame:
    """Loads raw retail data and cleans invalid or cancelled transactions."""
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    
    # Clean descriptions and remove missing values or cancelled orders (starting with 'C')
    df['Description'] = df['Description'].astype(str).str.strip()
    df.dropna(subset=['InvoiceNo', 'Description'], inplace=True)
    df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
    df = df[df['Quantity'] > 0]
    
    return df

def create_basket_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """Transforms raw transaction log into a boolean basket matrix."""
    basket = (df.groupby(['InvoiceNo', 'Description'])['Quantity']
              .sum().unstack().reset_index().fillna(0)
              .set_index('InvoiceNo'))
    
    # Cast directly to bool to fix the mlxtend deprecation warnings
    basket_encoded = (basket > 0).astype(bool)
    return basket_encoded