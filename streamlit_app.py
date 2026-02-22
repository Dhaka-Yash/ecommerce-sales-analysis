"""Streamlit dashboard for the e-commerce sales analysis project."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

from src.analyzer import (
    analyze_by_category,
    analyze_by_region,
    analyze_by_time,
    analyze_customer_demographics,
    analyze_payment_methods,
    analyze_top_products,
    calculate_kpis,
)
from src.data_cleaner import clean_sales_data
from src.data_loader import load_sales_data

sns.set_style("whitegrid")

DEFAULT_RAW_PATH = Path("data/raw/sales_data.csv")
DEFAULT_PROCESSED_PATH = Path("data/processed/sales_data_cleaned.csv")


@st.cache_data(show_spinner=False)
def load_base_data(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        if "Order_Date" in df.columns:
            df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
        return df

    if DEFAULT_PROCESSED_PATH.exists():
        return pd.read_csv(DEFAULT_PROCESSED_PATH, parse_dates=["Order_Date"])

    if DEFAULT_RAW_PATH.exists():
        return load_sales_data(str(DEFAULT_RAW_PATH))

    raise FileNotFoundError(
        "No dataset found. Add data at data/raw/sales_data.csv or upload a CSV file."
    )


@st.cache_data(show_spinner=False)
def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    required_cols = {"Year", "Month", "Quarter", "Day_of_Week", "Revenue_After_Discount"}
    if required_cols.issubset(df.columns):
        return df.copy()
    return clean_sales_data(df)


def fmt_currency(value: float) -> str:
    return f"${value:,.2f}"


def build_filters(df: pd.DataFrame) -> pd.DataFrame:
    st.sidebar.header("Filters")

    min_date = pd.to_datetime(df["Order_Date"]).min().date()
    max_date = pd.to_datetime(df["Order_Date"]).max().date()

    date_range = st.sidebar.date_input(
        "Order date range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )

    if isinstance(date_range, tuple) and len(date_range) == 2:
        start_date, end_date = date_range
    else:
        start_date, end_date = min_date, max_date

    categories = st.sidebar.multiselect(
        "Category",
        options=sorted(df["Category"].dropna().unique().tolist()),
        default=sorted(df["Category"].dropna().unique().tolist()),
    )

    regions = st.sidebar.multiselect(
        "Region",
        options=sorted(df["Region"].dropna().unique().tolist()),
        default=sorted(df["Region"].dropna().unique().tolist()),
    )

    payments = st.sidebar.multiselect(
        "Payment method",
        options=sorted(df["Payment_Method"].dropna().unique().tolist()),
        default=sorted(df["Payment_Method"].dropna().unique().tolist()),
    )

    mask = (
        (df["Order_Date"].dt.date >= start_date)
        & (df["Order_Date"].dt.date <= end_date)
        & (df["Category"].isin(categories))
        & (df["Region"].isin(regions))
        & (df["Payment_Method"].isin(payments))
    )

    return df.loc[mask].copy()


def plot_monthly_trend(df: pd.DataFrame):
    monthly_sales = df.groupby(["Year", "Month"], as_index=False)["Total_Amount"].sum()
    monthly_sales["Date"] = pd.to_datetime(monthly_sales[["Year", "Month"]].assign(DAY=1))

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(
        monthly_sales["Date"],
        monthly_sales["Total_Amount"],
        marker="o",
        linewidth=2,
        color="#1f77b4",
    )
    ax.set_title("Monthly Sales Trend")
    ax.set_xlabel("Date")
    ax.set_ylabel("Revenue")
    ax.tick_params(axis="x", rotation=45)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))
    fig.tight_layout()
    return fig


def plot_bar(series: pd.Series, title: str, xlabel: str, horizontal: bool = False):
    fig, ax = plt.subplots(figsize=(10, 5))

    if horizontal:
        ax.barh(series.index, series.values, color=sns.color_palette("viridis", len(series)))
        ax.set_xlabel(xlabel)
        ax.set_ylabel("")
        ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))
    else:
        ax.bar(series.index, series.values, color=sns.color_palette("Set2", len(series)))
        ax.set_xlabel("")
        ax.set_ylabel(xlabel)
        ax.tick_params(axis="x", rotation=45)
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))

    ax.set_title(title)
    fig.tight_layout()
    return fig


def plot_payment_share(df: pd.DataFrame):
    payment_series = df.groupby("Payment_Method")["Total_Amount"].sum().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.pie(payment_series.values, labels=payment_series.index, autopct="%1.1f%%", startangle=90)
    ax.set_title("Revenue Share by Payment Method")
    fig.tight_layout()
    return fig


def main():
    st.set_page_config(page_title="E-commerce Sales Dashboard", layout="wide")
    st.title("E-commerce Sales Analysis Dashboard")
    st.caption("Built from the project pipeline in src/*.py")

    uploaded_file = st.sidebar.file_uploader("Upload CSV (optional)", type=["csv"])

    try:
        raw_df = load_base_data(uploaded_file)
    except FileNotFoundError as exc:
        st.error(str(exc))
        st.stop()

    df = prepare_data(raw_df)
    filtered_df = build_filters(df)

    if filtered_df.empty:
        st.warning("No records found for selected filters.")
        st.stop()

    kpis = calculate_kpis(filtered_df)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Revenue", fmt_currency(kpis["Total_Revenue"]))
    c2.metric("Total Orders", f"{kpis['Total_Orders']:,}")
    c3.metric("Avg Order Value", fmt_currency(kpis["Average_Order_Value"]))
    c4.metric("Unique Customers", f"{kpis['Unique_Customers']:,}")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["Overview", "Trends", "Products", "Customers", "Data"]
    )

    with tab1:
        st.subheader("Revenue by Category and Region")
        col_a, col_b = st.columns(2)
        category_series = (
            filtered_df.groupby("Category")["Total_Amount"].sum().sort_values(ascending=False)
        )
        region_series = (
            filtered_df.groupby("Region")["Total_Amount"].sum().sort_values(ascending=False)
        )
        col_a.pyplot(plot_bar(category_series, "Revenue by Category", "Revenue"))
        col_b.pyplot(plot_bar(region_series, "Revenue by Region", "Revenue", horizontal=True))

    with tab2:
        st.subheader("Time-Based Analysis")
        st.pyplot(plot_monthly_trend(filtered_df))
        time_analysis = analyze_by_time(filtered_df)
        st.dataframe(time_analysis["monthly"], use_container_width=True)

    with tab3:
        st.subheader("Top Products")
        top_n = st.slider("Top N Products", min_value=5, max_value=20, value=10)
        top_products = analyze_top_products(filtered_df, top_n=top_n)
        st.dataframe(top_products, use_container_width=True)

        top_products_series = (
            filtered_df.groupby("Product_Name")["Total_Amount"].sum().sort_values(ascending=False).head(top_n)
        )
        st.pyplot(plot_bar(top_products_series[::-1], f"Top {top_n} Products by Revenue", "Revenue", horizontal=True))

    with tab4:
        st.subheader("Customer and Payment Insights")
        col_c, col_d = st.columns(2)

        demo = analyze_customer_demographics(filtered_df)
        payment = analyze_payment_methods(filtered_df)

        demo_series = demo["Total_Revenue"].sort_values(ascending=False)
        col_c.pyplot(plot_bar(demo_series, "Revenue by Age Group", "Revenue"))
        col_d.pyplot(plot_payment_share(filtered_df))

        st.markdown("Customer Demographics")
        st.dataframe(demo, use_container_width=True)
        st.markdown("Payment Methods")
        st.dataframe(payment, use_container_width=True)

    with tab5:
        st.subheader("Analysis Tables")
        st.markdown("Category Analysis")
        st.dataframe(analyze_by_category(filtered_df), use_container_width=True)
        st.markdown("Region Analysis")
        st.dataframe(analyze_by_region(filtered_df), use_container_width=True)
        st.markdown("Filtered Dataset")
        st.dataframe(filtered_df, use_container_width=True)


if __name__ == "__main__":
    main()
