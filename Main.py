import folium
import datetime
def GetCircleColour2012(blockageId):
    colour = 'black' #Other
    if blockageId == '1': # Fat
        colour = 'red'
    elif blockageId == '2':#Sanitary Products
        colour = 'blue'
    elif blockageId == '3': #Silt
        colour = 'orange'
    return colour

def GetCircleColour2013(blockageId):
    colour = 'gray' #Other
    if blockageId == '1': # Fat
        colour = 'purple'
    elif blockageId == '2':#Sanitary Products
        colour = 'green'
    elif blockageId == '3': #Silt
        colour = 'lightorange'
    return colour


fileHandler2012 = open('./DataCleanBlockages2012.csv', 'r')
fileHandler2013 = open('./DataCleanBlockages2013.csv', 'r')
i = 0
mapToner = folium.Map(location=[52.478400, -1.895224], tiles='Stamen Toner', zoom_start=10)
mapTerrain = folium.Map(location=[52.478400, -1.895224], tiles='Stamen Terrain', zoom_start=10)
mapOpenCombined = folium.Map(location=[52.478400, -1.895224],zoom_start=10)
mapOpen2012 = folium.Map(location=[52.478400, -1.895224],zoom_start=10)
mapOpen2013 = folium.Map(location=[52.478400, -1.895224],zoom_start=10)

for line in fileHandler2012.readlines():
    try:
        line = line.strip('\n')
        if i > 10000:
            break
        if line:
            tokens = line.strip().split(',')
            latitude = tokens[1]
            longitude = tokens[2]
            altitude = tokens[3]
            blockageCause = tokens[4]
            weatherCondition = tokens[5]
            incidentDate = tokens[6]
            # components = incidentDate.split('/')
            # incidentDateObj = datetime.datetime.strptime(incidentDate,'%d/%m/%Y')

            if latitude != '' and longitude != '':
                i += 1
                la = float(latitude)
                lo = float(longitude)
                #print(latitude, ' ', longitude)
                colour = GetCircleColour2012(blockageCause)
                # map_2.simple_marker(location=[la,lo], popup='The Waterfront')
                #mapToner.circle_marker(location=[la, lo], fill_color=colour, radius=50,line_color=colour,fill_opacity=1)
                mapOpenCombined.circle_marker(location=[la, lo], fill_color=colour, radius=5, line_color=colour, fill_opacity=1)
                mapOpen2012.circle_marker(location=[la, lo], fill_color=colour, radius=5, line_color=colour,
                                          fill_opacity=1)
                #mapTerrain.circle_marker(location=[la, lo], fill_color=colour, radius=50,line_color=colour, fill_opacity=1)
                #mapOpen.polygon_marker(location=[la,lo],line_color=colour,fill_color=colour,popup_width=2,num_sides=3)
    except:
        print('Exception occurred.')

fileHandler2012.close()
print('Finished 2012, now starting 2013.')
i=0
for line in fileHandler2013.readlines():
    try:
        line = line.strip('\n')
        if i > 10000:
            break
        if line:
            tokens = line.strip().split(',')
            latitude = tokens[1]
            longitude = tokens[2]
            altitude = tokens[3]
            blockageCause = tokens[4]
            weatherCondition = tokens[5]
            incidentDate = tokens[6]
            # components = incidentDate.split('/')
            # incidentDateObj = datetime.datetime.strptime(incidentDate,'%d/%m/%Y')

            if latitude != '' and longitude != '':
                i += 1
                la = float(latitude)
                lo = float(longitude)
                #print(latitude, ' ', longitude)
                colour = GetCircleColour2013(blockageCause)
                # map_2.simple_marker(location=[la,lo], popup='The Waterfront')
                #mapToner.circle_marker(location=[la, lo], fill_color=colour, radius=50,line_color=colour,fill_opacity=1)
                mapOpenCombined.circle_marker(location=[la, lo], fill_color=colour, radius=5, line_color=colour, fill_opacity=1)
                mapOpen2013.circle_marker(location=[la, lo], fill_color=colour, radius=5, line_color=colour,
                                              fill_opacity=1)
                #mapTerrain.circle_marker(location=[la, lo], fill_color=colour, radius=50,line_color=colour, fill_opacity=1)
                #mapOpen.polygon_marker(location=[la,lo],line_color=colour,fill_color=colour,popup_width=2,num_sides=3)
    except:
        print('excption occurred')

fileHandler2013.close()

#mapToner.save(outfile='birminghamTonerCombined.html', close_file=True)
#mapTerrain.save(outfile='birminghamTerrainCombined.html', close_file=True)
mapOpenCombined.save(outfile='birminghamOpenCombined.html', close_file=True)
mapOpen2013.save(outfile='birminghamOpen2013.html', close_file=True)
mapOpen2012.save(outfile='birminghamOpen2012.html', close_file=True)
