# O código a seguir para criar um dataframe e remover as linhas duplicadas sempre é executado e age como um preâmbulo para o script: 

# dataset = pandas.DataFrame(Tempo total de manutenção (horas), Custo de peças compradas, Valor gasto (R$), Valor total (HH + Peças), Ciclo de vida dos equipamentos (anos), Criticidade do equipamento, Qtd_Falhas)
# dataset = dataset.drop_duplicates()

# Cole ou digite aqui seu código de script:

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Renomear colunas para nomes simples (garantir que sejam válidas)
dataset.columns = [
    "Tempo total de manutenção (horas)", "Custo de peças compradas", "Valor gasto (R$)",
    "Valor total (HH + Peças)"
]

# Remover valores ausentes
dados = dataset.dropna()

# Estilo visual sem grid ou fundo
sns.set_style("white")  # Remove grid principal

# Gráfico de pares com cor personalizada
g = sns.pairplot(
    dados,
    diag_kind="kde",  # tipo de gráfico na diagonal
    plot_kws={
        "alpha": 0.8, "s": 60, "edgecolor": "none", "color": "#011184"
    },
    diag_kws={
        "fill": True, "color": "#011184", "linewidth": 0
    },
    corner=True
)

# Remover título geral da figura
g.fig.suptitle("")  # Garante que não há título

# Deixar o fundo da figura branco
g.fig.patch.set_alpha(0.0)  # Torna fundo da figura totalmente transparente

# Remove fundo dos eixos (de cada subplot)
for ax in g.axes.flat:
    if ax is not None:
        ax.set_facecolor("white")  # ou use (1,1,1,0) para transparência
        ax.patch.set_alpha(0.0)  # Torna fundo do gráfico transparente

plt.tight_layout()
plt.show()
