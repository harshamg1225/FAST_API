import joblib
import numpy as np

saved_model = joblib.load("model.joblib")
print("loaded the model")


def make_prediction(data: dict) -> float:

    features = np.array(
        [
            [
                data["Avg_Area_Income"],
                data["Avg_Area_House_Age"],
                data["Avg_Area_Number_of_Rooms"],
                data["Avg_Area_Number_of_Bedrooms"],
                data["Area_Population"],
            ]
        ]
    )

    return saved_model.predict(features)[0]


def Batch_prediction(data: list[dict]) -> np.array:

    X = np.array(
        [
            [
                x["Avg_Area_Income"],
                x["Avg_Area_House_Age"],
                x["Avg_Area_Number_of_Rooms"],
                x["Avg_Area_Number_of_Bedrooms"],
                x["Area_Population"],
            ]
            for x in data
        ]
    )

    return saved_model.predict(X)
