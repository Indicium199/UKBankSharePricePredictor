import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout with tabs
app.layout = html.Div([
    dcc.Tabs(id='tabs', value='tab1', children=[
        dcc.Tab(label='Barclays Plc', value='tab1'),
        dcc.Tab(label='HSBC', value='tab2'),
        dcc.Tab(label='Natwest Group', value='tab3'),
        dcc.Tab(label='Lloyds', value='tab4'),
        dcc.Tab(label='Standard Chartered', value='tab5'),
    ]),
    html.Div(id='tabs-content')
])

# Callback to update tab content
@app.callback(
    Output('tabs-content', 'children'),
    Input('tabs', 'value')
)
def render_content(tab):
    if tab == 'tab1':
        return html.Div([
            html.H3('Welcome to Bank A'),
            html.P('Here you can manage your accounts and view your transactions.')
        ])
    elif tab == 'tab2':
        return html.Div([
            html.H3('Welcome to Bank B'),
            html.P('Here you can view loan options and apply for a loan.')
        ])
    elif tab == 'tab3':
        return html.Div([
            html.H3('Welcome to Bank C'),
            html.P('Explore investment options and check your portfolio.')
        ])
    elif tab == 'tab4':
        return html.Div([
            html.H3('Welcome to Bank D'),
            html.P('Find the best savings accounts and rates here.')
        ])
    elif tab == 'tab5':
        return html.Div([
            html.H3('Welcome to Bank E'),
            html.P('Access credit card offers and rewards information.')
        ])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
