import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

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
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)