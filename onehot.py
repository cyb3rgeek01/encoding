import numpy as np
import pandas as pd


lungs_condition2 = {
    "name":["alex","alexa","bhoomika","charu","dinesh","ela","falguni","gokul","himanshu","isha","jaitra","kotim","lawd"],
    "age":[23,24,18,18,18,34,45,17,19,42,20,92,100],
    "region of existence":["nyc","manhattan","delhi","jaipur","indore","tokyo","delhi","delhi","shimal","chennai","hyderabad","chennai","delhi"],
    "condition":["medium","good","medium","good","good","medium","poor","poor","poor","good","good","medium","medium"],
    "socre of lung ":[5,3,6,2,4,6,9,8,8,3,2,7,6]
}

def onehotencoder_custom(lungs_condition2):
        lung_database2 = pd.DataFrame(lungs_condition2)
        favourable_col = lung_database2.select_dtypes(include='object').columns
        encodable_col = [col for col in favourable_col if lung_database2[col].nunique()<=10 and lung_database2[col].nunique()>3]

        for col in encodable_col:
            no_unique_values = lung_database2[col].unique()
            for value in no_unique_values:
                lung_database2[value] = (lung_database2[col] == value).astype(int)

        lung_database2 = lung_database2.drop(encodable_col,axis=1)
        return lung_database2
