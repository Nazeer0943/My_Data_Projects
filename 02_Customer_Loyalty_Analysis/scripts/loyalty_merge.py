import pandas as pd
import os

# 1. SETUP PATHS
sales_path = os.path.join('..', '..', '01_Global_Mart_Sales_Audit_and_Analysis', 'cleaned_data', 'clean_sales.csv')
customer_path = os.path.join('..', 'raw_data', 'customer_profiles.csv')

# 2. LOAD DATA
df_sales = pd.read_csv(sales_path)
df_customers = pd.read_csv(customer_path)

# 3. CLEAN HEADERS (Removing hidden spaces like ' amount_spent')
df_sales.columns = df_sales.columns.str.strip()
df_customers.columns = df_customers.columns.str.strip()

# 4. NORMALIZE DATA (Fixing 'Alice' vs 'ALICE')
# We target the specific column so we don't destroy the rest of the table
df_sales['customer_name'] = df_sales['customer_name'].str.upper()
df_customers['customer_name'] = df_customers['customer_name'].str.upper()

# 5. THE MERGE (The Grand Finale)
merged_data = pd.merge(df_sales, df_customers, on='customer_name', how='inner')

# 6. DISPLAY RESULTS
print("\n--- Project 02: Success! ---")
if not merged_data.empty:
    # Showing the link between names, their loyalty level, and their spending
    print(merged_data[['customer_name', 'membership_level', 'amount_spent']].head())
else:
    print("Zero rows matched. Double-check your CSV data!")