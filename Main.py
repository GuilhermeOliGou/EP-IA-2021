import pandas as pd

base = pd.read_csv("C:/Users/guilh/OneDrive/Área de Trabalho/Entrega 1/creditcard.csv")

base_sem_classe = base[["Time", "V1", "V2", "V3", "V4", "V5", "V6",
                        "V7", "V8", "V9", "V10", "V11", "V12", "V13",
                        "V14", "V15", "V16", "V17", "V18", "V19", "V20",
                        "V21", "V22", "V23", "V24", "V25", "V26", "V27", "V28", "Amount"]]

#Cálculo de médias

media_Time = base_sem_classe["Time"].mean()
media_V1 = base_sem_classe["V1"].mean()
media_V2 = base_sem_classe["V2"].mean()
media_V3 = base_sem_classe["V3"].mean()
media_V4 = base_sem_classe["V4"].mean()
media_V5 = base_sem_classe["V5"].mean()
media_V6 = base_sem_classe["V6"].mean()
media_V7 = base_sem_classe["V7"].mean()
media_V8 = base_sem_classe["V8"].mean()
media_V9 = base_sem_classe["V9"].mean()
media_V10 = base_sem_classe["V10"].mean()
media_V11 = base_sem_classe["V11"].mean()
media_V12 = base_sem_classe["V12"].mean()
media_V13 = base_sem_classe["V13"].mean()
media_V14 = base_sem_classe["V14"].mean()
media_V15 = base_sem_classe["V15"].mean()
media_V16 = base_sem_classe["V16"].mean()
media_V17 = base_sem_classe["V17"].mean()
media_V18 = base_sem_classe["V18"].mean()
media_V19 = base_sem_classe["V19"].mean()
media_V20 = base_sem_classe["V20"].mean()
media_V21 = base_sem_classe["V21"].mean()
media_V22 = base_sem_classe["V22"].mean()
media_V23 = base_sem_classe["V23"].mean()
media_V24 = base_sem_classe["V24"].mean()
media_V25 = base_sem_classe["V25"].mean()
media_V26 = base_sem_classe["V26"].mean()
media_V27 = base_sem_classe["V27"].mean()
media_V28 = base_sem_classe["V28"].mean()
media_Amount = base_sem_classe["Amount"].mean()

#Definição de máscaras para fazer a atualizar (como recomendado na documentação do Pandas: copia a base, cria as máscaras com a
#condição desejada e depois atualiza usando as máscaras)

base_aux = base_sem_classe.copy()

mask_Time = base_aux["Time"].isnull()
mask_V1 = base_aux["V1"].isnull()
mask_V2 = base_aux["V2"].isnull()
mask_V3 = base_aux["V3"].isnull()
mask_V4 = base_aux["V4"].isnull()
mask_V5 = base_aux["V5"].isnull()
mask_V6 = base_aux["V6"].isnull()
mask_V7 = base_aux["V7"].isnull()
mask_V8 = base_aux["V8"].isnull()
mask_V9 = base_aux["V9"].isnull()
mask_V10 = base_aux["V10"].isnull()
mask_V11 = base_aux["V11"].isnull()
mask_V12 = base_aux["V12"].isnull()
mask_V13 = base_aux["V13"].isnull()
mask_V14 = base_aux["V14"].isnull()
mask_V15 = base_aux["V15"].isnull()
mask_V16 = base_aux["V16"].isnull()
mask_V17 = base_aux["V17"].isnull()
mask_V18 = base_aux["V18"].isnull()
mask_V19 = base_aux["V19"].isnull()
mask_V20 = base_aux["V20"].isnull()
mask_V21 = base_aux["V21"].isnull()
mask_V22 = base_aux["V22"].isnull()
mask_V23 = base_aux["V23"].isnull()
mask_V24 = base_aux["V24"].isnull()
mask_V25 = base_aux["V25"].isnull()
mask_V26 = base_aux["V26"].isnull()
mask_V27 = base_aux["V27"].isnull()
mask_V28 = base_aux["V28"].isnull()
mask_Amount = base_aux["Amount"].isnull()

#Substituição de valores nulos pelas médias

base_aux.loc[mask_Time, "Time"] = media_Time
base_aux.loc[mask_V1, "V1"] = media_V1
base_aux.loc[mask_V2, "V2"] = media_V2
base_aux.loc[mask_V3, "V3"] = media_V3
base_aux.loc[mask_V4, "V4"] = media_V4
base_aux.loc[mask_V5, "V5"] = media_V5
base_aux.loc[mask_V6, "V6"] = media_V6
base_aux.loc[mask_V7, "V7"] = media_V7
base_aux.loc[mask_V8, "V8"] = media_V8
base_aux.loc[mask_V9, "V9"] = media_V9
base_aux.loc[mask_V10, "V10"] = media_V10
base_aux.loc[mask_V11, "V11"] = media_V11
base_aux.loc[mask_V12, "V12"] = media_V12
base_aux.loc[mask_V13, "V13"] = media_V13
base_aux.loc[mask_V14, "V14"] = media_V14
base_aux.loc[mask_V15, "V15"] = media_V15
base_aux.loc[mask_V16, "V16"] = media_V16
base_aux.loc[mask_V17, "V17"] = media_V17
base_aux.loc[mask_V18, "V18"] = media_V18
base_aux.loc[mask_V19, "V19"] = media_V19
base_aux.loc[mask_V20, "V20"] = media_V20
base_aux.loc[mask_V21, "V21"] = media_V21
base_aux.loc[mask_V22, "V22"] = media_V22
base_aux.loc[mask_V23, "V23"] = media_V23
base_aux.loc[mask_V24, "V24"] = media_V24
base_aux.loc[mask_V25, "V25"] = media_V25
base_aux.loc[mask_V26, "V26"] = media_V26
base_aux.loc[mask_V27, "V27"] = media_V27
base_aux.loc[mask_V28, "V28"] = media_V28
base_aux.loc[mask_Amount, "Amount"] = media_Amount

#Normalização

base_aux.loc[:, "Time"] = (base_aux.loc[:, "Time"] - base_aux["Time"].min())/(base_aux["Time"].max() - base_aux["Time"].min())
base_aux.loc[:, "V1"] = (base_aux.loc[:, "V1"] - base_aux["V1"].min())/(base_aux["V1"].max() - base_aux["V1"].min())
base_aux.loc[:, "V2"] = (base_aux.loc[:, "V2"] - base_aux["V2"].min())/(base_aux["V2"].max() - base_aux["V2"].min())
base_aux.loc[:, "V3"] = (base_aux.loc[:, "V3"] - base_aux["V3"].min())/(base_aux["V3"].max() - base_aux["V3"].min())
base_aux.loc[:, "V4"] = (base_aux.loc[:, "V4"] - base_aux["V4"].min())/(base_aux["V4"].max() - base_aux["V4"].min())
base_aux.loc[:, "V5"] = (base_aux.loc[:, "V5"] - base_aux["V5"].min())/(base_aux["V5"].max() - base_aux["V5"].min())
base_aux.loc[:, "V6"] = (base_aux.loc[:, "V6"] - base_aux["V6"].min())/(base_aux["V6"].max() - base_aux["V6"].min())
base_aux.loc[:, "V7"] = (base_aux.loc[:, "V7"] - base_aux["V7"].min())/(base_aux["V7"].max() - base_aux["V7"].min())
base_aux.loc[:, "V8"] = (base_aux.loc[:, "V8"] - base_aux["V8"].min())/(base_aux["V8"].max() - base_aux["V8"].min())
base_aux.loc[:, "V9"] = (base_aux.loc[:, "V9"] - base_aux["V9"].min())/(base_aux["V9"].max() - base_aux["V9"].min())
base_aux.loc[:, "V10"] = (base_aux.loc[:, "V10"] - base_aux["V10"].min())/(base_aux["V10"].max() - base_aux["V10"].min())
base_aux.loc[:, "V11"] = (base_aux.loc[:, "V11"] - base_aux["V11"].min())/(base_aux["V11"].max() - base_aux["V11"].min())
base_aux.loc[:, "V12"] = (base_aux.loc[:, "V12"] - base_aux["V12"].min())/(base_aux["V12"].max() - base_aux["V12"].min())
base_aux.loc[:, "V13"] = (base_aux.loc[:, "V13"] - base_aux["V13"].min())/(base_aux["V13"].max() - base_aux["V13"].min())
base_aux.loc[:, "V14"] = (base_aux.loc[:, "V14"] - base_aux["V14"].min())/(base_aux["V14"].max() - base_aux["V14"].min())
base_aux.loc[:, "V15"] = (base_aux.loc[:, "V15"] - base_aux["V15"].min())/(base_aux["V15"].max() - base_aux["V15"].min())
base_aux.loc[:, "V16"] = (base_aux.loc[:, "V16"] - base_aux["V16"].min())/(base_aux["V16"].max() - base_aux["V16"].min())
base_aux.loc[:, "V17"] = (base_aux.loc[:, "V17"] - base_aux["V17"].min())/(base_aux["V17"].max() - base_aux["V17"].min())
base_aux.loc[:, "V18"] = (base_aux.loc[:, "V18"] - base_aux["V18"].min())/(base_aux["V18"].max() - base_aux["V18"].min())
base_aux.loc[:, "V19"] = (base_aux.loc[:, "V19"] - base_aux["V19"].min())/(base_aux["V19"].max() - base_aux["V19"].min())
base_aux.loc[:, "V20"] = (base_aux.loc[:, "V20"] - base_aux["V20"].min())/(base_aux["V20"].max() - base_aux["V20"].min())
base_aux.loc[:, "V21"] = (base_aux.loc[:, "V21"] - base_aux["V21"].min())/(base_aux["V21"].max() - base_aux["V21"].min())
base_aux.loc[:, "V22"] = (base_aux.loc[:, "V22"] - base_aux["V22"].min())/(base_aux["V22"].max() - base_aux["V22"].min())
base_aux.loc[:, "V23"] = (base_aux.loc[:, "V23"] - base_aux["V23"].min())/(base_aux["V23"].max() - base_aux["V23"].min())
base_aux.loc[:, "V24"] = (base_aux.loc[:, "V24"] - base_aux["V24"].min())/(base_aux["V24"].max() - base_aux["V24"].min())
base_aux.loc[:, "V25"] = (base_aux.loc[:, "V25"] - base_aux["V25"].min())/(base_aux["V25"].max() - base_aux["V25"].min())
base_aux.loc[:, "V26"] = (base_aux.loc[:, "V26"] - base_aux["V26"].min())/(base_aux["V26"].max() - base_aux["V26"].min())
base_aux.loc[:, "V27"] = (base_aux.loc[:, "V27"] - base_aux["V27"].min())/(base_aux["V27"].max() - base_aux["V27"].min())
base_aux.loc[:, "V28"] = (base_aux.loc[:, "V28"] - base_aux["V28"].min())/(base_aux["V28"].max() - base_aux["V28"].min())
base_aux.loc[:, "Amount"] = (base_aux.loc[:, "Amount"] - base_aux["Amount"].min())/(base_aux["Amount"].max() - base_aux["Amount"].min())

print(base_aux.head(10))