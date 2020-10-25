import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from app import app
from graph import load_data, plot_data

button_groups = dbc.Row(
    [
        dbc.Col(
            [
                dbc.ButtonGroup(
                    [dbc.Button("Asset 1"), dbc.Button("Jess", outline=True)],
                    size="lg",
                    style={"width": "100%"},
                )
            ],
            width=4
        ),
        
        dbc.Col(
            [
                dbc.ButtonGroup(
                    [dbc.Button("Asset 2"), dbc.Button("Yves", outline=True)],
                    size="lg",
                    style={"width": "100%"},
                )
            ],
            width=4
        ),
        dbc.Col(
            [
                dbc.ButtonGroup(
                    [dbc.Button("Timeframe"), dbc.Button("Forever", outline=True)],
                    size="lg",
                    style={"width": "100%"},
                )
            ],
            width=4
        ),
    ]
)

button = dcc.Link(
    dbc.Button(
        "Show me some details",
        id="details_button", 
        n_clicks=0,
        color="success", 
        block=True,
        size='lg'),
    href='/cards'
)

analysis_card = dbc.CardBody(
    [
        html.H2("Analyis Results"),
        html.P(
            "The analysis of the underlying data shows some ups & downs but there is clearly an positive overall trend. Future returns look promising so my advice is to hold on the asset.",
        ),
        dbc.Row(
            dbc.Col(button)
        )
    ], 
    className='analysis_details'
),

input_card = dbc.CardBody(
    [
        html.H2("Analysis run for"),
        button_groups
    ]
)

data = load_data()
figure = plot_data(data)
            

layout = dbc.Jumbotron(
    [
        dbc.Row(
            [
                dbc.Col(input_card, width=6),
                dbc.Col(analysis_card, width= 6),
                
            ]
        ),
        dcc.Graph(id='graph', figure=figure)
    ],
)