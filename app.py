from dash import Dash, html, dcc, dash_table, Input, Output, State
from explorer import df

app = Dash(__name__)


app.layout = html.Div(children=[
    html.H1(children='UIL Results Explorer'),
    html.Div(style={"width": "50%"}, children=[
        html.Label(children='Search by School name:'),
        dcc.Input(id='school-input', value='', type='text'),
        html.Br(),
        html.Label(children='Filter by conference:'),
        dcc.Dropdown(
            id='conference-dropdown',
            options=[{'label': i, 'value': i}
                     for i in df['Conference'].unique()],
            value='Conference',
            multi=True
        ),

        dcc.Dropdown(
            id='classification-dropdown',
            options=[{'label': i, 'value': i}
                     for i in df['Classification'].sort_values().unique()],
            value='Classification',
            multi=True
        ),

        dcc.Dropdown(
            id='year-dropdown',
            options=[{'label': i, 'value': i} for i in df['Year'].sort_values().unique()],
            value='Year',
            multi=True
        ),
    ]),
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        style_cell={'textAlign': 'left'},
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'
        },
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            }
        ],
    )
])


@ app.callback(

    Output('table', 'data'),
    [
        Input('school-input', 'value'),
        Input('conference-dropdown', 'value'),
        Input('classification-dropdown', 'value'),
        Input('year-dropdown', 'value')
    ])
def update_table(school, conference, classification, year):
    dff = df
    if school != 'School':
        dff = dff[dff['School'].str.contains(school)]
    if conference != 'Conference':
        dff = dff[dff['Conference'] == conference]
    if classification != 'Classification':
        dff = dff[dff['Classification'] == classification]
    if year != 'Year':
        dff = dff[dff['Year'] == year]
    return dff.to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)


'''
dash_table.DataTable(df.to_dict('records'), [
    {"name": i, "id": i} for i in df.columns])
])'''
