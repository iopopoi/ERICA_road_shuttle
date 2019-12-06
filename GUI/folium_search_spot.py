import folium
from folium import plugins
from folium.plugins import Search
from latitude_and_longtitude import loca, lati, longti
from jinja2 import Template


points = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
                "name": "셔틀콕",
            },
            "geometry": {
                "type": "Point",
                "coordinates": [longti['셔틀콕'], lati['셔틀콕']]
            },
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
        },
        {
            "type": "Feature",
            "properties": {
                "name": "제4공학관 "
            },
            "geometry": {
                "type": "Point",
                "coordinates": [longti['제4공학관'], lati['제4공학관']]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "name": "제5공학관 "
            },
            "geometry": {
                "type": "Point",
                "coordinates": [longti['제5공학관'], lati['제5공학관']]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "name": "컨퍼런스홀"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [longti['컨퍼런스홀'], lati['컨퍼런스홀']]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "name": "학연산 클러스터 "
            },
            "geometry": {
                "type": "Point",
                "coordinates": [longti['학연산 클러스터'], lati['학연산 클러스터']]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "name": "제2과학기술관 "
            },
            "geometry": {
                "type": "Point",
                "coordinates": [longti['제2과학기술관'], lati['제2과학기술관']]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "name": "제1학술관"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [longti['제1학술관'], lati['제1학술관']]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "name": "학생복지관"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [longti['학생복지관'], lati['학생복지관']]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "name": "학생회관"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [longti['학생회관'], lati['학생회관']]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "name": "학술정보관"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [longti['학술정보관'], lati['학술정보관']]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "name": "기숙사 셔틀콕"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [longti['기숙사 셔틀콕'], lati['기숙사 셔틀콕']]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "name": "창업보육센터"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [longti['창업보육센터'], lati['창업보육센터']]
            }
        },
        {
            "type": "Feature",
            "properties": {
                "name": "한대앞역"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [longti['한대앞역'], lati['한대앞역']]
            }
        }
    ]
}

m = folium.Map(
    location=[37.296854, 126.836715],
    min_zoom=13, max_zoom=20,
    zoom_start=16.5
)

geojson_obj = folium.GeoJson(points, name="마커 보기").add_to(m)


for i in points["features"]:
    lati = i["geometry"]["coordinates"][1]
    longti = i["geometry"]["coordinates"][0]
    name = i["properties"]["name"]
    html = Template("""
    <h3> {{name}} </h3><br>
    </p>
    """).render(name=name) #html 형태로 마커 클릭 시 팝업 추가

Search(layer=geojson_obj,
       geom_type='Point',
       placeholder="장소 검색",
       search_label='name',
       search_zoom=17,
       collapsed=False,
       position='topright').add_to(m) # 장소 검색 기능 추가

plugins.LocateControl().add_to(m) #gps 기능 추가

m.save('example.html')
m
