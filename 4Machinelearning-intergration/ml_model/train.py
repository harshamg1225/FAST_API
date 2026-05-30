import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression


df = pd.read_csv("housing.csv")
print("Read the dataset")
df = df.drop(columns=["Address"], axis=0)

x = df.iloc[:, :-1]
y = df.iloc[:, -1]
print("split the dataset")
model = LinearRegression()

model.fit(x, y)
print("trained the model")


joblib.dump(model, "model.joblib")
print("Saved the model")
