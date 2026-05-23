
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(
    page_title="Global Superstore Dashboard",
    page_icon="📊",
    layout="wide"
)

@st.cache_data
def load_data():
    import glob
    matches = glob.glob('/content/*uperstore*') + glob.glob('/content/*lobal*tore*')
    if matches:
        filename = matches[0]
    else:
        csvs = glob.glob('/content/*.csv') + glob.glob('/content/*.xlsx')
        filename = csvs[0]
    
    if filename.endswith('.xlsx'):
        df = pd.read_excel(filename, engine='openpyxl')
    else:
        df = pd.read_csv(filename, encoding='latin-1')
    
    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')
    df['Year'] = df['Order Date'].dt.year
    return df

df = load_data()

# Sidebar Filters
st.sidebar.title("Filters")

all_regions = sorted(df['Region'].dropna().unique().tolist())
selected_regions = st.sidebar.multiselect("Region", all_regions, default=all_regions)

all_categories = sorted(df['Category'].dropna().unique().tolist())
selected_categories = st.sidebar.multiselect("Category", all_categories, default=all_categories)

filtered_sub = df[df['Category'].isin(selected_categories)]['Sub-Category'].dropna().unique().tolist()
selected_subcategories = st.sidebar.multiselect("Sub-Category", sorted(filtered_sub), default=sorted(filtered_sub))

all_years = sorted(df['Year'].dropna().unique().tolist())
selected_years = st.sidebar.multiselect("Year", all_years, default=all_years)

filtered_df = df[
    (df['Region'].isin(selected_regions)) &
    (df['Category'].isin(selected_categories)) &
    (df['Sub-Category'].isin(selected_subcategories)) &
    (df['Year'].isin(selected_years))
]

st.title("📊 Global Superstore — Business Intelligence Dashboard")
st.markdown("Use the filters on the left to explore sales and profit data.")

if filtered_df.empty:
    st.warning("No data matches the selected filters.")
    st.stop()

# KPI Cards
st.subheader("Key Performance Indicators")
total_sales   = filtered_df['Sales'].sum()
total_profit  = filtered_df['Profit'].sum()
total_orders  = filtered_df['Order ID'].nunique()
profit_margin = (total_profit / total_sales * 100) if total_sales > 0 else 0

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales",   f"${total_sales:,.0f}")
col2.metric("Total Profit",  f"${total_profit:,.0f}")
col3.metric("Total Orders",  f"{total_orders:,}")
col4.metric("Profit Margin", f"{profit_margin:.1f}%")

st.divider()

# Sales by Region and Category
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Sales by Region")
    region_sales = filtered_df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(6,4))
    sns.barplot(x=region_sales.values, y=region_sales.index, palette='Blues_r', ax=ax)
    ax.set_xlabel("Total Sales ($)")
    ax.set_ylabel("")
    ax.set_title("Sales by Region")
    st.pyplot(fig)
    plt.close()

with col_b:
    st.subheader("Sales by Category")
    cat_sales = filtered_df.groupby('Category')['Sales'].sum()
    fig, ax = plt.subplots(figsize=(5,4))
    ax.pie(cat_sales.values, labels=cat_sales.index, autopct='%1.1f%%',
           colors=sns.color_palette('Set2', len(cat_sales)))
    ax.set_title("Sales Split by Category")
    st.pyplot(fig)
    plt.close()

st.divider()

# Monthly Trend and Profit by Sub-Category
col_c, col_d = st.columns(2)

with col_c:
    st.subheader("Monthly Sales Trend")
    monthly = filtered_df.groupby(filtered_df['Order Date'].dt.to_period('M'))['Sales'].sum()
    monthly.index = monthly.index.astype(str)
    fig, ax = plt.subplots(figsize=(8,4))
    ax.plot(monthly.index, monthly.values, color='steelblue', linewidth=2)
    ax.fill_between(monthly.index, monthly.values, alpha=0.2, color='steelblue')
    tick_positions = range(0, len(monthly), max(1, len(monthly)//10))
    ax.set_xticks([list(monthly.index)[i] for i in tick_positions])
    ax.set_xticklabels([list(monthly.index)[i] for i in tick_positions], rotation=45, ha='right')
    ax.set_title("Monthly Sales Over Time")
    ax.set_xlabel("Month")
    ax.set_ylabel("Sales ($)")
    st.pyplot(fig)
    plt.close()

with col_d:
    st.subheader("Profit by Sub-Category")
    sub_profit = filtered_df.groupby('Sub-Category')['Profit'].sum().sort_values()
    colors = ['#d73027' if v < 0 else '#1a9850' for v in sub_profit.values]
    fig, ax = plt.subplots(figsize=(6,6))
    ax.barh(sub_profit.index, sub_profit.values, color=colors)
    ax.axvline(0, color='black', linewidth=0.8)
    ax.set_title("Profit by Sub-Category (Red = Loss)")
    ax.set_xlabel("Profit ($)")
    st.pyplot(fig)
    plt.close()

st.divider()

# Top 5 Customers
st.subheader("Top 5 Customers by Sales")
top_customers = (
    filtered_df.groupby('Customer Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)
top_customers['Sales'] = top_customers['Sales'].round(2)
top_customers.columns = ['Customer Name', 'Total Sales ($)']

col_e, col_f = st.columns([1,2])
with col_e:
    st.dataframe(top_customers, use_container_width=True)
with col_f:
    fig, ax = plt.subplots(figsize=(7,4))
    sns.barplot(data=top_customers, x='Total Sales ($)', y='Customer Name',
                palette='viridis', ax=ax)
    ax.set_title("Top 5 Customers by Sales")
    ax.set_xlabel("Total Sales ($)")
    ax.set_ylabel("")
    st.pyplot(fig)
    plt.close()

st.divider()

with st.expander("View Raw Data (first 100 rows)"):
    st.dataframe(filtered_df.head(100))

st.caption("Dashboard built for DevelopersHub Corporation Data Science Internship")
