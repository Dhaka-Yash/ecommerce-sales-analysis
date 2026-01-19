"""
Data Visualization Functions
Create charts and visualizations for sales data
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

def create_output_dir():
    """Create output directory for visualizations"""
    os.makedirs('reports/visualizations', exist_ok=True)

def plot_sales_trend(df, save=True):
    """
    Plot sales trend over time
    
    Parameters:
    -----------
    df : pd.DataFrame
        Sales data
    save : bool
        Whether to save the plot
    """
    create_output_dir()
    
    # Monthly sales trend
    monthly_sales = df.groupby(['Year', 'Month'])['Total_Amount'].sum().reset_index()
    monthly_sales['Date'] = pd.to_datetime(monthly_sales[['Year', 'Month']].assign(DAY=1))
    
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(monthly_sales['Date'], monthly_sales['Total_Amount'], 
            marker='o', linewidth=2, markersize=8, color='#2E86AB')
    ax.set_title('Monthly Sales Trend', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Revenue ($)', fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.tick_params(axis='x', rotation=45)
    
    # Format y-axis as currency
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    
    plt.tight_layout()
    
    if save:
        plt.savefig('reports/visualizations/sales_trend.png', dpi=300, bbox_inches='tight')
        print("[OK] Saved: reports/visualizations/sales_trend.png")
    
    plt.show()

def plot_category_analysis(df, save=True):
    """
    Plot category performance analysis
    
    Parameters:
    -----------
    df : pd.DataFrame
        Sales data
    save : bool
        Whether to save the plot
    """
    create_output_dir()
    
    category_revenue = df.groupby('Category')['Total_Amount'].sum().sort_values(ascending=False)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Bar chart
    colors = sns.color_palette("husl", len(category_revenue))
    bars = ax1.bar(range(len(category_revenue)), category_revenue.values, color=colors)
    ax1.set_xticks(range(len(category_revenue)))
    ax1.set_xticklabels(category_revenue.index, rotation=45, ha='right')
    ax1.set_title('Revenue by Category', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Revenue ($)', fontsize=12)
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars
    for i, bar in enumerate(bars):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'${height:,.0f}',
                ha='center', va='bottom', fontsize=9)
    
    # Pie chart
    ax2.pie(category_revenue.values, labels=category_revenue.index, autopct='%1.1f%%',
           startangle=90, colors=colors)
    ax2.set_title('Revenue Share by Category', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    
    if save:
        plt.savefig('reports/visualizations/category_analysis.png', dpi=300, bbox_inches='tight')
        print("[OK] Saved: reports/visualizations/category_analysis.png")
    
    plt.show()

def plot_region_analysis(df, save=True):
    """
    Plot regional sales analysis
    
    Parameters:
    -----------
    df : pd.DataFrame
        Sales data
    save : bool
        Whether to save the plot
    """
    create_output_dir()
    
    region_revenue = df.groupby('Region')['Total_Amount'].sum().sort_values(ascending=False)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    colors = sns.color_palette("muted", len(region_revenue))
    bars = ax.barh(range(len(region_revenue)), region_revenue.values, color=colors)
    ax.set_yticks(range(len(region_revenue)))
    ax.set_yticklabels(region_revenue.index)
    ax.set_title('Revenue by Region', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Revenue ($)', fontsize=12)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    ax.grid(True, alpha=0.3, axis='x')
    
    # Add value labels
    for i, bar in enumerate(bars):
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height()/2.,
               f'${width:,.0f}',
               ha='left', va='center', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    
    if save:
        plt.savefig('reports/visualizations/region_analysis.png', dpi=300, bbox_inches='tight')
        print("[OK] Saved: reports/visualizations/region_analysis.png")
    
    plt.show()

def plot_top_products(df, top_n=10, save=True):
    """
    Plot top performing products
    
    Parameters:
    -----------
    df : pd.DataFrame
        Sales data
    top_n : int
        Number of top products to show
    save : bool
        Whether to save the plot
    """
    create_output_dir()
    
    top_products = df.groupby('Product_Name')['Total_Amount'].sum().sort_values(ascending=False).head(top_n)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    colors = sns.color_palette("viridis", len(top_products))
    bars = ax.barh(range(len(top_products)), top_products.values, color=colors)
    ax.set_yticks(range(len(top_products)))
    ax.set_yticklabels(top_products.index)
    ax.set_title(f'Top {top_n} Products by Revenue', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('Revenue ($)', fontsize=12)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    ax.grid(True, alpha=0.3, axis='x')
    
    # Add value labels
    for i, bar in enumerate(bars):
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height()/2.,
               f'${width:,.0f}',
               ha='left', va='center', fontsize=9, fontweight='bold')
    
    plt.tight_layout()
    
    if save:
        plt.savefig('reports/visualizations/top_products.png', dpi=300, bbox_inches='tight')
        print("[OK] Saved: reports/visualizations/top_products.png")
    
    plt.show()

def plot_customer_demographics(df, save=True):
    """
    Plot customer demographics analysis
    
    Parameters:
    -----------
    df : pd.DataFrame
        Sales data
    save : bool
        Whether to save the plot
    """
    create_output_dir()
    
    demo_data = df.groupby('Customer_Age_Group').agg({
        'Total_Amount': 'sum',
        'Customer_ID': 'nunique'
    }).reset_index()
    demo_data.columns = ['Age_Group', 'Revenue', 'Customers']
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Revenue by age group
    colors1 = sns.color_palette("coolwarm", len(demo_data))
    bars1 = ax1.bar(demo_data['Age_Group'], demo_data['Revenue'], color=colors1)
    ax1.set_title('Revenue by Customer Age Group', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Age Group', fontsize=12)
    ax1.set_ylabel('Revenue ($)', fontsize=12)
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    ax1.grid(True, alpha=0.3, axis='y')
    ax1.tick_params(axis='x', rotation=45)
    
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'${height:,.0f}',
                ha='center', va='bottom', fontsize=9)
    
    # Customer count by age group
    colors2 = sns.color_palette("Set2", len(demo_data))
    bars2 = ax2.bar(demo_data['Age_Group'], demo_data['Customers'], color=colors2)
    ax2.set_title('Customer Count by Age Group', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Age Group', fontsize=12)
    ax2.set_ylabel('Number of Customers', fontsize=12)
    ax2.grid(True, alpha=0.3, axis='y')
    ax2.tick_params(axis='x', rotation=45)
    
    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    
    if save:
        plt.savefig('reports/visualizations/customer_demographics.png', dpi=300, bbox_inches='tight')
        print("[OK] Saved: reports/visualizations/customer_demographics.png")
    
    plt.show()

def plot_payment_methods(df, save=True):
    """
    Plot payment method analysis
    
    Parameters:
    -----------
    df : pd.DataFrame
        Sales data
    save : bool
        Whether to save the plot
    """
    create_output_dir()
    
    payment_data = df.groupby('Payment_Method')['Total_Amount'].sum().sort_values(ascending=False)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = sns.color_palette("pastel", len(payment_data))
    bars = ax.bar(range(len(payment_data)), payment_data.values, color=colors)
    ax.set_xticks(range(len(payment_data)))
    ax.set_xticklabels(payment_data.index, rotation=45, ha='right')
    ax.set_title('Revenue by Payment Method', fontsize=16, fontweight='bold', pad=20)
    ax.set_ylabel('Revenue ($)', fontsize=12)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    ax.grid(True, alpha=0.3, axis='y')
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'${height:,.0f}',
               ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    
    if save:
        plt.savefig('reports/visualizations/payment_methods.png', dpi=300, bbox_inches='tight')
        print("[OK] Saved: reports/visualizations/payment_methods.png")
    
    plt.show()

def plot_heatmap_correlation(df, save=True):
    """
    Plot correlation heatmap for numerical variables
    
    Parameters:
    -----------
    df : pd.DataFrame
        Sales data
    save : bool
        Whether to save the plot
    """
    create_output_dir()
    
    # Select numerical columns
    numerical_cols = ['Quantity', 'Unit_Price', 'Total_Amount', 'Discount']
    corr_data = df[numerical_cols].corr()
    
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_data, annot=True, fmt='.2f', cmap='coolwarm', 
               center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8}, ax=ax)
    ax.set_title('Correlation Heatmap - Numerical Variables', fontsize=16, fontweight='bold', pad=20)
    
    plt.tight_layout()
    
    if save:
        plt.savefig('reports/visualizations/correlation_heatmap.png', dpi=300, bbox_inches='tight')
        print("[OK] Saved: reports/visualizations/correlation_heatmap.png")
    
    plt.show()

def create_all_visualizations(df):
    """
    Create all visualizations
    
    Parameters:
    -----------
    df : pd.DataFrame
        Sales data
    """
    print("\n" + "=" * 60)
    print("GENERATING VISUALIZATIONS")
    print("=" * 60)
    
    plot_sales_trend(df, save=True)
    plot_category_analysis(df, save=True)
    plot_region_analysis(df, save=True)
    plot_top_products(df, top_n=10, save=True)
    plot_customer_demographics(df, save=True)
    plot_payment_methods(df, save=True)
    plot_heatmap_correlation(df, save=True)
    
    print("\n" + "=" * 60)
    print("ALL VISUALIZATIONS GENERATED")
    print("=" * 60)
