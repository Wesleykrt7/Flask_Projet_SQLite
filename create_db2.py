-- Création de la table des livres
CREATE TABLE IF NOT EXISTS livres (
    livre_id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT NOT NULL,
    auteur TEXT NOT NULL,
    annee_publication INTEGER NOT NULL,
    genre TEXT,
    description TEXT,
    disponible BOOLEAN DEFAULT 1
);

-- Exemple d'autres tables (facultatif) que vous pouvez ajouter selon les besoins
-- CREATE TABLE IF NOT EXISTS utilisateurs (
--     utilisateur_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     nom TEXT NOT NULL,
--     prenom TEXT NOT NULL,
--     email TEXT UNIQUE NOT NULL
-- );
