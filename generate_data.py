"""
Data Generation Script
Generates synthetic e-commerce sales data for analysis
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def generate_sales_data(n_records=5000, start_date='2023-01-01', end_date='2024-12-31'):
    """
    Generate synthetic e-commerce sales data
    
    Parameters:
    -----------
    n_records : int
        Number of sales records to generate
    start_date : str
        Start date for sales period
    end_date : str
        End date for sales period
    
    Returns:
    --------
    pd.DataFrame: Generated sales data
    """
    np.random.seed(42)  # For reproducibility
    
    # Date range
    start = pd.to_datetime(start_date)
    end = pd.to_datetime(end_date)
    date_range = (end - start).days
    
    # Product categories and names
    categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Sports', 
                  'Beauty', 'Toys', 'Food & Beverages']
    
    products = {
        'Electronics': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Smartwatch', 
                       'Camera', 'Speaker', 'Monitor'],
        'Clothing': ['T-Shirt', 'Jeans', 'Dress', 'Jacket', 'Shoes', 'Hat', 
                     'Sweater', 'Shorts'],
        'Home & Kitchen': ['Coffee Maker', 'Blender', 'Cookware Set', 'Dinnerware', 
                          'Bedding', 'Lamp', 'Rug', 'Storage'],
        'Books': ['Fiction', 'Non-Fiction', 'Mystery', 'Romance', 'Sci-Fi', 
                  'Biography', 'Self-Help', 'Cookbook'],
        'Sports': ['Yoga Mat', 'Dumbbells', 'Running Shoes', 'Bicycle', 'Tennis Racket',
                   'Basketball', 'Gym Bag', 'Water Bottle'],
        'Beauty': ['Skincare Set', 'Makeup Palette', 'Perfume', 'Shampoo', 
                   'Face Mask', 'Lipstick', 'Sunscreen', 'Hairbrush'],
        'Toys': ['Action Figure', 'Board Game', 'Puzzle', 'Doll', 'Building Blocks',
                'Remote Car', 'Educational Toy', 'Stuffed Animal'],
        'Food & Beverages': ['Coffee', 'Tea', 'Snacks', 'Chocolate', 'Wine', 
                            'Juice', 'Cereal', 'Protein Bar']
    }
    
    # Regions
    regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Oceania']
    
    # Payment methods
    payment_methods = ['Credit Card', 'Debit Card', 'PayPal', 'Cash on Delivery', 'Bank Transfer']
    
    # Customer age groups
    age_groups = ['18-25', '26-35', '36-45', '46-55', '56+']
    
    # Generate data
    data = []
    
    for i in range(n_records):
        # Random date within range
        days_offset = np.random.randint(0, date_range)
        order_date = start + timedelta(days=days_offset)
        
        # Select category and product
        category = np.random.choice(categories)
        product = np.random.choice(products[category])
        
        # Generate prices (with some variation)
        base_prices = {
            'Electronics': (200, 1500),
            'Clothing': (20, 150),
            'Home & Kitchen': (30, 300),
            'Books': (10, 50),
            'Sports': (25, 500),
            'Beauty': (15, 100),
            'Toys': (10, 80),
            'Food & Beverages': (5, 50)
        }
        min_price, max_price = base_prices[category]
        unit_price = round(np.random.uniform(min_price, max_price), 2)
        
        # Quantity (most orders are 1-3 items, occasional bulk)
        quantity = np.random.choice([1, 2, 3, 4, 5], p=[0.5, 0.25, 0.15, 0.07, 0.03])
        
        # Calculate total
        total_amount = round(unit_price * quantity, 2)
        
        # Add some discounts (10% of orders)
        if np.random.random() < 0.1:
            discount = round(total_amount * np.random.uniform(0.05, 0.25), 2)
            total_amount = round(total_amount - discount, 2)
        else:
            discount = 0
        
        # Other fields
        region = np.random.choice(regions)
        payment_method = np.random.choice(payment_methods)
        age_group = np.random.choice(age_groups)
        
        # Customer ID
        customer_id = f"CUST{np.random.randint(1000, 9999)}"
        
        # Order ID
        order_id = f"ORD{order_date.strftime('%Y%m%d')}{np.random.randint(1000, 9999)}"
        
        data.append({
            'Order_ID': order_id,
            'Order_Date': order_date,
            'Customer_ID': customer_id,
            'Product_Name': product,
            'Category': category,
            'Quantity': quantity,
            'Unit_Price': unit_price,
            'Total_Amount': total_amount,
            'Discount': discount,
            'Region': region,
            'Payment_Method': payment_method,
            'Customer_Age_Group': age_group
        })
    
    df = pd.DataFrame(data)
    
    # Add some missing values (realistic scenario)
    missing_indices = np.random.choice(df.index, size=int(n_records * 0.02), replace=False)
    df.loc[missing_indices, 'Customer_Age_Group'] = np.nan
    
    return df

def main():
    """Main function to generate and save data"""
    print("Generating synthetic e-commerce sales data...")
    
    # Create directories if they don't exist
    os.makedirs('data/raw', exist_ok=True)
    os.makedirs('data/processed', exist_ok=True)
    
    # Generate data
    df = generate_sales_data(n_records=5000)
    
    # Save to CSV
    output_path = 'data/raw/sales_data.csv'
    df.to_csv(output_path, index=False)
    
    print(f"[OK] Generated {len(df)} records")
    print(f"[OK] Data saved to {output_path}")
    print(f"\nData Summary:")
    print(f"  - Date Range: {df['Order_Date'].min()} to {df['Order_Date'].max()}")
    print(f"  - Total Revenue: ${df['Total_Amount'].sum():,.2f}")
    print(f"  - Categories: {df['Category'].nunique()}")
    print(f"  - Unique Products: {df['Product_Name'].nunique()}")
    print(f"  - Regions: {df['Region'].nunique()}")
    
    return df

if __name__ == "__main__":
    main()
