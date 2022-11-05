from dash import Dash, html, dcc, Input, Output, State, dash_table
import plotly.express as px
import pandas as pd
from explorer import df

app = Dash(__name__)
# add a header

app.layout = html.Div(
    [

dash_table.DataTable(df.to_dict('records'), [
    {"name": i, "id": i} for i in df.columns])
])



if __name__ == '__main__':
    app.run_server(debug=True)
