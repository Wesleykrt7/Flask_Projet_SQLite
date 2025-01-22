from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Clé secrète pour les sessions

# Fonction pour vérifier l'authentification de l'utilisateur
def est_authentifie():
    return session.get('authentifie')

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/fiche_nom', methods=['GET', 'POST'])
def fiche_nom():
    # Vérifier si l'utilisateur est authentifié
    if not est_authentifie():
        return redirect(url_for('authentification'))
    
    if request.method == 'POST':
        nom_recherche = request.form['nom']
        
        # Connexion à la base de données pour effectuer la recherche
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM clients WHERE nom LIKE ?', ('%' + nom_recherche + '%',))
        clients = cursor.fetchall()
        conn.close()

        # Renvoyer les résultats à la page de recherche
        return render_template('fiche_nom.html', clients=clients)

    # Si la méthode est GET, juste afficher le formulaire de recherche
    return render_template('fiche_nom.html', clients=None)

@app.route('/authentification', methods=['GET', 'POST'])
def authentification():
    if request.method == 'POST':
        # Vérifier les identifiants de l'utilisateur (user/12345)
        if request.form['username'] == 'user' and request.form['password'] == '12345':
            session['authentifie'] = True
            return redirect(url_for('fiche_nom'))
        else:
            # Afficher un message d'erreur si les identifiants sont incorrects
            return render_template('formulaire_authentification.html', error=True)

    return render_template('formulaire_authentification.html', error=False)

@app.route('/lecture')
def lecture():
    if not est_authentifie():
        return redirect(url_for('authentification'))
    
    return "<h2>Bravo, vous êtes authentifié</h2>"

# Autres routes (exemple : consultation, formulaire client, etc.)

if __name__ == "__main__":
    app.run(debug=True)
