# pip install ( all the required libraries )
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import dash
from dash import html,dcc
from dash.dependencies import Input,Output
import plotly.express as px
from numpy.f2py.rules import options

# install flask

# Data loading and clearning process Row 1
patients = pd.read_csv("corona.csv")
total = patients.shape[0]
active = patients[patients["Status"]=="Confirmed"].shape[0]
recovered = patients[patients["Status"]=="Recovered"].shape[0]
deceased = patients[patients["Status"]=="Deceased"].shape[0]

# create a option for bar graph row number 3
options = [
    {"label":"all", "value":"all"},
    {"label":"Hospitalized", "value":"Hospitalized"},
    {"label":"Recovered", "value":"Recovered"},
    {"label":"Deceased", "value":"Deceased"},
]

# create a option for left side line graph row number 2
options1 = [
    {"label":"all", "value":"all"},
    {"label":"Mask", "value":"Mask"},
    {"label":"Sanitizer", "value":"Sanitizer"},
    {"label":"Oxygen", "value":"Oxygen"},
]

# create a option for right side pie graph row number 2
options2 = [
    {"label":"all", "value":"State"},
    {"label":"Red Zone", "value":"Red Zone"},
    {"label":"Blue Zone", "value":"Blue Zone"},
    {"label":"Green Zone", "value":"Green Zone"},
    {"label":'Orange Zone', "value":"Orange Zone"},
]



# css
external_stylesheets = [
                          {
                            "href":"https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css",
                            "rel":"stylesheet",
                            "integrity":"sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC",
                            "crossorigin":"anonymous"
                          }
                        ]

# local host
meesal = dash.Dash(__name__, external_stylesheets = external_stylesheets)


#  layout
meesal.layout = html.Div([

    # headling of project name
    html.H1("Corona virus COVID-19",style={"textAlign":"center", "color":"white"}),
    html.H2("Create By Yanaguntikar Meesal", style={"textAlign": "center", "color": "white"}),


    # Row 1
    html.Div([

        # create a 4 columns

        # column 1
        html.Div([
            html.Div([
                html.Div([
                    # text
                    html.H3("Total Cases",style={"textAlign":"center", "color":"white"}),
                    html.H4(total,style={"textAlign":"center", "color":"white"}),
                ],className="card-body"),
            ],className="card, bg-danger"),
        ],className="col-md-3"),

        #  column 2
        html.Div([
            html.Div([
                html.Div([
                    # text
                    html.H3("Active Cases",style={"textAlign":"center", "color":"white"}),
                    html.H4(active,style={"textAlign":"center", "color":"white"}),
                ],className="card-body"),
            ],className="card, bg-info"),
        ],className="col-md-3"),

        # column 3
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Recovered Cases",style={"textAlign":"center", "color":"white"}),
                    html.H4(recovered,style={"textAlign":"center", "color":"white"}),
                ],className="card-body")
            ],className="card, bg-warning"),
        ],className="col-md-3"),

        # column 4
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total Deaths",style={"textAlign":"center", "color":"white"}),
                    html.H4(deceased,style={"textAlign":"center", "color":"white"}),
                ],className="card-body"),
            ],className="card, bg-success"),
        ],className="col-md-3"),


    ],className="row"), # row 1 end





    # Row 2
    html.Div([
        # crete a 2 columns

        # create a line graph
        html.Div([
            html.Div([
                html.Div([
                    # create a line graph
                    dcc.Dropdown(id="ploty-graph", options=options1, value="all"),
                    dcc.Graph(id="graph") # create function line graph
                ],className="card-body"),
            ],className="card bg-success"),
        ],className="col-md-6"),



        # create a pie graph
        html.Div([
            html.Div([
                html.Div([
                    # graph
                    dcc.Dropdown(id="my-dropdown", options=options2, value="State"),
                    dcc.Graph("the_graph")
                ],className="card-body"),
            ],className="card bg-primary"),
        ],className="col-md-6"),


    ],className="row"), # end of row 2




    # Row 3 create a bar graph
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    # graph
                    dcc.Dropdown(id="picker", options=options, value="all"), # dropdown menu
                    dcc.Graph(id="bar") # function core rate with id
                ],className="card-body"),
            ],className="card bg-warning"),
        ],className="col-md-12"),
    ],className="row"),


],className="container") # end the layout


# create a function for bar graph row number 3 using decorde function

@meesal.callback(Output("bar","figure"), [Input("picker","value")])
def update_graph(type):

    # condition 1
    if type == "all":
        return {
            "data":[
                go.Bar(  x = patients["State"], # create a bar with the help of plotly
                         y = patients["Total"]
                        )
            ],
                'layout':go.Layout(
                    title="State Total Count",
                    plot_bgcolor="orange",
                )
        }

    # condition 2
    if type == "Hospitalized":
        return {
            "data":[
                go.Bar(  x = patients["State"], # create a bar with the help of plotly
                         y = patients["Hospitalized"]
                        )
            ],
            'layout':go.Layout(
                title="Hospitalized Total Count",
                plot_bgcolor="orange",
            )

        }
    # condition 3
    if type == "Recovered":
        return {
            "data":[
                go.Bar(
                         x = patients["State"], # create a bar with the help of plotly
                         y = patients["Recovered"]
                       )
            ],
            'layout':go.Layout(
                title="Recovered Total Count",
                plot_bgcolor="orange",
            )

        }
    # condition 4
    if type == "Deceased":
        return {
            "data":[
                go.Bar(
                         x = patients["State"], # create a bar with the help of plotly
                         y = patients["Deceased"]
                     )
            ],
            'layout':go.Layout(
                title="Deceased Total Count",
                plot_bgcolor="orange",
            )

        }
    # end the function of bar graph row number 3


# create a line graph function for row number 2 left side graph
@meesal.callback(Output("graph","figure"),
                 [Input("ploty-graph","value")])
def generate_graph(type):

    # condition 1
    if type == "all":
        return {
            "data":[
                go.Line( x = patients["State"], y = patients["Total"])
            ],
            'layout':go.Layout(title="Commodities Total Count", plot_bgcolor="pink",)
        }

    # condition 2
    if type == "Mask":
        return {
            "data":[
                go.Line( x = patients["State"], y = patients["Mask"])
            ],
            'layout':go.Layout(title="Commodities Total Count", plot_bgcolor="pink",)
        }
    # condition 3
    if type == "Sanitizer":
        return {
            "data":[
                go.Line( x = patients["State"], y = patients["Sanitizer"])
            ],
            'layout':go.Layout(title="Commodities Total Count", plot_bgcolor="pink",)
        }
    # condition 4
    if type == "Oxygen":
        return {
            "data":[
                go.Line( x = patients["State"], y = patients["Oxygen"])
            ],
            'layout':go.Layout(title="Commodities Total Count", plot_bgcolor="pink",)
        }


# create a function for pie graph row number 2 right side
@meesal.callback(  Output("the_graph","figure"),
                    [Input("my-dropdown","value")]
                   )
def generate_graph(my_dropdown):
    piechart = px.pie(data_frame=patients, names=my_dropdown, hole=0.3)
    return piechart



# host id
if __name__ == "__main__":
    meesal.run(debug=True)
