from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.iris import flowers
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool
# from screeninfo import get_monitors

output_file("iris.html")

# Create a figure plot
f = figure()


# Style the Tools
# La f.tools va a ser igual a una lista de herramientas que se muestran en la gráfica. Se importan de bokeh.models
f.tools = [PanTool(), ResetTool()] # Si especificamos la lista de herramientas serán las que se muestren, sino las q vienen por defecto
f.add_tools(HoverTool()) # Añadir una herramienta a la lista
f.toolbar_location = "above"  # below, left, rigth
f.toolbar.logo = None # Para quitar el logo de bokeh


# Style the plot area (gráfico)
f.plot_width = 1500
f.plot_height = 650

# Si se utiliza la lirería screeninfo import get_monitors, se puede determinar el tamaño del plot en función de la pantalla
# f.plot_width= get_monitors()[0].width #get_monitors is part of the screeninfo module imported above
# f.plot_height= get_monitors()[0].height-50 #get_monitors is part of the screeninfo module imported above



f.background_fill_color = "olive" # Color de fondo
f.background_fill_alpha = 0.3 # Transparencia (0 es la máxima transparencia)
# f.border_fill_color = "green" # Color del borde que rodea al gráfico (incluye la zona de la toolBar)

# Formas de poner colores
# f.background_fill_color="olive"
# f.background_fill_color="#CD5C5C"
# f.background_fill_color=(205, 92, 92)
# f.background_fill_color=(205, 92, 92, 0.3)

# Style the title
f.title.text = "Flowers"
f.title.text_color = "olive"
f.title.text_font = "times"
f.title.text_font_size = "25px"
f.title.align = "center"
f.title_location = "above"  # Posición del title con respecto al gráfico: above, below, left, rigth,

# Style the axis
f.axis.minor_tick_line_color = "blue" # Cambia el color de las rayas de los ejes
    # f.xaxis.minor_tick_line_color = "red" # Cambia solo las rayas del eje X
    # f.yaxis.minor_tick_line_color = "red" # Cambia solo las rayas del eje Y

f.yaxis.major_label_orientation = "horizontal" # Posición de las etiquetas del eje Y (horizontal o vertical)

    # f.xaxis.visible = False # No se visualiza el eje X. True es el valor por defecto, si no se quiere mostrar se usa False
    # f.xaxis.minor_tick_line_color = None # Para que no se visualicen las rayas intermedias de un eje

f.xaxis.minor_tick_in = -6 # La longitud en pixeles de lo que entran las rayas dentro del gráfico. Se pueden usar valores negativos
    # f.xaxis.minor_tick_out = 10 # La longitud en pixeles de lo que salen las rayas fuera del gráfico Se pueden usar valores negativos

# Texto de las etiquetas de los ejes
f.xaxis.axis_label = "Petal length"
f.yaxis.axis_label = "Petal width"
f.axis.axis_label_text_color = "blue" # Color de las etiquetas de los ejes
f.axis.major_label_text_color = "orange" # Color del texto de los ejes major

# Geometría de los ejes (axis)
# Para establecer los rangos de los ejes, es necesario importar Range1d from bokeh.models
f.x_range = Range1d(start=0, end=10)
f.y_range = Range1d(start=0, end=5)
f.xaxis.bounds = (2, 6) # Solo pone los rangos desde el 2 al 5
f.xaxis[0].ticker.desired_num_ticks = 2  # Especifica el número de rayas mayor que se quieren en el eje. Es necesario poner el [0] porque es una lista de figuras
f.yaxis[0].ticker.desired_num_ticks = 2
f.yaxis[0].ticker.num_minor_ticks = 10 # Especifica el número de rayas minor que se quieren en el eje. Es necesario poner el [0] porque es una lista de figuras


# Style the grid (la cuadrícula)
f.xgrid.grid_line_color = None # Para cambiar el color de las líneas del grid del eje X o no verlas con None
f.ygrid.grid_line_alpha = 0.6 # Transparencia del grid del eje Y
f.grid.grid_line_dash = [5, 3]  # No se que hace


# Se crea un diccionario de colores en función de las distintas especies de flores
colormap = {"setosa" : "red", "versicolor" : "green", "virginica" : "blue"}

# Se construye una columna "color" en flowers y se rellena con los datos del diccionario de colores en función de la especie

flowers["color"] = [colormap[x] for x in flowers["species"]]

# La expresión anterior es igual a este código
#listaColores = []
#
#for x in flowers["species"]:
#    listaColores.append(colormap[x])
#
#flowers["color"] = listaColores;



# Los datos vienen importados de ejemplos de bokeh. X e y son columnas de los datos integrados en flowers (que es un dataframe)

# f.circle (x,y, etc) # Los puntos tendrán un tamaño en función de su anchura de sepalo multiplicado por 4 # Transparencia con fill_alpha, y color con color y poniendo color o usando variable
# Se va a añadir una nueva columna "color" en los datos de flowers a través de panda, donde se va a establecer un color para los circulos. Line_dash para poner las lineas discontinuas

f.circle(x=flowers["petal_length"][flowers["species"] == "setosa"], y=flowers["petal_width"][flowers["species"] == "setosa"], size=flowers["sepal_width"][flowers["species"] == "setosa"]*4, fill_alpha=0.2, color=flowers["color"][flowers["species"] == "setosa"],
         line_dash=[5, 3], legend="Setosa")

f.circle(x=flowers["petal_length"][flowers["species"] == "versicolor"], y=flowers["petal_width"][flowers["species"] == "versicolor"], size=flowers["sepal_width"][flowers["species"] == "versicolor"]*4, fill_alpha=0.2, color=flowers["color"][flowers["species"] == "versicolor"],
         line_dash=[5, 3], legend="Versicolor")

f.circle(x=flowers["petal_length"][flowers["species"] == "virginica"], y=flowers["petal_width"][flowers["species"] == "virginica"], size=flowers["sepal_width"][flowers["species"] == "virginica"]*4, fill_alpha=0.2, color=flowers["color"][flowers["species"] == "virginica"],
         line_dash=[5, 3], legend="Virginica")

# Para poder tener 3 leyendas en vez de una, se ha dividido los datos en 3 partes en función del nombre de la especie. Y se han incluido 3 nombres diferentes de leyenda

# Style the legend
f.legend.location = "top_left" # Posición de la leyenda
# f.legend.location = (70, 70) # También se puede posicionar por pixeles
f.legend.background_fill_alpha = 0.3 # Transparencia del cuadro de la leyenda
f.legend.border_line_color = None # Borde del cuadro de la leyenda
f.legend.margin = 10 # Margenes de la leyenda con respecto a la location establecida. 10px top y 10px left
f.legend.padding = 18 # No me va el padding
f.legend.label_text_color = "olive"
f.legend.label_text_font = "times"





# Save and show
show(f)

# Explorar propiedades
print(dir(f))
print(dir(f.axis))
print(dir(f.grid))
import bokeh.models
print(dir(bokeh.models.tools))
print(dir(f.legend))