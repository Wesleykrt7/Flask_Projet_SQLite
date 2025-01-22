-- Création de la base de données
CREATE DATABASE Bibliotheque;

-- Sélection de la base de données à utiliser
USE Bibliotheque;

-- Table des utilisateurs
CREATE TABLE Utilisateurs (
    utilisateur_id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    mot_de_passe VARCHAR(255) NOT NULL,
    role ENUM('Utilisateur', 'Administrateur') DEFAULT 'Utilisateur',
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table des livres
CREATE TABLE Livres (
    livre_id INT AUTO_INCREMENT PRIMARY KEY,
    titre VARCHAR(255) NOT NULL,
    auteur VARCHAR(255) NOT NULL,
    annee_publication YEAR NOT NULL,
    genre VARCHAR(100),
    description TEXT,
    disponible BOOLEAN DEFAULT TRUE,
    date_ajout TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table des emprunts
CREATE TABLE Emprunts (
    emprunt_id INT AUTO_INCREMENT PRIMARY KEY,
    utilisateur_id INT,
    livre_id INT,
    date_emprunt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_retour_prevu DATE,
    date_retour_effectif DATE,
    FOREIGN KEY (utilisateur_id) REFERENCES Utilisateurs(utilisateur_id) ON DELETE CASCADE,
    FOREIGN KEY (livre_id) REFERENCES Livres(livre_id) ON DELETE CASCADE
);

-- Table des stocks de livres (gère la quantité de chaque livre dans le stock)
CREATE TABLE Stocks (
    stock_id INT AUTO_INCREMENT PRIMARY KEY,
    livre_id INT,
    quantite INT DEFAULT 0,
    FOREIGN KEY (livre_id) REFERENCES Livres(livre_id) ON DELETE CASCADE
);

-- Table des logs de notifications (par exemple, pour les retours en retard)
CREATE TABLE Notifications (
    notification_id INT AUTO_INCREMENT PRIMARY KEY,
    utilisateur_id INT,
    message TEXT,
    date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    lue BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (utilisateur_id) REFERENCES Utilisateurs(utilisateur_id) ON DELETE CASCADE
);

-- Index pour la recherche rapide de livres
CREATE INDEX idx_titre_auteur ON Livres(titre, auteur);

-- Exemple d'utilisateur administrateur (à modifier pour vos besoins)
INSERT INTO Utilisateurs (nom, prenom, email, mot_de_passe, role)
VALUES ('Admin', 'Library', 'admin@bibliotheque.com', 'hashed_password', 'Administrateur');

-- Exemple de livres
INSERT INTO Livres (titre, auteur, annee_publication, genre, description, disponible)
VALUES ('Le Petit Prince', 'Antoine de Saint-Exupéry', 1943, 'Conte', 'Un conte poétique et philosophique', TRUE),
       ('1984', 'George Orwell', 1949, 'Dystopie', 'Un roman sur un futur totalitaire', TRUE);

-- Exemple de stocks
INSERT INTO Stocks (livre_id, quantite)
VALUES (1, 5), (2, 3);
