import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

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

button = dbc.Button(
    "Submit",
    id="submit_button", 
    color="success", 
    block=True)

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

layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(buttongroup, width=3),
                dbc.Col(
                    dcc.Graph(id='graph'), 
                    width=9
                )
            ]
        ),

        html.Br(),

        dcc.Link('Navigate to "/page-1"', href='/page-1')
    ],
className="dash-bootstrap p-5"
)