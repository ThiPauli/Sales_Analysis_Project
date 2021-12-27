# Electronic Store Sales Analysis

## Project Overview
- Analysing the data from an electronic store, which contains 12 months worth of sales data.
- Getting insights from the data to understand some correlations in order to increase the store profits.
- Exploring the sales by their product types, costs, purchase city, time of the year and time of purchase.
- The main Python libraries used in this project analysis were Pandas, Numpy, Matplotlib and Seaborn. Access the Jupyter Notebook **[here](https://github.com/ThiPauli/Sales_Analysis_Project/blob/main/Sales%20Analysis/Electronics%20Sales%20Analysis.ipynb)**.
- Sales Dashboard was built in Python and the Streamlit and Plotly libraries. Access the Python code **[here](https://github.com/ThiPauli/Sales_Analysis_Project/blob/main/app.py)**.
- The Dashboard was deployed using Heroku. Acess the Sales Dashboard via https://saleseletronicsdashboard.herokuapp.com/

## Objectives
### The goal is to answer business questions as follow:
* Which months generated the highest profits?
* Which cities purchased the most?
* Which products sold the most?

### Additionally, other questions which may help to understand relationships in order to decision-making process in the future to increase the sales.
* Which hour of the day customers bought the most? Order x Time.
* Which products are bought together? Orders which have more than 1 purchase.

## Exploratory Data Analysis and Data Cleaning
### Data Cleaning
* Checking columns with missing values.
* Drop NaN values from DataFrame.
* Convert column as object to datetime.

### Exploratory Data Analysis
* Adding new columns as well as extracting months and hours from the order date.
* Using groupby to perform aggregate analysis.
* Using .apply() method to get the city names for each sale.
* Using .transform() method to get all product names of the same order.
* Plotting bar charts and lines graphs to visualize the results.

## Data analysis and visualizations
* Defining the total sales per each month in order to know what month had the highest profit and its values.
<img src="Sales Analysis\images\Sales by Month.png" width="600" />

* Defining the total sales and getting the results per city.
<img src="Sales Analysis\images\Sales by City.png" width="500" height="400" />

* Evaluating the purchase's time of all cities (top) as well as for each city (bottom)(Seattle (WA) in this case). Evaluated by the hour purchased in each sale.
<img src="Sales Analysis\images\Sales by Hour.png" width="500"/>
<img src="Sales Analysis\images\Sales by Hour in Seattle (WA).png" width="500" height="300"/>

* Evaluating the most sold products. Data grouped by their products and the total number of sales. Also, the price of each product was considered to evaluate their relationship.
<img src="Sales Analysis\images\Sales by Product and Price.png" width="500" height="400" />

* Evaluating the orders which have more than 1 purchase by the same customer to see which products are most sold together. Evaluated the total number of sales of the pair of products bought together.
<img src="Sales Analysis\images\Top 5 pairs products bought together in one order.png" width="550" height="450"/>

## Sales Dashboard
