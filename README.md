# E-commerce Sales Performance Analysis

A comprehensive data science project analyzing e-commerce sales data to derive actionable business insights. This project demonstrates essential data analysis skills including data cleaning, exploratory data analysis (EDA), visualization, and statistical analysis.

## Project Overview

This project analyzes e-commerce sales data to answer key business questions:
- What are the sales trends over time?
- Which products and categories perform best?
- What are the customer demographics and purchasing patterns?
- Which regions generate the most revenue?
- What are the peak sales periods?
- How can we optimize pricing and inventory?

## Key Features

- **Data Cleaning & Preprocessing**: Handles missing values, outliers, and data inconsistencies
- **Exploratory Data Analysis**: Comprehensive statistical analysis and data exploration
- **Data Visualization**: Charts and dashboards using Matplotlib and Seaborn
- **Interactive Dashboard**: Streamlit app with filters, KPI cards, and analysis tabs
- **Business Insights**: Actionable recommendations based on data findings
- **Professional Documentation**: Well-documented code with clear explanations

## Technologies Used

- **Python 3.8+**
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib**: Static visualizations
- **Seaborn**: Statistical visualizations
- **Streamlit**: Interactive dashboard
- **Jupyter Notebook**: Interactive analysis
- **Scikit-learn**: Statistical analysis (optional)

## Project Structure

```text
.
|- README.md                   # Project documentation
|- requirements.txt            # Python dependencies
|- streamlit_app.py            # Streamlit dashboard app
|- .gitignore                  # Git ignore file
|- data/                       # Data directory
|  |- raw/                     # Raw data files
|  |- processed/               # Processed data files
|- src/                        # Source code
|  |- data_loader.py           # Data loading utilities
|  |- data_cleaner.py          # Data cleaning functions
|  |- analyzer.py              # Main analysis functions
|  |- visualizer.py            # Visualization functions
|  |- insights_generator.py    # Insights report generation
|  |- main_analysis.py         # End-to-end pipeline runner
|- notebooks/                  # Jupyter notebooks
|  |- sales_analysis.ipynb     # Main analysis notebook
|- reports/                    # Generated reports and charts
|  |- insights_report.txt      # Analysis insights
|- generate_data.py            # Script to generate sample data
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone or download this repository**

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Generate sample data**
   ```bash
   python generate_data.py
   ```

## Running the Analysis

### Option 1: Streamlit Dashboard (Recommended)
```bash
streamlit run streamlit_app.py
```

### Option 2: Jupyter Notebook (Exploration)
```bash
jupyter notebook notebooks/sales_analysis.ipynb
```

### Option 3: Python Script (Batch Pipeline)
```bash
python src/main_analysis.py
```

## Streamlit Dashboard Highlights

- Sidebar filters for date range, category, region, and payment method
- KPI cards for revenue, orders, AOV, and unique customers
- Tabs for overview, trends, products, customer insights, and detailed tables
- Optional CSV upload for ad-hoc analysis

## Analysis Outputs

The project generates:
- **Cleaned Data**: `data/processed/sales_data_cleaned.csv`
- **Visualizations**: `reports/visualizations/` (7 charts)
- **Insights Report**: `reports/insights_report.txt`

## Key Metrics Analyzed

- Total Revenue and Sales Volume
- Average Order Value (AOV)
- Product Performance Rankings
- Regional Sales Distribution
- Customer Segmentation
- Monthly/Quarterly Trends
- Category Performance
- Payment Method Preferences

## Learning Outcomes

This project demonstrates:
- Data cleaning and preprocessing techniques
- Exploratory Data Analysis (EDA)
- Data visualization best practices
- Statistical analysis and interpretation
- Business intelligence and reporting
- Python programming for data science
- Professional code organization

## Contributing

This is a learning project. Feel free to:
- Add more analysis features
- Improve visualizations
- Add machine learning models
- Enhance documentation

## License

This project is open source and available for educational purposes.

## Author

**Yash Dhaka** - Data Science & Data Analyst Aspirant

- GitHub: [@Dhaka-Yash](https://github.com/Dhaka-Yash)
- LinkedIn: [yash-dhaka-15a6823a2](https://www.linkedin.com/in/yash-dhaka-15a6823a2)

---

**Note**: This project uses synthetic data for demonstration purposes. In a real-world scenario, you would work with actual business data.
