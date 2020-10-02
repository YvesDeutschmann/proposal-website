import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

import flask

subject_dropdown = dbc.FormGroup(
    [
        dbc.Label("Subject", html_for="dropdown"),
        dcc.Dropdown(
            id="subject",
            options=[
                {"label": "Jess", "value": "Jess"},
            ],
        ),
    ]
)

object_dropdown = dbc.FormGroup(
    [
        dbc.Label("Object", html_for="dropdown"),
        dcc.Dropdown(
            id="object",
            options=[
                {"label": "Yves", "value": "Yves"},
            ],
        ),
    ]
)

timeframe_dropdown = dbc.FormGroup(
    [
        dbc.Label("Timeframe", html_for="dropdown"),
        dcc.Dropdown(
            id="timeframe",
            options=[
                {"label": "forever", "value": "forever"},
            ],
        ),
    ]
)

form = dbc.Form([subject_dropdown, object_dropdown, timeframe_dropdown])

layout = html.Div([

    form,
    html.Br(),

    dcc.Link('Navigate to "/page-1"', href='/page-1'),
])