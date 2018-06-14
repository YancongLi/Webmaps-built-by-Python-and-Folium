import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[43.07, -105.30],
                 zoom_start=3, tiles='Mapbox Bright')

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[
             49.2614, -123.2459], popup="I study Computer Science at UBC !", icon=folium.Icon(color='blue', icon='home')))
fg.add_child(folium.Marker(location=[
             49.8815, -119.4625], popup="My first Co-Op !", icon=folium.Icon(color='blue', icon='flag')))

fgv = folium.FeatureGroup(name="Volcanoes_USA")


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 2000:
        return 'orange'
    else:
        return 'red'


for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=f'The elevation is {str(el)} m.', fill_color=color_producer(
        el), color='grey', fill=True, fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()), style_function=lambda x: {
    'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)
map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map1.html")
# In command line, Map1.html will be generated if you run: python3 map1.py
