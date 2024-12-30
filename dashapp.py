import model.data
import view.GUI
import pandas as pd
import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SKETCHY])
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUMEN])

# Styles pour le Sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#212121",
    "color": "#fff",
    "font-family": "Arial, sans-serif",
}

# Styles pour le contenu de la page
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#f2f2f2",
    "box-shadow": "2px 2px 2px #ccc",
    "border-radius": "5px",
    "font-family": "Arial, sans-serif",
}
sidebar = html.Div(
	[
		html.H2("CMI ISI", className="display-4"),
		html.Hr(),
		html.P(
			"Données emplois", className="lead"
		),
		dbc.Nav(
			[
				dbc.NavLink("Carte", href="/map", active="exact"),
				dbc.NavLink("Barchart", href="/barchart", active="exact"),
				dbc.NavLink("Lignes", href="/lines", active="exact"),
			],
			vertical=True,
			pills=True,
		),
	],
	style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
	dcc.Location(id="url"),
	sidebar,
	content
])

@app.callback(
	Output("page-content", "children"),
	[Input("url", "pathname")]
)
def render_page_content(pathname):
	if pathname == "/map":
			dropdown = view.GUI.build_dropdown_menu(['xmet','smet','met'])
			map = view.GUI.init_map()
			return [
							html.Div([html.Button("Download CSV", id="btn_csv"),
        	dcc.Download(id="download-dataframe-csv"),
				dropdown, map
			])
		]
	elif pathname == "/barchart":
		dropdown = view.GUI.build_dropdown_menu(model.data.get_codemet())
		graph = view.GUI.init_graph2()
		return [
			html.Div([
				dropdown, graph
			])
		]
	elif pathname == "/lines":
		slidedown = view.GUI.build_slidedown(['2017','2018','2019','2020','2021','2022'])
		graph = view.GUI.init_graph3()
		return [
			html.Div([
				slidedown, graph
			])
		]
	elif pathname == "/":
		return html.Div([
    html.H1('Visualisation des données d\'emplois'),
    html.P('Par Justine, Yasmine, Estelle, et Anaïs')
])
		

@app.callback(
    Output("barchart", "figure"),
    [Input("dropdown", "value")])
def update_bar_chart(emplois_name):
    df, attributes = model.data.extract_emplois(emplois_name)
    return view.GUI.build_barchart(df, attributes)

@app.callback(
    Output("lines", "figure"),
    [Input("slidedown", "value")])
def update_slide(annee):
    df, attributes = model.data.extract_recrutement_datav2(annee)
    return view.GUI.build_line(df, attributes)

@app.callback(
    Output("map", "figure"),
    [Input("dropdown", "value")])
def update_map(value):
    fig=  view.GUI.build_map(value)
    return fig

@app.callback(
    Output("download-dataframe-csv", "data"),
    Input("btn_csv", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    df_recrutement = model.data.extract_recrutement_all_data()
    df_bassin = model.data.extract_bassin_data()
    df_coords = model.data.extract_coords_data()
    df_merged = pd.merge(df_bassin, df_recrutement, on='be')
    df_merged = pd.merge(df_merged, df_coords, on='dept')
    df_by_departement = df_merged.groupby(['dept', 'latitude', 'longitude']).sum().reset_index()
    df_by_departement = df_by_departement.rename(columns={'latitude': 'lat', 'longitude': 'lon','SUM(met)':'met','SUM(xmet)':'xmet','SUM(smet)':'smet'}) 
    df_by_departement = df_by_departement[['dept', 'lat', 'lon','met','xmet','smet']]

    return dcc.send_data_frame(df_by_departement.to_csv, "df_recrutements_par_dep.csv")


if __name__=='__main__':
	app.run_server(debug=False)