import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import Dash, html, dash_table, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc


data = pd.read_csv('student-por.csv')


# grades = data[['G1', 'G2', 'G3']].columns
grades = [{'label': g, 'value': g} for g in ['G1', 'G2', 'G3']]


lowest = data['absences'].min()
highest = data['absences'].max()


app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])


app.layout = dbc.Container(
    [
        dbc.Row(
                dbc.Col(
                        html.Div(
                            [
                                html.H2('Student School Metrics', className = 'label-font'),
                                html.P('Exploring different academic, health, and lifestyle metrics for students', 
                                       className = 'paragraph-text'),
                            ],
                            className = 'header-block',
                        ),
                        width = 12,
                ),
                className = 'mb-4',
        ),
        
        # dbc.Row(
        #     [
        #         dbc.Col(
        #             html.Div(
        #                 [
        #                     html.H5('Graph 1 menu', className = 'label-font'),
        #                     dcc.Dropdown(
        #                         id = 'Graph1_grade',
        #                         options = grades,
        #                         value = 'G3',
        #                         clearable = False,
        #                         className = 'dropdown-background',
        #                     ),

        #                     dbc.Switch(
        #                         id = 'Graph1_points',
        #                         label = 'On/Off',
        #                         value = True,
        #                         className = 'switch-style',
        #                     ),
        #                 ],
        #                 className = 'section-box',
        #             ),
        #             md = 6,
        #             className = 'mb-4',
        #         ),

        #         dbc.Col(
        #             html.Div(
        #                 [
        #                     html.H5('Graph 1: Study Time vs. Grade', className = 'label-font'),
        #                     dcc.Graph(id = 'graph1'),
        #                 ],
        #                 className = 'section-box',
        #             ),
        #             md = 6,
        #             className = 'mb-4',
        #         ),
        #     ]
        # ),
        
        # dbc.Row(
        #     [
        #         dbc.Col(
        #             html.Div(
        #                 [
        #                     html.H5('Graph 2 menu', className = 'label-font'),

        #                     dcc.Dropdown(
        #                         id = 'Graph2_grade',
        #                         options = grades,
        #                         value = 'G3',
        #                         clearable = False,
        #                         className = 'dropdown-background',
        #                     ),

        #                     dcc.RangeSlider(
        #                         id = 'Graph2_Absences',
        #                         min = lowest,
        #                         max = highest,
        #                         step = 1,
        #                         value = [lowest, highest],
        #                         tooltip = {'placement': 'bottom'},
        #                         className = 'slider-style',
        #                     ),

        #                     dbc.Switch(
        #                         id = 'Graph2_trend',
        #                         label = 'Trendline',
        #                         value = True,
        #                         className = 'switch-style',
        #                     ),
        #                 ],
        #                 className = 'section-box',
        #             ),
        #             md = 6,
        #             className = 'mb-4',
        #         ),

        #          dbc.Col(
        #             html.Div(
        #                 [
        #                     html.H5('Graph 2: Absences vs. Grade', className = 'label-font'),
                            
        #                     dcc.Graph(id = 'graph2'),
        #                 ],
        #                 className = 'section-box',
        #             ),
        #             md = 6,
        #             className = 'mb-4',
        #         ),
        #     ]
        # ),

        # dbc.Row(
        #     [
        #         dbc.Col(
        #             html.Div(
        #                 [
        #                     html.H5('Graph 3: Family Relationship vs. Grade', className = 'label-font'),
                            
        #                     dcc.Graph(id = 'graph3'),
        #                 ],
        #                 className = 'section-box',
        #             ),
        #             md = 6,
        #             className = 'mb-4',
        #         ),
                
        #         dbc.Col(
        #             html.Div(
        #                 [
        #                     html.H5('Graph 4: Weekend alc. Consumption vs Going out', className = 'label-font'),
        #                     dcc.Graph(id = 'graph4'),
        #                 ],
        #                 className = 'section-box',
        #             ),
        #             md = 6,
        #             className = 'mb-4',
        #         ),
        #     ]
        # ),

        # started this over, since this stacked my first 2 graphs and the last 2 were side-by-side
        # 

        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.H5('Study Time vs. Grade', className = 'label-font'),

                            dcc.Dropdown(
                                id = 'Graph1_grade',
                                options = grades,
                                value = 'G3',
                                clearable = False,
                                className = 'dropdown-background',
                            ),
                            
                            dbc.Switch(
                                id = 'Graph1_points',
                                label = 'On/Off',
                                value = True,
                                className = 'switch-style',
                            ),

                            dcc.Graph(id = 'graph1'),
                            
                        ],
                        
                        className = 'section-box',
                    ),
                    
                    md = 6,
                    className = 'mb-4',
                    
                ),

                dbc.Col(
                    
                    html.Div(
        
                        [
                            html.H5('Absences vs. Grade', className = 'label-font'),

                            dcc.Dropdown(
                                id = 'Graph2_grade',
                                options = grades,
                                value = 'G3',
                                clearable = False,
                                className = 'dropdown-background',
                            ),
                            
                            dcc.RangeSlider(
                                id = 'Graph2_Absences',
                                min = lowest,
                                max = highest,
                                step = 1, #without this, would jump by 8 absences 
                                value = [lowest, highest],
                                className = 'slider-style',
                            ),
                            
                            dbc.Switch(
                                id = 'Graph2_trend',
                                label = 'Trendline',
                                value = True,
                                className = 'switch-style',
                            ),

                            dcc.Graph(id = 'graph2'),
                            
                        ],
                        className = 'section-box',
                        
                    ),
                    md = 6,
                    className = 'mb-4',
                    
                ),
            ]
        ),


        dbc.Row(
            [
                dbc.Col(
                    
                    html.Div(
                        
                        [
                            html.H5('Family Relationship vs. Grade', className = 'label-font'),
                            dcc.Graph(id = 'graph3'),
                        ],
                        className = 'section-box',
                        
                    ),
                    
                    md = 6,
                    className = 'mb-4',
                    
                ),

                dbc.Col(
                    
                    html.Div(
                        [
                            html.H5('Weekend Alc. Consumption vs. Going Out', className = 'label-font'),
                            dcc.Graph(id = 'graph4'),
                        ],
                        
                        className = 'section-box',
                        
                    ),
                    md = 6,
                    className = 'mb-4',
                    
                ),
            ]
        ),
    ],
    fluid = True,
)



@app.callback(
    Output('graph1', 'figure'),
    Output('graph2', 'figure'),
    Output('graph3', 'figure'),
    Output('graph4', 'figure'),
    Input('Graph1_grade', 'value'),
    Input('Graph1_points', 'value'),
    Input('Graph2_grade', 'value'),
    Input('Graph2_Absences', 'value'),
    Input('Graph2_trend', 'value'),
)



def update_graphs(graph1_grade, graph1_points, graph2_grade, absence, trend):

    # data 1: We will compare weekly study time (studytime) to the final grade (G3) 
    # , and group by extra educational support (schoolsup | binary yes no) #boxplot

    points_setting = 'all' if graph1_points else False # needed help figuring this out 
    
    fig1 = px.box(data, x = 'studytime', y = graph1_grade, color = 'schoolsup', points = points_setting,
                  title = 'Study time vs. Final Grade', labels = {'studytime': 'Study Time (1: <2 hours, 2: 2-5 hours, 3: 5-10 hours,4: >10 hours)', graph1_grade: 'Grade',
                                                           'schoolsup': 'Extra Edu. Support'})
    fig1.update_layout(
        height = 360,
        autosize = True)

    # data 2: We will compare the number of school absences (absences) to the final 
    # grade (G3), and group it by the students current health status (health) #scatterplot
    
    trend_setting = "ols" if trend else None #needed help figuring this out 
    
    low, high = absence
    data2 = data[ (data['absences'] >= low) & (data['absences'] <= high) ]

    fig2 = px.scatter(data2, x = 'absences', y = graph2_grade, color = 'health', opacity = 0.7,
                      trendline = trend_setting, title = 'Absences vs. Grade', labels = {'absences':
                                                                                         '# Absences',
                                                                                         graph2_grade:
                                                                                         'Final Grade'}
                     )
    fig2.update_layout(
        height = 360,
        autosize = True)

    # data 3: We will compare quality of family relationships (famrel) to how they did in their final grade 
    # (G3), grouped by if they had extra family educational support (famsup | binary yes or no)
    
    # since famsup is binary, we are going to take the mean finals by family relationship (numerical),
    # and group by family support

    grouped = data.groupby(['famrel', 'famsup'])['G3'].mean().reset_index()

    fig3 = px.bar(grouped, x = 'famrel', y = 'G3', color = 'famsup', barmode = 'group',
                  title = 'Average Final Grade by Family Relationship',
                 labels = {'famrel': 'Family Relationship (1 = low, 5 = high)', 'G3': 'Final Grade',
                          'famsup': 'Family Support'})
    fig3.update_layout(
        height = 360,
        autosize = True)

    # data 4: We will compare weekend alcohol consumption (Walc) to the number of times going out with 
    # friends (goout), grouped by the number of past class failures (failures | numeric 1-4)

    heatmap = data.groupby(['Walc', 'goout'])['G3'].mean().reset_index()

    fig4 = px.density_heatmap(heatmap, x = 'Walc', y = 'goout', z = 'G3', histfunc = 'avg', 
                              title = 'Weekend alcohol consumption vs. going out',
                             labels = {'Walc': 'Weekend Alc. Consumption', 'goout': '# Times going out', 'G3': 'final grade (0-20)'})
    fig4.update_layout(
        height = 360,
        autosize = True)
    

    return fig1, fig2, fig3, fig4


if __name__ == "__main__":
    app.run(debug=True, port=8064)