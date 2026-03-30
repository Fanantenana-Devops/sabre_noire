import sqlite3
def connecter_db():
    try:
        conn=sqlite3.connect("sabre_noire.db")
        return conn
    except sqlite3.Error as e:
        print(f"Erreur de connexion:{e}")
        return None
def afficher_especes():
    conn=connecter_db()
    if conn:
        cursor=conn.cursor()
        query='''SELECT e.nom_commun, c.nom_categories 
        FROM espece e
        JOIN categories c ON e.id_categories=c.id'''
        cursor.execute(query)
        resultats=cursor.fetchall()
        print("Les listes des especes")
        for ligne in resultats:
            print(f"Nom:{ligne[o]}|Categories:{ligne[1]}")
        conn.close()
def lister_tout():
    conn=connecter_db()
    cursor=conn.cursor()
    print("\n---NOS SITES ET LEURS GESTIONNAIRE ---n/")
    query=""""SELECT e.nom_especes,c.nom_categories,e.status_conservation
    FROM espece e JOIN 
    categorie c ON e.id_categories=c.id
    """
    cursor.execute(query)
    for row in query.fetchall():
        print(f"{row[0]} Type:{row[1]}  Statut:{row[2]}")
    conn.close()
def ajouter_des_especes():
    global nom, sci, stat, desc, cat_id
    print("---AJOUT DE QUELQUE ESPECE---")
    nom=input("Nom de l'espece(ex:Fossa):")
    sci=input("Nom scientifique:")
    stat=input("Statut de conservation(ex: Vulnerable):")
    desc=input("Description courte:")
    cat_id=int(input("ID de la categorie(1 pour Lemurien, 2 pour Reptiles,..):"))
def executeur():
    ajouter_des_especes()
    conn=connecter_db()
    cursor=conn.cursor()
    conn.execute('''
        INSERT INTO espece(nom_commun, nom_sceintifique, status_conservation, descriptions,id_categories)
        VALUES(?,?,?,?,?)''',(nom,sci,stat,desc,cat_id))
    conn.commit()
    conn.close()

#if __name__=="__name__":
executeur()
afficher_especes()
lister_tout()
