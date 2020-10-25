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
            id = '{}_collapse'.format(option),
        )

def generate_option_modal(option):
    """
    Serves modal depending on the chosen answer.
    Input:
    option - str - choses answer ('yes' OR 'no')
    Returns:
    modal - html object - modal object with content respective to the option
    """
    header_yes = 'She said YES!'
    src_yes = 'https://media.giphy.com/media/s2qXK8wAvkHTO/giphy.gif'
    text_yes = 'This goes rioght along with my prediction. Good choice in the first place and now hold on to this asset. Also grab a drink and celebrate!'
    button_yes = dbc.Button(
        "Alright, gimme that ring!",
        id='final_yes',
        color='success',
        className='ml-auto'
    )

    header_no = 'Say whut?'
    src_no = 'https://media.giphy.com/media/l3q2K5jinAlChoCLS/giphy.gif'
    text_no = 'Please note: By confirming this choice countless puppies & kittens will be tortured and killed. Do you really want to confirm your choice?'
    button_no = dbc.Button(
        "Well, kill those puppies...",
        id='final_no',
        color='danger',
        className='ml-auto'
    )

    return dbc.Modal(
            [
                dbc.ModalHeader(header_yes if option == 'yes' else header_no),
                dbc.ModalBody(
                    [
                        html.Img(
                        src= src_yes if option == 'yes' else src_no
                        ),
                        html.P(text_yes if option == 'yes' else text_no)
                    ]
                ),
                dbc.ModalFooter(
                    button_yes if option == 'yes' else button_no
                ),
            ],
            id="{}_modal".format(option),
            centered=True,
        )

def generate_decision_objects():
    """
    Generates cards & modals for answer options 'Yes' & 'No'.
    Returns:
    decisions - dictionary containing html objects
    """
    decisions = dict.fromkeys(['yes', 'no'])

    for option in decisions.keys():
        card = generate_option_card(option)
        modal = generate_option_modal(option)
        decisions[option] = {'card' : card, 'modal': modal}
        
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
decisions = generate_decision_objects()
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
        dbc.Col(decisions["yes"].get("card")),
        dbc.Col(empty_card),
        assignments['31']['card'],
        dbc.Col(empty_card),
        dbc.Col(decisions["no"].get("card")),
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
        decisions["yes"].get("modal"),
        decisions["no"].get("modal")
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

@app.callback(
    Output("yes_collapse", "is_open"),
    [Input("answer_button", "n_clicks")],
    [State("yes_collapse", "is_open")],
)
def toggle_yes(click, is_open):
    if click:
        return not is_open
    return is_open

@app.callback(
    Output("no_collapse", "is_open"),
    [Input("answer_button", "n_clicks")],
    [State("no_collapse", "is_open")],
)
def toggle_no(click, is_open):
    if click:
        return not is_open
    return is_open

@app.callback(
    Output('yes_modal', 'is_open'),
    [Input('yes_button', 'n_clicks')],
    [State('yes_modal', 'is_open')]
)
def toggle_yes_modal(yes, is_open):
    if yes:
        return not is_open
    return is_open

@app.callback(
    Output('no_modal', 'is_open'),
    [Input('no_button', 'n_clicks')],
    [State('no_modal', 'is_open')]
)
def toggle_no_modal(no, is_open):
    if no:
        return not is_open
    return is_open