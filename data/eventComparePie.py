import matplotlib.pyplot as plt

#generate a pie chart with our olympic data

values = [350, 274]
colors = ['blue', 'orange']
labels = ["Ice Hockey", "Everything Else"]



plt.pie(values, labels=labels, colors=colors)
plt.title("Ice Hockey Win Prevalence", pad="20")

plt.show()
