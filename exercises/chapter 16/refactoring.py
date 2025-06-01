import json
from pathlib import Path

import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path('eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']
mags, lons, lats, eq_titles = [],[],[],[]
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    eq_titles.append(eq_dict['properties']['title'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])

title = all_eq_data['metadata']['title']
fig = px.scatter_geo(lat=lats, lon=lons, title=title, size=mags,
    color=mags,
    color_continuous_scale='Viridis', 
    hover_name=eq_titles,
    labels={'color':'Magnitude'},
    projection='natural earth',
    )
fig.show()