import folium
from folium import plugins
from latitude_and_longtitude import spot_num_latlng


def draw_path(path_list):
    coords = []
    bus = []

    inbus = -1 # 도보면 -1 버스면 1
    start = -1
    end = -1
    for i in range(len(path_list)):
        x = path_list[i]

        if x == 0:
            if inbus == -1 and i != 0: #버스 탑승
                coords.append(spot_num_latlng[path_list[i+1]])
            elif inbus == 1 and i != len(path_list)-1: #버스 하차
                coords.append(spot_num_latlng[path_list[i-1]])
            inbus *= -1
            continue
        if start == -1:
            start = spot_num_latlng[x]
        end = spot_num_latlng[x]
        if inbus == 1:
            bus.append(spot_num_latlng[x])
        else:
            coords.append(spot_num_latlng[x])  # 경로에 포함된 스팟 위도,경도 정보 추가

    m = folium.Map(
        location=start,
        min_zoom=13, max_zoom=20,
        zoom_start=16.5
    )

    #출도착지 마커 표시
    folium.Marker(location=start).add_to(m)
    folium.Marker(location=end, icon=folium.Icon(color="red", icon='star')).add_to(m)

    if coords != []:
        plugins.PolyLineOffset(coords, dash_array="5,15", color="#f00",
                           opacity=1, offset=-5).add_to(m)

    #버스 경로 표시
    if bus != []:
        plugins.PolyLineOffset(bus,dash_array = "5,15", color="green",
                            opacity=1,offset=-5).add_to(m)

    m.save('path_line.html')
    return m
