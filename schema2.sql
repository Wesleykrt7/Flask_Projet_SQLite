-- Table des utilisateurs
CREATE TABLE utilisateurs (
    utilisateur_id INTEGER PRIMARY KEY,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    mot_de_passe TEXT NOT NULL,
    role TEXT CHECK (role IN ('Utilisateur', 'Administrateur')) DEFAULT 'Utilisateur',
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table des livres
CREATE TABLE Livres (
    livre_id INTEGER PRIMARY KEY,
    titre TEXT NOT NULL,
    auteur TEXT NOT NULL,
    annee_publication INTEGER NOT NULL,
    genre TEXT,
    description TEXT,
    disponible INTEGER DEFAULT 1, -- 1 = TRUE, 0 = FALSE
    date_ajout TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table des emprunts
CREATE TABLE Emprunts (
    emprunt_id INTEGER PRIMARY KEY,
    utilisateur_id INTEGER,
    livre_id INTEGER,
    date_emprunt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_retour_prevu DATE,
    date_retour_effectif DATE,
    FOREIGN KEY (utilisateur_id) REFERENCES utilisateurs(utilisateur_id) ON DELETE CASCADE,
    FOREIGN KEY (livre_id) REFERENCES Livres(livre_id) ON DELETE CASCADE
);

-- Table des stocks de livres (gère la quantité de chaque livre dans le stock)
CREATE TABLE Stocks (
    stock_id INTEGER PRIMARY KEY,
    livre_id INTEGER,
    quantite INTEGER DEFAULT 0,
    FOREIGN KEY (livre_id) REFERENCES Livres(livre_id) ON DELETE CASCADE
);

-- Table des logs de notifications (par exemple, pour les retours en retard)
CREATE TABLE Notifications (
    notification_id INTEGER PRIMARY KEY,
    utilisateur_id INTEGER,
    message TEXT,
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    lue INTEGER DEFAULT 0, -- 0 = non lu, 1 = lu
    FOREIGN KEY (utilisateur_id) REFERENCES utilisateurs(utilisateur_id) ON DELETE CASCADE
);

-- Index pour la recherche rapide de livres
CREATE INDEX idx_titre ON Livres(titre);
CREATE INDEX idx_auteur ON Livres(auteur);

-- Exemple d'utilisateur administrateur
INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe, role)
VALUES ('Admin', 'Library', 'admin@bibliotheque.com', 'hashed_password', 'Administrateur');

-- Exemple de livres
INSERT INTO Livres (titre, auteur, annee_publication, genre, description, disponible)
VALUES ('Le Petit Prince', 'Antoine de Saint-Exupéry', 1943, 'Conte', 'Un conte poétique et philosophique', 1),
       ('1984', 'George Orwell', 1949, 'Dystopie', 'Un roman sur un futur totalitaire', 1);

-- Exemple de stocks
INSERT INTO Stocks (livre_id, quantite)
VALUES (1, 5), (2, 3);
