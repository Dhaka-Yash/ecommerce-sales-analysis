"""
Data Analysis Functions
Core analysis functions for sales data
"""

import pandas as pd
import numpy as np

def calculate_kpis(df):
    """
    Calculate Key Performance Indicators (KPIs)
    
    Parameters:
    -----------
    df : pd.DataFrame
        Sales data
    
    Returns:
    --------
    dict: Dictionary of KPIs
    """
    kpis = {
        'Total_Revenue': df['Total_Amount'].sum(),
        'Total_Orders': len(df),
        'Average_Order_Value': df['Total_Amount'].mean(),
        'Total_Quantity_Sold': df['Quantity'].sum(),
        'Average_Quantity_per_Order': df['Quantity'].mean(),
        'Total_Discount_Given': df['Discount'].sum(),
        'Discount_Rate': (df['Discount'].sum() / df['Total_Amount'].sum()) * 100 if df['Total_Amount'].sum() > 0 else 0,
        'Unique_Customers': df['Customer_ID'].nunique(),
        'Unique_Products': df['Product_Name'].nunique(),
        'Unique_Categories': df['Category'].nunique()
    }
    
    return kpis

def print_kpis(kpis):
    """Print KPIs in a formatted way"""
    print("\n" + "=" * 60)
    print("KEY PERFORMANCE INDICATORS (KPIs)")
    print("=" * 60)
    print(f"\n[REVENUE] Total Revenue: ${kpis['Total_Revenue']:,.2f}")
    print(f"[ORDERS] Total Orders: {kpis['Total_Orders']:,}")
    print(f"[AOV] Average Order Value: ${kpis['Average_Order_Value']:,.2f}")
    print(f"[QUANTITY] Total Quantity Sold: {kpis['Total_Quantity_Sold']:,} units")
    print(f"[AVG QTY] Average Quantity per Order: {kpis['Average_Quantity_per_Order']:.2f} units")
    print(f"[DISCOUNT] Total Discount Given: ${kpis['Total_Discount_Given']:,.2f}")
    print(f"[DISCOUNT %] Discount Rate: {kpis['Discount_Rate']:.2f}%")
    print(f"[CUSTOMERS] Unique Customers: {kpis['Unique_Customers']:,}")
    print(f"[PRODUCTS] Unique Products: {kpis['Unique_Products']:,}")
    print(f"[CATEGORIES] Unique Categories: {kpis['Unique_Categories']:,}")

def analyze_by_category(df):
    """
    Analyze sales by product category
    
    Parameters:
    -----------
    df : pd.DataFrame
        Sales data
    
    Returns:
    --------
    pd.DataFrame: Category analysis
    """
    category_analysis = df.groupby('Category').agg({
        'Total_Amount': ['sum', 'mean', 'count'],
        'Quantity': 'sum'
    }).round(2)
    
    category_analysis.columns = ['Total_Revenue', 'Avg_Order_Value', 'Order_Count', 'Total_Quantity']
    category_analysis = category_analysis.sort_values('Total_Revenue', ascending=False)
    category_analysis['Revenue_Share_%'] = (category_analysis['Total_Revenue'] / 
                                            category_analysis['Total_Revenue'].sum() * 100).round(2)
    
    return category_analysis

def analyze_by_region(df):
    """
    Analyze sales by region
    
    Parameters:
    -----------
    df : pd.DataFrame
        Sales data
    
    Returns:
    --------
    pd.DataFrame: Region analysis
    """
    region_analysis = df.groupby('Region').agg({
        'Total_Amount': ['sum', 'mean', 'count'],
        'Quantity': 'sum'
    }).round(2)
    
    region_analysis.columns = ['Total_Revenue', 'Avg_Order_Value', 'Order_Count', 'Total_Quantity']
    region_analysis = region_analysis.sort_values('Total_Revenue', ascending=False)
    region_analysis['Revenue_Share_%'] = (region_analysis['Total_Revenue'] / 
                                          region_analysis['Total_Revenue'].sum() * 100).round(2)
    
    return region_analysis

def analyze_by_time(df):
    """
    Analyze sales trends over time
    
    Parameters:
    -----------
    df : pd.DataFrame
        Sales data
    
    Returns:
    --------
    dict: Dictionary with monthly, quarterly, and yearly analysis
    """
    time_analysis = {}
    
    # Monthly analysis
    monthly = df.groupby(['Year', 'Month']).agg({
        'Total_Amount': ['sum', 'count'],
        'Quantity': 'sum'
    }).round(2)
    monthly.columns = ['Revenue', 'Orders', 'Quantity']
    time_analysis['monthly'] = monthly
    
    # Quarterly analysis
    quarterly = df.groupby(['Year', 'Quarter']).agg({
        'Total_Amount': ['sum', 'count'],
        'Quantity': 'sum'
    }).round(2)
    quarterly.columns = ['Revenue', 'Orders', 'Quantity']
    time_analysis['quarterly'] = quarterly
    
    # Yearly analysis
    yearly = df.groupby('Year').agg({
        'Total_Amount': ['sum', 'count'],
        'Quantity': 'sum'
    }).round(2)
    yearly.columns = ['Revenue', 'Orders', 'Quantity']
    time_analysis['yearly'] = yearly
    
    return time_analysis

def analyze_top_products(df, top_n=10):
    """
    Analyze top performing products
    
    Parameters:
    -----------
    df : pd.DataFrame
        Sales data
    top_n : int
        Number of top products to return
    
    Returns:
    --------
    pd.DataFrame: Top products analysis
    """
    top_products = df.groupby(['Product_Name', 'Category']).agg({
        'Total_Amount': ['sum', 'count'],
        'Quantity': 'sum',
        'Unit_Price': 'mean'
    }).round(2)
    
    top_products.columns = ['Total_Revenue', 'Order_Count', 'Total_Quantity', 'Avg_Price']
    top_products = top_products.sort_values('Total_Revenue', ascending=False).head(top_n)
    
    return top_products

def analyze_customer_demographics(df):
    """
    Analyze customer demographics
    
    Parameters:
    -----------
    df : pd.DataFrame
        Sales data
    
    Returns:
    --------
    pd.DataFrame: Customer demographics analysis
    """
    demo_analysis = df.groupby('Customer_Age_Group').agg({
        'Customer_ID': 'nunique',
        'Total_Amount': ['sum', 'mean'],
        'Order_ID': 'count'
    }).round(2)
    
    demo_analysis.columns = ['Unique_Customers', 'Total_Revenue', 'Avg_Order_Value', 'Total_Orders']
    demo_analysis = demo_analysis.sort_values('Total_Revenue', ascending=False)
    
    return demo_analysis

def analyze_payment_methods(df):
    """
    Analyze payment method preferences
    
    Parameters:
    -----------
    df : pd.DataFrame
        Sales data
    
    Returns:
    --------
    pd.DataFrame: Payment method analysis
    """
    payment_analysis = df.groupby('Payment_Method').agg({
        'Total_Amount': ['sum', 'count'],
        'Order_ID': 'count'
    }).round(2)
    
    payment_analysis.columns = ['Total_Revenue', 'Transaction_Count', 'Order_Count']
    payment_analysis = payment_analysis.sort_values('Total_Revenue', ascending=False)
    payment_analysis['Usage_%'] = (payment_analysis['Order_Count'] / 
                                   payment_analysis['Order_Count'].sum() * 100).round(2)
    
    return payment_analysis
