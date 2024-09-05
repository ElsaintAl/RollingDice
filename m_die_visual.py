import matplotlib.pyplot as plt

from die import Die

# Create a D6 die.
die = Die()


# Make some rolls, and store results in a list.
results = [die.roll() for _ in range(1_000)]

# Analyze the results.
max_result = die.num_sides
frequencies = [results.count(value) for value in range(1, max_result + 1)]

print(frequencies)

plt.style.use('classic')

fig, ax = plt.subplots(figsize=(10, 4), dpi=128)

ax.bar(x=range(1, len(frequencies) + 1), color='r', height=frequencies, width=0.5, )

plt.show()
