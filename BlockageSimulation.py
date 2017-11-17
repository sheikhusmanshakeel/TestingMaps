import folium
import pandas as pd
from IPython.display import HTML
from os import listdir
from os.path import isfile, join
import time
from selenium import webdriver
import os


SF_COORDINATES = (52.478400, -1.895224)
folderLocation = "C:\\Users\\lenovo\\Documents\\Dissertation\\Report\\DataFiles\\" \
                       "ClipFiles"
folderLocationMapPath = "C:\\Users\\lenovo\\Documents\\Dissertation\\Report\\DataFiles\\" \
                       "MapFiles"

onlyfiles = [f for f in listdir(folderLocation) if isfile(join(folderLocation, f))]
i = 0

for file in onlyfiles:
    completeFileGridAnalysis = '{0}\\{1}'.format(folderLocation, file)
    map = folium.Map(location=SF_COORDINATES, zoom_start=10)
    data = pd.DataFrame(pd.read_csv(completeFileGridAnalysis))
    fileComponents = file.split('_')
    gridId = fileComponents[0][4:]
    # add a marker for every record in the filtered data, use a clustered view
    color = '#0971B2'
    print('Processing File {0}'.format(file))
    for each in data.iterrows():
        date = each[1]['IncidentDate']
        blockageCause = each[1]['IncidentCause']
        la = each[1]['Latitude']
        lo = each[1]['Longitude']
        marker = folium.CircleMarker(location=[la, lo],
                                     radius=50,
                                     color=color,
                                     fill_color=color,
                                     fill_opacity=10)
        map.add_children(marker)
    mapFileName = '{0}\\{1}.html'.format(folderLocationMapPath,i)
    map.save(mapFileName)
    i += 1
