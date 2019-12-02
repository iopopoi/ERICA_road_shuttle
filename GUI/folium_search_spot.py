import folium
from folium import plugins
from folium.plugins import Search
from latitude_and_longtitude import loca, lati, longti


points = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "name": "셔틀콕"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [longti['셔틀콕'], lati['셔틀콕']]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "name": "제1공학관"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [longti['제1공학관'], lati['제1공학관']]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "name": "제3공학관 "
            },
            "geometry": {
                "type": "Point",
                "coordinates": [longti['제3공학관'], lati['제3공학관']]
            }
        }
    ]
}

m = folium.Map(
    location=[37.298215, 126.837191],
    zoom_start=15
)


def style_one(x): return {'fillColor': '#ffdc30'}


geojson_obj = folium.GeoJson(points, style_function=style_one).add_to(m)

statesearch = Search(layer=geojson_obj,
                     geom_type='Point',
                     placeholder="장소 검색",
                     search_label='name',
                     search_zoom=16.5,
                     position='topright'
                     ).add_to(m)

m.save('example.html')
m
