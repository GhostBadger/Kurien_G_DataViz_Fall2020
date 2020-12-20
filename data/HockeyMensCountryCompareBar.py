import matplotlib.pyplot as plt

#generate a pie chart with our olympic data

x = ["Canada", "Sweden", "USSR", "USA"]
y = [250, 178, 168, 167]

plt.bar(x, y, width = 0.5, color = "orange")
plt.title("Gender Ratio in Ice Hockey, Canada Winter Olympics", pad="10")


plt.ylabel("Medals Won")


plt.xlabel("Top Countries")

plt.show()
