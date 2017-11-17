import folium


mapOpen2012 = folium.Map(location=[52.478400, -1.895224],zoom_start=10)

la = 52.352961
lo = -2.397092
mapOpen2012.circle_marker(location=[la, lo], fill_color='red', radius=500, line_color='red',fill_opacity = 1)
la = 52.5056745983003
lo = -2.14706786067914
mapOpen2012.circle_marker(location=[la, lo], fill_color='red', radius=500, line_color='red',fill_opacity = 1)
la = 52.5056745983003
lo = -2.397092
mapOpen2012.circle_marker(location=[la, lo], fill_color='red', radius=500, line_color='red',fill_opacity = 1)
la = 52.6583881966006
lo = -2.14620009823937
mapOpen2012.circle_marker(location=[la, lo], fill_color='red', radius=500, line_color='red',fill_opacity = 1)
la = 52.6583881966006
lo = -2.397092
mapOpen2012.circle_marker(location=[la, lo], fill_color='red', radius=500, line_color='red',fill_opacity = 1)
la = 52.8111017949009
lo = -2.14532449649506
mapOpen2012.circle_marker(location=[la, lo], fill_color='red', radius=500, line_color='red',fill_opacity = 1)
la = 52.352961
lo = -2.14532449649506
mapOpen2012.circle_marker(location=[la, lo], fill_color='red', radius=500, line_color='red',fill_opacity = 1)
la = 52.5056745983003
lo = -1.8953003571742
mapOpen2012.circle_marker(location=[la, lo], fill_color='red', radius=500, line_color='red',fill_opacity = 1)
la = 52.5056745983003
lo = -2.14532449649506
mapOpen2012.circle_marker(location=[la, lo], fill_color='red', radius=500, line_color='red',fill_opacity = 1)
la = 52.6583881966006
lo = -1.89443259473443
mapOpen2012.circle_marker(location=[la, lo], fill_color='red', radius=500, line_color='red',fill_opacity = 1)
la = 52.6583881966006
lo = -2.14532449649506
mapOpen2012.circle_marker(location=[la, lo], fill_color='red', radius=500, line_color='red',fill_opacity = 1)
la = 52.8111017949009
lo = -1.89355699299013
mapOpen2012.circle_marker(location=[la, lo], fill_color='red', radius=500, line_color='red',fill_opacity = 1)
la = 52.352961
lo = -1.89355699299013
mapOpen2012.circle_marker(location=[la, lo], fill_color='red', radius=500, line_color='red',fill_opacity = 1)
la = 52.5056745983003
lo = -1.64353285366926
mapOpen2012.circle_marker(location=[la, lo], fill_color='red', radius=500, line_color='red',fill_opacity = 1)
la = 52.5056745983003
lo = -1.89355699299013
mapOpen2012.circle_marker(location=[la, lo], fill_color='red', radius=500, line_color='red',fill_opacity = 1)
la = 52.6583881966006
lo = -1.64266509122949
mapOpen2012.circle_marker(location=[la, lo], fill_color='red', radius=500, line_color='red',fill_opacity = 1)
la = 52.6583881966006
lo = -1.89355699299013
mapOpen2012.circle_marker(location=[la, lo], fill_color='red', radius=500, line_color='red',fill_opacity = 1)
la = 52.8111017949009
lo = -1.64178948948519
mapOpen2012.circle_marker(location=[la, lo], fill_color='red', radius=500, line_color='red',fill_opacity = 1)

mapOpen2012.save(outfile='mesh.html', close_file=True)