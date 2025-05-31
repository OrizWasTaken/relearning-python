import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # Make a random walk.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(16,9), subplot_kw={'aspect':1})
    ax.plot(rw.x_values, rw.y_values, zorder=0)

    # Emphasize the start and end positions.
    ax.scatter(rw.start_x, rw.start_y, s=50, c='green', zorder=1)
    ax.scatter(rw.end_x, rw.end_y, s=50, c='red', zorder=1)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    # Make a new random walk?
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break