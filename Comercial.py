import pandas as pd
import matplotlib.pyplot as plt

# Verifica se as colunas existem
if 'Segmento' in dataset.columns and 'Valor vendido' in dataset.columns:

    # Converte 'Valor vendido' para número
    dataset['Valor vendido'] = pd.to_numeric(dataset['Valor vendido'], errors='coerce')

    # Remove valores nulos
    dataset = dataset.dropna(subset=['Segmento', 'Valor vendido'])

    # Agrupa os dados por Segmento
    agrupado = dataset.groupby('Segmento')['Valor vendido'].sum().reset_index()

    # Ordena do maior para o menor e mantém apenas os 6 maiores
    top6 = agrupado.sort_values(by='Valor vendido', ascending=False).head(6)

    # Cria o gráfico sem background
    fig, ax = plt.subplots(figsize=(9, 5), facecolor='none')
    ax.set_facecolor('none')

    # Gráfico de barras
    ax.bar(top6['Segmento'], top6['Valor vendido'], color='#12239E')

    # Título ajustado com espaçamento
    ax.set_title('', fontsize=22, color='#FFFFFF', pad=30)

    # Remove os títulos dos eixos
    ax.set_xlabel('')
    ax.set_ylabel('')

    # Configura os ticks com cor e tamanho de fonte
    ax.tick_params(axis='x', labelrotation=45, labelcolor='#FFFFFF', labelsize=18)
    ax.tick_params(axis='y', labelcolor='#FFFFFF', labelsize=10)

    # Grade discreta no eixo Y
    ax.grid(axis='y', linestyle='--', alpha=0.3)

    plt.tight_layout()
    plt.show()

else:
    print("")
