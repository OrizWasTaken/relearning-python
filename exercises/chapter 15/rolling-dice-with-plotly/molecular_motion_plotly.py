import plotly.express as px
from random_walk import RandomWalk

while True:
    # Make a random walk.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the points in the walk.
    x_axis = rw.x_values
    y_axis = rw.y_values
    fig = px.line(x=x_axis, y=y_axis)

    # plt.show()
    fig.show()

    # Make a new random walk?
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break