import json
import requests
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
from dash.dependencies import Input, Output, State
from flask import Flask
import plotly.graph_objects as go
pd.options.mode.chained_assignment = None

external_stylesheets = ['https://fonts.googleapis.com/css?family=Open+Sans:300,400,700',
                        'https://codepen.io/chriddyp/pen/bWLwgP.css']

server = Flask(__name__)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, server=server)

app.css.config.serve_locally = True
app.config.suppress_callback_exceptions = True
app.scripts.config.serve_locally = True

application = app.server

app.layout = html.Div(children=[

    # first column
    html.Div(children=[

        # start time
        html.Label(children=['Start Time'], style={'font-size': '120%', 'margin-top': '2vw', 'color': '#343a40',
        'font-weight': 'bold'}),

        html.Div(children=[

            html.Label('Day', style={'font-size': '90%', 'width': '2.5vw', 'margin': '1vw 0.5vw 0vw 0vw',
            'display': 'inline-block'}),

            dcc.Input(id='start-day',
                      type='number',
                      min=1,
                      max=31,
                      value=1,
                      style={'height': '1.75vw', 'width': '50%', 'font-size': '90%', 'display': 'inline-block'}),

        ], className='row'),

        html.Div(children=[

            html.Label('Month', style={'font-size': '90%', 'width': '2.5vw', 'margin': '1vw 0.5vw 0vw 0vw',
            'display': 'inline-block'}),

            dcc.Input(id='start-month',
                      type='number',
                      min=1,
                      max=12,
                      value=6,
                      style={'height': '1.75vw', 'width': '50%', 'font-size': '90%', 'display': 'inline-block'}),

        ], className='row'),

        html.Div(children=[

            html.Label('Year', style={'font-size': '90%', 'width': '2.5vw', 'margin': '1vw 0.5vw 0vw 0vw',
            'display': 'inline-block'}),

            dcc.Input(id='start-year',
                      type='number',
                      min=2019,
                      max=2020,
                      value=2020,
                      style={'height': '1.75vw', 'width': '50%', 'font-size': '90%', 'display': 'inline-block'}),

        ], className='row'),

        html.Div(children=[

            html.Label('Hour', style={'font-size': '90%', 'width': '2.5vw', 'margin': '1vw 0.5vw 0vw 0vw',
            'display': 'inline-block'}),

            dcc.Input(id='start-hour',
                      type='number',
                      min=0,
                      max=23,
                      value=7,
                      style={'height': '1.75vw', 'width': '50%', 'font-size': '90%', 'display': 'inline-block'}),

        ], className='row'),

        html.Div(children=[

            html.Label('Minute', style={'font-size': '90%', 'width': '2.5vw', 'margin': '1vw 0.5vw 0vw 0vw',
            'display': 'inline-block'}),

            dcc.Input(id='start-minute',
                      type='number',
                      min=0,
                      max=60,
                      value=0,
                      style={'height': '1.75vw', 'width': '50%', 'font-size': '90%', 'display': 'inline-block'}),

        ], className='row'),

        html.Div(children=[

            html.Label('Second', style={'font-size': '90%', 'width': '2.5vw', 'margin': '1vw 0.5vw 0vw 0vw',
            'display': 'inline-block'}),

            dcc.Input(id='start-second',
                      type='number',
                      min=0,
                      max=60,
                      value=0,
                      style={'height': '1.75vw', 'width': '50%', 'font-size': '90%', 'display': 'inline-block'}),

        ], className='row'),

        # end time
        html.Label(children=['End Time'], style={'font-size': '120%', 'margin-top': '2vw', 'color': '#343a40',
        'font-weight': 'bold'}),

        html.Div(children=[

            html.Label('Day', style={'font-size': '90%', 'width': '2.5vw', 'margin': '1vw 0.5vw 0vw 0vw',
            'display': 'inline-block'}),

            dcc.Input(id='end-day',
                      type='number',
                      min=1,
                      max=31,
                      value=1,
                      style={'height': '1.75vw', 'width': '50%', 'font-size': '90%', 'display': 'inline-block'}),

        ], className='row'),

        html.Div(children=[

            html.Label('Month', style={'font-size': '90%', 'width': '2.5vw', 'margin': '1vw 0.5vw 0vw 0vw',
            'display': 'inline-block'}),

            dcc.Input(id='end-month',
                      type='number',
                      min=1,
                      max=12,
                      value=6,
                      style={'height': '1.75vw', 'width': '50%', 'font-size': '90%', 'display': 'inline-block'}),

        ], className='row'),

        html.Div(children=[

            html.Label('Year', style={'font-size': '90%', 'width': '2.5vw', 'margin': '1vw 0.5vw 0vw 0vw',
            'display': 'inline-block'}),

            dcc.Input(id='end-year',
                      type='number',
                      min=2019,
                      max=2020,
                      value=2020,
                      style={'height': '1.75vw', 'width': '50%', 'font-size': '90%', 'display': 'inline-block'}),

        ], className='row'),

        html.Div(children=[

            html.Label('Hour', style={'font-size': '90%', 'width': '2.5vw', 'margin': '1vw 0.5vw 0vw 0vw',
            'display': 'inline-block'}),

            dcc.Input(id='end-hour',
                      type='number',
                      min=0,
                      max=23,
                      value=12,
                      style={'height': '1.75vw', 'width': '50%', 'font-size': '90%', 'display': 'inline-block'}),

        ], className='row'),

        html.Div(children=[

            html.Label('Minute', style={'font-size': '90%', 'width': '2.5vw', 'margin': '1vw 0.5vw 0vw 0vw',
            'display': 'inline-block'}),

            dcc.Input(id='end-minute',
                      type='number',
                      min=0,
                      max=60,
                      value=0,
                      style={'height': '1.75vw', 'width': '50%', 'font-size': '90%', 'display': 'inline-block'}),

        ], className='row'),

        html.Div(children=[

            html.Label('Second', style={'font-size': '90%', 'width': '2.5vw', 'margin': '1vw 0.5vw 0vw 0vw',
            'display': 'inline-block'}),

            dcc.Input(id='end-second',
                      type='number',
                      min=0,
                      max=60,
                      value=0,
                      style={'height': '1.75vw', 'width': '50%', 'font-size': '90%', 'display': 'inline-block'}),

        ], className='row'),

        # update button
        html.Button(id='update-button', n_clicks=0, children=['Update'], style={'display': 'block', 'color': 'white',
        'background-color': '#8a348e', 'width': '10vw', 'height': '2.25vw', 'line-height': '2.25vw', 'font-size': '0.6vw',
        'text-align': 'center', 'margin': '2.5vw 0vw 0vw 0vw'}),

    ], style={'display': 'inline-block', 'vertical-align': 'top', 'width': '20vw', 'margin': '0vw 3vw 0vw 2vw'}),

    # second column
    html.Div(children=[

        # graph
        html.Div(children=[

            dcc.Graph(id='graph', config={'responsive': True, 'autosizable': True}, style={'margin': '0',
            'padding': '0', 'height': '22vw', 'width': '62vw'}),

        ], className='row', style={'height': '22vw', 'width': '62vw', 'display': 'block'}),

        # tables
        html.Div([

            html.Div(children=[

                html.Label(children=['Historical Data'], style={'font-size': '120%', 'margin-top': '2vw',
                'color': '#343a40', 'font-weight': 'bold'}),

                dt.DataTable(id='data-table', style_table={'width': '27vw', 'min-width': '27vw', 'max-width': '27vw',
                'height': '15vw', 'min-height': '15vw', 'max-height': '15vw', 'overflow-y': 'auto', 'overflow-x': 'auto',
                'margin-top': '1vw'}, style_cell={'text-align': 'left', 'font-family': 'Open Sans', 'font-size': '90%',
                'height': '98%', 'color': '#212121'}, style_header={'color': 'white', 'background-color': '#8a348e',
                'text-transform': 'capitalize'}),

            ], style={'display': 'inline-block', 'vertical-align': 'top', 'margin-left': '2vw'}),

            html.Div(children=[

                html.Label(children=['Descriptive Statistics'], style={'font-size': '120%', 'margin-top': '2vw',
                'color': '#343a40', 'font-weight': 'bold'}),

                dt.DataTable(id='stats-table', style_table={'width': '27vw', 'min-width': '27vw', 'max-width': '27vw',
                'height': '15vw', 'min-height': '15vw', 'max-height': '15vw', 'overflow-y': 'auto', 'overflow-x': 'auto',
                'margin-top': '1vw'}, style_cell={'text-align': 'left', 'font-family': 'Open Sans', 'font-size': '90%',
                'height': '98%', 'color': '#212121'}, style_header={'color': 'white', 'background-color': '#8a348e',
                'text-transform': 'capitalize'}),

            ], style={'display': 'inline-block', 'vertical-align': 'top', 'margin-left': '4vw'}),

        ], className='row', style={'height': '15vw', 'width': '65vw', 'display': 'block'}),

    ], style={'display': 'inline-block', 'vertical-align': 'top', 'width': '60vw', 'margin': '0vw 1vw 0vw 2vw'}),

])

@app.callback([Output('graph', 'figure'), Output('data-table', 'data'), Output('data-table', 'columns'),
    Output('stats-table', 'data'), Output('stats-table', 'columns')], [Input('update-button', 'n_clicks')],
    [State('start-day', 'value'), State('start-month', 'value'), State('start-year', 'value'),
     State('start-hour', 'value'), State('start-minute', 'value'), State('start-second', 'value'),
     State('end-day', 'value'), State('end-month', 'value'), State('end-year', 'value'),
     State('end-hour', 'value'), State('end-minute', 'value'), State('end-second', 'value')])
def update_dashboard(n_clicks, start_day, start_month, start_year, start_hour, start_minute, start_second,
    end_day, end_month, end_year, end_hour, end_minute, end_second):

    #####################################################################################################
    # # extract the start time
    # start_time = pd.Timestamp(str(start_year) + '-' + str(start_month) + '-' + str(start_day) + \
    # ' ' + str(start_hour) + ':' + str(start_minute) + ':' + str(start_second))
    #
    # # extract the end time
    # end_time = pd.Timestamp(str(end_year) + '-' + str(end_month) + '-' + str(end_day) + \
    # ' ' + str(end_hour) + ':' + str(end_minute) + ':' + str(end_second))
    #
    # # load the data
    # df = pd.read_csv('data/database.csv', index_col=0)
    # df['time'] = pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M:%S')
    # df = df[(df['time'] >= start_time) & (df['time'] <= end_time)]
    #####################################################################################################

    # extract the start time
    start_time = pd.Timestamp(str(start_year) + '-' + str(start_month) + '-' + str(start_day) + \
    ' ' + str(start_hour) + ':' + str(start_minute) + ':' + str(start_second))

    # extract the end time
    end_time = pd.Timestamp(str(end_year) + '-' + str(end_month) + '-' + str(end_day) + \
    ' ' + str(end_hour) + ':' + str(end_minute) + ':' + str(end_second))

    # define the time interval
    intervals = [start_time.strftime(format='%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z' + '/' + \
                 end_time.strftime(format='%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z']

    # define the Druid URL
    url = 'http://54.78.73.75:8888/druid/v2/?pretty'

    # define the Druid query
    query = {'queryType': 'scan',
             'dataSource': '1_1_Orders',
             'intervals': intervals,
             'granularity': 'all'}

    # run the Druid query
    results = json.dumps(requests.post(url, headers={'Content-Type': 'application/json'}, json=query).json()[1]['events'])

    # organize the results of the Druid
    # query in a pandas data frame
    df = pd.read_json(results, orient='records')
    df = df[['__time', 'Value']]
    df.rename(columns={'__time': 'time', 'Value': 'value'}, inplace=True)
    df.sort_values(by='time', inplace=True)

    # calculate the descriptive statistics
    ds = df.describe().reset_index()
    ds.columns = ['metric', 'value']

    # create the graph
    layout = {'plot_bgcolor': 'white',
              'paper_bgcolor': 'white',
              'margin': {'t': 10, 'b': 10, 'l': 10, 'r': 10, 'pad': 0},
              'showlegend': False,
              'yaxis': {'showgrid': True,
                        'zeroline': False,
                        'mirror': True,
                        'color': '#737373',
                        'linecolor': '#d9d9d9',
                        'gridcolor': '#d9d9d9',
                        'tickformat': '$,.0f'},
              'xaxis': {'range': [df['time'].min(), df['time'].max()],
                        'autorange': False,
                        'showgrid': True,
                        'zeroline': False,
                        'mirror': True,
                        'color': '#737373',
                        'linecolor': '#d9d9d9',
                        'gridcolor': '#d9d9d9',
                        'type': 'date',
                        'tickformat': '%d %b %y %H:%M',
                        'tickangle': 0,
                        'nticks': 5,
                        'rangeslider': {'visible': True},
                        'rangeselector': {'buttons': [
                            {'count': 10, 'label': '10m', 'step': 'minute', 'stepmode': 'backward'},
                            {'count': 30, 'label': '30m', 'step': 'minute', 'stepmode': 'backward'},
                            {'count': 60, 'label': '60m', 'step': 'minute', 'stepmode': 'backward'},
                            {'step': 'all'}]}}}

    data = go.Scatter(x=df['time'],
                      y=df['value'],
                      mode='lines',
                      line=dict(color='#8a348e', width=1),
                      hovertemplate='<b>Time:</b> %{x|%d %b %Y %H:%M:%S}<br>'
                                    '<b>Value:</b> %{y: $,.2f}<extra></extra>')

    fig = go.Figure(data=data, layout=layout)

    # create the table with the data
    df['value'] = df['value'].apply(lambda x: format(x, ',.2f'))
    data_table_data = df.to_dict(orient='records')
    data_table_columns = [{'id': str(x), 'name': str(x)} for x in list(df.columns)]

    # create the table with the descriptive statistics
    ds['value'] = ds['value'].apply(lambda x: format(x, ',.2f'))
    stats_table_data = ds.to_dict(orient='records')
    stats_table_columns = [{'id': str(x), 'name': str(x)} for x in list(ds.columns)]

    return [fig, data_table_data, data_table_columns, stats_table_data, stats_table_columns]

if __name__ == '__main__':
    application.run(debug=False)
