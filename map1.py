import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location = [49.58, -120.88], zoom_start = 6, tiles = 'Mapbox Bright')

fg = folium.FeatureGroup(name = "My Map")
fg.add_child(folium.Marker(location = [49.2614, -123.2459], popup = "I study Computer Science at UBC !", icon = folium.Icon(color='blue', icon = 'home')))
fg.add_child(folium.Marker(location = [49.8815, -119.4625], popup = "My first Co-Op !", icon = folium.Icon(color='blue', icon = 'flag')))

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 2000:
        return 'orange'
    else:
        return 'red'

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location = [lt, ln], radius = 6, popup = f'The elevation is {str(el)} m.', fill_color = color_producer(el), color = 'grey', fill = True, fill_opacity = 0.7))

map.add_child(fg)

map.save("Map1.html")
