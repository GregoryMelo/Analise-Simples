import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('DataFrame.xlsx')
data = df.copy().dropna()
data['Data'] = pd.to_datetime(data['Data'])
data['Total'] = data['Quantidade'] * data['Preco_unitario'].astype(float)
data['Produto'] = data['Produto'].str.strip()

produtos_agrupados = data.groupby('Produto')['Quantidade'].sum().reset_index()
top_5_produtos = produtos_agrupados.sort_values(by='Quantidade', ascending=False).head(5)

sns.set_style("white")
f, ax = plt.subplots(figsize=(20, 5))
ax.set_facecolor('white')
bars = sns.barplot(data=top_5_produtos, x='Produto', y='Quantidade', color="lightblue", ax=ax)
ax.bar_label(ax.containers[0], padding=0.3, fontsize=14)
ax.set_title("Top 5 Produtos Mais Vendidos", fontsize=24)
ax.set_xlabel("Produtos", fontsize=18)
ax.set_ylabel("Quantidade", fontsize=18)
ax.set_ylim((0, top_5_produtos['Quantidade'].max() + 5))
plt.show()
