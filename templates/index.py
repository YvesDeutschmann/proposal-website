import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as bsc
from dash.dependencies import Input, Output, State

import flask

from templates import card_deck.layout as card_deck

app = dash.Dash(__name__)

url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

layout_index = html.Div([

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

form = dbc.Form([dropdown, slider, range_slider])

    dcc.Link('Navigate to "/page-1"', href='/page-1'),
    html.Br(),
    dcc.Link('Navigate to "/page-2"', href='/page-2'),
])



layout_page_2 = html.Div([
    html.H2('Page 2'),
    dcc.Dropdown(
        id='page-2-dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='page-2-display-value'),
    html.Br(),
    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    dcc.Link('Navigate to "/page-1"', href='/page-1'),
])

# index layout
app.layout = url_bar_and_content_div

# "complete" layout
app.validation_layout = html.Div([
    url_bar_and_content_div,
    layout_index,
    card_deck,
    layout_page_2,
])


# Index callbacks
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == "/page-1":
        return layout_page_1
    elif pathname == "/page-2":
        return layout_page_2
    else:
        return layout_index





# Page 2 callbacks
@app.callback(Output('page-2-display-value', 'children'),
              [Input('page-2-dropdown', 'value')])
def display_value(value):
    print('display_value')
    return 'You have selected "{}"'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)