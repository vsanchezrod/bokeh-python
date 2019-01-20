from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.iris import flowers
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool, ColumnDataSource


# Se crea un diccionario de colores en función de las distintas especies de flores
# Se construye una columna "color" en flowers y se rellena con los datos del diccionario de colores en función de la especie
# IMPORTANTE: Es necesario hacerlo antes que los ColumnDataSource, para ya tener el valor del color
colormap = {"setosa" : "red", "versicolor" : "green", "virginica" : "blue"}
flowers["color"] = [colormap[x] for x in flowers["species"]]
flowers["size"] = flowers['sepal_width'] * 4

# Se crea una columna para añadir las rutas de las imagenes de las especies
urlmap = {'setosa':'https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg/800px-Kosaciec_szczecinkowaty_Iris_setosa.jpg',
        'versicolor':'https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Blue_Flag%2C_Ottawa.jpg/800px-Blue_Flag%2C_Ottawa.jpg',
        'virginica':'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Iris_virginica.jpg/800px-Iris_virginica.jpg'}
flowers['imgs'] = [urlmap[x] for x in flowers['species']]

# Por cada glyphs, se va a crear un ColumnDataSource con los valores de un dataframe de pandas
setosa = ColumnDataSource(flowers[flowers["species"]=="setosa"])
versicolor = ColumnDataSource(flowers[flowers["species"]=="versicolor"])
virginica = ColumnDataSource(flowers[flowers["species"]=="virginica"])

# Se puede extraer datos de los ColumnDataSource
print(setosa.data["petal_width"])

# Se puede obtener el valor mayor de una columna de un ColumnDataSource
print(max(setosa.data["petal_width"]))

# Tambien se puede pasar el ColumnDataSource los valores de un diccionario
cds = ColumnDataSource(dict(x=[1, 2, 3], y=[4, 5, 6]))
print(cds.data)

# Se pueden añadir más columnas a un ColumnDataSource
cds.add(data=[7, 8, 9], name="z")
print(cds.data)

# Se puede acceder a los valores de una columna
print(cds.data["z"])

# Se multiplica por 4 la lista (no los valores, si no los elementos tal cual)
print(cds.data["z"]*4)

# Para multiplicar los valores por 4
print(i*4 for i in cds.data["x"])


output_file("iris.html")

# Create a figure plot
f = figure()

# Style the Tools
# La f.tools va a ser igual a una lista de herramientas que se muestran en la gráfica. Se importan de bokeh.models
f.tools = [PanTool(), ResetTool()] # Si especificamos la lista de herramientas serán las que se muestren, sino las q vienen por defecto
f.toolbar_location = "above"  # below, left, rigth
f.toolbar.logo = None # Para quitar el logo de bokeh

# Se va a crear una herramienta HoverTool personalizada. Con los tooltips, se elige lo que se quiere mostrar cuando el usuario
# pase el ratón por cualquiera de los elementos que se muestran en el gráfico. Con @_____ especificamos el campo de la tabla al que hace referencia
# Si no se crean los ColumnDataSource, no se muestran los valores de los campos sino ???
hover = HoverTool(tooltips=[("Species", "@species"), ("Sepal Width", "@sepal_width")])

# Otra forma de hacer los tooltips del HoverTool es meter directamente código HTML entre """ """ y los valores de los campos van con @
hover = HoverTool(tooltips="""
    <div>
        <div>
            <img src="@imgs" height="42" alt="@imgs" width="42" style="float: left; margin: 0px 15px 15px 0px;" border="2"></img>
        </div>
        <div>
            <span style="font-size: 25px; font-weight: bold;">@species</span>
        </div>
        <div>
            <span style="font-size: 10px; color: #696;">Petal length: @petal_length</span><br>
            <span style="font-size: 10px; color: #696;">Petal width: @petal_width</span>
        </div>
    </div>
           
""")





# Se añade a la lista de Tools
f.add_tools(hover) # Añadir una herramienta a la lista

# Style the plot area (gráfico)
f.plot_width = 1500
f.plot_height = 650
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

# Adding glyphs
# Ahora los glyphs se le pasa como x e y el nombre de la columna, y como fuente de datos se usa source y se indica el DataColumnSource en el que están los datos a mostrar
f.circle(x="petal_length", y="petal_width", size='size', fill_alpha=0.2, color="color", line_dash=[5,3], legend='Setosa', source=setosa)

f.circle(x="petal_length", y="petal_width", size='size', fill_alpha=0.2, color="color", line_dash=[5,3], legend='Versicolor', source=versicolor)

f.circle(x="petal_length", y="petal_width", size='size', fill_alpha=0.2, color="color", line_dash=[5,3], legend='Virginica', source=virginica)

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



# Bokeh no es capaz de sacar datos de un dataframe de Pandas, por lo que es necesario crear una Column Data Source que se importa de bokeh.models