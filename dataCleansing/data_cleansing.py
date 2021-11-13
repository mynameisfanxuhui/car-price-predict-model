# importing Pandas library
import pandas as pd

# Import label encoder
from sklearn import preprocessing

# label_encoder object knows how to understand word labels.
label_encoder = preprocessing.LabelEncoder()

# Encode labels in column 'species'.
# df['species'] = label_encoder.fit_transform(df['species'])
#
# df['species'].unique()
#originalDF = pd.read_csv("C:\\Users\\torres_fan\\Desktop\\CS586\\Project\\autos.csv", encoding="windows-1252")
#print(type(originalDF))
#print(originalDF.keys())
# print("before drop ", len(originalDF))
#newDF = originalDF.dropna()
# print("after drop", len(newDF))
# newCopy1 = newDF.copy()
# newCopy1['gearbox'] = label_encoder.fit_transform(newDF['gearbox'])
# newCopy1['model'] = label_encoder.fit_transform(newDF['model'])
# newCopy1['fuelType'] = label_encoder.fit_transform(newDF['fuelType'])
# newCopy1['brand'] = label_encoder.fit_transform(newDF['brand'])
# newCopy1['notRepairedDamage'] = label_encoder.fit_transform(newDF['notRepairedDamage'])
# newCopy1.to_csv("final_data.csv")

dataDF = pd.read_csv("C:\\Users\\torres_fan\\Desktop\\CS586\\carPricePredict\\car-price-predict-model\\dataCleansing\\final_data.csv", encoding="windows-1252")
newCopy1 = dataDF.copy()
newCopy1['abtest'] = label_encoder.fit_transform(dataDF['abtest'])
newCopy1['vehicleType'] = label_encoder.fit_transform(dataDF['vehicleType'])
newCopy2 = newCopy1[['price', 'abtest', 'vehicleType', 'gearbox', 'powerPS', 'model', 'kilometer', 'fuelType', 'brand', 'notRepairedDamage']]
newCopy2.to_csv("final_data2.csv")
# print(dataDF["price"].max())
# print(dataDF["price"].min())
# print(dataDF["price"].mean())
# print(len(dataDF["model"].unique()))
# print(len(dataDF["vehicleType"].unique()))
# print(len(dataDF["brand"].unique()))

# dataDF = pd.read_csv("C:\\Users\\torres_fan\\Desktop\\CS586\\final_data.csv")
# print(dataDF["price"].max())
# print(dataDF["price"].min())
# print(dataDF["price"].mean())
# print(dataDF["price"].median())