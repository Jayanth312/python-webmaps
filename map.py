import folium
import pandas
data = pandas.read_csv("/webmapindia/Book1.csv")
lati = list(data['latitude'])
lngi = list(data['longitude'])
name = list(data['State/UTs'])
positive = list(data['Confirmed'])
recovered = list(data['Recovered'])
not_recoverd = list(data['Active'])
Deaths = list(data['Deceased'])
Names  = folium.FeatureGroup(name="State.Names")
for lts,lngs,names in zip(lati,lngi,name):
    Names.add_child(folium.CircleMarker(location =[lts,lngs],radius=6,popup=str(names),fill_color='green',color = None,fill= True ,fill_opacity = 0.7))

Out = folium.FeatureGroup(name="Outline")
Out.add_child(folium.GeoJson(data=open("/webmapindia/13.1 world.json.json",'r',encoding='utf-8-sig').read(),
style_function = lambda x : {'fillColor':"black"}))
def color(x):
        if x >= 100000:
            return 'red'
        elif x >= 10000:
            return 'orange'
        elif x >= 5000:
            return 'lightblue'
        else:
            return 'green'

corona = folium.FeatureGroup(name="Corona Rough Sketch")
for lts,lngs,names,pos,recover,not_recover,Death in zip(lati,lngi,name,positive,recovered,not_recoverd,Deaths):
    corona.add_child(folium.Marker(location=[lts,lngs],popup='Positive :'+str(pos)+'\n'+'Recovered :'+str(recover)+'\n'+'Active :'+str(not_recover)+'\n'+'Deceased :'+str(Death), icon = folium.Icon(color=color(pos))))
map = folium.Map(location=[20.593684,78.96288])
map.add_child(Names)
map.add_child(Out)
map.add_child(corona)
map.add_child(folium.LayerControl())
map.save("India.html")
print('sucess')
