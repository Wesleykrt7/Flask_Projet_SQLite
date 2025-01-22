import sqlite3

# Connexion à la base de données (ou création si elle n'existe pas)
connection = sqlite3.connect('bibliotheque.db')

# Exécution du script de création des tables
with open('schema2.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Insertion de données de livres
cur.execute("INSERT INTO livres (titre, auteur, annee_publication, genre, description, disponible) VALUES (?, ?, ?, ?, ?, ?)", 
            ('Le Petit Prince', 'Antoine de Saint-Exupéry', 1943, 'Conte', 'Un conte poétique et philosophique', 1))
cur.execute("INSERT INTO livres (titre, auteur, annee_publication, genre, description, disponible) VALUES (?, ?, ?, ?, ?, ?)", 
            ('1984', 'George Orwell', 1949, 'Dystopie', 'Un roman sur un futur totalitaire', 1))
cur.execute("INSERT INTO livres (titre, auteur, annee_publication, genre, description, disponible) VALUES (?, ?, ?, ?, ?, ?)", 
            ('Les Misérables', 'Victor Hugo', 1862, 'Roman historique', 'Une fresque sociale sur la France du XIXe siècle', 1))
cur.execute("INSERT INTO livres (titre, auteur, annee_publication, genre, description, disponible) VALUES (?, ?, ?, ?, ?, ?)", 
            ('Moby Dick', 'Herman Melville', 1851, 'Aventure', 'L\'épopée de la chasse à la baleine', 1))
cur.execute("INSERT INTO livres (titre, auteur, annee_publication, genre, description, disponible) VALUES (?, ?, ?, ?, ?, ?)", 
            ('Harry Potter à l\'école des sorciers', 'J.K. Rowling', 1997, 'Fantasy', 'Un jeune sorcier découvre son destin', 1))
cur.execute("INSERT INTO livres (titre, auteur, annee_publication, genre, description, disponible) VALUES (?, ?, ?, ?, ?, ?)", 
            ('La Peste', 'Albert Camus', 1947, 'Philosophique', 'Une réflexion sur l\'absurde face à la souffrance', 1))
cur.execute("INSERT INTO livres (titre, auteur, annee_publication, genre, description, disponible) VALUES (?, ?, ?, ?, ?, ?)", 
            ('Le Seigneur des Anneaux', 'J.R.R. Tolkien', 1954, 'Fantasy', 'L\'épopée épique du bien contre le mal', 1))
cur.execute("INSERT INTO livres (titre, auteur, annee_publication, genre, description, disponible) VALUES (?, ?, ?, ?, ?, ?)", 
            ('Le Comte de Monte-Cristo', 'Alexandre Dumas', 1844, 'Aventure', 'L\'histoire d\'un homme avide de vengeance', 1))

# Validation des changements et fermeture de la connexion
connection.commit()

# Fermeture de la connexion à la base de données
connection.close()
