import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from assignments import assignments
from app import app

def generate_card(id, image_src, name):
    """
    Creates Html.Div element as flippable card.
    Input:
    id - string - unique id for the created Div for later reference
    image_src - string - path to related image for that card
    name - string - name of the person(s) on the picture
    Returns:
    card_XY - object - Html.Div with row and column index
    """

    return html.Div(
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
                    html.Img(
                        src='/static/pics/{}'.format(image_src),
                        className = "cards_image"
                    ),
                    html.H1(name),
                    html.P("Some funnyx text...")
                ],
                className = "cards_back"
            )
        ],
        className = "cards_single",
        id = id)

def generate_mycard(id, image_src, name):
    """
    Creates Html.Div element as flippable card.
    Input:
    id - string - unique id for the created Div for later reference
    image_src - string - path to related image for that card
    name - string - name of the person(s) on the picture
    Returns:
    card_XY - object - Html.Div with row and column index
    """

    return html.Div(
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
                    html.Img(src='/static/{}'.format(image_src)),
                    html.H1(name),
                    dbc.Button(
                        "Answer", 
                        id='answer_button',
                        color='primary',
                        block=True
                    ),
                ],
                className = "cards_back"
            )
        ],
        className = "cards_single",
        id = id)

def generate_option_card(option):
    """
    Generates card for answer options.
    Returns
    dbc.Collapse - collapsable html object
    """
    src_no = 'https://media.giphy.com/media/1zSz5MVw4zKg0/source.gif'
    src_yes = 'https://media.giphy.com/media/Ld0P4AdeSDjoY/source.gif'

    return dbc.Collapse(
            [
                html.Div(
                    [
                        html.Img(
                            src= src_yes if option == 'yes' else src_no,
                            className = "cards_gif"
                        ),
                        dbc.Row(
                            [
                                dbc.Col(),
                                dbc.Col(
                                    [
                                        dbc.Button(
                                            option.upper(), 
                                            id='{}_button'.format(option), 
                                            color= 'success' if option == 'yes' else 'danger',
                                            block=True,
                                            size='large'
                                        ),
                                    ],
                                    width=8
                                ),
                                dbc.Col()
                            ],
                            justify='center'
                        )
                    ],
                    className = "cards_gif",
                )
            ],
            className = "cards_single",
            id = '{}_collapse'.format(option)
        )

def generate_decision_cards():
    """
    Generates cards for answer options 'Yes' & 'No'.
    Returns:
    decisions - dictionary containing html objects
    """
    decisions = dict.fromkeys(['yes', 'no'])

    for option in decisions.keys():
        html_object = generate_option_card(option)
        decisions.update({option: html_object})
    return decisions

def create_card_deck():
    """
    Generates all cards that will be rendered on the web page.
    Returns:
    card_deck - List - List of id's for the created cards
    """

    card_deck = []

    for key, element in assignments.items():
        if key == '31':
            card = generate_mycard(element.get("id"), element.get("image"), element.get("name"))
        else:
            card = generate_card(element.get("id"), element.get("image"), element.get("name"))
        
        card_deck.append(element.get("id"))
        assignments.update({ str(key) : {'card': card}})
    return card_deck

card_deck = create_card_deck()
decisions = generate_decision_cards()
empty_card = dbc.Card(className="cards_empty")

row1 = dbc.CardGroup(
    [
        assignments['11']['card'],
        assignments['12']['card'],
        assignments['13']['card'],
        assignments['14']['card'],
        empty_card,
        assignments['15']['card'],
        assignments['16']['card'],
        assignments['17']['card']
    ]
)

row2 = dbc.CardGroup(
    [
        assignments['21']['card'],
        assignments['22']['card'],
        assignments['23']['card'],
        assignments['24']['card'],
        assignments['25']['card'],
        empty_card,
        assignments['26']['card'],
        assignments['27']['card']
    ]
)

row3 = dbc.Row(
    [
        dbc.Col(empty_card),
        dbc.Col(decisions.get("yes")),
        dbc.Col(empty_card),
        assignments['31']['card'],
        dbc.Col(empty_card),
        dbc.Col(decisions.get("no")),
        dbc.Col(empty_card),
    ],
    justify='around'
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
        dbc.Row(
            dbc.Col(row1),
            style={"width":"100%"}
        ),
        dbc.Row(
            dbc.Col(row2),
            style={"width":"100%"}
        ),
        dbc.Row(
            dbc.Col(row3),
            style={"width":"100%"}
        ),
    ]
)

for card in  card_deck:
    @app.callback(
        Output(card, 'className'),
        [Input(card, 'n_clicks')]
    )
    def flip_card(n_clicks):
        if n_clicks is None:
            raise PreventUpdate
        elif (n_clicks % 2 == 0):
            return "cards_single"
        else:
            return "cards_single flip"

# Card Deck callbacks
@app.callback(
    Output("yes_collapse", "is_open"),
    [Input("answer_button", "n_clicks")],
    [State("yes_button", "is_open")],
)
def toggle_yes(click, is_open):
    if click:
        return not is_open
    return is_open

@app.callback(
    Output("no_collapse", "is_open"),
    [Input("answer_button", "n_clicks")],
    [State("no_button", "is_open")],
)
def toggle_no(click, is_open):
    if click:
        return not is_open
    return is_open
