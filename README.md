📊 Customer Churn Analysis & Prediction
🔍 Business Problem
A European bank wants to understand why customers are leaving (churning) and predict future churners based on historical data. Retaining customers is cheaper than acquiring new ones, so this analysis can help the bank target high-risk customers with interventions.
Key Insights from the data:
*Early and Late Tenure Vulnerability: Churn peaks during early customer relationships and again at the 9-year mark.
*Gender Disparity (insignificant): Females show higher churn (1 in 5) compared to males (1 in 8).
*Tenure Group Pattern: Churn rate is relatively consistent across tenure groups.
*Geographic Variation: Germany has significantly higher churn rates proportionally compared to France and Spain.
*Credit Card Correlation: Customers with credit cards are more likely to exit the bank.
*Multi-Service Risk: Customers using all three services (loan, savings account, credit card) have higher exit rates.
*Account Balance Factor: Higher account balance correlates with increased likelihood of churning.
Recommended Decisions for Bank:
1. First-Year Customer Experience Enhancement: Create a comprehensive onboarding program with regular check-ins and can offer first-year benefits such as fee waivers or special rates.
2. Targeted Senior Retention Program: Create a senior focused" service with dedicated support representatives and can offer competitive retirement account options with better interest rates.
3.Germany-Focused Retention Campaign: Conduct market research specific to German customers' needs.
-Consider region-specific product offerings.
-Increase local branch support if applicable.
4.Bundle Service Optimization: Review the integration and user experience of bundled services.
5.Develop targeted communications and products that address female customers' priorities.
6.Review credit card benefits and competitiveness and improve the digital experience for credit card management.
For the prediction model development the following steps were taken:
1.EDA included:
a.Distribution plots
b.Histograms
c.Scatter and bar plots
d.Grouped analysis by categorical variables
🛠️ Feature Engineering
Steps taken:
1.Renamed columns for clarity (e.g., CreditScore → Credit_repay_score).
2.Created new features like:
balance_salary_ratio = Balance / (EstimatedSalary + 1)
3.age_group using binning.
4.Encoded categorical features like Geography, Gender.
5.Removed outliers using IQR method for Age, CreditScore, NumOfProducts.
6.Class imbalance handling with stratified train-test split and integrate SMOTE.
🤖 Model Building
Chosen model: Random Forest Classifier
Why? It handles non-linearity, multicollinearity, and doesn’t require feature scaling.
Evaluation Insight: The model performs well on customers who stay, but struggles to recall churned customers — which is critical for the business. Precision is moderate, but recall needs improvement.
