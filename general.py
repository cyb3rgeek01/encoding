import pandas as pd

def Onehot_encoding(df):
    objdf = df.select_dtypes(include='object')
    othdf = df.select_dtypes(exclude='object')

    objcols = objdf.columns
    uni = pd.DataFrame()

    for i in objcols:
        uniq=objdf[i].unique()
        for j in uniq:
            uni[j] = (objdf[i] == j).astype(int)

    return pd.concat([othdf, uni], axis=1)

def ordinal_encoding(df):
    objdf = df.select_dtypes(include='object')
    othdf = df.select_dtypes(exclude='object')

    objcols = objdf.columns
    uni = pd.DataFrame()

    for i in objcols:
        uniq = objdf[i].unique()
        d = {}
        l = []
        for j in range(len(uniq)):
            d[uniq[j]] = j+1
        l = [d[k] for k in objdf[i]]
        uni[i] = pd.Series(l)
    
    return pd.concat([othdf, uni], axis=1)
