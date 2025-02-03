from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)                                                                                                                  
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Clé secrète pour les sessions

# Fonction pour vérifier si l'utilisateur est authentifié
def est_authentifie():
    return session.get('authentifie')

# Page d'accueil -> Redirige automatiquement vers la page d'authentification
@app.route('/')
def accueil():
    return redirect(url_for('authentification'))

# Route d'authentification
@app.route('/authentification', methods=['GET', 'POST'])
def authentification():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'password':  
            session['authentifie'] = True
            return redirect(url_for('livres'))
        else:
            return render_template('formulaire_authentification.html', error=True)
    return render_template('formulaire_authentification.html', error=False)

# Route pour afficher les livres
@app.route('/livres', methods=['GET', 'POST'])
def livres():
    if not est_authentifie():
        return redirect(url_for('authentification'))

    # Ajouter un livre si le formulaire est soumis
    if request.method == 'POST':
        titre = request.form['titre']
        auteur = request.form['auteur']
        annee_publication = request.form['annee_publication']
        genre = request.form['genre']
        description = request.form['description']
        disponible = request.form['disponible'] == 'on'

        conn = sqlite3.connect('bibliotheque.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Livres (titre, auteur, annee_publication, genre, description, disponible)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (titre, auteur, annee_publication, genre, description, disponible))
        conn.commit()
        conn.close()

        return redirect(url_for('livres'))  # Rafraîchir la page pour afficher le livre ajouté

    # Affichage des livres
    conn = sqlite3.connect('bibliotheque.db')  
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Livres')  
    livres = cursor.fetchall()
    conn.close()
    
    return render_template('livres.html', livres=livres)  

# Route pour supprimer un livre
@app.route('/supprimer_livre/<int:livre_id>', methods=['GET'])
def supprimer_livre(livre_id):
    if not est_authentifie():
        return redirect(url_for('authentification'))

    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Livres WHERE livre_id = ?', (livre_id,))
    conn.commit()
    conn.close()

    return redirect(url_for('livres'))

if __name__ == "__main__":
    app.run(debug=True)
