import folium
import pandas as pd
from IPython.display import HTML
from os import listdir
from os.path import isfile, join
import time
from selenium import webdriver
import os

delay = 10

def GetCircleColour2012(blockageId):
    colour = '#AF0000' #Other
    if blockageId == '1': # Fat
        colour = '#5B1025' #red color
    elif blockageId == '2':#Sanitary Products
        colour = '#588B8B'
    elif blockageId == '4': #Silt
        colour = '#C8553D'
    return colour

def GetCircleColour2013(blockageId):
    colour = '#2E5339' #Other
    if blockageId == '1': # Fat
        colour = '#3587A4'
    elif blockageId == '2':#Sanitary Products
        colour = '#6B2737'
    elif blockageId == '4': #Silt
        colour = '#2A3D45'
    return colour

def GetCircleColour2014(blockageId):
    colour = '#111DAA' #Other
    if blockageId == '1': # Fat
        colour = '#3D405B'
    elif blockageId == '2':#Sanitary Products
        colour = '#81B29A'
    elif blockageId == '4': #Silt
        colour = '#2B061E'
    return colour



SF_COORDINATES = (52.478400, -1.895224)
folderLocationData20 = "C:\\Users\\lenovo\\Documents\\Dissertation\\Report\\DataFiles\\" \
                       "GridFiles_All_20km\\Blockage"
# for speed purposes
MAX_RECORDS = 1000

onlyfiles = [f for f in listdir(folderLocationData20) if isfile(join(folderLocationData20, f))]
i = 0
map = folium.Map(location=SF_COORDINATES,zoom_start=10)
# create empty map zoomed in on San Francisco

fn='testmap.html'
tmpurl='file://{path}/{mapfile}'.format(path=os.getcwd(),mapfile=fn)

arrayOfColor = ['#B21212','#0971B2','#FF8F0A','#12B286','#9C00B2',
                '#8AFF19','#071A66','#FF2CC1','#38CACC','#FF8F0A']

for file in onlyfiles:
    completeFileGridAnalysis = '{0}\\{1}'.format(folderLocationData20, file)
    data = pd.DataFrame(pd.read_csv(completeFileGridAnalysis))
    fileComponents = file.split('_')
    gridId = fileComponents[0][4:]
    # add a marker for every record in the filtered data, use a clustered view
    color = arrayOfColor[i]
    i += 1
    print('Processing File {0}'.format(file))
    for each in data.iterrows():
        date = each[1]['IncidentDate']
        blockageCause = each[1]['IncidentCause']
        la = each[1]['Latitude']
        lo = each[1]['Longitude']
        d = date.split('-')
        #color = '#C66A00'
       # if d[2] == '2012':
        #    color = GetCircleColour2014(blockageCause)
        #elif d[2]== '2013':
        #    color = GetCircleColour2013(blockageCause)
        #elif d[2] == '2014':
        #    color= GetCircleColour2014(blockageCause)
        if d[2] == '2014':
            marker = folium.CircleMarker(location=[la, lo],
                                         radius=50,
                                         color=color,
                                         fill_color=color,
                                         fill_opacity=10)
            map.add_children(marker)

map.save('20kmBlockages2014.html')