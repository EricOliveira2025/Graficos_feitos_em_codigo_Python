import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Renomear colunas
dataset.columns = ["Etapa", "Custo_Total"]

# Limpar dados
df = dataset.dropna()

# Estilo sem fundo
sns.set(style="white")

# Criar figura com fundo transparente
fig, ax = plt.subplots(figsize=(9, 6), facecolor='none')

# Gráfico violin com boxplot embutido e cores vibrantes
sns.violinplot(
    data=df,
    x="Etapa",
    y="Custo_Total",
    inner="box",
    palette="Set1",  # paleta com cores mais vivas
    scale="width",
    ax=ax
)

# Ajustar rótulos para fundo escuro
ax.set_title("", fontsize=14, weight="bold", color='white')
ax.set_xlabel("Etapa da Obra", color='white')
ax.set_ylabel("Custo Total (R$)", color='white')
ax.tick_params(colors='white')
sns.despine()

# Manter fundo da área do gráfico transparente
ax.set_facecolor("none")

# Layout final
plt.tight_layout()
plt.show()
