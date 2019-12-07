import folium
from folium import plugins
from latitude_and_longtitude import spot_num_latlng


def draw_path(path_list):
    coords = []
    for x in path_list:
        coords.append(spot_num_latlng[x])  # 경로에 포함된 스팟 위도,경도 정보 추가

    m = folium.Map(
        location=coords[0],
        min_zoom=13, max_zoom=20,
        zoom_start=16.5
    )

    plugins.PolyLineOffset(coords, color="#f00",
                           opacity=1, offset=-5).add_to(m)
    m.save('path_line.html')
    return m


draw_path([12, 11, 10, 39, 9, 8, 7, 18, 20]) #테스트 코드
