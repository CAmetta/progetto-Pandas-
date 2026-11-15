import pandas as pd

class primo:

    def __init_ (self,a,b):
    
        self.a = a 
        self.b = b 
        
    def calcolo (a,b):
    
        c = -(b/a)
        
        print (f'il risultato è {c}')
        
primo.calcolo(1,2)


df = pd.DataFrame({"prezzo": [10, 20, 30]})


def applica_iva(x):
  return x * 1.22


df["con_iva"] = df["prezzo"].apply(applica_iva)

  

