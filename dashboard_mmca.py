import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, State
from mmcalib import *
import ast
import plotly.express as px
"""
Source codes for pre-processing MMCA literature review dataset (data metrics)

author: Pankaj Chejara (pankajchejara23@gmail.com)


"""

lit = LiteratureDataset('4.2023 Summer - data_metrics_constructs.csv',
                        '4.2023 Summer - paper_details.csv','4.2023 Summer - paper_meta.csv')

def reduce_intensity(c,intensity=.2):
    return c.replace('0.8','0.2')

year_options = list(range(1999,2023,1))

marks = {}
for year in year_options:
    marks[year] = year
sankey, node, link = lit.generate_sankey_data(2000,2010)
# creating dash app
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
start_year = []

overview_content = [dbc.Row([
    html.Hr(),
    html.H5('Start and End year selection'), 
    html.P('Select duration which you are interested to explore.')]),
    dbc.Row([
        dcc.RangeSlider(1999, 2023, 1, value=[2000, 2005], marks=marks, id='year_range')
        ]),
    dbc.Row(
        dcc.Graph(id='sankey',
            style={'padding':'2em','width': '100%', 'height': '150%'},
            figure=go.Figure(
                data=[
                    go.Sankey(
                        node = node,
                        link = link,
                    )
                ]
            ))
    )]

app.layout = dbc.Container([
    dbc.Row([]),
    dbc.Row([
        dbc.Col([

                html.H1("MMCA"),
                html.H4("Relationship between data metrics and collaboration aspects"),
                html.P("This visualisation gives an overview of the field of Multiomdal Collaboration Analytics"+
                ". In particular, it provides overview of relationship between data-metrics and collaboration aspects found in past two decades."),
                html.P("LIT lab, Harvard University")
            ])
        ]),
    dbc.Button(
            "Configure dashboard",
            id="collapse-button",
            className="mb-3",
            color="primary",
            n_clicks=0,
        ),
    dbc.Collapse([
        dbc.Row([
            html.H3('Configure dashboard'), 
            html.P('Select what you want to visualize.'),
            dbc.Checklist([
                {'label':'Data types', 'value':1},
                {'label':'metrics smaller', 'value':2},
                {'label':'metrics larger', 'value':3},
                {'label':'outcomes smaller', 'value':4},
                {'label':'outcomes types', 'value':5},
                {'label':'outcomes instrument', 'value':6},
                {'label':'study setting', 'value':7},
            ],value=[],switch=True,inline=True,id='configure'),
            ],style={'padding':'3em','margin-bottom':'2em'},className='border rounded-top rounded-bottom')],id='collapse',is_open=False
    ),
    dbc.Row([
        dbc.Card([
            dbc.CardBody([
                html.H3('Start and End year selection'), 
                html.P('Select duration which you are interested to explore.')]),
                dbc.Row([
                    dcc.RangeSlider(1999, 2023, 1, value=[2000, 2005], marks=marks, id='year_range')
                ]),
            ],style={'padding':'3em','margin-bottom':'2em'})
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='data_type',style={'display':'none'}
            )
        ]),
        dbc.Col([
            dcc.Graph(id='metrics_smaller',style={'display':'none'}
            )
        ]),
        dbc.Col([
            dcc.Graph(id='metrics_larger',style={'display':'none'}
            )
        ]),
    ]
    ),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='outcomes_smaller',style={'display':'none'}
            )
        ]),
        dbc.Col([
            dcc.Graph(id='outcomes_larger',style={'display':'none'}
            )
        ]),
        dbc.Col([
            dcc.Graph(id='outcomes_instrument',style={'display':'none'}
            )
        ]),
    ]
    ),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='study_setting',style={'display':'none'}
            )
        ]),
    ]
    ),
    dbc.Row([
        dcc.Graph(id='sankey',
                    style={'padding':'3em','width': '100%', 'height': '100%'},
                    figure=go.Figure(
                        data=[
                            go.Sankey(
                                node = node,
                                link = link,
                            )
                        ]
                    )
            )
    ]
    )
])

@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(Output('data_type', 'style'),
              [Input('configure', 'value')])
def display_value(value):
    if 1 in value:
        return {'display':'block'}
    else:
        return {'display':'none'}

@app.callback(Output('data_type', 'figure'),
              [Input('configure', 'value_con'),Input('year_range', 'value')])
def display_value(value_con,value):
    year_range = value
    year1 = year_range[0]
    year2= year_range[1]
    data = lit.count_or_mean(year1,year2)['data_stats']
    print(data)
    figure=go.Figure(go.Pie(labels = list(data.keys()),values=list(data.values()),hole=.3,title='Data types'))
    return figure


@app.callback(Output('metrics_smaller', 'style'),
              [Input('configure', 'value')])
def display_value(value):
    if 2 in value:
        return {'display':'block'}
    else:
        return {'display':'none'}

@app.callback(Output('metrics_smaller', 'figure'),
              [Input('configure', 'value_con'),Input('year_range', 'value')])
def display_value(value_con,value):
    year_range = value
    year1 = year_range[0]
    year2= year_range[1]
    data = lit.count_or_mean(year1,year2)['metrics_sm_stats']
    figure=go.Figure(go.Pie(labels = list(data.keys()),values=list(data.values()),hole=.3,title='Metrics'))
    return figure

@app.callback(Output('metrics_larger', 'style'),
              [Input('configure', 'value')])
def display_value(value):
    if 3 in value:
        return {'display':'block'}
    else:
        return {'display':'none'}

@app.callback(Output('metrics_larger', 'figure'),
              [Input('configure', 'value_con'),Input('year_range', 'value')])
def display_value(value_con,value):
    year_range = value
    year1 = year_range[0]
    year2= year_range[1]
    data = lit.count_or_mean(year1,year2)['metrics_lg_stats']
    figure=go.Figure(go.Pie(labels = list(data.keys()),values=list(data.values()),hole=.3,title='Metrics groups'))
    return figure

@app.callback(Output('outcomes_smaller', 'style'),
              [Input('configure', 'value')])
def display_value(value):
    if 4 in value:
        return {'display':'block'}
    else:
        return {'display':'none'}

@app.callback(Output('outcomes_smaller', 'figure'),
              [Input('configure', 'value_con'),Input('year_range', 'value')])
def display_value(value_con,value):
    year_range = value
    year1 = year_range[0]
    year2= year_range[1]
    data = lit.count_or_mean(year1,year2)['outcomes_sm_stats']
    print(data)
    figure=go.Figure(go.Pie(labels = list(data.keys()),values=list(data.values()),hole=.3,title='Outcomes'))
    return figure

@app.callback(Output('outcomes_larger', 'style'),
              [Input('configure', 'value')])
def display_value(value):
    if 5 in value:
        return {'display':'block'}
    else:
        return {'display':'none'}

@app.callback(Output('outcomes_larger', 'figure'),
              [Input('configure', 'value_con'),Input('year_range', 'value')])
def display_value(value_con,value):
    year_range = value
    year1 = year_range[0]
    year2= year_range[1]
    data = lit.count_or_mean(year1,year2)['outcomes_lg_stats']
    print(data)
    figure=go.Figure(go.Pie(labels = list(data.keys()),values=list(data.values()),hole=.3,title='Outcomes groups'))
    return figure

@app.callback(Output('outcomes_instrument', 'style'),
              [Input('configure', 'value')])
def display_value(value):
    if 6 in value:
        return {'display':'block'}
    else:
        return {'display':'none'}

@app.callback(Output('outcomes_instrument', 'figure'),
              [Input('configure', 'value_con'),Input('year_range', 'value')])
def display_value(value_con,value):
    year_range = value
    year1 = year_range[0]
    year2= year_range[1]
    data = lit.count_or_mean(year1,year2)['outcomes_instrument_stats']
    print(data)
    figure=go.Figure(go.Pie(labels = list(data.keys()),values=list(data.values()),hole=.3,title='Outcomes instrument'))
    return figure

@app.callback(Output('study_setting', 'style'),
              [Input('configure', 'value')])
def display_value(value):
    if 7 in value:
        return {'display':'block'}
    else:
        return {'display':'none'}

@app.callback(Output('study_setting', 'figure'),
              [Input('configure', 'value_con'),Input('year_range', 'value')])
def display_value(value_con,value):
    year_range = value
    year1 = year_range[0]
    year2= year_range[1]
    data = lit.count_or_mean(year1,year2)['setting_stats']
    print(data)
    figure=go.Figure(go.Pie(labels = list(data.keys()),values=list(data.values()),hole=.3,title='Outcomes instrument'))
    return figure




@app.callback(Output('sankey', 'figure'),
              [Input('year_range', 'value')])
def display_value(value):
    year_range = value
    value1 = year_range[0]
    value2= year_range[1]
    print(year_range)
    sankey, node, link = lit.generate_sankey_data(year_range[0],year_range[1])
    figure=go.Figure(
        data=[
            go.Sankey(
                node = node,
                link = link,
            )
        ]
    )
    """
    if value2 - value1 > 10:
        figure.update_layout(
            autosize=False,
            width=1500,
            height=2500,)
    elif value2 - value1 >= 3 and value2 > 2018:
        figure.update_layout(
            autosize=False,
            width=1500,
            height=1200,)
    else:
        
    """
    figure.update_layout(height=900,
            font_size=10)
    return figure


if __name__ == "__main__":
    app.run_server(port=8070)

