from dash.dcc.Graph import Graph
from dash.html.Div import Div
from dash.html.H1 import H1
from dash.html.H4 import H4
import pandas as pd
import numpy as np
import dash
import plotly.graph_objects as go
from dash import html
from dash import dcc
from dash.dependencies import Input,Output
import plotly.express as px

data=pd.read_csv('covid19.csv')
Total=data['Total Cases'].sum()
Active=data['Active'].sum()
Discharged=data['Discharged'].sum()
Deaths=data['Deaths'].sum()
fig=px.scatter(data,
          x='State/UTs',
          y='Total Cases',
          color='State/UTs',
          hover_data=['Active','Discharged','Deaths','Active Ratio','Discharge Ratio','Death Ratio']
          
)
import plotly.graph_objects as go
from plotly.subplots import make_subplots

labels = ['Total Cases','Active Cases','Discharged Cases','Total Deaths']

# Create subplots: use 'domain' type for Pie subplot
fig1 = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
fig1.add_trace(go.Pie(labels=labels, values=[Total, Active, Discharged,Deaths], name="Corona Cases"),
              1, 1)

# Use `hole` to create a donut-like pie chart
fig1.update_traces(hole=.4, hoverinfo="label+percent+name")

fig1.update_layout(
    
    # Add annotations in the center of the donut pies.
    plot_bgcolor='#cefcfc',
    annotations=[dict(text='Top Stats', x=0.50, y=0.5, font_size=20, showarrow=False)
                 ])
fig1.show()

fig2=px.line(data,
      'State/UTs',
      'Active',
       )
fig2.show()

fig3=px.line(data,
      'State/UTs',
      'Discharged',
       )
fig3.show()

fig4=px.line(data,
      'State/UTs',
      'Active Ratio',
       )
fig4.show()

fig5=px.line(data,
      'State/UTs',
      'Discharge Ratio',
       )
fig5.show()

fig6=px.line(data,
      'State/UTs',
      'Death Ratio',
       )
fig6.show()

## external stylesheet
external_stylesheet=[
{
'link rel':"stylesheet" ,
'href':"https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css",
'integrity':"sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" ,
'crossorigin':"anonymous"
}
]

app=dash.Dash(__name__,external_stylesheets=external_stylesheet)
## cotainer
app.layout=html.Div([html.H1('Coronavirus Pandemic',style={'color':'#000','text-align':'center'}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Total Cases'),
                    html.H4(Total)
                ],className='card-body')
            ],className='card bg-danger')
        ],className='col-md-3'),

        html.Div([
            html.Div([
                html.Div([
                    html.H3('Active Cases'),
                    html.H4(Active)
                ],className='card-body')
            ],className='card bg-info')
        ],className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Discharged'),
                    html.H4(Discharged)
                ],className='card-body')
            ],className='card bg-success')
        ],className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Total Deaths'),
                    html.H4(Deaths)
                ],className='card-body')
            ],className='card bg-warning')
        ],className='col-md-3')
    ],className='row'),
    
    html.Div([
        html.Div([
            html.H3('Corona Stats Of All States',style={'color':'#000','text-align':'center','padding': 10}),
            dcc.Graph(figure=fig)

        ],className='col-md-12')
    ],className='row'),
    html.Div([
        html.Div([
            html.H3('Pie chart comparison of all type of cases',style={'color':'#000','text-align':'center','padding': 10}),
            dcc.Graph(figure=fig1)
        ],className='col-md-12')
    ],className='row'),
    html.Div([
        html.Div([
            html.H3('Active Cases Trend',style={'color':'#000','text-align':'center','padding': 10}),
            dcc.Graph(figure=fig2)
        ],className='col-md-12')
    ],className='row'),
    html.Div([
        html.Div([
            html.H3('Discharged Cases Trend',style={'color':'#000','text-align':'center','padding': 10}),
            dcc.Graph(figure=fig3)
        ],className='col-md-12')
    ],className='row'),
    html.Div([
        html.Div([
            html.H3('Active Ratio Trend',style={'color':'#000','text-align':'center','padding': 10}),
            dcc.Graph(figure=fig4)
        ],className='col-md-12')
    ],className='row'),
    html.Div([
        html.Div([
            html.H3('Discharge Ratio Trend',style={'color':'#000','text-align':'center','padding': 10}),
            dcc.Graph(figure=fig5)
        ],className='col-md-12')
    ],className='row'),
    html.Div([
        html.Div([
            html.H3('Death Ratio Trend',style={'color':'#000','text-align':'center','padding': 10}),
            dcc.Graph(figure=fig6)
        ],className='col-md-12')
    ],className='row')
    
],className='container')
if __name__=='__main__':
    app.run_server(debug=True)