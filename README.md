# Ecommerce Project
This is a sales transaction data set of UK-based e-commerce (online retail) for one year. This London-based shop has been selling gifts and homewares for adults and children through the website since 2007. Their customers come from all over the world and usually make direct purchases for themselves. There are also small businesses that buy in bulk and sell to other customers through retail outlet channels.
The data set contains 500K rows and 8 columns. The following is the description of each column.
1.	TransactionNo (categorical): a six-digit unique number that defines each transaction. The letter “C” in the code indicates a cancellation.
2.	Date (numeric): the date when each transaction was generated.
3.	ProductNo (categorical): a five or six-digit unique character used to identify a specific product.
4.	Product (categorical): product/item name.
5.	Price (numeric): the price of each product per unit in pound sterling (£).
6.	Quantity (numeric): the quantity of each product per transaction. Negative values related to cancelled transactions.
7.	CustomerNo (categorical): a five-digit unique number that defines each customer.
8.	Country (categorical): name of the country where the customer resides.
There is a small percentage of order cancellation in the data set. Most of these cancellations were due to out-of-stock conditions on some products. Under this situation, customers tend to cancel an order as they want all products delivered all at once.
This python program analyses the data to produce meaningful information from it. The data is manipulated using pandas, NumPy, seaborn and Matplotlib. It is cleaned using Pandas to remove, null values, negative unit price and quantity. 
The data is then manipulated to derive meaningful information to give us insights about the data so that “statistically backed data” can be used to improve the business’ sales. Firstly, a series of question are asked to make meaning of the data and then visualization using Matplotlib and Seaborn to make sense of the data.
BASIC INFORMATION:
1.	sales per country. 
2.	Most profitable country.
3.	Least profitable country.
4.	What is the top-selling products in different countries/profit per country
5.	Total profit.
6.	Most expensive Item per country
7.	Cheapest Item per country
8.	Over most expensive and cheapest.
9.	What is the total quantity of products sold over the year?
10.	Are there any products with consistently low sales i.e. product with the lowest sales that barely sold? (below-average level of product or service purchases1)
11.	Most sold Item per country.
12.	Least sold item per country.
13.	Which products generate the most revenue?
SALES TRENDS
14.	Most profitable period/What are the peak sales months?
15.	Which countries contribute the most to the total sales revenue?
16.	Are there specific products that are more commonly bought in bulk?
17.	Are there specific products that are more commonly bought together?
18.	Least profitable period. 
19.	What is the total sales revenue generated over each month?
20.	How does the order size distribution look like (e.g., small, medium, large orders)?
21.	How does the price of products influence the quantity sold?
22.	Are there any noticeable trends in purchasing behavior across different regions?
23.	Are there any products with price changes during each month, and how did it affect their sales?
24.	Most profitable customer?
25.	Most popular (bought) products per region?

By analyzing the data thoroughly, I was able to deliver valuable insights about the data and come to certain conclusions. Firstly, Considering the number of sales made In the UK and EIRE (“Ireland”), it is safe to assume that this company is based in the UK. The company has made a lot of changes to its prices considering it made 12,656 changes with no real correlation with an increase in sales, it is safe to say that the company should reduce the number of changes it makes to sales.
Other insights include the most profitable time of the day (when the most sales were made) was between 6 am to 12 pm so it would be wise to make sure products are accessible for purchase by customers at that time. They had the highest number of sales and sold the highest quantity of products in the month of November which could be attributed to Black Friday.
There is also no real correlation between the price of products and the quantity of goods sold which is a bad thing for the company as a higher price should be for products with a higher quantity bought ceteris paribus.






