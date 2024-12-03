import folium
import pandas

map= folium.Map(location= [39.474416, -0.375389], zoom_start=15)


data= pandas.read_csv("horchaterias.txt")
nombres= list(data["Nombre"])
latitudes= list(data["Latitud"])
longitudes= list(data["Longitud"])
telefonos= list(data["Teléfono"])

dic_coordenadas={}

for i in range(len(longitudes)):
    dic_coordenadas[nombres[i]]= [latitudes[i], longitudes[i], telefonos[i]]

#dic_coordenadas= {"Horchatería Fabián":[39.472042, -0.375983, 1223], "Santa Catalina":[39.473915, -0.376243], "Horchatería Daniel": [39.474006, -0.374921] , "Horchatería Subies": [39.478135, -0.374855], "Horchatería El Collado": [39.474153, -0.377764]}
html = """ Nombre Horchatería:<br> 
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br><br>
Teléfono: %s
"""


def decidir_color(numero):
    ultimo_digito= numero[-1]
    if int(ultimo_digito) % 2 ==0:
        return "red"
    else:
        return "green"
    

# CAPA DE MARCADORES
fgh= folium.FeatureGroup(name= "Horchaterías")

for nombre in dic_coordenadas:
    iframe = folium.IFrame(html=html % (nombre, nombre, dic_coordenadas[nombre][-1]), width=200, height=100)
    fgh.add_child(folium.CircleMarker(location=dic_coordenadas[nombre][:2], radius=8, fill_color= "yellow", fill_opacity= 0.8, popup=folium.Popup(iframe) , color= decidir_color(dic_coordenadas[nombre][-1])))


# CAPA DE ZONAS
fgz= folium.FeatureGroup(name= "Zonas y Población")

# VAMOS A AÑADIR POLÍGONOS PARA DIFERENCIAR FRONTERAS DE PAÍSES
fgz.add_child(folium.GeoJson(data=open("world.json","r", encoding= "utf-8-sig").read(), 
style_function= lambda x: {"fillColor":"cyan" if x["properties"]["POP2005"]<10000000
else "blue" if 10000000 <= x["properties"]["POP2005"] < 20000000
else "yellow"}))



map.add_child(fgh)
map.add_child(fgz)

map.add_child(folium.LayerControl())

map.save("Map1.html")