# Generating Data

- Matplotlib is an object-oriented plotting library.

- `pyplot` is a `matplotlib` module that provides an implicit, MATLAB-like, way of plotting.

- It's a convention to import the `pyplot` module using the alias `plt`.

  ```python
  import matplotlib.pyplot as plt
  ```

- `axes`: an **area** where points can be specified in terms of x-y coordinates (or theta-r in a polar plot, x-y-z in a 3D plot, etc.).

- `figure`: the entire drawing or window which can contain one or more `axes`.

- `plot`: a function that plots y versus x as lines and/or markers on an Axes.

- Functions, like `plot`, automatically create Figure and/or Axes objects to plot on if either objects don't already exist.

- Matplotlib provides an object-oriented approach to creating Figures and Axes, and ploting graphs on them.

- It's a convention to create a Figure with an Axes using the `pyplot.subplots` function.

  ```python
  import matplotlib as plt
  fig, ax = plt.subplots() # Returns figure and axes (or array of axes) objects in a tuple.
  ```

- `plt.show`: a function that opens Matplotlib’s viewer and displays all open figures.
