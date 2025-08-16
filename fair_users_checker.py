print('Fair users checker start')

import pandas as pd
import matplotlib.pyplot as plt

# Configure plot style
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (8, 6)
plt.rcParams['font.size'] = 12

def header(msg):
    print('*' * 100)
    print(f'[ {msg} ]')
    print('*' * 100)

# 📥 Load CSV files
fair_users_df = pd.read_csv('fair_users.csv')
fraud_users_df = pd.read_csv('fraud_users.csv')
transactions_fair_df = pd.read_csv('transactions_by_fair_users.csv')
transactions_fraud_df = pd.read_csv('transactions_by_fraudsters.csv')

# 📊 Display data samples
header("Top 5 Fair Users")
print(fair_users_df.head())

header("Last 5 Fair Users")
print(fair_users_df.tail())

header("Top 5 Fraudster Users")
print(fraud_users_df.head())

header("Last 5 Fraudster Users")
print(fraud_users_df.tail())

# 📈 Statistical summaries
header("Fair Users Summary")
print(fair_users_df.describe())

header("Fraudster Users Summary")
print(fraud_users_df.describe())

# 📊 Country comparison
header("Country Distribution")
fair_users_df['country'].value_counts().plot.bar(title="Fair Users by Country")
plt.show()

fraud_users_df['country'].value_counts().plot.bar(title="Fraudster Users by Country")
plt.show()

# 📊 KYC comparison
header("KYC Status Distribution")
fair_users_df['kyc'].value_counts().plot.bar(title="Fair Users KYC Status")
plt.show()

fraud_users_df['kyc'].value_counts().plot.bar(title="Fraudster Users KYC Status")
plt.show()

# 📊 Birth year comparison
header("Birth Year Distribution")
fair_users_df['birth_year'].value_counts().plot.bar(title="Fair Users Birth Year")
plt.show()

fraud_users_df['birth_year'].value_counts().plot.bar(title="Fraudster Users Birth Year")
plt.show()

# 📊 Transaction state comparison
header("Transaction State Distribution")
transactions_fair_df['state'].value_counts().plot.bar(title="Fair User Transactions by State")
plt.show()

transactions_fraud_df['state'].value_counts().plot.bar(title="Fraudster Transactions by State")
plt.show()

# 📈 Amount comparison
header("Transaction Amount Comparison")
transactions_fair_df['amount'].plot.line(title="Fair User Transaction Amounts")
plt.show()

transactions_fraud_df['amount'].plot.line(title="Fraudster Transaction Amounts")
plt.show()

# 📊 Merchant category comparison
header("Merchant Category Distribution")
transactions_fair_df['merchant_category'].value_counts().plot.bar(title="Fair User Merchant Categories")
plt.show()

transactions_fraud_df['merchant_category'].value_counts().plot.bar(title="Fraudster Merchant Categories")
plt.show()

# 🔍 Correlation analysis
header("Correlation: Failed Sign-ins vs Fraudster Amounts")
correlation = fair_users_df['failed_sign_in_attempts'].corr(transactions_fraud_df['amount'])
print(f"Correlation: {correlation:.4f}")




print('Fair users checker end')