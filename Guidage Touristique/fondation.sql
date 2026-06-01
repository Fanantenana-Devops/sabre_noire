CREATE TABLE  photos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    destination_id INTEGER, --la cle qui fai le lien
    chemin_photo TEXT NOT NULL, --ex: '/static/image/andasibe.img
    genre_photo TEXT,--ici tu stockes 'faune','lemurien',..
    legend_photo TEXT,--ex: Sifaka mal
    date_ajout DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (destination_id)
    REFERENCES destinations(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS destinations(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    region TEXT,
    categorie TEXT,
    description TEXT,
    budget_moyen REAL
);
