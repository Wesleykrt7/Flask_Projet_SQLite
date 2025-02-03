from flask import Flask, render_template, jsonify, request, redirect, url_for, session
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
        # Vérification des identifiants
        if request.form['username'] == 'admin' and request.form['password'] == 'password':  # À sécuriser
            session['authentifie'] = True
            # Rediriger vers la route /livres après une authentification réussie
            return redirect(url_for('livres'))
        else:
            # Afficher un message d'erreur si les identifiants sont incorrects
            return render_template('formulaire_authentification.html', error=True)

    return render_template('formulaire_authentification.html', error=False)

# Route pour afficher les livres (accessible seulement si authentifié)
@app.route('/livres')
def livres():
    if not est_authentifie():
        return redirect(url_for('authentification'))  # Redirection si non authentifié

    conn = sqlite3.connect('bibliotheque.db')  
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM Livres')  # Supposons que la table s'appelle 'Livres'
    livres = cursor.fetchall()
    conn.close()
    
    return render_template('livres.html', livres=livres)  

# Route pour consulter la fiche d'un client
@app.route('/fiche_client/<int:post_id>')
def Readfiche(post_id):
    if not est_authentifie():
        return redirect(url_for('authentification'))

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients WHERE id = ?', (post_id,))
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data.html', data=data)

# Route pour consulter la base de données clients
@app.route('/consultation/')
def ReadBDD():
    if not est_authentifie():
        return redirect(url_for('authentification'))

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients;')
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data.html', data=data)

# Route pour afficher le formulaire d'ajout de client
@app.route('/enregistrer_client', methods=['GET'])
def formulaire_client():
    if not est_authentifie():
        return redirect(url_for('authentification'))
        
    return render_template('formulaire.html')

# Route pour enregistrer un nouveau client
@app.route('/enregistrer_client', methods=['POST'])
def enregistrer_client():
    if not est_authentifie():
        return redirect(url_for('authentification'))
        
    nom = request.form['nom']
    prenom = request.form['prenom']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO clients (created, nom, prenom, adresse) VALUES (?, ?, ?, ?)', (1002938, nom, prenom, "ICI"))
    conn.commit()
    conn.close()
    return redirect('/consultation/')

if __name__ == "__main__":
    app.run(debug=True)
