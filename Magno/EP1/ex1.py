import pandas as pd

cars_data = pd.read_csv("vehicles_cleaned_train.csv")

fuel_dummy = pd.get_dummies(cars_data.fuel) #Transforma a variável categórica em dummy
size_dummy = pd.get_dummies(cars_data.size)

print(size_dummy)