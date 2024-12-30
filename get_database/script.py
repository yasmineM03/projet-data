# -*- coding: utf-8 -*-
import csv
import sqlite3


def create_tables(emplois):
    db = sqlite3.connect(emplois)
    cur = db.cursor()



    ''' une fois qu'une table est créee, je la commente pour ne pas être obligé de tout réinsérer à chaque fois'''
    # on suppose que si cette fonction est appelee
    # c'est que l'on souhaite reprendre la construciton de la base
    # donc on suppprime les tables existantes et on les reconstruit
    cur.execute("DROP TABLE IF EXISTS bassin")
    cur.execute(''' CREATE TABLE bassin
    (be int PRIMARY KEY,
    nombe text,
    dept text,
    FOREIGN KEY (dept) REFERENCES departement(dep)
    )''')
     
    cur.execute("DROP TABLE IF EXISTS departement")
    cur.execute('''
    CREATE TABLE departement (
    dep int PRIMARY KEY,
    nomdept text,
    reg int,
    FOREIGN KEY (reg) REFERENCES region(reg)
    )''')

    cur.execute("DROP TABLE IF EXISTS region")
    cur.execute('''
    CREATE TABLE region (
    reg int PRIMARY KEY,
    nomregion text
    )''')
    
    cur.execute("DROP TABLE IF EXISTS fam_metier")
    cur.execute('''
    CREATE TABLE fam_metier (
        
        famillemet text PRIMARY KEY,
        lblfamille text
        
    )''')

    cur.execute("DROP TABLE IF EXISTS metier")
    cur.execute('''
    CREATE TABLE metier (
    codemetier text PRIMARY KEY,
    nommetier text,
    famillemet text,
    FOREIGN KEY (famillemet) REFERENCES fam_metier(famillemet)
    )''')

    cur.execute("DROP TABLE IF EXISTS recrutement")
    cur.execute('''
    CREATE TABLE recrutement (
    annee int,
    codemet int,
    be int,
    xmet int,
    smet int,
    met int,
    FOREIGN KEY (codemet) REFERENCES metier(codemet),
    FOREIGN KEY (be) REFERENCES bassin(be)
    )''')

    db.commit()
    db.close()
    

def insert_bassin(database_name, bassin_infos):
    be = bassin_infos['BE']
    nombe = bassin_infos["NOMBE"]
    dept = bassin_infos["Dept"]
    query = '''
            INSERT INTO bassin ('be','nombe','dept') \
            VALUES ("{}", "{}", "{}")
        '''.format(be,nombe,dept)
    db = sqlite3.connect(database_name)
    cur = db.cursor()
    cur.execute(query)
    db.commit()
    db.close()

def insert_departement(database_name,dep_infos):
    dep = dep_infos["Dept"]
    nomdept = dep_infos["NomDept"]
    reg = dep_infos["REG"]
    query = '''
            INSERT INTO departement ('dep','nomdept','reg') \
            VALUES ("{}", "{}", "{}")
        '''.format(dep,nomdept,reg)
    db = sqlite3.connect(database_name)
    cur = db.cursor()
    cur.execute(query)
    db.commit()
    db.close()

def insert_region(database_name, reg_infos):
    reg = reg_infos["REG"]
    nomregion = reg_infos["NOM_REG"]

    query = '''
            INSERT INTO region ('reg','nomregion') \
            VALUES ("{}", "{}")
        '''.format(reg,nomregion)
    db = sqlite3.connect(database_name)
    cur = db.cursor()
    cur.execute(query)
    db.commit()
    db.close()



def insert_fammetier(database_name, fammet_infos):
    famillemet = fammet_infos["Famille_met"]
    lblfamille = fammet_infos["Lbl_fam_met"]

    query = '''
            INSERT INTO fam_metier ('famillemet','lblfamille') \
            VALUES ("{}", "{}")
        '''.format(famillemet,lblfamille)
    db = sqlite3.connect(database_name)
    cur = db.cursor()
    cur.execute(query)
    db.commit()
    db.close()


def insert_metier(database_name, metier_infos):
    codemetier = metier_infos["codemetier"]
    nommetier = metier_infos["nommetier"]
    famillemet = metier_infos["Famille_met"]
    query = '''
            INSERT INTO metier ('codemetier','nommetier','famillemet') \
            VALUES ("{}", "{}", "{}")
        '''.format(codemetier,nommetier,famillemet)
    db = sqlite3.connect(database_name)
    cur = db.cursor()
    cur.execute(query)
    db.commit()
    db.close()


    
def insert_recrutement(database_name, recrutement_infos):
    annee =recrutement_infos['annee']
    codemet = recrutement_infos['codemetier']
    be = recrutement_infos['BE']
    xmet =recrutement_infos['xmet']
    smet = recrutement_infos['smet']
    met = recrutement_infos['met']

    query = '''
            INSERT INTO recrutement ('annee','codemet','be', 'xmet', 'smet', 'met') \
            VALUES ("{}", "{}","{}","{}", "{}", "{}")
            '''.format(annee,codemet,be, xmet, smet, met)
    db = sqlite3.connect(database_name)
    cur = db.cursor()
    cur.execute(query)
    db.commit()
    db.close()    
    

database_name = "emplois2.sql"
create_tables(database_name)

print('Inserting Emplois')
for i in range (17,23) :
    with(open(f'ResMetBE{i}.csv', 'r')) as csvfile:
                    b = 0
                    c = 0
                    d = 0
                    e = 0
                    g = 0
                    a = 0
                    reader = csv.DictReader(csvfile, delimiter=';')
                    for row in reader:
                                    g +=1
                                    a +=1
                                    b +=1
                                    c += 1
                                    d +=1
                                    e +=1
                                    try:
                                        insert_fammetier(database_name, row)
                                    except sqlite3.IntegrityError:
                                        a -= 1
                                        pass
                                    try:
                                        insert_region(database_name, row)
                                    except sqlite3.IntegrityError:
                                        e -= 1
                                        pass
                                    try:
                                        insert_metier(database_name, row)
                                    except sqlite3.IntegrityError:
                                        b -= 1
                                        pass
                                    try:
                                        insert_departement(database_name, row)
                                    except sqlite3.IntegrityError:
                                        c -= 1
                                        pass
                                    try:
                                        insert_bassin(database_name, row)
                                    except sqlite3.IntegrityError:
                                        g -= 1
                                        pass
                                    try:
                                        insert_recrutement(database_name, row)
                                    except sqlite3.IntegrityError:
                                        d -= 1
                                        pass
                        
			