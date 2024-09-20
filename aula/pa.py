import seaborn as sns
import matplotlib.pyplot as plt

# Dados de exemplo
data = sns.load_dataset("iris")

# Criando gráfico
sns.scatterplot(x="sepal_length", y="sepal_width", data=data)
plt.show()
