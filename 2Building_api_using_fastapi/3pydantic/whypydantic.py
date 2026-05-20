def insert_patient_data(name: str, age: int):
    
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("inserted into database")
    else:
        raise TypeError("Enter the correct data type")


insert_patient_data("harsha", 34)



