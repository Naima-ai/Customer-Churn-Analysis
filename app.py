import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(page_title="Customer Churn Analysis Of A European bank", layout="wide")

# Title and introduction
st.title("📊 European Bank Customer Churn Analysis Dashboard")
st.markdown("""
Welcome to the dashboard analyzing customer churn behavior.  
This report presents churn trends, model performance, insights, and data-driven recommendations.
""")

# SECTION: Data Visualizations
st.header("🔍 Data Visualizations")

# Centered Subheader
st.markdown("<h3 style='text-align: center;'>Churn vs Retained Distribution</h3>", unsafe_allow_html=True)

# Center the image using columns
col9, col10, col11 = st.columns([1, 2, 1])  # middle column is wider
with col10:
    st.image("images/churn_distribution.png")

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Churn Based On Age")
    st.image("images/age_distribution (2).png")

with col2:
    st.subheader("2. Churn Based on Gender")
    st.image("images/gender_distribution.png")

# Row 2: Country & Services
col3, col4 = st.columns(2)
with col3:
    st.subheader("3. Churn Based on Country")
    st.image("images/country_distribution.png")

with col4:
    st.subheader("4. Churn Based on Services Taken")

    st.image("images/services_distribution.png")

# Row 3: Account Balance & Tenure
col5, col6 = st.columns(2)

with col5:
    st.subheader("5. Churn Based on Tenure with Bank")
    st.image("images/tenure_vs_churnrate_distribution.png")
with col6:
    st.subheader("6. Churn Based on Account Balance")
    st.image("images/balance_distribution.png")

# Row 4: Credit Repay
col7, col8 = st.columns(2)
with col7:
    st.subheader("7. Churn Based on Credit Repayment")
    st.image("images/credit_repay_distribution.png")
with col8:
    st.subheader("8. Churn Based on Salary")
    st.image("images/salarybin_distribution.png")
col12, _=st.columns(2)
with col12:
    st.subheader("9. Churn Based on Credit Card Use")
    st.image("images/credit_distribution.png")
    


# SECTION: Model Evaluation
st.header("🤖 Model Performance (Random Forest)")

# Model metrics
st.markdown("""
- **Accuracy:** 0.867  
- **Precision:** 0.725  
- **Recall:** 0.490  
- **F1 Score:** 0.585
""")

# Confusion matrix
st.subheader("Confusion Matrix")
st.image("images/confusion_distribution.png", use_container_width=False)

# SECTION: Insights and Recommendations
st.header("📌 Key Insights and Recommended Actions")

st.subheader("🧠 Key Insights from the Data:")
st.markdown("""
- **Early and Late Tenure Vulnerability**: Churn peaks during early customer relationships and again at the 9-year mark.  
- **Gender Disparity (insignificant)**: Females show higher churn (1 in 5) compared to males (1 in 8).  
- **Geographic Variation**: Germany has significantly higher churn rates proportionally compared to France and Spain.  
- **Credit Card Correlation**: Customers with credit cards are more likely to exit the bank.  
- **Multi-Service Risk**: Customers using 3 or more services (loan, savings account, credit card) have higher exit rates.  
- **Account Balance Factor**: Higher account balance correlates with increased likelihood of churning.
""")

st.subheader("✅ Recommended Decisions for the Bank:")
st.markdown("""
1. **First-Year Customer Experience Enhancement**  
   - Create a comprehensive onboarding program with regular check-ins  
   - Offer first-year benefits such as fee waivers or special rates  

2. **Targeted Senior Retention Program**  
   - Create a "senior-focused" service with dedicated support reps  
   - Offer retirement account options with better interest rates  

3. **Germany-Focused Retention Campaign**  
   - Conduct region-specific market research  
   - Offer localized product offerings and branch support  

4. **Bundle Service Optimization**  
   - Improve integration and user experience of bundled services  

5. **Female Customer Strategy**  
   - Develop targeted communication and services aligned with female priorities  

6. **Credit Card Review**  
   - Re-evaluate credit card benefits  
   - Improve digital experience for credit card management  
""")

# Footer
st.markdown("---")
st.markdown("© 2025 Customer Churn Analysis by Naima Tasnia")

