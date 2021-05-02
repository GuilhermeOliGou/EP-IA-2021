import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from TratamentoBase import *

base = pd.read_csv("C:/Users/guilh/OneDrive/Área de Trabalho/Entrega 1/creditcard.csv")

base_aux = base.copy();
base = tratar(base_aux)

y = base.loc[:,"Class"]

base = base.loc[:,["Time", "V1", "V2", "V3", "V4", "V5", "V6",
                        "V7", "V8", "V9", "V10", "V11", "V12", "V13",
                        "V14", "V15", "V16", "V17", "V18", "V19", "V20",
                        "V21", "V22", "V23", "V24", "V25", "V26", "V27", "V28", "Amount"]]

X_train, X_test, y_train, y_test  = train_test_split(base, y, test_size=0.2, random_state=12345)

vizinhanca = KNeighborsClassifier(n_neighbors=3)
#vizinhanca = KNeighborsClassifier(n_neighbors=3,metric='manhattan')
vizinhanca.fit(X_train,y_train)

print(vizinhanca.predict(X_test))