import pandas as pd
import plotly.express as px
import streamlit as st

import calendar

#defining the page title and icon 
st.set_page_config(page_title='Sales Dashboard', page_icon=':bar_chart:', layout='wide')

#reading the df which we handled before
df = pd.read_csv('./Sales Analysis/Data/All_sales.csv')

# ---- sidebar section -----
# Creating the sidebar section to enable filters in the df
st.sidebar.header('Please Filter Here:')

#defining the options to filter
city = st.sidebar.multiselect(
    'Select the City:',
    options=df['City'].unique(),
    default=df['City'].unique()
)

product = st.sidebar.multiselect(
    'Select the Product:',
    options=df['Product'].unique(),
    default=df['Product'].unique()
)


#filter using the query method
#using @ to refert to the variable
df_selection = df.query(
    'City == @city & Product == @product'
)


# ---- main page -----
st.title(':bar_chart: Sales Dashboard')

#inserting a new paraghaph to separe the title from KPIs
st.markdown('##')

#Display some KPIs in the main page.
total_sales = int(df_selection['Sales'].sum())
total_quantity_ordered = df_selection['Quantity Ordered'].sum()
average_sales_by_order = round(df_selection['Sales'].mean(), 2)

#defining 3 columns to display the KPIs
left_column, middle_column, right_column = st.columns(3)

with left_column:
    st.subheader('Total Sales:')
    st.subheader(f'US $ {total_sales:,}')

with middle_column:
    st.subheader('Total Products Sold:')
    st.subheader(f'{total_quantity_ordered:,}')

with right_column:
    st.subheader('Average Sales Per Order:')
    st.subheader(f'US $ {average_sales_by_order}')

#adding a markdown to separate.
st.markdown('---')



#Adding the charts:

#Sales by month [bar chart]

#Getting the name months by their indeces
months = []

for month_idx in range(1, 13):
    months.append(calendar.month_abbr[month_idx])

sales_by_month = df_selection.groupby('Month')['Sales'].sum()

fig_month_sales = px.bar(
    sales_by_month,
    x = months, 
    y = 'Sales',
    title = '<b>Sales by Month</b>',
    color_discrete_sequence = ['#0083B8'] * len(sales_by_month),
    template = 'plotly_white'
)

#Updating the title axis and remove the background color and the grid.
fig_month_sales.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_title='Months',
    yaxis_title='Sales in USD ($)',
    yaxis=(dict(showgrid=False))
)


#Sales by city [bar chart]

sales_by_city = df_selection.groupby('City')['Sales'].sum()
cities = sales_by_city.index

fig_city_sales = px.bar(
    sales_by_city,
    x = cities, 
    y = 'Sales',
    title = '<b>Sales by City</b>',
    color_discrete_sequence = ['#0083B8'] * len(sales_by_city),
    template = 'plotly_white'
)

fig_city_sales.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_title='Cities',
    yaxis_title='Sales in USD ($)',
    yaxis=(dict(showgrid=False))
)

#Ploting them side by side
left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_month_sales, use_container_width=True)
right_column.plotly_chart(fig_city_sales, use_container_width=True)


#Quantity of purchasing per hour [line chart]
sales_by_hour = df_selection.groupby('Order Hour')['Quantity Ordered'].count()
hours = sales_by_hour.index

fig_order_hour = px.line(
    sales_by_hour,
    x = hours, 
    y = 'Quantity Ordered',
    title = '<b>Sales by Hour</b>',
    color_discrete_sequence = ['#0083B8'] * len(sales_by_hour),
    template = 'plotly_white'
)

fig_order_hour.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_title='Hours',
    yaxis_title='Number of Sales',
    xaxis=dict(showgrid=False, tickmode='linear'),
    yaxis=(dict(showgrid=False))
)

#Quantity sold by product [bar chart]
sales_by_product = df_selection.groupby('Product')['Quantity Ordered'].sum()
product = sales_by_product.index

fig_product_sales = px.bar(
    sales_by_product,
    x = product, 
    y = 'Quantity Ordered',
    title = '<b>Sales by Product</b>',
    color_discrete_sequence = ['#0083B8'] * len(sales_by_product),
    template = 'plotly_white'
)

fig_product_sales.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_title='Products',
    yaxis_title='Number of Sales',
    yaxis=(dict(showgrid=False))
)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_order_hour, use_container_width=True)
right_column.plotly_chart(fig_product_sales, use_container_width=True)

# Changing the visibility of the page
# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

#Appearances from streamlit default was changed by the parameters defined in the config.toml file