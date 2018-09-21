
# Cholera - London Outbreak 1851

## About
Presenter: Yubi Peterson

Contact: email: yubi@hawaii.edu | ig: @yubibimbap

For: ICS 484 - Data Visualization

Data created and compiled by Robin Wilson
[Link to his website](www.rtwilson.com/academic)

Libraries used: plotly, numpy, pandas

Topic: This dataset is centered on the cholera outbreak in London during 1851. It was found that the highest concentrated areas of those infected with cholera were near water pumps. This led to the discovery that Cholera is a disease spread through water. 


```python
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF
import numpy as np
import pandas as pd
```

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

#produce data table with values
trace = go.Table(
    header=dict(values=list(dfcholera.columns),
                fill = dict(color='#C2D4FF'), # blue cause cholera is "blue death"
                line = dict(color = 'white'),
                align = ['center'] * 5),
    cells=dict(values=[dfcholera.Date, dfcholera.Attack, dfcholera.Death, dfcholera.TotAttack, dfcholera.TotDeath],
               fill = dict(color='#ffffff'),
               line = dict(color = 'white'),
               align = ['right'] * 5))

data = [trace] 
py.iplot(data, filename = 'data_table')
```




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~notyubi/185.embed" height="525px" width="100%"></iframe>



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
py.iplot(fig, filename='cholera_line')
```




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~notyubi/187.embed" height="525px" width="100%"></iframe>



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
    header=dict(values=list(dfnaples.columns),
                fill = dict(color='#fada5e'), # fada5e is called "naples yellow"
                line = dict(color = 'white'),
                align = ['center'] * 5),
    cells=dict(values=[dfnaples.age, dfnaples.male, dfnaples.female],
               fill = dict(color='#ffffff'),
               line = dict(color = 'white'),
               align = ['center'] * 5))

layout = go.Layout(
    title='Table'
)
dataN = [trace] 
py.iplot(dataN, filename = 'naples_table')
```




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~notyubi/189.embed" height="525px" width="100%"></iframe>




```python
#creating a bar chart
maleTrace = go.Bar(
    x=dfnaples['age'],
    y=dfnaples['male'],
    name='Males',
    marker=dict(
        color='#408977'
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
py.iplot(fig, filename='naplesAgenSex')
```




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~notyubi/191.embed" height="525px" width="100%"></iframe>



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
                fill = dict(color='#fccfcf'),
                line = dict(color = 'white'),
                align = ['center']),
    cells=dict(values=[dfcensus.age, dfcensus.male, dfcensus.female, dfcensus.total],
               fill = dict(color='#ffffff'),
               line = dict(color = 'white'),
               align = ['right']))

dataN = [trace] 
py.iplot(dataN, filename = 'ukCensus_table')
```




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~notyubi/193.embed" height="525px" width="100%"></iframe>




```python
#creating a bar chart
maleTrace = go.Bar(
    x=dfcensus['age'],
    y=dfcensus['male'],
    name='Males',
    marker=dict(
        color='#408977'
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
py.iplot(fig, filename='ukcensusbar')
```




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~notyubi/195.embed" height="525px" width="100%"></iframe>




```python
#pie chart for men
labels = dfcensus['age']
values = dfcensus['male']
colors = ['#0c5387', '#1068a9', '#2777b1', '#5795c2','#6fa4cb', '#87b3d4','#9fc2dc', '#adc7db', '#cfe0ed']

trace = go.Pie(labels=labels, values=values,
               hoverinfo='label+percent', textinfo='value', 
               textfont=dict(color='#ffffff', size=17),
               marker=dict(colors=colors, 
                           line=dict(color='#ffffff', width=1)))

py.iplot([trace], filename='pieMen')
```




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~notyubi/197.embed" height="525px" width="100%"></iframe>




```python
#pie chart for women
labels = dfcensus['age']
values = dfcensus['female']
colors = ['#cc5151', '#e55b5b', '#ff7f7f', '#ffb2b2','#ffcccc', '#f9d9d9','#f9e3e3', '#f7e6e6', '#f5efd5']

trace = go.Pie(labels=labels, values=values,
               hoverinfo='label+percent', textinfo='value', 
               textfont=dict(size=17),
               marker=dict(colors=colors, 
                           line=dict(color='#ffffff', width=1)))

py.iplot([trace], filename='pieGirl')
```




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~notyubi/199.embed" height="525px" width="100%"></iframe>




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

py.iplot([trace], filename='pieOverall')
```




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~notyubi/201.embed" height="525px" width="100%"></iframe>



### Pump Locations Map


```python
#read in data for pump and locations
tsv_file='https://raw.githubusercontent.com/notyubi/cholera/master/choleraDeathLocations.tsv'
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv('choleraLocate.csv',index=False)

tsv_file='https://raw.githubusercontent.com/notyubi/cholera/master/choleraPumpLocations.tsv'
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv('pumpLocate.csv',index=False)
```


```python
dfmap = pd.read_csv('choleraLocate.csv')
dfpump = pd.read_csv('pumpLocate.csv')
```


```python
trace1 = {"x": dfpump['lat'], 
          "y": dfpump['long'], 
          "marker": {"color": "black", "size": 12}, 
          "mode": "markers", 
          "name": "Pump Location", 
          "type": "scatter"
}

trace2 = {"x": dfmap['lat'], 
          "y": dfmap['long'], 
          "marker": {"color": "red", "size": 5}, 
          "mode": "markers", 
          "name": "Attack Location", 
          "type": "scatter", 
}

data = [trace1, trace2]

layout = {"title": "Trying to do a map"}

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filenmae='plsaveme')
```




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~notyubi/203.embed" height="525px" width="100%"></iframe>


