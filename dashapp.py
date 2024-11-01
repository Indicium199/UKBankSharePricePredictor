import dash
import dash_bootstrap_components as dbc
import yfinance as yf
from dash import dcc, html
from dash.dependencies import Input, Output

# Fetch bank data
banks = ['HSBA.L', 'LLOY.L', 'BARC.L', 'NWG.L', 'STAN.L']  # List of bank ticker names
data = yf.download(banks, start='2020-01-01', end='2024-10-31')  # Get historical data

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the app layout with tabs
app.layout = html.Div([
    # Landing page title section
    html.Div(
        children="FTSE 100 Banks Close Price Prediction Dashboard",
        style={
            "backgroundColor": "#001f3f",  # Navy blue background
            "color": "white",              # White text colour
            "textAlign": "center",         # Centered text
            "padding": "10px",             # Padding around the text
            "fontSize": "24px",            # Font size for the title
            "fontWeight": "bold"           # Bold text
        }
    ),
    
    # Tabs section
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
            html.H2('Welcome'),
            html.P('This dashboard provides predictive insights regarding the closing performance of UK banks listed on the FTSE 100, indicating the likelihood of their closing prices being higher or lower than the previous trading day.'),
            html.P('The predictions used in this dashboard...')
        ])
    elif tab == 'tab2':
        return html.Div([
            html.H3('Barclays'),
            html.P('Here you can...')
        ])
    elif tab == 'tab3':
        # HSBC tab content with title bar
        return html.Div([
            dbc.Row([
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            html.H3("HSBC Business Information", className="text-center", style={"fontSize": "18px", "color": "white"}),  # Adjusted font size
                        ),
                        style={"backgroundColor": "#001f3f", "height": "40px"},  # Navy blue background color
                    ),
                    width=6  # Span half the page (6 out of 12 columns)
                )
            ]),
            # Additional content for the HSBC tab below the title bar
            dbc.Row([
                dbc.Col(
                    html.Div([
                        html.P('HSBC Holdings plc provides banking and financial services worldwide. The company operates through Wealth and Personal Banking, Commercial Banking, and Global Banking and Markets segments.'),
                        # Add more content as needed
                    ]),
                    width={"size": 4, "offset": 4},  # Same width as the card
                )
            ])
        ])
    elif tab == 'tab4':
        return html.Div([
            html.H3('Natwest Group'),
            html.P('Here you can...')
        ])
    elif tab == 'tab5':
        return html.Div([
            html.H3('Lloyds'),
            html.P('Here you can ...')
        ])
    elif tab =='tab6':
        return html.Div([
            html.H3('Standard Chartered'),
            html.P('Here you can...')
        ])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
