# UE : Projet programmation - L2 CMI ISI

Groupe composé de :
* Estelle **ABOU TAYEH**
* Anais **AIT ABDELKADER**
* Yasmine **MAABOUT**
* Justine **RUCH**


## Introduction 
Ce projet git a pour but de cloturer le semestre de l'UE en realisant un travail de Visualisation de données avec Dash.  
Dans ce projet nous étudions les données d'emplois de différentes années qui proviennent du site [data.gouv.fr](https://www.data.gouv.fr/fr/) au format csv. Elles regroupent différentes familles de métiers, types d'emplois en fonctions des années et des régions.
Le but est de réaliser une application web avec plusieurs représentations sous formes de graphiques pour répondre aux problématiques suivantes : 
> **Quelle est la répartition des différents types de propositions d'emplois par département?**   

> **Quelle est la proportion de propositions de métiers dangereux et saisonniers par année par rapport aux propositions d'emplois?**  

> **Pour chaque famille de métier, comment les emplois ce répartissent-il entre les différents types de métiers chaque années?**  


Pour cela nous avons utiliser des représentations telles que: une carte (bubblemap), un barchart et un graphe linéaire.

## Comment avons nous opéré 
Dans un premier temps, nous utilisons les données présentes dans les fichiers csv initiaux, afin de créer plusieurs entités qui nous permettront de former une base de données réduite à une seule relation. En effet, la base de données est formée par six entités  :
***bassin***,  ***departement***,  ***fam_metier***,  ***metier***, ***recrutement*** et ***region***  
Chacune d'elles est formée de différentes colonnes liées directement entre elle:
* ***bassin*** est formé de 'be' pour le numéro de la ville par rapport aux chiffres de l'INSEE, 'nombe' pour le nom de cette dernière et enfin 'dep' pour le numéro du département. 
* ***departement*** est formé de 'dep' pour le numéro du département, 'nomdep' pour le nom du departement et 'reg' pour le numéro de la region. 
* ***fam_metier*** est formé de 'famillemet' qui représente la famille de métier et 'lbl_famille' qui represente le libellé de la famille de métier.
* ***metier*** est formé de 'codemetier' qui représente un code par métier, 'nommetier' pour le nom du metier et 'famillemet' pour la famille auquels on associe le metier. 
* ***recrutement*** est formé de 'annee' qui est l'année associée a l'étude, 'codemet' qui represente les codes du metiers données, 'be', représente les numéros attribuées par l'INSEE pour chaque villes,'met',represente le nombre de projet de recrutement,'xmet',représente le nombre de projets de recrutement jugés difficiles et 'smet',le nombre de projets de recrutement saisonniers.
* ***region*** formé de 'reg' qui est le numéro de région et 'nomregion' qui est le nom de la région. 

## Visualisation des données 
En partant de ces données, et en utilisant la librairie **plotly**, nous avons crée deux différentes modélisations qui permettent de mieux visualiser les données dans le contexte de la problématique. Une carte ou bubblemap qui permet de choisir des données spéciales et de les filtrer. De plus, un BarChart est aussi généré lors du lancement du code, et qui lui aussi permet une visualisation des données tout en ayant également la possibilité de les filtrer. 

## Mode d'emploi 
Pour pouvoir obtenir les visualisations, il suffit de lancer le code sur python avec {python dashapp.py} et de copier l'URL fournit dans un navigateur. 
Les données vues de cette manière sont très explicites et permenttent d'obtenir des modélisations plus plaisible pour comprendre et interpréter les données.

## Interprétations
L'application web que nous avons mit en place,  permet de visualiser les données relatives aux emplois sous forme de bubble map, de barchart et de graphes linéaires.  
- La bubble map permet de visualiser les données de l'emploi à l'aide d'une carte interactive qui affiche des bulles de différentes tailles et couleurs en fonction des données de l'emploi. 
- Le barchart , affiche des données de l'emploi sous forme de diagramme en barres pour une analyse plus détaillée. 
- Le graphe linéaire quant à lui, nous permet une meilleure comparaison entre chaque famille de métier selon les années.
Les utilisateurs peuvent facilement interagir avec les graphiques pour explorer les données et obtenir des informations pertinentes sur les tendances de l'emploi dans différentes régions géographiques.

Pour conclure ce projet, Cette application offre une interface pour les utilisateurs qui souhaitent explorer les tendances en matière d'emploi dans différentes régions en France entre 2017 et 2022.
Cette application est utile pour les entreprises, les chercheurs et les décideurs politiques qui souhaitent suivre l'évolution des tendances de l'emploi.
