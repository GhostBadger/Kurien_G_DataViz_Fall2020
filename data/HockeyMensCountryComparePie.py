import matplotlib.pyplot as plt

#generate a pie chart with our olympic data

values = [250, 178, 168, 167]
colors = ['Red', 'Yellow','Purple','Blue']
labels = ["Canada", "Sweden", "USSR", "USA"]
explode = (0, 0.1)

plt.pie(values, labels=labels, colors=colors)
plt.title("Top Countries in the game of Ice Hockey", pad="20")

plt.show()

