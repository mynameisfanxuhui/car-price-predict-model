# importing Pandas library
import pandas as pd
import numpy as np

# Import label encoder
#from sklearn import preprocessing

# Several data statistics
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


# label_encoder object knows how to understand word labels.
from sklearn import preprocessing

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

dataDF = pd.read_csv("final_data2.csv", encoding="windows-1252")

df1 = dataDF.loc[(dataDF['price'] >= 500) & (dataDF['price'] < 999999)]
df2 = df1.copy()
df2["priceNormalized"] = np.log(df2["price"])
df2["combinedFeature"] = df2["model"].map(str) + "," + df2["vehicleType"].map(str)
df2['combinedFeatureCoded'] = label_encoder.fit_transform(df2['combinedFeature'])


# first selection
# newCopy2 = df2[['priceNormalized', 'model', 'kilometer', 'brand', 'gearbox', 'fuelType', 'notRepairedDamage']]
# newCopy2.to_csv("final_data3.csv", index=False)

# second selection
# newCopy2 = df2[['priceNormalized', 'model', 'kilometer', 'brand', 'gearbox', 'fuelType', 'notRepairedDamage', 'vehicleType']]
# newCopy2.to_csv("final_data3.csv", index=False)

#third selection, combined feature, compare to second se111lection
# newCopy2 = df2[['priceNormalized', 'kilometer', 'combinedFeatureCoded', 'gearbox', 'fuelType', 'notRepairedDamage', 'vehicleType']]
# newCopy2.to_csv("final_data3.csv", index=False)

# forth selection, combined feature, compare to first selection
# newCopy2 = df2[['priceNormalized', 'combinedFeatureCoded', 'kilometer', 'gearbox', 'fuelType', 'notRepairedDamage']]
# newCopy2.to_csv("final_data3.csv", index=False)

# fifth selection, without 'notRepairedDamage'
# newCopy2 = df2[['priceNormalized', 'model', 'kilometer', 'brand', 'gearbox', 'fuelType', 'vehicleType']]
# newCopy2.to_csv("final_data3.csv", index=False)

# # sixth selection, combined feature of fifth selection
# newCopy2 = df2[['priceNormalized', 'kilometer', 'combinedFeatureCoded', 'gearbox', 'fuelType', 'notRepairedDamage', 'vehicleType']]
# newCopy2.to_csv("final_data3.csv", index=False)
#
#
# # seventh selection, without 'fuelType'
# newCopy2 = df2[['priceNormalized', 'model', 'kilometer', 'brand', 'gearbox', 'notRepairedDamage', 'vehicleType']]
# newCopy2.to_csv("final_data3.csv", index=False)
#
# # eighth selection, combined feature of seven selection
# newCopy2 = df2[['priceNormalized', 'kilometer', 'combinedFeatureCoded', 'gearbox', 'notRepairedDamage', 'vehicleType']]
# newCopy2.to_csv("final_data3.csv", index=False)
#
# # ninth selection, without 'gearbox'
# newCopy2 = df2[['priceNormalized', 'model', 'kilometer', 'brand', 'fuelType', 'notRepairedDamage', 'vehicleType']]
# newCopy2.to_csv("final_data3.csv", index=False)
#
# # tenth selection, combined feature of nine selection
# newCopy2 = df2[['priceNormalized', 'kilometer', 'combinedFeatureCoded', 'fuelType', 'notRepairedDamage', 'vehicleType']]
# newCopy2.to_csv("final_data3.csv", index=False)
#
#
# # eleventh selection, without 'kilometer'
# newCopy2 = df2[['priceNormalized', 'model', 'brand', 'gearbox', 'fuelType', 'notRepairedDamage', 'vehicleType']]
# newCopy2.to_csv("final_data3.csv", index=False)
#
# # twelve selection, combined feature of eleven selection
newCopy2 = df2[['priceNormalized', 'combinedFeatureCoded', 'gearbox', 'fuelType', 'notRepairedDamage', 'vehicleType']]
newCopy2.to_csv("final_data3.csv", index=False)







