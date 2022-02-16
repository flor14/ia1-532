from dash import Dash, html, dcc, Input, Output
import altair as alt
from vega_datasets import data


# Read in global data
cars = data.cars()

# Setup app and layout/frontend
app = Dash(__name__,  external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server

app.layout = html.Div([
    html.Iframe(
        id='iframe',
        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
    dcc.Dropdown(
        id='xcol-widget',
        value='Horsepower',  # REQUIRED to show the plot on the first page load
        options=[{'label': col, 'value': col} for col in cars.columns]),
    dcc.Dropdown(
        id='ycol-widget',
        value='Horsepower',  # REQUIRED to show the plot on the first page load
        options=[{'label': col, 'value': col} for col in cars.columns])])


# Set up callbacks/backend

@app.callback(
    Output('iframe', 'srcDoc'),
    Input('xcol-widget', 'value'),
    Input('ycol-widget', 'value')
)
def plot_altair(xcol, ycol):
    chart = alt.Chart(cars).mark_point().encode(
    x= xcol,
    y= 'Horsepower',
    tooltip= ycol).interactive()
    return chart.to_html()


if __name__ == '__main__':
    app.run_server(debug=True)