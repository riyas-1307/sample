import matplotlib.pyplot as plt
'''x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y)
plt.show()

values = [3, 8, 1, 10, 5]
plt.plot(values)
plt.show()


x = [1, 2, 3, 4, 5]
y = [10, 25, 15, 40, 30]

plt.plot(x, y, marker="*")
plt.show()


x = [1, 2, 3, 4, 5]
y = [10, 25, 15, 40, 30]

plt.plot(x, y, linestyle="-.", color="r",marker="*")
plt.show()

x = [1, 2, 3, 4, 5]
y = [10, 25, 15, 40, 30]

plt.plot(
    x, y,
    marker="o",
    markersize=15,
    markerfacecolor="red",
    markeredgecolor="blue",
    markeredgewidth=2
)
plt.show()


x = [1, 2, 3, 4, 5]
y = [10, 25, 15, 40, 30]

plt.plot(x, y, linewidth=4, linestyle=":", color="blue",alpha=1)
plt.show()


x = [2020, 2021, 2022, 2023, 2024]
y = [100, 150, 130, 200, 180]

plt.plot(x, y, marker="o", color="blue")
plt.xlabel("Year")
plt.ylabel("Sales (in thousands)")
plt.title("Monthly Sales", loc="center",pad=20)
plt.show()


x = [1, 2, 3, 4, 5]
y = [10, 25, 15, 40, 30]

title_font = {"family": "serif", "color": "darkblue", "size": 20, "weight": "bold"}
label_font = {"family": "sans-serif", "color": "darkred", "size": 13}

plt.plot(x, y, marker="o", color="steelblue")
plt.title("Sales Performance", fontdict=title_font)
plt.xlabel("Week", fontdict=label_font)
plt.ylabel("Units Sold", fontdict=label_font)
plt.show()
'''

x = [1, 2, 3, 4, 5]
y = [10, 25, 15, 40, 30]

plt.plot(x, y, marker="o")
plt.grid(True)
plt.show()
