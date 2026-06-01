# ***Creation du logique du site guidage touristique version 1.0*** #
#"Se script doit probablement recevoir le choix du formulaire, interroge la base, renvoie les destinations qui correspondent"
from flask import Flask, render_template, request
import sqlite3
#LA LIGNE INDISPENSABLE:
app= Flask(__name__)
def initialiser_tables():
    conn=sqlite3.connect("guidage_touristique.db")
    cursor=conn.cursor()

    with open("fondation.sql","r",encoding="utf-8") as f:
        cursor.executescript(f.read())
    conn.close()
    print("Le schema SQL a ete aplique avec succes!")
        

def get_db_connection():
    conn=sqlite3.connect("guidage_touristique.db")
    conn.row_factory=sqlite3.Row

def seed_tourisme():
    #connexion a la base de donnees
    conn= get_db_connection()
    cursor=conn.cursor()
    
    #Quelques donnee pour la test reelles
    destinations=[
        ('Andasibe','Est','Nature/Parcs','Observation de lemurien et foret humide',50000),
        ('Nosy Be','Nord','Plage/Luxe','Escale balneaire et plongee sous-marine',1500000),
        ('Antsirabe','Hauts Plateaux','Culture/Thermes','Pousse-pousse et pierres precieuses',30000),
        ('Morondava','Ouest','Paysage','L/allee de Baobab et le Kirindy',70000)
    ]
    andasibe_id=cursor.lastrowid
    #Insertion des photos liees a cet ID
    liste_photo=[
        {"chemin":"static/images/1778942686741.png",
         "genre":"Faune",
         "legende":"Photo de sifaka dans son habitat naturel"
        },
        {"chemin":"static/images/1778943126292.png",
         "genre":"Paysage",
         "legende":"Vue panoramique de la foret tropicale"
        },
        {"chemin":"static/images/IMG_20260517_183146.jpg",
         "genre":"Faune",
         "legende":"Le celebre lemurien Indri Indri"
        },
        {"chemin":"static/images/IMG_20260517_183102.jpg",
         "genre":"Hotel",
         "legende":"Bungalow eco-responsable pres du parc"
        }
    ]
    try:
        #Insertion
        cursor.executemany("INSERT INTO destinations(nom,region,categorie,description,budget_moyen)VALUES(?,?,?,?,?)",destinations)
        requete_photo="""
        INSERT INTO photos(destination_id,chemin_photo,genre_photo,legend_photo)
        VALUES(?,?,?,?)
        """
        for p in liste_photo:
            cursor.execute(requete_photo,(andasibe_id,p["chemin"],p["genre"],p["legende"]))
        conn.commit()
        print(f"Succes!{len(destinations)} destinations ajoutees a Sabre Noir.")
        print(f"Succes ! {len(liste_photo)} photos ont ete liees a la destination")
    except Exception as e:
        print(f"Erreur:{e}")
    finally:
        conn.commit()
        conn.close()
        
def get_db_connection():
    #connection a la base de donnee
    conn=sqlite3.connect("guidage_touristique.db")
    #permet d'acceder aux colonnes par nom 
    conn.row_factory=sqlite3.Row
    return conn
@app.route('/')
def home():
    return render_template('index.html',destinations=[])
@app.route('/recherche-guide', methods=['POST'])
def recherche_guide():
    budget = request.form.get('budget')
    categorie = request.form.get('categorie')
    
    conn = get_db_connection() # La fonction habituelle pour ouvrir la base
    cursor = conn.cursor()
    
    # La requête SQL avec la jointure (JOIN)
    # d représente la table destinations, p la table photos
    query = """
        SELECT d.nom, d.region, d.description, d.budget_moyen, p.chemin_photo 
        FROM destinations d
        LEFT JOIN photos p ON d.id = p.destination_id
        WHERE d.budget_moyen <= ? AND d.categorie = ?
    """
    
    destinations = cursor.execute(query, (budget, categorie)).fetchall()
    conn.close()
    
    return render_template('index.html', destinations=destinations)
def guide_intelligent(budget_max,categorie_pref):
    #La requete SQL qui filtre selon les criteres du touriste
    query="SELECT nom,description FROM destinations WHERE budget_moyen<= ? AND categorie LIKE ?"    
    return render_template('index.html',destinations=resultats)
#initialiser_tables()
if __name__ == "__main__":
    app.run(debug=True)
    #seed_tourisme()
