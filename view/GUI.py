import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
from dash import dcc
import model.data

GRAPH_STYLE = {
    "background-color": "#fff",
    "box-shadow": "2px 2px 2px #ccc",
    "border-radius": "5px",
}


#pour séléctionner l'attribut que l'on veut voir représenter
def build_dropdown_menu(menu_items):
    return dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x} for x in menu_items],
        value=menu_items[-1],
        clearable=False,
    )
def build_slidedown(menu_items):
    return dcc.Slider(
        2017,2022,1,
        value=menu_items[0],
        marks={2017: '2017',2018: '2018',2019: '2019',2020: '2020',2021: '2021',2022: '2022'},
        id="slidedown",
    )



####barcharte####
def init_graph2():
    return dcc.Graph(id="barchart", style=GRAPH_STYLE)

def build_barchart(df,attributes):
    x,y = attributes
    fig = px.bar(df, x=x, y=y, title="Proportion de métiers dangereux et saisonniers",barmode="group")
    return fig


####cartee####
def build_map(param):
    df_bassin = model.data.extract_bassin_data()
    if param == 'met':
        df_recrutement = model.data.extract_recrutement_data()
        met = 'offres_emplois'
    elif param == 'xmet':
        df_recrutement = model.data.extract_recrutement_xmet_data()
        met = 'metiers_dangereux'
    else :
        df_recrutement = model.data.extract_recrutement_smet_data()
        met = 'metiers_saisonniers'
    
    df_coords = model.data.extract_coords_data()
    df_merged = pd.merge(df_bassin, df_recrutement, on='be')
    df_merged = pd.merge(df_merged, df_coords, on='dept')
    df_by_departement = df_merged.groupby(['dept', 'latitude', 'longitude']).sum().reset_index()
    df_by_departement = df_by_departement.rename(columns={'latitude': 'lat', 'longitude': 'lon'})
    fig = px.scatter_mapbox(df_by_departement, 
                        lat='lat', 
                        lon='lon', 
                        color=met,
                        size=met,
                        hover_name='dept',
                        color_continuous_scale='haline',
                        zoom=5,
                        mapbox_style='carto-positron'
                       )
    fig.update_geos(fitbounds='locations', visible=False)
    fig.update_layout(height=600, 
                      margin={"r":0,"t":25,"l":0,"b":0})
    return fig


def init_map():
        return dcc.Graph(id='map', style=GRAPH_STYLE)



####graphique liénaire####

def build_line(df, attributes): 
    x,y = attributes
    fig = px.line(df, y,x,markers=True)
    return fig

def init_graph3():
    return dcc.Graph(id="lines", style=GRAPH_STYLE)



