from bokeh.plotting import figure, output_file, show
import pandas as pd

df = pd.read_csv("bachelors.csv")
x = df["Year"]
y = df["Engineering"]

p = figure(title="The percentage of women who have received a bachelor's degree over years in USA", x_axis_label='Año', y_axis_label='Número mujeres')
p.line(x, y, legend="Bacherlor's degree", line_width=5)

output_file("bachelor.html")
show(p)

