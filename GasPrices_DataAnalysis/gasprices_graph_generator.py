# -*- coding: utf-8 -*-
""" Importing pandas and dataset """
import pandas as pd
url = "2004-2019.tsv"
data = pd.read_csv(url, sep='\t', index_col=0)
data.head()

""" Renaming cols """
data = data.rename(columns=(lambda x: x.replace(" ", "_"))).copy()

""" Converting col from object to numeric """
data["PREÇO_MÉDIO_DISTRIBUIÇÃO"] = data["PREÇO_MÉDIO_DISTRIBUIÇÃO"].replace("-", "")
data["PREÇO_MÉDIO_DISTRIBUIÇÃO"] = data["PREÇO_MÉDIO_DISTRIBUIÇÃO"].replace(" ", "")
data['PREÇO_MÉDIO_DISTRIBUIÇÃO'] = pd.to_numeric(data['PREÇO_MÉDIO_DISTRIBUIÇÃO'])


""" Plotting Graphics """

""" Importing Graphics Libs """
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot') # estilo de gráfico


# Gasoline Graphic
sns.set(style="darkgrid")
f, ax = plt.subplots(figsize=(30, 10))

sns.set_color_codes("pastel")
g = sns.barplot(y="PREÇO_MÉDIO_REVENDA", x="ANO", data=data[data['PRODUTO'] == "GASOLINA COMUM"],
            label="AVERAGE RESELL PRICE", color="r")

sns.set_color_codes("muted")
sns.barplot(y="PREÇO_MÉDIO_DISTRIBUIÇÃO", x="ANO", data=data[data['PRODUTO'] == "GASOLINA COMUM"],
            label="AVERAGE DISTRIBUTION PRICE", color="r")

ax.legend(ncol=2, loc="upper center", frameon=True)
ax.set(ylabel="REAIS PER LITER",
       xlabel="AVERAGE PRICE OF REGULAR GASOLINE PER YEAR ON BRAZIL")
sns.despine(left=True, bottom=True)
plt.savefig("Average price of regular gasoline in Brazil")

# Hydrous Ethanol Graphic
sns.set(style="darkgrid")
f, ax = plt.subplots(figsize=(30, 10))

sns.set_color_codes("pastel")
g = sns.barplot(y="PREÇO_MÉDIO_REVENDA", x="ANO", data=data[data['PRODUTO']=="ETANOL HIDRATADO"],
            label="AVERAGE RESELL PRICE", color="g")

sns.set_color_codes("muted")
sns.barplot(y="PREÇO_MÉDIO_DISTRIBUIÇÃO", x="ANO", data=data[data['PRODUTO']=="ETANOL HIDRATADO"],
            label="AVERAGE DISTRIBUTION PRICE", color="g")

ax.legend(ncol=2, loc="upper center", frameon=True)
ax.set(ylabel="REAIS PER LITER",
       xlabel="AVERAGE PRICE OF HYDROUS ETHANOL PER YEAR ON BRAZIL")
sns.despine(left=True, bottom=True)
plt.savefig("Average price of hydrous ethanol in Brazil")