from pydantic import BaseModel, Field, StrictInt


class InputSchema(BaseModel):
    Avg_Area_Income: float = Field(..., gt=0, description="Enter the avg_area income")
    Avg_Area_House_Age: float = Field(
        ..., gt=0, description="Enter the avg area house age"
    )
    Avg_Area_Number_of_Rooms: float = Field(
        ..., gt=0, description="Enter the number of room"
    )
    Avg_Area_Number_of_Bedrooms: float = Field(
        ..., gt=0, description="enter avg area number of bedrooms"
    )
    Area_Population: float = Field(..., gt=0)


class OutputSchema(BaseModel):
    Price: float
