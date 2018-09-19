
# coding: utf-8

# # Cholera

# ## About
# Presenter: Yubi Peterson
# 
# Contact: email: yubi@hawaii.edu | ig: @yubibimbap
# 
# For: ICS 484 - Data Visualization
# 
# Data created and compiled by Robin Wilson
# [Link to his website](www.rtwilson.com/academic)
# 
# Libraries used: plotly, numpy, pandas

# In[99]:


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


# ### Cholera Deaths

# In[45]:


#To convert tsv file into csv
tsv_file='https://raw.githubusercontent.com/notyubi/cholera/master/choleraDeaths.tsv'
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv('choleraDeaths.csv',index=False)


# Table holding data on the specific dates of an Attack/Death recording as well as total value.

# In[100]:


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


# Line chart showing 4 different types of relationships:
# - Attacks on a particular date
# - Deaths on a particular date
# - Total attacks on a particular date
# - Total deaths on a particular date

# In[101]:


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


# For this graph I chose a dark and light purple combo to indicate attacks and yellow-green combo for deaths because these are two color sets that color blind people can see (and what most colors default for them). 

# ### Naples Age and Sex Data

# In[60]:


#To convert tsv file into csv
tsv_file='https://raw.githubusercontent.com/notyubi/cholera/master/naplesCholeraAgeSexData.tsv'
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv('naplesAgeSex.csv',index=False)


# In[102]:


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


# In[103]:


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


# ### UK Census 1851 Dataset

# In[64]:


#To convert tsv file into csv
tsv_file='https://raw.githubusercontent.com/notyubi/cholera/master/UKcensus1851.tsv'
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv('ukCensus.csv',index=False)


# In[104]:


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


# In[105]:


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


# In[92]:


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


# In[91]:


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


# In[106]:


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

