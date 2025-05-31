import matplotlib.pyplot as plt

x_values = range(1, 5001)
cubes = [x**3 for x in x_values]

# Create a Figure with an Axis.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# Make plot.
ax.scatter(x_values, cubes, c=cubes, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes.
ax.set_title('Cubes', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)
ax.ticklabel_format(style='plain')

# Show plot.
plt.show()