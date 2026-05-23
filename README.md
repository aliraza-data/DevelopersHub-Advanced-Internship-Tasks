# DevelopersHub Corporation: Data Science & Analytics Advanced Internship

**Intern:** Ali Raza
**Program:** Data Science & Analytics Advanced Internship
**Organization:** DevelopersHub Corporation

---

## Completed Tasks

### Task 1: Term Deposit Subscription Prediction
**Objective:** Predict whether a bank customer will subscribe to a term deposit after a marketing campaign.
**Dataset:** Bank Marketing Dataset (UCI / Kaggle)

**Approach:**
- Loaded and explored the dataset
- Encoded all categorical features using Label Encoding
- Trained Logistic Regression and Random Forest classifiers
- Evaluated using Confusion Matrix, F1-Score, and ROC Curve
- Used SHAP to explain 5 individual model predictions

**Results:**
- Random Forest outperformed Logistic Regression with higher F1 and AUC score
- Top predictors: call duration, month of contact, account balance, age, job type
- Best months to contact customers: March, September, October, December

**File:** `term_deposit.ipynb`

---

### Task 2: Customer Segmentation Using Unsupervised Learning
**Objective:** Cluster customers based on spending habits and propose marketing strategies for each segment.
**Dataset:** Mall Customers Dataset (Kaggle)

**Approach:**
- Performed EDA on age, income, and spending score
- Used the Elbow Method to find the optimal number of clusters (k=5)
- Applied K-Means Clustering on scaled features
- Visualized clusters using PCA

**Results:**
- 5 distinct customer segments identified
- High income, high spending group is the most valuable segment
- High income, low spending group has the most untapped potential
- Low income, high spending group is a churn risk

| Cluster | Income | Spending | Strategy |
|---------|--------|----------|----------|
| 0 | Low | Low | Discount offers |
| 1 | Low | High | Loyalty rewards |
| 2 | Medium | Medium | General promotions |
| 3 | High | Low | Premium quality messaging |
| 4 | High | High | VIP programs |

**File:** `customer_segmentation.ipynb`

---

### Task 5: Interactive Business Dashboard (Streamlit)
**Objective:** Build an interactive dashboard to analyze sales, profit, and customer performance.
**Dataset:** Global Superstore Dataset (Kaggle)

**Approach:**
- Cleaned and prepared the dataset
- Built a Streamlit dashboard with filters for Region, Category, Sub-Category, and Year
- Displayed KPIs: Total Sales, Total Profit, Total Orders, Profit Margin
- Added charts: Sales by Region, Sales by Category, Monthly Trend, Profit by Sub-Category
- Showed Top 5 Customers by Sales
- Deployed on Google Colab using ngrok for public URL access

**Results:**
- Technology is the highest revenue category
- Tables and Bookcases are loss-making sub-categories
- Top 5 customers contribute a significant share of total revenue
- Regional filters reveal performance gaps across markets

**File:** `streamlit_dashboard.ipynb`

---

## Tech Stack
- Python 3
- pandas, numpy
- matplotlib, seaborn
- scikit-learn
- shap
- streamlit
- pyngrok
- Jupyter Notebook / Google Colab

## How to Run

### Task 1 and Task 2 (Notebooks)
1. Open the `.ipynb` file in Google Colab
2. Run all cells from top to bottom
3. Kaggle credentials required for dataset download (kagglehub will prompt on first run)

### Task 5 (Streamlit Dashboard)
1. Open `task5_colab.ipynb` in Google Colab
2. Run all cells in order
3. Add your ngrok token in the secrets panel (key icon in Colab sidebar)
4. Click the ngrok public URL printed in the output to open the dashboard
