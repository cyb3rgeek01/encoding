import pandas as pd
import numpy as np
from pandas.core.interchange.from_dataframe import categorical_column_to_series

lungs_condition = {
    "name":["alex","alexa","bhoomika","charu","dinesh","ela","falguni","gokul","himanshu","isha","jaitra","kotim","lawd"],
    "age":[23,24,18,18,18,34,45,17,19,42,20,92,100],
    "region of existence":["nyc","manhattan","delhi","jaipur","indore","tokyo","delhi","delhi","shimal","chennai","hyderabad","chennai","delhi"],
    "condition":["medium","good","medium","good","good","medium","poor","poor","poor","good","good","medium","medium"],
    #"test":["low","low","low","low","low","low","low","low","low","low","low","low","low"],
    "socre of lung ":[5,3,6,2,4,6,9,8,8,3,2,7,6]
}

def key_transformation(lung_condition):
    lung_database = pd.DataFrame(lungs_condition)
    categorical_columns = lung_database.select_dtypes(include='object').columns
    encodable_columns = [col for col in categorical_columns if lung_database[col].nunique() <= 3]
    for cols in encodable_columns:
        lung_database[cols] = lung_database[cols].replace({
            "poor":0,
            "medium":1,
            "good":2,
            "high":2,
            "low":0,
            "bad":0,
            "average":1,
            "big":2,
            "small":0,
            "major":2,
            "minor":0
        })

    return lung_database

new_database = key_transformation(lungs_condition)
print(new_database)
