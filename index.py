import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app
from templates import prediction, card_deck

# index layout
app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ]
)

# "complete" layout
app.validation_layout = html.Div([
    prediction.layout,
    card_deck.layout,
])

# Index callbacks
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == "/":
        return prediction.layout
    elif pathname == "/cards":
        return card_deck.layout
    else:
        return '404'

# # Page 1 callbacks
@app.callback(Output('Placeholder', 'children'),
              [Input('submit_button', 'n_clicks')])
def update_output(n_clicks):
    return static/test.jpg

if __name__ == '__main__':
    app.run_server(debug=True)