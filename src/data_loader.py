"""
Data Loading Utilities
Functions to load and inspect data
"""

import pandas as pd
import os

def load_sales_data(file_path='data/raw/sales_data.csv'):
    """
    Load sales data from CSV file
    
    Parameters:
    -----------
    file_path : str
        Path to the CSV file
    
    Returns:
    --------
    pd.DataFrame: Loaded sales data
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Data file not found at {file_path}. "
            "Please run 'python generate_data.py' first to generate sample data."
        )
    
    df = pd.read_csv(file_path, parse_dates=['Order_Date'])
    return df

def get_data_info(df):
    """
    Display basic information about the dataset
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame to analyze
    """
    print("=" * 60)
    print("DATASET INFORMATION")
    print("=" * 60)
    print(f"\nShape: {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"\nColumn Names:")
    for i, col in enumerate(df.columns, 1):
        print(f"  {i}. {col}")
    
    print(f"\nData Types:")
    print(df.dtypes)
    
    print(f"\nMissing Values:")
    missing = df.isnull().sum()
    if missing.sum() > 0:
        print(missing[missing > 0])
    else:
        print("  No missing values found")
    
    print(f"\nBasic Statistics:")
    print(df.describe())
    
    return df.info()
