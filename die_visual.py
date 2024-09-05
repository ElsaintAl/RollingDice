from die import Die

from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create a D6 and a D10.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for _ in range(1_000)]

# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(1, max_result + 1)]


# Visualize the results.
x_values = list(range(1, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
m_layout = Layout(title='Result of rolling 2D6 dices 1_000 times',
                  xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': m_layout}, filename='2d6.html')
