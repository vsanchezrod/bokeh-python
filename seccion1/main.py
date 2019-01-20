# Gráfico de líneas básico
from bokeh.plotting import figure, output_file, show, save

# prepare some data
x = [1, 2, 3, 4, 5]
y = [14, 15, 12, 14, 20]

# Prepare to static HTML output file
output_file("lines.html")

# Create a new plot with a title and axis labels
p = figure(title="Ejemplo de gráfico", x_axis_label='Día', y_axis_label='Temperatura')

# Add a line renderer with X and Y values, legend and line thickness
# También podría ser círculo (circle) o triangulos (triangle)
p.line(x, y, legend="Temperatura", line_width=2)

# Show the results
show(p)

save(p)  # (Show and save ==> Ambos guardan los datos, pero el método save no lo abre en el navegador)


