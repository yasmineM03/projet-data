import pandas as pd
import sqlite3

#données à charger
database_name = './model/emplois2.sql'
coordonnees = 'view/dep1.csv'

#récupère les labels des familles de métier pour les placer dans le dropdown
def get_codemet():
    db = sqlite3.connect(database_name)
    cur = db.cursor()
    query = f"SELECT lblfamille FROM fam_metier;"
    res = cur.execute(query)
    all = res.fetchall()
    db.close()
    return sorted(map(lambda x: x[0], all))

#récupère la somme des propositions de recrutement de chaque sorte et totale pour chaque famille de métier

def extract_emplois(emplois_fam):
    db = sqlite3.connect(database_name)
    cur = db.cursor()
    query = f'SELECT lblfamille as famille_metier,sum(xmet) as total_xmet, sum(smet) as total_smet, sum(met) as total_met, annee, codemet FROM recrutement,metier, fam_metier where recrutement.codemet= metier.codemetier and metier.famillemet = fam_metier.famillemet AND fam_metier.lblfamille = "{emplois_fam}" GROUP BY annee,lblfamille'
    res = cur.execute(query)
    df = pd.read_sql(query, db)
    attributes = ['annee',['total_xmet','total_smet','total_met']]
    return df,attributes


def extract_recrutement_all_data():
    conn = sqlite3.connect(database_name)
    df = pd.read_sql_query("SELECT be, met, SUM(smet),SUM(met),SUM(xmet) FROM recrutement GROUP BY be, smet", conn)
    return df


def extract_bassin_data():
    conn = sqlite3.connect(database_name)
    df = pd.read_sql_query("SELECT be, dept FROM bassin", conn)
    return df

def extract_recrutement_data():
    conn = sqlite3.connect(database_name)
    df = pd.read_sql_query("SELECT be, met, SUM(met) AS offres_emplois FROM recrutement GROUP BY be, met", conn)
    return df

def extract_recrutement_xmet_data():
    conn = sqlite3.connect(database_name)
    df = pd.read_sql_query("SELECT be, met, SUM(xmet) AS metiers_dangereux FROM recrutement GROUP BY be, xmet", conn)
    return df

def extract_recrutement_smet_data():
    conn = sqlite3.connect(database_name)
    df = pd.read_sql_query("SELECT be, met, SUM(smet) AS metiers_saisonniers FROM recrutement GROUP BY be, smet", conn)
    return df

def extract_recrutement_datav2(annee):
    conn = sqlite3.connect(database_name)
    df = pd.read_sql_query(f'SELECT fm.lblfamille, SUM(r.met) AS somme_met, SUM(r.xmet) AS somme_xmet, SUM(r.smet) AS somme_smet FROM recrutement r JOIN metier m ON r.codemet = m.codemetier JOIN fam_metier fm ON m.famillemet = fm.famillemet WHERE r.annee = "{annee}" GROUP BY fm.lblfamille',conn)
    if (annee == 2020): #Fonctions sociales et medico-sociales non définies en 2020
        df = df.append(pd.Series(), ignore_index=True)
    attributes = [['somme_met','somme_xmet','somme_smet'],["Autres metiers","Ouvriers de la construction et du batiment","Autres techniciens et employes","Fonctions d'encadrement","Ouvriers des secteurs de l'industrie","Fonctions liees a  la vente, au tourisme et aux services","Fonctions administratives","Fonctions sociales et medico-sociales"]]
    return df,attributes


def extract_coords_data():
    df = pd.read_csv(coordonnees, usecols=['Departement', 'LatitudeH', 'LongitudeH','LatitudeB', 'LongitudeB'])
    #calcul du centre de chaque département
    df['Latitude'] = (df['LatitudeH'] + df['LatitudeB']) / 2
    df['Longitude'] = (df['LongitudeH'] + df['LongitudeB']) / 2
    df = df.rename(columns={'Departement': 'dept', 'Latitude': 'latitude','Longitude':'longitude'})
    return df



