import folium
import sys
from sklearn import cluster


def GetRadiusSize(count):
    radiusSize = 10
    if count <= 150 and count >= 120:
        radiusSize = 800
    elif count < 120 and count >= 100:
        radiusSize = 700
    elif count < 99 and count >= 80:
        radiusSize = 600
    elif count < 79 and count >= 60:
        radiusSize = 500
    elif count < 59 and count >= 40:
        radiusSize = 400
    elif count < 39 and count >= 30:
        radiusSize = 20
    elif count < 29 and count >= 20:
        radiusSize = 18
    elif count < 19 and count >= 15:
        radiusSize = 12
    elif count < 14 and count >= 10:
        radiusSize = 8
    elif count < 9:
        radiusSize = 5
    return radiusSize

def GetColour(count):
    colour = 'black'
    if count <= 150 and count >= 120:
        colour = 'red'
    elif count < 120 and count >= 100:
        colour = 'blue'
    elif count < 99 and count >= 80:
        colour = 'purple'
    elif count < 79 and count >= 60:
        colour = 'orange'
    elif count < 59 and count >= 40:
        colour = 'black'
    elif count < 39 and count >= 30:
        colour = 'purple'
    elif count < 29 and count >= 20:
        colour = 'pink'
    elif count < 19 and count >= 15:
        colour = 'black'
    elif count < 14 and count >= 10:
        colour = 'black'
    elif count < 9:
        colour = 'black'
    return colour



missingPostCodes = open(
    'C:\\Users\\lenovo\\Documents\\Dissertation\\Report\\DataFiles\\PostCodesWithMissingBlockages.csv', 'r')
missingPostCodesMap = folium.Map(location=[52.478400, -1.895224], zoom_start=10)
i = 0

for line in missingPostCodes.readlines():
    try:
        line = line.strip('\n')
        if line:
            tokens = line.strip().split(',')
            postCode = tokens[0]
            count = int(tokens[1])
            latitude = tokens[2]
            longitude = tokens[3]
            altitude = tokens[4]
            if latitude != '' and longitude != '':
                i += 1
                la = float(latitude)
                lo = float(longitude)
                radius = GetRadiusSize(count)
                r = int(radius)
                colour = GetColour(count)
                popupString = "Post Code {0} - Count {1}".format(postCode,count)
                marker = folium.CircleMarker(location=[la, lo],
                                      radius=r,
                                      color=colour,
                                      fill_color=colour,
                                      fill_opacity=10,
                                      popup=popupString)
                missingPostCodesMap.add_children(marker)
    except:
        print("Unexpected error:", sys.exc_info()[0])

missingPostCodes.close()

missingPostCodesMap.save(outfile='PostCodesWithMissingBlockages.html', close_file=True)
