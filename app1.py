import base64
import datetime
import io

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.express as px
import pandas as pd

df=pd.read_csv('/Users/pcworld/Desktop/dashproject/2014.csv')

df_division=df[['v016','v024','v025','v027','v013']]
df_five=df_division.groupby('v013').count()
print(df_five)

fig=px.pie(df_division,values='v016',names='v024',title='Divisional Survey Distribution')
fig1=px.pie(df_division,values='v027',names='v025',title='Rural vs Urban count')
fig2=px.bar(df_five,x='v013',y='v024')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app1 = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#1E497F',
    'text': '#111111',
    'text1': 'white'}

app1.layout = html.Div([

    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            # 'textAlign':'left',
        }
    ),

    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    html.Hr(),

    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '50%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-data-upload'),

    html.Div([
        dcc.Graph(figure=fig1),
        html.Hr(),
        dcc.Graph(
            id='example-graph-1',
            figure={
                'data': [
                    {'x': [1], 'y': [4], 'type': 'bar', 'name': 'Dhaka'},
                    {'x': [2], 'y': [7], 'type': 'bar', 'name': 'Chittagong'},
                    {'x': [3], 'y': [2], 'type': 'bar', 'name': 'Barishal'},
                    {'x': [4], 'y': [5], 'type': 'bar', 'name': 'Rangpur'},
                ],
                'layout': {
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text1']
                    }
                }
            }
        ),
        html.Hr(),
        dcc.Graph(figure=fig),
        html.Hr(),
    ], style={'columnCount': 3}, ),


    html.Div([
        #dcc.Graph(figure=fig2),


    ]),
], style={'columnCount': 1}, )


def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            data=df.to_dict('records'),
            filter_action='native',
            columns=[{'name': i, 'id': i} for i in df.columns],
            style_header={'backgroundColor': 'rgb(30, 30, 30)',
                          'fontWeight': 'bold'},
            style_cell={
                'backgroundColor': colors['background'],  # 'rgb(50, 50, 50)',
                'color': 'white',
                'textAlign': 'left'
            },
            page_action='none',
            style_table={'height': '500px', 'width': '70%', 'overflowY': 'auto', 'margin': '10px'}
        ),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all',
            'width': '50%'
        })
    ])


@app1.callback(Output('output-data-upload', 'children'),
               [Input('upload-data', 'contents')],
               [State('upload-data', 'filename'),
                State('upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children


if __name__ == '__main__':
    app1.run_server(debug=True)
