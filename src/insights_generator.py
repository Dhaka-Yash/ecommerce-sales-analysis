"""
Insights Report Generator
Generate business insights and recommendations from analysis
"""

import os
import pandas as pd

def generate_insights_report(df, kpis, category_analysis, region_analysis, 
                            time_analysis, top_products, demo_analysis, payment_analysis):
    """
    Generate comprehensive insights report
    
    Parameters:
    -----------
    df : pd.DataFrame
        Cleaned sales data
    kpis : dict
        Key performance indicators
    category_analysis : pd.DataFrame
        Category performance analysis
    region_analysis : pd.DataFrame
        Regional performance analysis
    time_analysis : dict
        Time-based analysis
    top_products : pd.DataFrame
        Top products analysis
    demo_analysis : pd.DataFrame
        Customer demographics analysis
    payment_analysis : pd.DataFrame
        Payment method analysis
    """
    os.makedirs('reports', exist_ok=True)
    
    report = []
    report.append("=" * 80)
    report.append("E-COMMERCE SALES PERFORMANCE ANALYSIS - INSIGHTS REPORT")
    report.append("=" * 80)
    report.append("")
    
    # Executive Summary
    report.append("EXECUTIVE SUMMARY")
    report.append("-" * 80)
    report.append(f"Total Revenue: ${kpis['Total_Revenue']:,.2f}")
    report.append(f"Total Orders: {kpis['Total_Orders']:,}")
    report.append(f"Average Order Value: ${kpis['Average_Order_Value']:,.2f}")
    report.append(f"Unique Customers: {kpis['Unique_Customers']:,}")
    report.append("")
    
    # Key Insights
    report.append("KEY INSIGHTS")
    report.append("-" * 80)
    
    # 1. Top Performing Category
    top_category = category_analysis.index[0]
    top_category_revenue = category_analysis.loc[top_category, 'Total_Revenue']
    top_category_share = category_analysis.loc[top_category, 'Revenue_Share_%']
    report.append(f"\n1. TOP PERFORMING CATEGORY: {top_category}")
    report.append(f"   - Revenue: ${top_category_revenue:,.2f} ({top_category_share}% of total)")
    report.append(f"   - Orders: {int(category_analysis.loc[top_category, 'Order_Count']):,}")
    report.append(f"   - Recommendation: Focus marketing efforts and inventory on {top_category}")
    
    # 2. Top Region
    top_region = region_analysis.index[0]
    top_region_revenue = region_analysis.loc[top_region, 'Total_Revenue']
    top_region_share = region_analysis.loc[top_region, 'Revenue_Share_%']
    report.append(f"\n2. TOP PERFORMING REGION: {top_region}")
    report.append(f"   - Revenue: ${top_region_revenue:,.2f} ({top_region_share}% of total)")
    report.append(f"   - Recommendation: Expand presence in {top_region} and replicate success strategies")
    
    # 3. Top Product
    top_product = top_products.index[0][0]
    top_product_revenue = top_products.iloc[0]['Total_Revenue']
    report.append(f"\n3. TOP PRODUCT: {top_product}")
    report.append(f"   - Revenue: ${top_product_revenue:,.2f}")
    report.append(f"   - Orders: {int(top_products.iloc[0]['Order_Count']):,}")
    report.append(f"   - Recommendation: Ensure adequate stock and consider bundling opportunities")
    
    # 4. Customer Demographics
    top_age_group = demo_analysis.index[0]
    top_age_revenue = demo_analysis.loc[top_age_group, 'Total_Revenue']
    top_age_customers = int(demo_analysis.loc[top_age_group, 'Unique_Customers'])
    report.append(f"\n4. PRIMARY CUSTOMER SEGMENT: {top_age_group}")
    report.append(f"   - Revenue: ${top_age_revenue:,.2f}")
    report.append(f"   - Customers: {top_age_customers:,}")
    report.append(f"   - Recommendation: Tailor marketing campaigns and product recommendations for {top_age_group}")
    
    # 5. Payment Method
    top_payment = payment_analysis.index[0]
    top_payment_usage = payment_analysis.loc[top_payment, 'Usage_%']
    report.append(f"\n5. PREFERRED PAYMENT METHOD: {top_payment}")
    report.append(f"   - Usage: {top_payment_usage}% of all transactions")
    report.append(f"   - Recommendation: Ensure seamless {top_payment} experience and consider incentives")
    
    # 6. Time Trends
    monthly = time_analysis['monthly']
    best_month = monthly.loc[monthly['Revenue'].idxmax()]
    best_month_idx = monthly['Revenue'].idxmax()
    worst_month = monthly.loc[monthly['Revenue'].idxmin()]
    worst_month_idx = monthly['Revenue'].idxmin()
    
    report.append(f"\n6. SEASONAL TRENDS")
    report.append(f"   - Best Month: {best_month_idx[0]}-{best_month_idx[1]:02d} (Revenue: ${best_month['Revenue']:,.2f})")
    report.append(f"   - Worst Month: {worst_month_idx[0]}-{worst_month_idx[1]:02d} (Revenue: ${worst_month['Revenue']:,.2f})")
    report.append(f"   - Recommendation: Plan inventory and promotions around peak months")
    
    # Business Recommendations
    report.append("\n" + "=" * 80)
    report.append("STRATEGIC RECOMMENDATIONS")
    report.append("=" * 80)
    
    report.append("\n1. PRODUCT PORTFOLIO OPTIMIZATION")
    report.append("   - Focus on top-performing categories: " + ", ".join(category_analysis.head(3).index.tolist()))
    report.append("   - Review underperforming categories and consider promotions or discontinuation")
    report.append("   - Develop product bundles featuring top-selling items")
    
    report.append("\n2. MARKET EXPANSION")
    report.append(f"   - Prioritize growth in {top_region} (highest revenue region)")
    report.append("   - Investigate low-performing regions for improvement opportunities")
    report.append("   - Consider regional marketing campaigns tailored to local preferences")
    
    report.append("\n3. CUSTOMER ENGAGEMENT")
    report.append(f"   - Target {top_age_group} demographic with personalized campaigns")
    report.append("   - Implement loyalty programs to increase customer retention")
    report.append(f"   - Average Order Value: ${kpis['Average_Order_Value']:,.2f} - Consider upselling strategies")
    
    report.append("\n4. OPERATIONAL EFFICIENCY")
    report.append(f"   - Discount Rate: {kpis['Discount_Rate']:.2f}% - Review discount strategy")
    report.append(f"   - Optimize payment processing for {top_payment} (most used method)")
    report.append("   - Monitor inventory levels for top products to avoid stockouts")
    
    report.append("\n5. GROWTH OPPORTUNITIES")
    report.append("   - Cross-sell complementary products from top categories")
    report.append("   - Develop seasonal campaigns aligned with peak sales months")
    report.append("   - Expand product range in high-performing categories")
    
    # Performance Metrics Summary
    report.append("\n" + "=" * 80)
    report.append("PERFORMANCE METRICS SUMMARY")
    report.append("=" * 80)
    report.append(f"\nFinancial Metrics:")
    report.append(f"  - Total Revenue: ${kpis['Total_Revenue']:,.2f}")
    report.append(f"  - Average Order Value: ${kpis['Average_Order_Value']:,.2f}")
    report.append(f"  - Total Discount Given: ${kpis['Total_Discount_Given']:,.2f}")
    report.append(f"  - Discount Rate: {kpis['Discount_Rate']:.2f}%")
    
    report.append(f"\nOperational Metrics:")
    report.append(f"  - Total Orders: {kpis['Total_Orders']:,}")
    report.append(f"  - Total Quantity Sold: {kpis['Total_Quantity_Sold']:,} units")
    report.append(f"  - Average Quantity per Order: {kpis['Average_Quantity_per_Order']:.2f} units")
    
    report.append(f"\nCustomer Metrics:")
    report.append(f"  - Unique Customers: {kpis['Unique_Customers']:,}")
    report.append(f"  - Unique Products: {kpis['Unique_Products']:,}")
    report.append(f"  - Unique Categories: {kpis['Unique_Categories']:,}")
    
    report.append("\n" + "=" * 80)
    report.append("END OF REPORT")
    report.append("=" * 80)
    
    # Write report to file
    report_text = "\n".join(report)
    report_path = 'reports/insights_report.txt'
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_text)
    
    print(f"\n[OK] Insights report generated: {report_path}")
    print("\nReport Preview:")
    print("-" * 80)
    print("\n".join(report[:50]))  # Print first 50 lines as preview
    if len(report) > 50:
        print(f"\n... ({len(report) - 50} more lines in full report)")
