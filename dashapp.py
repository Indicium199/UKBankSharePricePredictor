import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout with tabs
app.layout = html.Div([
    dcc.Tabs(id='tabs', value='tab1', children=[
        dcc.Tab(label='Welcome', value='tab1'),
        dcc.Tab(label='Barclays Plc', value='tab2'),
        dcc.Tab(label='HSBC', value='tab3'),
        dcc.Tab(label='Natwest Group', value='tab4'),
        dcc.Tab(label='Lloyds', value='tab5'),
        dcc.Tab(label='Standard Chartered', value='tab6'),
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
            html.H2('FTSE 100 Listed Banks Dashboard'),
            html.P('The purpose of this dashboard is to...')
        ])
    elif tab == 'tab2':
        return html.Div([
            html.H3('Barclays'),
            html.P('Here you can view loan options and apply for a loan.')
        ])
    elif tab == 'tab3':
        return html.Div([
            html.H3('HSBC'),
            html.P('Explore investment options and check your portfolio.')
        ])
    elif tab == 'tab4':
        return html.Div([
            html.H3('Natwest Group'),
            html.P('Find the best savings accounts and rates here.')
        ])
    elif tab == 'tab5':
        return html.Div([
            html.H3('Lloyds'),
            html.P('Access credit card offers and rewards information.')
        ])
    elif tab =='tab6':
        return html.Div([
            html.H3('Standard Chartered'),
            html.P('Access credit card offers and rewards information.')
        ])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
