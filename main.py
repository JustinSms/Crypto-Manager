import coinbase_api
import pandas as pd 
import datetime as dt 
import csv 

class Manager:

    def __init__(self, BTC_amount, ETH_amount, ADA_amount, principal):
        self.data = coinbase_api.call_api()
        self.BTC_rate = self.data.loc["BTC","Price"]
        self.ETH_rate = self.data.loc["ETH","Price"]
        self.ADA_rate = self.data.loc["ADA","Price"]

        self.BTC_amount = BTC_amount
        self.ETH_amount = ETH_amount
        self.ADA_amount = ADA_amount

        self.coin_value_list = [] 
        self.excel_index_counter = 0
        self.principal = principal

    def determine_portfolio_value(self): 
        portfolio_value_profit_list = []
        BTC_value = round(self.BTC_amount * self.BTC_rate,2)
        ETH_value = round(self.ETH_amount * self.ETH_rate,2)
        ADA_value = round(self.ADA_amount * self.ADA_rate,2)
        self.coin_value_list = [BTC_value, ETH_value, ADA_value]

        absolute_portfolio_value = sum(self.coin_value_list)
        portfolio_value_profit_list.append(absolute_portfolio_value)

        portfolio_profit = absolute_portfolio_value - self.principal
        portfolio_value_profit_list.append(portfolio_profit)

        return portfolio_value_profit_list


    def store_data_in_csv(self):
        readable_date = self.data.loc["BTC","Last_updated"]
        portfolio_value_profit_list = self.determine_portfolio_value()
        absolute_portfolio_value = portfolio_value_profit_list[0]
        portfolio_profit = portfolio_value_profit_list[1]
    

        api_call_list = [readable_date,self.BTC_rate,self.ETH_rate,self.ADA_rate,absolute_portfolio_value,portfolio_profit]

        with open ("Database_Portfolio.csv","a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(api_call_list)


Manager = Manager( BTC_amount=0.08513419, ETH_amount=4.19800311, ADA_amount=2160.16510, principal=16510)
Manager.determine_portfolio_value()
Manager.store_data_in_csv()