from die import Die
import matplotlib.pylab as plt

# Create three dice.
d5 = Die(5)
d6 = Die()
d8 = Die(8)

# Make some rolls, and store results in a list.
max_result = d5.num_sides + d6.num_sides + d8.num_sides
poss_results = range(3, max_result+1)
results = [(d5.roll()+d6.roll()+d8.roll()) for _ in range(1_000_000)]

# Analyze the results.
frequencies = [results.count(poss_result) for poss_result in poss_results]

# Plot the results.
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(16,9))
ax.bar(poss_results, frequencies)
plt.xticks(range(3, max_result+1))

# Set chart title and label axes.
title = "Results of Rolling two D8s 50,000 Times"
ax.set_title(title, fontsize=24)
ax.set_xlabel('Result', fontsize=14)
ax.set_ylabel('Frequency of Result', fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

plt.show()