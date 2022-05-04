import pandas as pd


class dataset:
    def __init__(self) -> None:
        self.sales = pd.read_excel("sales_bcs.xlsx")
        self.customers=pd.read_excel('sales_bcs.xlsx', 'Customers Sheet')
        self.sites = pd.read_excel('sales_bcs.xlsx', 'Site Location sheet')
        self.products=pd.read_excel('sales_bcs.xlsx', 'Products_Sheet')
        self.sales_team= pd.read_excel('sales_bcs.xlsx','Sales Team Sheet')

        #Add a total amount to every transaction
        self.add_sales()
        #Add a month column
        self.add_month()
        
    def add_month(self):
        self.sales['Month'] = pd.DatetimeIndex(self.sales['OrderDate']).month

    def add_sales(self):
        self.sales['Total'] = (self.sales['Order Quantity'] * self.sales['Unit Price']) - self.sales['Discount Applied']

    @property
    def best_months_df(self):
        best_month = self.sales.groupby('Month').sum()
        return best_month['Total']

    @property
    def best_district_df(self):
        best_district = self.sales.groupby('_SiteID').sum()
        return best_district['Total']

    @property
    def best_district_products(self):
        all_transactions = self.sales[(self.sales['_SiteID']) == 284]
        product = all_transactions.groupby('_ProductID', as_index=False).sum()
        return product[['_ProductID', 'Total']]

    
import streamlit as st
from BreastData import dataset

dataframe = dataset()

def PredModel():

    
    inputs = dict()
    labels = dict()

    with st.form("ai form"):

        


	    # submition form
    #submitted = st.form_submit_button("Submit")

    #if submitted:
       # inputs['airline'] = airline
       # inputs['flight'] = flight
	   # inputs['stops'] = stops
		#inputs['class'] = class_
		#inputs['duration'] = duration


		    
# predicting for the model
    #prediction = model.predict([[labels['airline'],labels['flight'],labels['stops'],labels['class'],labels['duration']]])
	#st.subheader('Predicted Price')
	#st.subheader(int(prediction[0]))

    