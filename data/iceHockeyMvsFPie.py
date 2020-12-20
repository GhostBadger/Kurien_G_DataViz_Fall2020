import matplotlib.pyplot as plt

#generate a pie chart with our olympic data

values = [71, 101]
colors = ['blue', 'Pink']
labels = ["Males", "Females"]
explode = (0, 0.1)

plt.pie(values, labels=labels, colors=colors,explode=explode)
plt.title("Gender Ratio in Ice Hockey, Canada Winter Olympics", pad="20")

plt.show()
