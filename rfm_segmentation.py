# %% [markdown]
# # Part 2: RFM Segmentation & Retention Strategy
# 
# **What is RFM?**
# RFM stands for Recency, Frequency, Monetary — three simple metrics that 
# tell you how valuable a customer is:
# - **Recency**: How many days since their last order? (lower = better)
# - **Frequency**: How many orders did they place? (higher = better)
# - **Monetary**: How much did they spend in total? (higher = better)
# 
# The idea is simple — a customer who ordered yesterday, orders every week, 
# and spends a lot is WAY more valuable than someone who ordered once 
# six months ago and never came back.
# 
# In this notebook, I'll:
# 1. Build R, F, M from the raw order data
# 2. Score each customer on a 1-5 scale
# 3. Add extra signals (support tickets, web activity, returns)
# 4. Create meaningful customer segments
# 5. Recommend retention actions for each segment

# %%
# Starting with pandas — our main tool for working with data tables
import pandas as pd

# %%
# Load the datasets we need for Part 2
# orders.csv — the raw purchase history (this is where R, F, M come from)
# customers.csv — demographics and loyalty info
# support_tickets.csv — complaint history
# web_events_snapshot.csv — website activity
# churn_labels.csv — who actually churned (we'll use this to validate our segments)
# intervention_history.csv — campaign data

orders = pd.read_csv('data/orders.csv')
customers = pd.read_csv('data/customers.csv')
support_tickets = pd.read_csv('data/support_tickets.csv')
web_events = pd.read_csv('data/web_events_snapshot.csv')
churn_labels = pd.read_csv('data/churn_labels.csv')
interventions = pd.read_csv('data/intervention_history.csv')

print("📊 Datasets loaded:")
print(f"  orders:           {orders.shape[0]:,} rows × {orders.shape[1]} columns")
print(f"  customers:        {customers.shape[0]:,} rows × {customers.shape[1]} columns")
print(f"  support_tickets:  {support_tickets.shape[0]:,} rows × {support_tickets.shape[1]} columns")
print(f"  web_events:       {web_events.shape[0]:,} rows × {web_events.shape[1]} columns")
print(f"  churn_labels:     {churn_labels.shape[0]:,} rows × {churn_labels.shape[1]} columns")
print(f"  interventions:    {interventions.shape[0]:,} rows × {interventions.shape[1]} columns")

# %% [markdown]
# ## Step 1: Understand the order data
# 
# Before building RFM, I need to understand what the order data looks like.
# Key questions:
# - What columns do we have?
# - What date range do orders cover?
# - Are there duplicates we need to clean (like we found in Part 1)?

# %%
print("📋 Order columns:")
print(f"  {list(orders.columns)}")
print(f"\nFirst 5 orders:")
print(orders.head())
print(f"\nColumn types:")
print(orders.dtypes)

# %% [markdown]
# ## Step 2: Clean the order data
# 
# From Part 1, I already know there are issues:
# - 12 orders have `_DUP` suffix in their order_id (duplicates)
# - order_date is text, not a proper date
# - Some orders happened AFTER the snapshot date (2025-09-30) — can't use those
# 
# Let me fix all of this before computing RFM.

# %%
# Remove duplicate orders (order_id ending with '_DUP')
dup_count = orders['order_id'].str.endswith('_DUP').sum()
print(f"🔍 Found {dup_count} duplicate orders — removing them")

orders_clean = orders[~orders['order_id'].str.endswith('_DUP')].copy()
print(f"   Orders before: {len(orders)} → After: {len(orders_clean)}")

# Convert order_date from text to datetime so we can do date math
orders_clean['order_date'] = pd.to_datetime(orders_clean['order_date'])

# The snapshot date — all RFM calculations are relative to this date
snapshot_date = pd.to_datetime('2025-09-30')

# Split orders into pre-snapshot (safe to use) and post-snapshot (future data, can't use)
pre_snapshot = orders_clean[orders_clean['order_date'] <= snapshot_date]
post_snapshot = orders_clean[orders_clean['order_date'] > snapshot_date]

print(f"\n📅 Snapshot date: {snapshot_date.date()}")
print(f"   Pre-snapshot orders:  {len(pre_snapshot):,} (using these for RFM)")
print(f"   Post-snapshot orders: {len(post_snapshot):,} (ignoring — future data)")
print(f"   Date range: {pre_snapshot['order_date'].min().date()} to {pre_snapshot['order_date'].max().date()}")

# %% [markdown]
# ## Step 3: Build the R, F, M features
# 
# Now the fun part. For each customer, I need to calculate:
# - **R (Recency)**: Days between their LAST order and the snapshot date
#   → Lower is better (ordered recently = still engaged)
# - **F (Frequency)**: Total number of orders they placed
#   → Higher is better (orders often = loyal)
# - **M (Monetary)**: Total amount they spent across all orders
#   → Higher is better (spends a lot = valuable)
# 
# I'll use `groupby('customer_id')` to calculate these per customer.

# %%
# Build RFM table — one row per customer
rfm = pre_snapshot.groupby('customer_id').agg(
    last_order_date=('order_date', 'max'),          # Most recent order date
    frequency=('order_id', 'count'),                 # Number of orders
    monetary=('gross_amount', 'sum')                 # Total spending
).reset_index()

# Calculate recency: how many days between last order and snapshot
rfm['recency_days'] = (snapshot_date - rfm['last_order_date']).dt.days

# Drop the last_order_date column — we only needed it to calculate recency
rfm = rfm.drop(columns=['last_order_date'])

# Reorder columns so it reads nicely: customer_id, recency, frequency, monetary
rfm = rfm[['customer_id', 'recency_days', 'frequency', 'monetary']]

print("📊 RFM table built! Here are the first 10 customers:")
print(rfm.head(10).to_string(index=False))
print(f"\n📈 RFM Statistics:")
print(rfm[['recency_days', 'frequency', 'monetary']].describe().round(1))

