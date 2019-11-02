import pandas as pd
import xlrd


dataSet1 = pd.read_csv(r"C:\Users\Davy Sheehy\Desktop\SoftwareProject\DataSets\eCommerceData.csv", encoding = 'unicode_escape')
##print(type(dataSet1))
##print(dataSet1)
dataSet2 = pd.read_csv(r"../online_retail.csv", encoding= 'unicode_escape')
##print(dataSet2)

dataSet3 = pd.read_excel(r"../online_retail_II_uci.xlsx",)
##print(dataSet3)

dataSet4 = pd.read_excel(r"../onlineRetail.xlsx")
##print(dataSet4)

