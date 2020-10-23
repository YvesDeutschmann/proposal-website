import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ClientsideFunction

from app import app

empty_card = dbc.Card()

card = dbc.Card(
    [
        
                dbc.CardImg(src='/static/question.png', className="card-img"),
                dbc.CardImg(src='/static/sample200.png'),
                dbc.CardHeader(html.H4("Someones Name")),
                dbc.CardBody(html.P("Some funny punchline"))
    ],
    className="card"
)

# card = html.Div(
#     [
#         html.Div(
#             [
#                 html.Img(src='/static/question.png', className="card-img"),
#                 html.Div(
#                     [
#                         html.Img()
#                     ],
#                     className="card-img-overlay"
#                 )
#             ],
#             className="card-inner"
#         )
        
#                 dbc.CardImg(src='/static/question.png', className="card-img"),
#                 dbc.CardImg(src='/static/sample200.png'),
#                 dbc.CardHeader(html.H4("Someones Name")),
#                 dbc.CardBody(html.P("Some funny punchline"))
#     ],
#     className="card bg-dark text-white"
# )

front = dbc.Card(
                html.Img(src='/static/question.png'),
                id = "front",
                className="front"
)

back = dbc.Card(
    [
        html.Img(src='/static/sample200.png'),
        html.H4("Mr. Bossypants"),
        html.Button(
            "Answer", 
            id='answer_button',
            # color='primary',
            # block=True
        ),
    ],
    id = "back",
    className="back"
)

my_card = html.Div(
    html.Div(
        [
            front, 
            back
        ],
        id = "card",
        className = "card",        
    ),
    className="container"
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

test = html.Div(
    [
        html.Div(
            [
                html.Img(
                    src='/static/question.png',
                    className = "cards_image"
                ),
                html.H1("Click Me!")
            ],
            className = "cards_front"
        ),
        html.Div(
            [
                html.Img(src='/static/sample200.png'),
                html.H1("Some Name"),
                html.P("Some funnyx text...")
            ],
            className = "cards_back"
        )
    ],
    className = "cards_single",
    id = 'test'
)

layout = html.Div(
    [
        # dbc.Row(
        #     dbc.Col(row1),
        #     style={"width":"100%"}
        # ),
        # dbc.Row(
        #     dbc.Col(row2),
        #     style={"width":"100%"}
        # ),
        # row3
        dbc.Col(
            test,
            width=2
        )
        
    ]
)

@app.callback(
    Output('test', 'className'),
    [Input('test', 'n_clicks')]
)
def flip_card(n_clicks):
    
    if (n_clicks % 2 == 0):
        return "cards_single"
    else:
        return "cards_single flip"
