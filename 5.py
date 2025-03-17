import seaborn as sns
import matplotlib.pyplot as plt

#Loading dataset
df =sns.load_dataset("iris")
print(df)
sns.barplot(x="species",y="sepal_width",data=df)
plt.title("Title using matplotlib function")
plt.show()