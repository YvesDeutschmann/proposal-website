import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app

subject1_dd =  dcc.Dropdown(
    options=[{"label": "Jess", "value": "Jess"}],
    placeholder="Select subject 1 for prediction"
    )

subject2_dd =  dcc.Dropdown(
    options=[{"label": "Yves", "value": "Yves"}],
    placeholder="Select subject 2 for prediction"
    )

timeframe_dd =  dcc.Dropdown(
    options=[{"label": "forever", "value": "forever"}],
    placeholder="Select timeframe for prediction"
    )

button = dcc.Link(
    dbc.Button(
        "Analyze",
        id="analyze_button", 
        n_clicks=0,
        color="success", 
        block=True,
        size='lg'),
    href='/prediction'
)


buttongroup = html.Div(
    [
        subject1_dd,
        html.Br(), 
        subject2_dd,
        html.Br(),
        timeframe_dd,
        html.Br(),
        button
    ]
)

jumbotron = dbc.Jumbotron(
    [
        html.H1("Asset Forecast"),
        html.P("This is a simple app to forecast developments on specific assets"),
        html.Hr(),
        html.P("Please choose from the assets below and start the prediction."),
        buttongroup,
    ],
    className='jumbo'
)

layout = dbc.Row(
    dbc.Col(jumbotron, width={"size":6, "offset":3})
)