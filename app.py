import flask
import dash
import dash_bootstrap_components as dbc

# create app object
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', dbc.themes.BOOTSTRAP]
server = flask.Flask(__name__)
app = dash.Dash(
    __name__,
    server=server,
    external_stylesheets=external_stylesheets,
    assets_external_path='https://proposal-pics.s3-us-west-2.amazonaws.com/')
app.scripts.config.serve_locally=False
app.css.config.serve_locally=True

