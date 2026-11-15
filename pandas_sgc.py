import pandas as pd


df = pd.DataFrame({"prezzo": [10, 20, 30]})


def applica_iva(x):
  return x * 1.22


df["con_iva"] = df["prezzo"].apply(applica_iva)

  

