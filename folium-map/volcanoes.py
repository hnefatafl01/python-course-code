import pandas
import folium

df = pandas.read_csv("Volcanoes-USA.txt")

map = folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=5, tiles="Mapbox bright")

def color(elevation):
    minimum = int(min(df['ELEV']))
    step = int((max(df['ELEV']) - minimum) / 3)

    if elevation in range(minimum, minimum + step):
        col='green'
    elif elevation in range(minimum + step, minimum + step * 2):
        col='orange'
    else:
        col='red'
    return col

fg = folium.FeatureGroup(name='Volcano Locations')

for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    map.add_child(folium.Marker(location = [lat,lon], popup = name, icon = folium.Icon(color = color(elev), icon_color = 'green')))

map.add_child(fg)

map.add_child(folium.GeoJson(data=open('world-geojson-from-ogr.json',
encoding="utf-8-sig"),
name = 'World Population',
style_function = lambda x: { 'fillColor':'green' if x['properties']['POP2005'] > 10000000 else 'orange' if 10000000 < x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(folium.LayerControl())

map.save(outfile = 'volcanoes.html')
