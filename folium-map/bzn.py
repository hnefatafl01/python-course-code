import folium
map=folium.Map(location=[45.6770, -111.0429],zoom_start=12,tiles="Stamen Terrain")
map.add_child(folium.Marker([45.6770, -111.0429],popup='Bozeman',icon=folium.icon(icon_color='red')))
map.add_child(folium.Marker([45.8174, -110.8966],'Bridger Bowl',icon=folium.icon(icon_color='green')))
map.save(outfile='bzn.html')
