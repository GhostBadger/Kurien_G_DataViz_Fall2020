import matplotlib.pyplot as plt

#generate a pie chart with our olympic data

x = ["Ice Hockey", "Everything Else"]
y = [350, 274]

plt.bar(x, y, width = 0.5, color = "orange")
plt.title("Ice Hockey Win Prevalence", pad="10")


plt.ylabel("Total medals for event")


plt.xlabel("Events")

plt.show()
