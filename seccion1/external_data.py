# Gráfico de líneas básico
from bokeh.plotting import figure, output_file, show
import pandas

# prepare some data
# Crear un dataframe con pandas y los datos de un csv
df = pandas.read_csv("data.csv")

# Se crean dos variables que recogen los valores de las columnas x e y del .csv
x = df["x"]
y = df["y"]

# Prepare to static HTML output file
output_file("lines_from_csv.html")

# Create a new plot with a title and axis labels
p = figure(title="Ejemplo de gráfico", x_axis_label='Día', y_axis_label='Temperatura')

# Add a line renderer with X and Y values, legend and line thickness
# También podría ser círculo (circle) o triangulos (triangle)
p.line(x, y, legend="Temperatura", line_width=2)

# Show the results
show(p)

# Imprime la columna llamada x
print(df["x"])