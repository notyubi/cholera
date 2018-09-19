
# Cholera

## About
Presenter: Yubi Peterson

Contact: email: yubi@hawaii.edu | ig: @yubibimbap

For: ICS 484 - Data Visualization

Data created and compiled by Robin Wilson
[Link to his website](www.rtwilson.com/academic)

Libraries used: plotly, numpy, pandas


```python
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF
import numpy as np
import pandas as pd
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.offline as offline

init_notebook_mode(connected=True)
offline.init_notebook_mode()
```


<script>requirejs.config({paths: { 'plotly': ['https://cdn.plot.ly/plotly-latest.min']},});if(!window.Plotly) {{require(['plotly'],function(plotly) {window.Plotly=plotly;});}}</script>



<script type='text/javascript'>if(!window.Plotly){define('plotly', function(require, exports, module) {/**
* plotly.js v1.40.1
* Copyright 2012-2018, Plotly, Inc.
* All rights reserved.
* Licensed under the MIT license
*/


### Cholera Deaths


```python
#To convert tsv file into csv
tsv_file='https://raw.githubusercontent.com/notyubi/cholera/master/choleraDeaths.tsv'
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv('choleraDeaths.csv',index=False)
```

Table holding data on the specific dates of an Attack/Death recording as well as total value.


```python
#read in the choleraDeaths.csv data file
dfcholera = pd.read_csv('choleraDeaths.csv')

#produce data table with some values
trace = go.Table(
    header=dict(values=list(dfcholera.columns),
                fill = dict(color='#C2D4FF'),
                align = ['center'] * 5),
    cells=dict(values=[dfcholera.Date, dfcholera.Attack, dfcholera.Death, dfcholera.TotAttack, dfcholera.TotDeath],
               fill = dict(color='#ffffff'),
               align = ['right'] * 5))

data = [trace] 
offline.iplot(data, filename = 'data_table')
```


<div id="eec11e8e-55c4-44cb-b0bb-24f68fea9f5a" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("eec11e8e-55c4-44cb-b0bb-24f68fea9f5a", [{"cells": {"align": ["right", "right", "right", "right", "right"], "fill": {"color": "#ffffff"}, "values": [["19-Aug-1854", "20-Aug-1854", "21-Aug-1854", "22-Aug-1854", "23-Aug-1854", "24-Aug-1854", "25-Aug-1854", "26-Aug-1854", "27-Aug-1854", "28-Aug-1854", "29-Aug-1854", "30-Aug-1854", "31-Aug-1854", "1-Sep-1854", "2-Sep-1854", "3-Sep-1854", "4-Sep-1854", "5-Sep-1854", "6-Sep-1854", "7-Sep-1854", "8-Sep-1854", "9-Sep-1854", "10-Sep-1854", "11-Sep-1854", "12-Sep-1854", "13-Sep-1854", "14-Sep-1854", "15-Sep-1854", "16-Sep-1854", "17-Sep-1854", "18-Sep-1854", "19-Sep-1854", "20-Sep-1854", "21-Sep-1854", "22-Sep-1854", "23-Sep-1854", "24-Sep-1854", "25-Sep-1854", "26-Sep-1854", "27-Sep-1854", "28-Sep-1854", "29-Sep-1854"], [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 8, 56, 143, 116, 54, 46, 36, 20, 28, 12, 11, 5, 5, 1, 3, 0, 1, 4, 2, 3, 0, 0, 2, 1, 1, 1, 1, 1, 1, 0, 0], [1, 0, 2, 0, 0, 2, 0, 0, 1, 0, 1, 2, 3, 70, 127, 76, 71, 45, 37, 32, 30, 24, 18, 15, 6, 13, 6, 8, 6, 5, 2, 3, 0, 0, 2, 3, 0, 0, 2, 0, 2, 1], [1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9, 17, 73, 216, 332, 386, 432, 468, 488, 516, 528, 539, 544, 549, 550, 553, 553, 554, 558, 560, 563, 563, 563, 565, 566, 567, 568, 569, 570, 571, 571, 571], [1, 1, 3, 3, 3, 5, 5, 5, 6, 6, 7, 9, 12, 82, 209, 285, 356, 401, 438, 470, 500, 524, 542, 557, 563, 576, 582, 590, 596, 601, 603, 606, 606, 606, 608, 611, 611, 611, 613, 613, 615, 616]]}, "header": {"align": ["center", "center", "center", "center", "center"], "fill": {"color": "#C2D4FF"}, "values": ["Date", "Attack", "Death", "TotAttack", "TotDeath"]}, "type": "table", "uid": "db4b3a12-bc09-11e8-a23e-b8e85626e578"}], {}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


Line chart showing 4 different types of relationships:
- Attacks on a particular date
- Deaths on a particular date
- Total attacks on a particular date
- Total deaths on a particular date


```python
#Line chart of Attacks
attacks = go.Scatter(
    x = dfcholera['Date'],
    y = dfcholera['Attack'],
    name = "Day Attacks",
    line = dict(
    color = '#a670c5' #a lighter purple
    )
)

#Line for deaths
deaths = go.Scatter(
    x = dfcholera['Date'],
    y = dfcholera['Death'],
    name = "Day Deaths",
    line = dict(
    color = '#bbc515' #a lighter olive
    )
)

#Line for totAttack
totAttack = go.Scatter(
    x = dfcholera['Date'],
    y = dfcholera['TotAttack'],
    name = "Total Attacks",
    line = dict(
    color = '#5d0c8b' #a darker purple
    )
)

#Line for totDeaths
totDeaths = go.Scatter(
    x = dfcholera['Date'],
    y = dfcholera['TotDeath'],
    name = "Total Deaths",
    line = dict(
    color = '#575c09' #a dark olive color
    )
)

data = [attacks, deaths, totAttack, totDeaths]

layout = go.Layout(
    title='Cholera Outbreak 1854',
    xaxis=dict(
        title='Date'
    ),
    yaxis=dict(
        title='# of Observations'
    )
)

fig = go.Figure(data=data, layout=layout)
offline.iplot(fig, filename='cholera_line')
```


<div id="b92a3e0c-0c5d-4475-89e5-3b2205283add" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("b92a3e0c-0c5d-4475-89e5-3b2205283add", [{"line": {"color": "#a670c5"}, "name": "Day Attacks", "x": ["19-Aug-1854", "20-Aug-1854", "21-Aug-1854", "22-Aug-1854", "23-Aug-1854", "24-Aug-1854", "25-Aug-1854", "26-Aug-1854", "27-Aug-1854", "28-Aug-1854", "29-Aug-1854", "30-Aug-1854", "31-Aug-1854", "1-Sep-1854", "2-Sep-1854", "3-Sep-1854", "4-Sep-1854", "5-Sep-1854", "6-Sep-1854", "7-Sep-1854", "8-Sep-1854", "9-Sep-1854", "10-Sep-1854", "11-Sep-1854", "12-Sep-1854", "13-Sep-1854", "14-Sep-1854", "15-Sep-1854", "16-Sep-1854", "17-Sep-1854", "18-Sep-1854", "19-Sep-1854", "20-Sep-1854", "21-Sep-1854", "22-Sep-1854", "23-Sep-1854", "24-Sep-1854", "25-Sep-1854", "26-Sep-1854", "27-Sep-1854", "28-Sep-1854", "29-Sep-1854"], "y": [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 8, 56, 143, 116, 54, 46, 36, 20, 28, 12, 11, 5, 5, 1, 3, 0, 1, 4, 2, 3, 0, 0, 2, 1, 1, 1, 1, 1, 1, 0, 0], "type": "scatter", "uid": "dfc589e4-bc09-11e8-adb3-b8e85626e578"}, {"line": {"color": "#bbc515"}, "name": "Day Deaths", "x": ["19-Aug-1854", "20-Aug-1854", "21-Aug-1854", "22-Aug-1854", "23-Aug-1854", "24-Aug-1854", "25-Aug-1854", "26-Aug-1854", "27-Aug-1854", "28-Aug-1854", "29-Aug-1854", "30-Aug-1854", "31-Aug-1854", "1-Sep-1854", "2-Sep-1854", "3-Sep-1854", "4-Sep-1854", "5-Sep-1854", "6-Sep-1854", "7-Sep-1854", "8-Sep-1854", "9-Sep-1854", "10-Sep-1854", "11-Sep-1854", "12-Sep-1854", "13-Sep-1854", "14-Sep-1854", "15-Sep-1854", "16-Sep-1854", "17-Sep-1854", "18-Sep-1854", "19-Sep-1854", "20-Sep-1854", "21-Sep-1854", "22-Sep-1854", "23-Sep-1854", "24-Sep-1854", "25-Sep-1854", "26-Sep-1854", "27-Sep-1854", "28-Sep-1854", "29-Sep-1854"], "y": [1, 0, 2, 0, 0, 2, 0, 0, 1, 0, 1, 2, 3, 70, 127, 76, 71, 45, 37, 32, 30, 24, 18, 15, 6, 13, 6, 8, 6, 5, 2, 3, 0, 0, 2, 3, 0, 0, 2, 0, 2, 1], "type": "scatter", "uid": "dfc58bba-bc09-11e8-a627-b8e85626e578"}, {"line": {"color": "#5d0c8b"}, "name": "Total Attacks", "x": ["19-Aug-1854", "20-Aug-1854", "21-Aug-1854", "22-Aug-1854", "23-Aug-1854", "24-Aug-1854", "25-Aug-1854", "26-Aug-1854", "27-Aug-1854", "28-Aug-1854", "29-Aug-1854", "30-Aug-1854", "31-Aug-1854", "1-Sep-1854", "2-Sep-1854", "3-Sep-1854", "4-Sep-1854", "5-Sep-1854", "6-Sep-1854", "7-Sep-1854", "8-Sep-1854", "9-Sep-1854", "10-Sep-1854", "11-Sep-1854", "12-Sep-1854", "13-Sep-1854", "14-Sep-1854", "15-Sep-1854", "16-Sep-1854", "17-Sep-1854", "18-Sep-1854", "19-Sep-1854", "20-Sep-1854", "21-Sep-1854", "22-Sep-1854", "23-Sep-1854", "24-Sep-1854", "25-Sep-1854", "26-Sep-1854", "27-Sep-1854", "28-Sep-1854", "29-Sep-1854"], "y": [1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9, 17, 73, 216, 332, 386, 432, 468, 488, 516, 528, 539, 544, 549, 550, 553, 553, 554, 558, 560, 563, 563, 563, 565, 566, 567, 568, 569, 570, 571, 571, 571], "type": "scatter", "uid": "dfc58d54-bc09-11e8-b376-b8e85626e578"}, {"line": {"color": "#575c09"}, "name": "Total Deaths", "x": ["19-Aug-1854", "20-Aug-1854", "21-Aug-1854", "22-Aug-1854", "23-Aug-1854", "24-Aug-1854", "25-Aug-1854", "26-Aug-1854", "27-Aug-1854", "28-Aug-1854", "29-Aug-1854", "30-Aug-1854", "31-Aug-1854", "1-Sep-1854", "2-Sep-1854", "3-Sep-1854", "4-Sep-1854", "5-Sep-1854", "6-Sep-1854", "7-Sep-1854", "8-Sep-1854", "9-Sep-1854", "10-Sep-1854", "11-Sep-1854", "12-Sep-1854", "13-Sep-1854", "14-Sep-1854", "15-Sep-1854", "16-Sep-1854", "17-Sep-1854", "18-Sep-1854", "19-Sep-1854", "20-Sep-1854", "21-Sep-1854", "22-Sep-1854", "23-Sep-1854", "24-Sep-1854", "25-Sep-1854", "26-Sep-1854", "27-Sep-1854", "28-Sep-1854", "29-Sep-1854"], "y": [1, 1, 3, 3, 3, 5, 5, 5, 6, 6, 7, 9, 12, 82, 209, 285, 356, 401, 438, 470, 500, 524, 542, 557, 563, 576, 582, 590, 596, 601, 603, 606, 606, 606, 608, 611, 611, 611, 613, 613, 615, 616], "type": "scatter", "uid": "dfc58e4c-bc09-11e8-b6bd-b8e85626e578"}], {"title": "Cholera Outbreak 1854", "xaxis": {"title": "Date"}, "yaxis": {"title": "# of Observations"}}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


For this graph I chose a dark and light purple combo to indicate attacks and yellow-green combo for deaths because these are two color sets that color blind people can see (and what most colors default for them). 

### Naples Age and Sex Data


```python
#To convert tsv file into csv
tsv_file='https://raw.githubusercontent.com/notyubi/cholera/master/naplesCholeraAgeSexData.tsv'
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv('naplesAgeSex.csv',index=False)
```


```python
#read in the naplesAgeSex.csv data file
dfnaples = pd.read_csv('naplesAgeSex.csv')

#produce data table with some values
trace = go.Table(
    header=dict(values=list(df.columns),
                fill = dict(color='#97d7e5'),
                align = ['center'] * 5),
    cells=dict(values=[dfnaples.age, dfnaples.male, dfnaples.female],
               fill = dict(color='#ffffff'),
               align = ['center'] * 5))

dataN = [trace] 
offline.iplot(dataN, filename = 'naples_table')
```


<div id="99d39602-6a88-45e9-bee8-b07f6331d94c" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("99d39602-6a88-45e9-bee8-b07f6331d94c", [{"cells": {"align": ["center", "center", "center", "center", "center"], "fill": {"color": "#ffffff"}, "values": [["0-1", "2-5", "6-10", "11-15", "16-20", "21-40", "41-60", "61-80", "over80"], [8.2, 14.0, 12.1, 7.8, 7.2, 12.1, 13.7, 20.5, 39.6], [8.9, 14.7, 11.2, 7.1, 7.2, 11.8, 12.9, 20.5, 37.8]]}, "header": {"align": ["center", "center", "center", "center", "center"], "fill": {"color": "#97d7e5"}, "values": ["age", "male", "female"]}, "type": "table", "uid": "e2e98cba-bc09-11e8-9543-b8e85626e578"}], {}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>



```python
#creating a bar chart
maleTrace = go.Bar(
    x=dfnaples['age'],
    y=dfnaples['male'],
    name='Males',
    marker=dict(
        color='#f8f97e'
    )
)
femaleTrace = go.Bar(
    x=dfnaples['age'],
    y=dfnaples['female'],
    name='Females',
    marker=dict(
        color='#e597d6'
    )
)
data = [maleTrace, femaleTrace]
layout = go.Layout(
    title='Naples Age and Sex',
    xaxis=dict(
        title='Age Range'
    ),
    yaxis=dict(
        title='Deaths per 10,000',
        titlefont=dict(
            size=16,
            color='rgb(107, 107, 107)'
        ),
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15,
    bargroupgap=0
)

fig = go.Figure(data=data, layout=layout)
offline.iplot(fig, filename='naplesAgenSex')
```


<div id="1429378e-cbaf-4f7a-9e30-a077717f0065" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("1429378e-cbaf-4f7a-9e30-a077717f0065", [{"marker": {"color": "#f8f97e"}, "name": "Males", "x": ["0-1", "2-5", "6-10", "11-15", "16-20", "21-40", "41-60", "61-80", "over80"], "y": [8.2, 14.0, 12.1, 7.8, 7.2, 12.1, 13.7, 20.5, 39.6], "type": "bar", "uid": "e6a0ec36-bc09-11e8-b7f1-b8e85626e578"}, {"marker": {"color": "#e597d6"}, "name": "Females", "x": ["0-1", "2-5", "6-10", "11-15", "16-20", "21-40", "41-60", "61-80", "over80"], "y": [8.9, 14.7, 11.2, 7.1, 7.2, 11.8, 12.9, 20.5, 37.8], "type": "bar", "uid": "e6a0ee02-bc09-11e8-a047-b8e85626e578"}], {"bargap": 0.15, "bargroupgap": 0, "barmode": "group", "legend": {"bgcolor": "rgba(255, 255, 255, 0)", "bordercolor": "rgba(255, 255, 255, 0)", "x": 0, "y": 1.0}, "title": "Naples Age and Sex", "xaxis": {"title": "Age Range"}, "yaxis": {"title": "Deaths per 10,000", "titlefont": {"color": "rgb(107, 107, 107)", "size": 16}}}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


### UK Census 1851 Dataset


```python
#To convert tsv file into csv
tsv_file='https://raw.githubusercontent.com/notyubi/cholera/master/UKcensus1851.tsv'
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv('ukCensus.csv',index=False)
```


```python
#produce data table with some values
dfcensus = pd.read_csv('ukCensus.csv')
trace = go.Table(
    header=dict(values=list(dfcensus.columns),
                fill = dict(color='#97d7e5'),
                align = ['center']),
    cells=dict(values=[dfcensus.age, dfcensus.male, dfcensus.female, dfcensus.total],
               fill = dict(color='#ffffff'),
               align = ['right']))

dataN = [trace] 
offline.iplot(dataN, filename = 'ukCensus_table')
```


<div id="2a3a807c-26e1-4848-9ff0-ffc472112992" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("2a3a807c-26e1-4848-9ff0-ffc472112992", [{"cells": {"align": ["right"], "fill": {"color": "#ffffff"}, "values": [["0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80+"], [2075391, 1711664, 1395091, 1073914, 810979, 560534, 351893, 166194, 40772], [2065096, 1711627, 1542876, 1140383, 845260, 592970, 399019, 199326, 55704], [4140487, 3423291, 2937967, 2214297, 1656239, 1153504, 750912, 365520, 96476]]}, "header": {"align": ["center"], "fill": {"color": "#97d7e5"}, "values": ["age", "male", "female", "total"]}, "type": "table", "uid": "e9f66438-bc09-11e8-b6b7-b8e85626e578"}], {}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>



```python
#creating a bar chart
maleTrace = go.Bar(
    x=dfcensus['age'],
    y=dfcensus['male'],
    name='Males',
    marker=dict(
        color='#f8f97e'
    )
)
femaleTrace = go.Bar(
    x=dfcensus['age'],
    y=dfcensus['female'],
    name='Females',
    marker=dict(
        color='#e597d6'
    )
)
data = [maleTrace, femaleTrace]
layout = go.Layout(
    title='UK Census 1851',
    xaxis=dict(
        title='Age Range'
    ),
    yaxis=dict(
        title='Number Impacted',
        titlefont=dict(
            size=16,
            color='rgb(107, 107, 107)'
        ),
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15,
    bargroupgap=0
)

fig = go.Figure(data=data, layout=layout)
offline.iplot(fig, filename='ukcensusbar')
```


<div id="d5e5f3b9-5489-4442-9c75-9a7ab3e3b839" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("d5e5f3b9-5489-4442-9c75-9a7ab3e3b839", [{"marker": {"color": "#f8f97e"}, "name": "Males", "x": ["0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80+"], "y": [2075391, 1711664, 1395091, 1073914, 810979, 560534, 351893, 166194, 40772], "type": "bar", "uid": "ed9549e2-bc09-11e8-a8ca-b8e85626e578"}, {"marker": {"color": "#e597d6"}, "name": "Females", "x": ["0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80+"], "y": [2065096, 1711627, 1542876, 1140383, 845260, 592970, 399019, 199326, 55704], "type": "bar", "uid": "ed954c1c-bc09-11e8-a94f-b8e85626e578"}], {"bargap": 0.15, "bargroupgap": 0, "barmode": "group", "legend": {"bgcolor": "rgba(255, 255, 255, 0)", "bordercolor": "rgba(255, 255, 255, 0)", "x": 0, "y": 1.0}, "title": "UK Census 1851", "xaxis": {"title": "Age Range"}, "yaxis": {"title": "Number Impacted", "titlefont": {"color": "rgb(107, 107, 107)", "size": 16}}}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>



```python
#pie chart for men
labels = dfcensus['age']
values = dfcensus['male']
colors = ['#0c5387', '#1068a9', '#2777b1', '#5795c2','#6fa4cb', '#87b3d4','#9fc2dc', '#b7dle5', '#cfe0ed']

trace = go.Pie(labels=labels, values=values,
               hoverinfo='label+percent', textinfo='value', 
               textfont=dict(color='#ffffff', size=17),
               marker=dict(colors=colors, 
                           line=dict(color='#ffffff', width=1)))

offline.iplot([trace], filename='pieMen')
```




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~notyubi/135.embed" height="525px" width="100%"></iframe>




```python
#pie chart for women
labels = dfcensus['age']
values = dfcensus['female']
colors = ['#cc5151', '#e55b5b', '#ff7f7f', '#ffb2b2','#ffcccc', '#efcbbb','#e3cf81', '#ecdfab', '#f5efd5']

trace = go.Pie(labels=labels, values=values,
               hoverinfo='label+percent', textinfo='value', 
               textfont=dict(size=17),
               marker=dict(colors=colors, 
                           line=dict(color='#ffffff', width=1)))

offline.iplot([trace], filename='pieGirl')
```




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~notyubi/137.embed" height="525px" width="100%"></iframe>




```python
#pie chart for overall
labels = ['Men', 'Women']
values = ['8186432', '8552261']
colors = ['#53d8b3', '#eee865']

trace = go.Pie(labels=labels, values=values,
               hoverinfo='label+percent', textinfo='value', 
               textfont=dict(size=17),
               marker=dict(colors=colors, 
                           line=dict(color='#ffffff', width=1)))

offline.iplot([trace], filename='overallPie')
```


<div id="b1a12cdd-0cfd-4a37-b4c3-8462622a0c69" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("b1a12cdd-0cfd-4a37-b4c3-8462622a0c69", [{"hoverinfo": "label+percent", "labels": ["Men", "Women"], "marker": {"colors": ["#53d8b3", "#eee865"], "line": {"color": "#ffffff", "width": 1}}, "textfont": {"size": 17}, "textinfo": "value", "values": ["8186432", "8552261"], "type": "pie", "uid": "f55c7ec0-bc09-11e8-a726-b8e85626e578"}], {}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>
