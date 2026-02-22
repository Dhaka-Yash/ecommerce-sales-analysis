"""
Data Cleaning Utilities
Functions to clean and preprocess data
"""

import pandas as pd
import numpy as np

def clean_sales_data(df):
    """
    Clean and preprocess sales data
    
    Parameters:
    -----------
    df : pd.DataFrame
        Raw sales data
    
    Returns:
    --------
    pd.DataFrame: Cleaned sales data
    """
    df_clean = df.copy()
    
    print("=" * 60)
    print("DATA CLEANING PROCESS")
    print("=" * 60)
    
    # 1. Handle missing values
    print("\n1. Handling missing values...")
    initial_missing = df_clean.isnull().sum().sum()
    if initial_missing > 0:
        # Fill missing age groups with 'Unknown'
        df_clean = df_clean.copy()
        df_clean['Customer_Age_Group'] = df_clean['Customer_Age_Group'].fillna('Unknown')
        print(f"   [OK] Filled {initial_missing} missing values")
    else:
        print("   [OK] No missing values found")
    
    # 2. Remove duplicates
    print("\n2. Checking for duplicates...")
    duplicates = df_clean.duplicated().sum()
    if duplicates > 0:
        df_clean = df_clean.drop_duplicates()
        print(f"   [OK] Removed {duplicates} duplicate records")
    else:
        print("   [OK] No duplicates found")
    
    # 3. Handle outliers in Total_Amount
    print("\n3. Handling outliers...")
    Q1 = df_clean['Total_Amount'].quantile(0.25)
    Q3 = df_clean['Total_Amount'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = ((df_clean['Total_Amount'] < lower_bound) | 
                (df_clean['Total_Amount'] > upper_bound)).sum()
    
    if outliers > 0:
        # Cap outliers instead of removing (preserve data)
        df_clean.loc[df_clean['Total_Amount'] < lower_bound, 'Total_Amount'] = lower_bound
        df_clean.loc[df_clean['Total_Amount'] > upper_bound, 'Total_Amount'] = upper_bound
        print(f"   [OK] Capped {outliers} outliers")
    else:
        print("   [OK] No significant outliers found")
    
    # 4. Ensure data types are correct
    print("\n4. Ensuring correct data types...")
    df_clean['Order_Date'] = pd.to_datetime(df_clean['Order_Date'])
    df_clean['Quantity'] = df_clean['Quantity'].astype(int)
    print("   [OK] Data types verified")
    
    # 5. Add derived columns
    print("\n5. Adding derived columns...")
    df_clean['Year'] = df_clean['Order_Date'].dt.year
    df_clean['Month'] = df_clean['Order_Date'].dt.month
    df_clean['Month_Name'] = df_clean['Order_Date'].dt.strftime('%B')
    df_clean['Quarter'] = df_clean['Order_Date'].dt.quarter
    df_clean['Day_of_Week'] = df_clean['Order_Date'].dt.day_name()
    df_clean['Revenue_After_Discount'] = df_clean['Total_Amount'] - df_clean['Discount']
    print("   [OK] Added Year, Month, Quarter, Day_of_Week, Revenue_After_Discount")
    
    print("\n" + "=" * 60)
    print("DATA CLEANING COMPLETE")
    print("=" * 60)
    print(f"\nFinal Dataset Shape: {df_clean.shape[0]} rows × {df_clean.shape[1]} columns")
    
    return df_clean

def save_cleaned_data(df, output_path='data/processed/sales_data_cleaned.csv'):
    """
    Save cleaned data to CSV
    
    Parameters:
    -----------
    df : pd.DataFrame
        Cleaned data
    output_path : str
        Output file path
    """
    import os
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"\n[OK] Cleaned data saved to {output_path}")
