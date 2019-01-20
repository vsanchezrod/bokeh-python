from bokeh.plotting import figure, output_file, show

x = [3, 7.5, 10]
y = [3, 6, 9]

output_file('triangle.html')

p = figure(title="Ejemplo de gráfico", x_axis_label='Día', y_axis_label='Temperatura')

p.triangle(x, y, legend="Temperatura")

show(p)