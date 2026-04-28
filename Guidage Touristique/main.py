# ***Creation du logique du site*** #
#"Se script doit probablement recevoir le choix du formulaire, interroge la base, renvoie les destinations qui correspondent"
#from flask import Flask, render_template, request
import sqlite3
def seed_tourisme():
    #connexion a la base de donnees
    conn=sqlite3.connect('guidage_touristique.db')
    cursor=conn.cursor()
    
    #Quelques donnee pour la test reelles
    destinations=[
        ('Andasibe','Est','Nature/Parcs','Observation de lemurien et foret humide',50000),
        ('Nosy Be','Nord','Plage/Luxe','Escale balneaire et plongee sous-marine',1500000),
        ('Antsirabe','Hauts Plateaux','Culture/Thermes','Pousse-pousse et pierres precieuses',30000),
        ('Morondava','Ouest','Paysage','L/allee de Baobab et le Kirindy',70000)
    ]
    try:
        #Insertion
        cursor.executemany("INSERT INTO destinations(nom,region,categorie,description,budget_moyen)VALUES(?,?,?,?,?)",destinations)
        conn.commit()
        print(f"Succes!{len(destinations)} destinations ajoutees a Sabre Noir.")
    except Exception as e:
        print(f"Erreur:{e}")
    finally:
        conn.close()
def get_db_connection():
    #connection a la base de donnee
    conn=sqlite3.connect("guidage_touristique.db")
    #permet d'acceder aux colonnes par nom si possible
    conn.row_factory=sqlite3.Row
    return conn
#@app.route('/recherche-guide',methods=['POST'])
def recherche_guide():
    budget=request.form.get('budget')
    categorie=request.form.get('categorie')
    
    conn=get_db_connection()
    #Requete SQL: On filtre par budget(>=) et categorie
    query="SELECT*FROM destinations WHERE bubget_moyen<=? AND categorie=?"
    resultats=conn.execute(query,(budget,categorie)).fetchall()
    conn.close()
    
    #return render_template('index.html',destinations=resultats)
#if__name__=="__main__":
seed_tourisme()
def guide_intelligent(budget_max,categorie_pref):
    #La requete SQL qui filtre selon les criteres du touriste
    query="SELECT nom,description FROM destinations WHERE budget_moyen<=? AND categorie LIKE?"