from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt
import csv

path = Path('weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header = next(reader)

dates, prcps = [],[]
for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    prcp = float(row[5])
    dates.append(date)
    prcps.append(prcp)

plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots(figsize=(16,9))
ax.plot(dates, prcps)
fig.autofmt_xdate()

title = 'Daily Rainfall, 2021, Sitka, Alaska.'
ax.set_title(title, fontsize=20)
ax.set_xlabel('')
ax.set_ylabel('Temperature (F)', fontsize=14)

plt.show()