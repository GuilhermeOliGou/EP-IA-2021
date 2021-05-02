import pandas as pd
from TratamentoBase import *

base = pd.read_csv("C:/Users/guilh/OneDrive/Área de Trabalho/Entrega 1/creditcard.csv")

base_aux = base.copy();
base = tratar(base_aux)

print(base.head(15))