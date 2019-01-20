from bokeh.plotting import figure, output_file, show

output_file("students.html")

# Establecer los ejes de la figura con datos no númericos x_range e y_range
f = figure(x_range=["F", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"],
           y_range=["F", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"])

f.circle(x=["A", "B"], y=["C", "D"], size=8)

show(f)