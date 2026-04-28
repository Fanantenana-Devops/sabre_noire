CREATE TABLE IF NOT EXISTS destinations(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    region TEXT,
    categorie TEXT,
    description TEXT,
    budget_moyen REAL
)
CREATE TABLE IF NOT EXISTS photos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_du_pub TEXT NOT NULL,
    photo 
    date_du_pub 
    genre TEXT NOT NULL
)
