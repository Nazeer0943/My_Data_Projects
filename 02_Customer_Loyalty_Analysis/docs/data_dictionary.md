# Project 02: Data Dictionary

## Table 1: Sales Data (Source: Project 01)
- **transaction_id**: Unique identifier for each purchase.
- **customer_name**: Name of the customer (Normalized to UPPERCASE for merging).
- **amount_spent**: The total dollar value of the transaction.

## Table 2: Customer Profiles (Source: Project 02)
- **customer_name**: Name used to link to the Sales Data.
- **age**: The age of the customer.
- **membership_level**: Loyalty tier (Gold, Silver, Bronze).
- **region**: Geographical location of the customer.