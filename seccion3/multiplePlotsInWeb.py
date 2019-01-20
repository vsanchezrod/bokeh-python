from bokeh.plotting import figure, output_file, show, gridplot

# gridPlot es lo que permite que se puedan tener varios plots

output_file("layout.html")

# Los datos van a ser listas de rangos (no incluye el valor maximo)
x1, y1 = list(range(0, 10)), list(range(10, 20))
x2, y2 = list(range(20, 30)), list(range(30, 40))
x3, y3 = list(range(40, 50)), list(range(50, 60))

# Crear new plot
f1 = figure(width=250, plot_height=250, title="Circles")
f1.circle(x1, y1, size=10, color="navy", alpha=0.5)

# Crear new plot
f2 = figure(width=250, plot_height=250, title="Triangles")
f2.triangle(x2, y2, size=10, color="firebrick", alpha=0.5)

# Crear new plot
f3 = figure(width=250, plot_height=250, title="Squares")
f3.square(x3, y3, size=10, color="olive", alpha=0.5)

# Se ponen todos los plots en un mismo layout
# Los grids se construyen mediante rows: row 1 f1 y f2, row 2 nada y luego f3
f = gridplot([[f1, f2], [None, f3]])

show(f)