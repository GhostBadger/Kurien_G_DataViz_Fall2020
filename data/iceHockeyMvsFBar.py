import matplotlib.pyplot as plt

#generate a pie chart with our olympic data

x = ["Males", "Females"]
y = [71, 101]

plt.bar(x, y, width = 0.5, color = "orange")
plt.title("Gender Ratio in Ice Hockey, Canada Winter Olympics", pad="10")


plt.ylabel("Number of Players")


plt.xlabel("Genders")

plt.show()
