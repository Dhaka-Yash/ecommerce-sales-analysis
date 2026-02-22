"""
Main Analysis Script
Complete end-to-end analysis pipeline
"""

import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_loader import load_sales_data, get_data_info
from src.data_cleaner import clean_sales_data, save_cleaned_data
from src.analyzer import (
    calculate_kpis, print_kpis, analyze_by_category, analyze_by_region,
    analyze_by_time, analyze_top_products, analyze_customer_demographics,
    analyze_payment_methods
)
from src.visualizer import create_all_visualizations
from src.insights_generator import generate_insights_report

def main():
    """Main analysis pipeline"""
    print("=" * 60)
    print("E-COMMERCE SALES PERFORMANCE ANALYSIS")
    print("=" * 60)
    
    # Step 1: Load Data
    print("\n" + "=" * 60)
    print("STEP 1: LOADING DATA")
    print("=" * 60)
    try:
        df = load_sales_data()
        print(f"\n[OK] Successfully loaded {len(df)} records")
    except FileNotFoundError as e:
        print(f"\n[ERROR] Error: {e}")
        print("\nPlease run 'python generate_data.py' first to generate sample data.")
        return
    
    # Step 2: Data Information
    print("\n" + "=" * 60)
    print("STEP 2: DATA INFORMATION")
    print("=" * 60)
    get_data_info(df)
    
    # Step 3: Clean Data
    print("\n" + "=" * 60)
    print("STEP 3: CLEANING DATA")
    print("=" * 60)
    df_clean = clean_sales_data(df)
    save_cleaned_data(df_clean)
    
    # Step 4: Calculate KPIs
    print("\n" + "=" * 60)
    print("STEP 4: CALCULATING KPIs")
    print("=" * 60)
    kpis = calculate_kpis(df_clean)
    print_kpis(kpis)
    
    # Step 5: Category Analysis
    print("\n" + "=" * 60)
    print("STEP 5: CATEGORY ANALYSIS")
    print("=" * 60)
    category_analysis = analyze_by_category(df_clean)
    print("\nCategory Performance:")
    print(category_analysis.to_string())
    
    # Step 6: Regional Analysis
    print("\n" + "=" * 60)
    print("STEP 6: REGIONAL ANALYSIS")
    print("=" * 60)
    region_analysis = analyze_by_region(df_clean)
    print("\nRegional Performance:")
    print(region_analysis.to_string())
    
    # Step 7: Time Analysis
    print("\n" + "=" * 60)
    print("STEP 7: TIME-BASED ANALYSIS")
    print("=" * 60)
    time_analysis = analyze_by_time(df_clean)
    print("\nMonthly Sales:")
    print(time_analysis['monthly'].to_string())
    print("\nQuarterly Sales:")
    print(time_analysis['quarterly'].to_string())
    print("\nYearly Sales:")
    print(time_analysis['yearly'].to_string())
    
    # Step 8: Top Products
    print("\n" + "=" * 60)
    print("STEP 8: TOP PRODUCTS ANALYSIS")
    print("=" * 60)
    top_products = analyze_top_products(df_clean, top_n=10)
    print("\nTop 10 Products by Revenue:")
    print(top_products.to_string())
    
    # Step 9: Customer Demographics
    print("\n" + "=" * 60)
    print("STEP 9: CUSTOMER DEMOGRAPHICS")
    print("=" * 60)
    demo_analysis = analyze_customer_demographics(df_clean)
    print("\nCustomer Demographics:")
    print(demo_analysis.to_string())
    
    # Step 10: Payment Methods
    print("\n" + "=" * 60)
    print("STEP 10: PAYMENT METHOD ANALYSIS")
    print("=" * 60)
    payment_analysis = analyze_payment_methods(df_clean)
    print("\nPayment Method Usage:")
    print(payment_analysis.to_string())
    
    # Step 11: Visualizations
    print("\n" + "=" * 60)
    print("STEP 11: GENERATING VISUALIZATIONS")
    print("=" * 60)
    create_all_visualizations(df_clean)
    
    # Step 12: Generate Insights Report
    print("\n" + "=" * 60)
    print("STEP 12: GENERATING INSIGHTS REPORT")
    print("=" * 60)
    generate_insights_report(df_clean, kpis, category_analysis, region_analysis, 
                            time_analysis, top_products, demo_analysis, payment_analysis)
    
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE!")
    print("=" * 60)
    print("\nAll outputs saved to:")
    print("  - Cleaned data: data/processed/sales_data_cleaned.csv")
    print("  - Visualizations: reports/visualizations/")
    print("  - Insights report: reports/insights_report.txt")
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
