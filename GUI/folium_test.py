#주피터 노트북에서 작성한 코드
import folium
from latitude_and_longtitude import loca


def view_spot(spot, marker_color='blue'):
    view = folium.Map(location=loca(spot), zoom_start=17)
    folium.Marker(location=loca(spot), popup='셔틀콕', icon=folium.Icon(
        color=marker_color, icon='ok-sign')).add_to(view)
    return view


view_spot('셔틀콕')
