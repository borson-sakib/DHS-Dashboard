import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv('/Users/pcworld/Desktop/dashproject/sample_25.csv')


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#20B2AA',
    'text': '#111111'
}

app.layout = html.Div([
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),


    html.Div([

    html.Div([

        html.H4(children='Demographic And Health Survey Data Overview'),
        generate_table(df),

    ]),

    html.Div([
        dcc.Graph(
            id='example-graph-2',
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
                        'color': colors['text']
                    }
                }
            }
        ),

    ],),


    ],style = {'columnCount': 2},),



],style={'backgroundColor': colors['background'],
         #"margin-right": "50px",
         #"margin-left": "25px",
         "width": "100%",
         },)

if __name__ == '__main__':
    app.run_server(debug=True)
