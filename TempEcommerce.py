import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import combinations
from collections import Counter

# Load the dataset
df = pd.read_csv(r"C:\Users\manny\Documents\EcommerceProj\EcommerceDB.csv", encoding='unicode_escape')

# Ensure the database has been read correctly and display its column types
print("Data loaded successfully. First few rows:")
print(df.head())
print("\nData types:")
print(df.dtypes)

# Change to appropriate data type
df['InvoiceNo'] = df['InvoiceNo'].astype(str)
df['Description'] = df['Description'].astype(str)
print(f"Number of duplicates: {df.duplicated().sum()}")

# Drop duplicates
df = df.drop_duplicates()

# Check for null values
print("\nNull values before dropping:")
print(df.isnull().sum())

# Drop rows with null values
df = df.dropna()
print("\nNull values after dropping:")
print(df.isnull().sum())

# Remove rows with negative values in 'UnitPrice' and 'Quantity' columns
df = df[(df['UnitPrice'] > 0) & (df['Quantity'] > 0)]
df = df[df['Description'].str.strip().astype(bool)]  # Removing any empty description rows

# Adjusting the data types (Country, InvoiceNo, and Description to string & InvoiceDate to date)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['CustomerID'] = df['CustomerID'].astype(str)
print("\nData types after adjustments:")
print(df.dtypes)

# Adding a new column that stores the sales from the sale of each item
df['Sales'] = df['Quantity'] * df['UnitPrice']
print("\nFirst few rows after adding the Sales column:")
print(df.head())

# Check for any anomalies in the data
#print("\nUnique countries in the dataset:")
#print(df['Country'].unique())
#print("\nSales column statistics:")
#print(df['Sales'].describe())

# Check for any null values in relevant columns
print("\nNull values in relevant columns:")
print(df[['Country', 'Sales']].isnull().sum())

# Ensure only numerical columns are summed
numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
print("\nNumerical columns in the dataframe:")
print(numerical_cols)

# Calculating sales per country
print("\nCalculating sales per country...")
try:
    sales_per_country = df.groupby('Country')[numerical_cols].sum()['Sales'].sort_values(ascending=False).reset_index()
    print("\nSales per country:")
    print(sales_per_country)
except Exception as e:
    print(f"Error calculating sales per country: {e}")

plt.figure(figsize=(10, 6))
sales_per_country.plot(kind='bar', color='skyblue')
plt.title('Total Sales per Country')
plt.xlabel('Country')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Group by Country and display sales for the UK
grp = df.groupby('Country', axis=0)
UK_grp = grp.get_group('United Kingdom')
print(UK_grp.sort_values(by='Sales', ascending=False)[['UnitPrice', 'Quantity', 'Sales']])

# Most/Least sold items per country
quantity_per_country = df.groupby('Country').sum(numeric_only=True)['Quantity'].sort_values(ascending=False)
print(quantity_per_country)

# Total profit
total_profit = df['Sales'].sum()
print("Total profit:", total_profit)

# Top-selling products in different countries/profit per country
for country, item in grp:
    top_item = item.sort_values(by='Sales', ascending=False).head(1)
    print(top_item[['Sales', 'Country', 'StockCode', 'Description']], "\n\n")

# Most expensive item per country
for country, item in grp:
    most_expensive = item.sort_values(by='UnitPrice', ascending=False).head(1)
    print(most_expensive[['UnitPrice', 'Country', 'StockCode', 'Description']], "\n\n")

# Cheapest item per country
for country, item in grp:
    cheapest = item.sort_values(by='UnitPrice', ascending=False).tail(1)
    print(cheapest[['UnitPrice', 'Country', 'StockCode', 'Description']], "\n\n")

# Overall most expensive and cheapest items
overall_most_expensive = df.groupby('UnitPrice').max()[['Country', 'StockCode', 'Description']]
print(overall_most_expensive)

# Total quantity of products sold over the year
total_quantity_sold = df['Quantity'].sum()
print("Total quantity sold:", total_quantity_sold)

# Products with consistently low sales
average_sales = df['Sales'].mean()
low_sales_products = df[df['Sales'] < average_sales].sort_values('Sales', ascending=False)
print(low_sales_products[['Description', 'Sales']].value_counts())

# Most sold item per country
grouped = df.groupby(['Country', 'Description', 'StockCode'])['Sales'].sum().reset_index()
for country, group in grouped.groupby('Country'):
    top_item = group.sort_values(by='Sales', ascending=False).head(1)
    print(top_item[['Sales', 'Country', 'StockCode', 'Description']], "\n\n")

# Least sold item per country
for country, item in grp:
    least_sold = item.sort_values(by='Sales', ascending=False).tail(1)
    print(least_sold[['Sales', 'Country', 'StockCode', 'Description']], "\n\n")

# Product with the highest revenue
highest_revenue_product = df.sort_values('Sales', ascending=False)[['Sales', 'Description']]
print(highest_revenue_product)

top_10_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
top_10_products.plot(kind='bar', color='orange')
plt.title('Top 10 Selling Products')
plt.xlabel('Product Description')
plt.ylabel('Total Quantity Sold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Monthly sales revenue
df['MonthYear'] = df['InvoiceDate'].dt.strftime('%B %Y')
df_monthly = df.groupby('MonthYear').sum(numeric_only=True).reset_index()
df_monthly['MonthYear'] = pd.to_datetime(df_monthly['MonthYear'], format='%B %Y')
df_monthly = df_monthly.sort_values('MonthYear').reset_index(drop=True)
df_monthly['MonthYear'] = df_monthly['MonthYear'].dt.strftime('%B %Y')
print(df_monthly.to_string(index=False))

plt.figure(figsize=(12, 6))
sns.lineplot(data=df_monthly, x='MonthYear', y='Sales', marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month and Year')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Products bought together
InvoiceCount = df.groupby('InvoiceNo')['Description'].count()
multiple_items_invoices = df[df['InvoiceNo'].isin(InvoiceCount[InvoiceCount > 1].index)]
product_pairs_counter = Counter()
for invoice_no, group in multiple_items_invoices.groupby('InvoiceNo'):
    products = list(group['Description'])
    pairs = combinations(products, 2)
    product_pairs_counter.update(pairs)
product_pairs_df = pd.DataFrame(product_pairs_counter.items(), columns=['ProductPair', 'Count'])
product_pairs_df = product_pairs_df.sort_values(by='Count', ascending=False)
pd.set_option('display.max_colwidth', None)
print(product_pairs_df)

# Products bought in bulk
InvoiceCount_df = InvoiceCount.reset_index(name='ItemCount')
mean_items_per_invoice = InvoiceCount_df['ItemCount'].mean()
print('Mean items per invoice:', mean_items_per_invoice)
over_twenty = InvoiceCount_df[InvoiceCount_df['ItemCount'] > 20].shape[0]
over_five_hundred = InvoiceCount_df[InvoiceCount_df['ItemCount'] > 500].shape[0]
print('Orders with over 20 items:', over_twenty)
print('Orders with over 500 items:', over_five_hundred)

# Price vs Quantity Sold
filtered_df = df[(df['UnitPrice'] > 0) & (df['UnitPrice'] < 4000) & (df['Quantity'] > 0) & (df['Quantity'] < 10000)]
plt.figure(figsize=(10, 6))
plt.scatter(filtered_df['UnitPrice'], filtered_df['Quantity'], alpha=0.5)
plt.title('Scatter Plot of Unit Price vs. Quantity Sold')
plt.xlabel('Unit Price')
plt.ylabel('Quantity Sold')
plt.show()

# Analyze price changes and their effect on sales
df['Month'] = df['InvoiceDate'].dt.to_period('M')
grouped = df.groupby(['Description', 'Month'])
price_change_analysis = []
for (product, month), group in grouped:
    sorted_group = group.sort_values(by='InvoiceDate')
    unique_prices = sorted_group['UnitPrice'].unique()
    if len(unique_prices) > 1:
        for i in range(1, len(unique_prices)):
            before_price = unique_prices[i-1]
            after_price = unique_prices[i]
            before_sales = sorted_group[sorted_group['UnitPrice'] == before_price]['Quantity'].sum()
            after_sales = sorted_group[sorted_group['UnitPrice'] == after_price]['Quantity'].sum()
            price_change_analysis.append({
                'Product': product,
                'Month': month,
                'Before_Price': before_price,
                'After_Price': after_price,
                'Before_Sales': before_sales,
                'After_Sales': after_sales,
                'Price_Change': 'Increase' if after_price > before_price else 'Decrease',
                'Sales_Change': 'Increase' if after_sales > before_sales else 'Decrease'
            })
price_change_analysis_df = pd.DataFrame(price_change_analysis)

# Select only the numeric columns for correlation calculation
numeric_cols = price_change_analysis_df.select_dtypes(include=['float64', 'int64']).columns
print(price_change_analysis_df[numeric_cols].corr())

#print(price_change_analysis_df.corr())

# Time of day analysis
df['Hour'] = df['InvoiceDate'].dt.hour
def time_of_day(hour):
    if 6 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 18:
        return 'Afternoon'
    elif 18 <= hour < 24:
        return 'Evening'
df['TimeOfDay'] = df['Hour'].apply(time_of_day)
time_of_day_analysis = df.groupby(['Country', 'TimeOfDay']).size().reset_index(name='PurchaseCount')
print(time_of_day_analysis)
for time in ['Morning', 'Afternoon', 'Evening']:
    filtered_time = time_of_day_analysis[time_of_day_analysis['TimeOfDay'] == time]
    print(f"Purchases during {time}:")
    print(filtered_time['PurchaseCount'].count())
    print("\n")

# Most popular products per region
popular_products_analysis = df.groupby(['Country', 'Description'])['InvoiceNo'].count().reset_index(name='PurchaseCount')
popular_products_analysis = popular_products_analysis.sort_values(by=['Country', 'PurchaseCount'], ascending=[True, False])
top_3_products_per_country = popular_products_analysis.groupby('Country').head(1)
print(top_3_products_per_country.to_string(index=False))
print('\n')

# Average order value per region
average_order_value_analysis = df.groupby('Country')['Sales'].mean().reset_index(name='AverageOrderValue')
print(average_order_value_analysis.to_string(index=False))

# Remove 'nan' values from CustomerID
df = df[df['CustomerID'] != 'nan']

# Most profitable customer
customer_sales = df.groupby('CustomerID')['Sales'].sum().reset_index()
most_profitable_customer = customer_sales.sort_values(by='Sales', ascending=False).head(1)
print("Most profitable customer:")
print(most_profitable_customer)
