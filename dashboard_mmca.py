import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, State
from mmcalib import *
import ast
import plotly.express as px
import json
"""
Source codes for pre-processing MMCA literature review dataset (data metrics)

author: Pankaj Chejara (pankajchejara23@gmail.com)


"""
lit = LiteratureDataset('4.2023 Summer - data_metrics_constructs.csv',
                        '4.2023 Summer - paper_details.csv', '4.2023 Summer - paper_meta.csv')


def reduce_intensity(c, intensity=.2):
    return c.replace('0.8', '0.2')


year_options = list(range(1999, 2023, 1))

marks = {}
for year in year_options:
    marks[year] = year
full, sankey, _, node, link = lit.generate_sankey_data(2000, 2010)
# creating dash app
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
start_year = []

overview_content = [dbc.Row([
    html.Hr(),
    html.H5('Start and End year selection'),
    html.P('Select duration which you are interested to explore.')]),
    dbc.Row([
        dcc.RangeSlider(1999, 2023, 1, value=[
                        2000, 2005], marks=marks, id='year_range')
    ]),
    dbc.Row(
        dcc.Graph(id='sankey',
                  style={'padding': '2em', 'width': '100%', 'height': '150%'},
                  figure=go.Figure(
                      data=[
                          go.Sankey(
                              node=node,
                              link=link,
                          )
                      ]
                  ))
)]

app.layout = dbc.Container([
    dbc.Row([]),
    dbc.Row([
        dbc.Col([

                html.H1("MMCA"),
                html.H4(
                    "Relationship between data metrics and collaboration aspects"),
                html.P("This visualisation gives an overview of the field of Multiomdal Collaboration Analytics" +
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
        html.Div([
            html.H3('Configure sankey dashboard'),
            html.P('Configure order of sankey diagram.'),
            dbc.Row([
                dbc.Col([
                    html.P('Larger metrics'),
                    dbc.Select([
                        {'label': '1', 'value': '1'},
                        {'label': '2', 'value': '2'},
                        {'label': '3', 'value': '3'},
                        {'label': '4', 'value': '4'}
                    ], 1, id='larger_metric')
                ]),
                dbc.Col([
                    html.P('Smaller metrics'),
                    dbc.Select([
                        {'label': '1', 'value': '1'},
                        {'label': '2', 'value': '2'},
                        {'label': '3', 'value': '3'},
                        {'label': '4', 'value': '4'}
                    ], 2, id='smaller_metric')
                ]),
                dbc.Col([
                    html.P('Smaller outcome'),
                    dbc.Select([
                        {'label': '1', 'value': '1'},
                        {'label': '2', 'value': '2'},
                        {'label': '3', 'value': '3'},
                        {'label': '4', 'value': '4'}
                    ], 3, id='smaller_outcome')
                ]),
                dbc.Col([
                    html.P('Larger outcome'),
                    dbc.Select([
                        {'label': '1', 'value': '1'},
                        {'label': '2', 'value': '2'},
                        {'label': '3', 'value': '3'},
                        {'label': '4', 'value': '4'}
                    ], 4, id='larger_outcome')
                ])
            ]),
            dbc.Button("Update layout", id="enter",
                       color="primary", className="p-2 my-3"),
            html.Div(id='error', className="p-2 my-3"),
        ], style={'padding': '3em', 'margin-bottom': '2em'}, className='border rounded-top rounded-bottom')], id='collapse', is_open=False
    ),

    dbc.Row([
        dbc.Card([
            dbc.CardBody([
                html.H3('Start and End year selection'),
                html.P('Select duration which you are interested to explore.')]),
            dbc.Row([
                    dcc.RangeSlider(1999, 2023, 1, value=[
                                    2000, 2005], marks=marks, id='year_range')
                    ]),
        ], style={'padding': '1em', 'margin-bottom': '1em'})
    ]),
    dbc.Modal(
        [
            dbc.ModalHeader("Header", id='modalheader'),
            dbc.ModalBody(dcc.Graph(id='node_details')),
            dbc.ModalFooter(
                dbc.Button("Close", id="close", className="ml-auto")
            ),
        ],
        size="xl",
        id="modal",
    ),
    dbc.Row([

    ]),
    dbc.Row([

        dbc.Col([
            dcc.Graph(id='sankey',
                      style={'padding': '3em',
                             'width': '100%', 'height': '100%'},
                      figure=go.Figure(
                          data=[
                              go.Sankey(
                                  node=node,
                                  link=link,
                              )
                          ]
                      )
                      )
        ])
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


@app.callback(
    Output("error", "children"),
    [Input("enter", "n_clicks"), Input('year_range', 'value')],
    [State("larger_metric", "value"), State("smaller_metric", "value"),
     State("smaller_outcome", "value"), State("larger_outcome", "value")]
)
def func(n_clicks, value, lg_metric, sm_metric, sm_outcome, lg_outcome):
    print('Inside function')
    year_range = value
    year1 = year_range[0]
    year2 = year_range[1]
    error_text = ''
    if len(list(set([str(lg_metric), str(sm_metric), str(sm_outcome), str(lg_outcome)]))) != 4:
        error_text = 'Each node type needs a different level. Please specify a unique level for each type of nodes.'

    return html.P(error_text, className='text-danger')


@app.callback(Output('data_type', 'style'),
              [Input('configure', 'value')])
def display_value(value):
    if 1 in value:
        return {'display': 'inline'}
    else:
        return {'display': 'none'}


@app.callback(Output('modal', 'is_open'),
              [Input('sankey', 'clickData'), Input(
                  'close', 'n_clicks')],
              [State("modal", "is_open")],)
def open_modal(clickData, n1, is_open):
    if n1:
        return not is_open
    elif clickData['points'][0]['label']:
        return True
    else:
        return False


@app.callback(Output('node_details', 'figure'),
              [Input('sankey', 'clickData'), Input('year_range', 'value')])
def display_value(clickData, value):
    print('Click Data:=======>')
    year_range = value
    year1 = year_range[0]
    year2 = year_range[1]
    full, sankey, level_wise_nodes, node, link = lit.generate_sankey_data(
        year_range[0], year_range[1])

    node_label = clickData['points'][0]['label']

    if node_label:
        for key in level_wise_nodes.keys():
            if node_label in level_wise_nodes[key]:
                clicked_node_level = key
                break
        msg = ''
        labels = []
        values = []
        title = ''
        if clicked_node_level == 1:
            targets = full.loc[full['metrics_lg'] == node_label, :]
            print('clicked data in full', targets.shape)
            total_papers = len(targets['paper_id'].unique())
            msg = '{} data has been used in {} papers'.format(
                node_label, total_papers)
            pie_data = targets['metrics_sm'].value_counts().to_dict()
            title = 'Type of features extracted from {} data'.format(
                node_label)
        elif clicked_node_level == 2:
            targets = full.loc[full['metrics_sm'] == node_label, :]
            total_papers = len(targets['paper_id'].unique())
            msg = '{} data has been used in {} papers'.format(
                node_label, total_papers)
            pie_data = targets['outcome_sm'].value_counts().to_dict()
            title = 'Type of outcomes found to be associated with {}'.format(
                node_label)
        elif clicked_node_level == 3:
            targets = full.loc[full['outcome_sm'] == node_label, :]
            total_papers = len(targets['paper_id'].unique())
            msg = '{} construct has been used in {} papers'.format(
                node_label, total_papers)
            pie_data = targets['metrics_sm'].value_counts().to_dict()
            title = 'Type of metrics found to be associated with {}'.format(
                node_label)
        elif clicked_node_level == 4:
            targets = full.loc[full['outcome_lg'] == node_label, :]
            total_papers = len(targets['paper_id'].unique())
            msg = '{} type of construct has been used in {} papers'.format(
                node_label, total_papers)
            pie_data = targets['outcome_sm'].value_counts().to_dict()
            title = 'Type of outcomes grouped under {}'.format(node_label)
        print_data = {}
        labels = [key for key in pie_data.keys()]
        values = [value for value in pie_data.values()]

        if clicked_node_level:
            print_data['level'] = clicked_node_level
        print_data['text'] = msg

        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
        fig.update_layout(title={'text': title, 'xanchor': 'left'})
        return fig
    else:
        return None


@app.callback(Output('sankey', 'figure'),
              [Input("enter", "n_clicks"), Input('year_range', 'value')],
              [State("larger_metric", "value"), State("smaller_metric", "value"), State("smaller_outcome", "value"), State("larger_outcome", "value")])
def display_value(n_clicks, value, lg_metric, sm_metric, sm_outcome, lg_outcome):
    year_range = value
    year1 = year_range[0]
    year2 = year_range[1]
    selected_levels = {'metrics_lg': int(lg_metric),
                       'metrics_sm': int(sm_metric),
                       'outcome_sm': int(sm_outcome),
                       'outcome_lg': int(lg_outcome)
                       }
    full, sankey, _, node, link = lit.generate_sankey_data(
        year_range[0], year_range[1], selected_levels)

    figure = go.Figure(
        data=[
            go.Sankey(
                node=node,
                link=link,
            )
        ]
    )
    figure.update_layout(height=900,
                         font_size=10)
    return figure


if __name__ == "__main__":
    app.run_server(port=8070)
