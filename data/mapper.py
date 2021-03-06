import matplotlib.pyplot as plt

hfont = {'fontname':'Lato'}

#draw a simple line chart showing population grown over the last 115 years

years = [1900, 1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]

pops = [1.6, 2.5, 2.6, 3.0, 3.3, 3.6, 4.2, 4.4, 4.8, 5.3, 5.7, 6.1, 6.5, 6.9, 7.3]

# plot out chart with the data above, and also format the line color and width
plt.plot(years, pops, color=(0/255, 100/255, 100/255), linewidth=3.0)

# label on the left hand side
plt.ylabel("World population by Billions")

# label on the bottom of the chart
plt.xlabel("Population growth by year")

# add a title to the chart
plt.title("World Population Growth", pad="20", **hfont)

#run the show method (this lives inside the pyplot package)
#this wil generate a graphic in a new window
plt.show()
