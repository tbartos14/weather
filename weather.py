#Datetime,RecNbr,WS_mph_Avg,PAR_Den_Avg,WS_mph_S_WVT,WindDir_SD1_WVT,AirTF_Avg,Rain_in_Tot,RH,WindDir_D1_WVT

import urllib.request
import time
from plotim import *

print("Weather info extracted from:")
url = "http://www.weather.unh.edu/data/" + time.strftime("%Y") + "/" + str(int(time.strftime("%j"))) + ".txt"
print(url)

weather = urllib.request.urlopen(url)
data = weather.readlines()

##def process(line):
##    line = line.split(b" ", 1)
##    line.pop(0)
##    line = line[0].split(b",")
##    line.pop(0)
##    line.pop(0)
##    return line

def process(line):
    result = line.split(b",")
    newresult = []
    for item in result[2:]:
        item = float(item)
        newresult.append(item)
    return newresult[2:]

linesset = []

for line in data:
    linesset.append(line[:-2])

linesset.pop(0)

newlines = []

for line in linesset:
    newlines.append(process(line))

xpoints = []
ypoints = []
time = 0

for line in newlines:
    xpoints.append(time)
    time = time + (1/60)
    ypoints.append(line[-4])

plot1 = linear_plot(line_of_best_fit = True,\
                   ytitle = "Temperature F\u00B0",\
                   xtitle = "Time (hours)",\
                   title = "Temperature in Durham NH Today",\
                   line_color = "#2222ff",\
                   windowx = 1200,\
                   windowy = 800,)
plot1.set_data(xpoints,ypoints)
plot1.plot_data()
a,b = plot1.residuals()

