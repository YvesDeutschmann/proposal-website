import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from app import app
from templates import home, prediction, card_deck


url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# index layout
app.layout = url_bar_and_content_div

# "complete" layout
app.validation_layout = html.Div([
    url_bar_and_content_div,
    prediction.layout,
    card_deck.layout,
])

# Index callbacks
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == "/":
        return home.layout
    elif pathname == "/prediction":
        return prediction.layout
    elif pathname == "/cards":
        return card_deck.layout
    else:
        return '404'

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
def toggle_left(click, is_open):
    if click:
        return not is_open
    return is_open

if __name__ == '__main__':
    app.run_server(debug=True)