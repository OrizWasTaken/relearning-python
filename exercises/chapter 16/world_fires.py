from pathlib import Path
import plotly.express as px
import csv

path = Path('eq_data/world_fires_1_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header = next(reader)

lat_idx = header.index('latitude')
lon_idx = header.index('longitude')
brtnss_indx = header.index('brightness')

lons, lats, brtnss = [],[],[]
for row in reader:
    lons.append(row[lon_idx])
    lats.append(row[lat_idx])
    brtnss.append(float(row[brtnss_indx]))

fig = px.scatter_geo(lat=lats, lon=lons, size=brtnss,
    title='World Fires.',
    labels={'color': 'brightness'},
    color=brtnss,
    size_max=15,
    color_continuous_scale='bluered',
    )
fig.show()