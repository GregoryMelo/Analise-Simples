# Projeto de Análise de Vendas Simples

Este projeto é uma análise simples das vendas de uma loja de roupas usando pandas, matplotlib e seaborn. O objetivo é identificar os produtos mais vendidos e gerar insights visuais a partir dos dados.

## Descrição

Desenvolvi um sistema que:
1. Lê dados de vendas a partir de uma tabela Excel.
2. Realiza tratamento e limpeza dos dados.
3. Analisa as vendas para identificar os produtos mais vendidos.
4. Gera gráficos visualmente apelativos para facilitar a interpretação dos dados.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação.
- **pandas**: Para manipulação e análise dos dados.
- **matplotlib**: Para criação dos gráficos.
- **seaborn**: Para estilização dos gráficos.

## Como Usar

1. Certifique-se de que o arquivo Excel está no diretório correto e nomeado como `DataFrame.xlsx`.

2. Execute o script principal para realizar a análise.
    ```bash
    python script_principal.py
    ```

3. Confira os gráficos gerados e os dados obtidos.

## Código

Aqui está a estrutura do codigo:
```python
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
