import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from app import app

empty_card = dbc.Card()

card = dbc.Card(
    [
        dbc.CardImg(src='/static/sample200.png'),
        dbc.CardHeader(html.H4("Someones Name")),
        dbc.CardBody(html.P("Some funny punchline")),
    ]
)

my_card = dbc.Card(
    [
        dbc.CardImg(src='/static/sample200.png'),
        dbc.CardHeader(html.H4("Mr. Bossypants")),
        dbc.Button(
            "Answer", 
            id='answer_button',
            color='primary',
            block=True), 
    ]
)

yes_card = dbc.Collapse(
    dbc.Card(
        [
            dbc.CardHeader(),
            dbc.CardImg(src='https://media.giphy.com/media/Ld0P4AdeSDjoY/source.gif'),
            dbc.Button("Yes", id='yes_button', color='success'),
            dbc.CardFooter()
        ]
    ),
    id='yes_collapse'
)

no_card = dbc.Collapse(
    dbc.Card(
        [
            dbc.CardHeader(),
            dbc.CardImg(src='https://media.giphy.com/media/1zSz5MVw4zKg0/source.gif'),
            dbc.Button("No", id='no_button', color='danger'),
            dbc.CardFooter()
        ]
    ),
    id='no_collapse'
)

row1 = dbc.CardGroup(
    [
        card, 
        card,
        card, 
        card, 
        empty_card,
        card,
        card,
        card
    ]
)

row2 = dbc.CardGroup(
    [
        card, 
        card,
        card,
        card,
        card,
        empty_card,
        card,
        card
    ]
)

row3 = dbc.Row(
    [
        dbc.Col(empty_card),
        dbc.Col(yes_card),
        dbc.Col(empty_card),
        dbc.Col(my_card),
        dbc.Col(empty_card),
        dbc.Col(no_card),
        dbc.Col(empty_card),
    ],
    
)

final_decision = dbc.Row(
    [
        dbc.Col(
            dbc.Button(
            "Yes", 
            id='yes_button',
            color='success',
            block=True), 
        width=4),
        dbc.Col(
            dbc.Button(
            "No", 
            id='no_button',
            color='danger',
            block=True), 
        width=4),
    ],
    justify='center'
)

layout = html.Div(
    [
        dbc.Row(
            dbc.Col(row1),
            style={"width":"100%"}
        ),
        dbc.Row(
            dbc.Col(row2),
            style={"width":"100%"}
        ),
        row3
        # dbc.Row(
        #     [
        #         dbc.Col(
        #             dbc.Button(
        #             "Yes", 
        #             id='yes_button',
        #             color='success',
        #             block=True), 
        #         width=4),
        #     ]
        #     my_card, justify='center'),
        # final_decision
    ]
)