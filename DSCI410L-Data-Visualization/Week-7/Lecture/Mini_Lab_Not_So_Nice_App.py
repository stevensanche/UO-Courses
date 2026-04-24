import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import Dash, html, dash_table, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

### Make this app not look like crap by possibly rearranging elements and using some combination of inline and stylesheet CSS
## Whatever you submit should clearly look better and make use of multiple CSS properties.

ad = pd.read_csv("https://raw.githubusercontent.com/UOdsci/DSCI_Data_Viz/refs/heads/main/data/adult_income.csv")

# Variable selections for the scatter graph
g1_choices = ["UnderOver50k","Sex", "Race", "Relationship", "MaritalStatus", "WorkClass"]

# Variable selections for the bar graph
g2_choices = ["Sex", "Race", "Relationship", "Education", "MaritalStatus", "WorkClass"]

# Toggle option for the bar graph
barmodes = ["group", "stack"]

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
    
    dbc.Row(
        [
            dbc.Col(
                [
                    html.H2('Income', className = 'label-font'),
                    html.P('Finding if someone earns more than or less than 50k depending on variables.', className = 'paragraph-text'),
                ],
                width = 10,
                className = 'header-block',
            )

        ],
        className = 'mb-3',
    ),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.H5('Scatter selections', className = 'label-font'),
                            dcc.Dropdown(
                                id = "Scatter Variable Select",
                                options = g1_choices,
                                value = "UnderOver50k",
                                clearable = False, 
                            className = 'dropdown-background',
                            ),
                            
                            html.H5("Age Jitter"),
                            dcc.Slider(
                                id ="x-jitter",
                                min = 0,  
                                max = 1, 
                                step = .05,
                                value = 0,  
                                marks = {i: str(i) for i in np.arange(0, 1.2, .2)},
                                className = 'slider-style',
                            ),
                            
                            html.H5("Education Jitter"),
                            dcc.Slider(
                                id = "y-jitter",
                                min = 0, 
                                max = 1,  
                                step = .05,  
                                value = 0, 
                                marks = {i: str(i) for i in np.arange(0, 1.2, .2)},  # Marks on the slider,
                                className = 'slider-style',
                                ),
    ],
                    className = 'section-box'
                    ),
                    md = 4,
                    className = 'mb-4'
                ),
                dbc.Col(
                    html.Div(
                        [
                            html.H5('Scatter plot', className = 'label-font'),
                            dcc.Graph(id = 'scatter', className = 'graph-shadow'),
                        ],
                        className = 'section-box'
                    ),
                ),
            ]
        ),
        
    # dbc.Row([
    #     dbc.Col(
    #         dcc.Graph(id = "bar", className = 'graph-shadow'),
    #         width = 12
    #     )
    # ]),

    dbc.Row(
        [
            dbc.Col(
                html.Div(
                    [
                        html.H5('Bar selections', className = 'label-font'),
                        dcc.Dropdown(
                            id = "Bar Variable Select",
                            options = g2_choices,
                            value = "Sex",
                            clearable = False,
                            className = 'dropdown-background',
                        ),
                        
                        dbc.Switch(
                            id = "Bar Mode",
                            label = "Grouped or Stacked",
                            value = False, # Default is off
                            className = 'switch-style',
                        ),
                    ],
                    className = 'section-box',
                ),
                md = 4,
                className = 'mb-4',
            ),
            dbc.Col(
                html.Div(
                    [
                        html.H5('Bar graph', className = 'label-font'),
                        dcc.Graph(id = 'bar', className = 'graph-shadow'),
                    ],
                    className = 'section-box',
                ),
                md = 8,
                className = 'mb-4',
            ),
        ]
    ),
    ])       
            

@app.callback(
    Output("scatter", "figure"),
    Output("bar", "figure"),
    Input("Scatter Variable Select", "value"),
    Input("Bar Variable Select", "value"),
    Input("x-jitter", "value"),
    Input("y-jitter", "value"),
    Input("Bar Mode", "value")
)

def update_plots(scatter_color, bar_variable, x_jitter, y_jitter, bar_mode):

    x_noise = np.random.normal(0,x_jitter,len(ad))
    y_noise = np.random.normal(0,y_jitter,len(ad))

    fig1 = px.scatter(x = ad["Age"] + x_noise, y = ad["EducationYears"] + y_noise, color = ad[scatter_color], opacity = 0.35)

    fig2 = px.bar(pd.crosstab(ad[bar_variable], ad["UnderOver50k"]), barmode = barmodes[bar_mode])

    return fig1, fig2

# Run the app
if __name__ == "__main__":
    app.run(debug=True, port = '8063')