
--Table des categories--
CREATE TABLE IF NOT EXISTS categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_categories TEXT NOT NULL
);

--La table des especes (le coeur de la donnees)--
CREATE TABLE IF NOT EXISTS espece(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_commun TEXT NOT NULL,
    nom_scientifique TEXT,
    status_conservation TEXT,
    descriptions TEXT,
    id_categories INTEGER,
    FOREIGN KEY ( id_categories ) REFERENCES categories(id)
);

--Table des lieu/Parc Nationaux
CREATE TABLE IF NOT EXISTS lieux(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_lieux TEXT NOT NULL,
    region TEXT,
    type_lieu TEXT,
    coordonnee_gps TEXT,
    gestionnaire TEXT
);

--Table d'Hotel present sur place--
CREATE TABLE IF NOT EXISTS hotels(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_hotel TEXT NOT NULL UNIQUE,
    localisation TEXT,
    prix_de_la_chambre REAL,
    Avis INTEGER
);

--Table de liaison--
CREATE TABLE IF NOT EXISTS localisation_especes(
    id_especes INTEGER,
    id_lieux INTEGER,
    id_hotels INTEGER,
    PRIMARY KEY (id_especes,id_lieux,id_hotels),
    FOREIGN KEY (id_especes) REFERENCES especes(id),
    FOREIGN KEY (id_lieux) REFERENCES lieux(id),
    FOREIGN KEY (id_hotels) REFERENCES hotels(id)
);

--Insertion des quelques donnees de test en cours--
INSERT INTO categories (nom_categories)
VALUES('Lemurien');

INSERT INTO espece(
                    nom_commun,
                    nom_scientifique,
                    status_conservation,
                    descriptions,
                    id_categories)
VALUES('','','','',1);

INSERT INTO lieux(
    nom_lieux,
    region,
    type_lieu,
    coordonnee_gps,
    gestionnaire);
VALUES()
INSERT INTO hotels(
    nom_hotel,
    localisation,
    prix_de_la_chambre,
    Avis);
VALUES()


SELECT*FROM espece;