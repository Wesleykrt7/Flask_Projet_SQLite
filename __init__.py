from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)                                                                                                                  
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Clé secrète pour les sessions

# Fonction pour vérifier si l'utilisateur est authentifié
def est_authentifie():
    return session.get('authentifie')

# Page d'accueil -> Redirige vers l'authentification
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
@app.route('/livres')
def livres():
    if not est_authentifie():
        return redirect(url_for('authentification'))

    conn = sqlite3.connect('bibliotheque.db')  
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Livres')  
    livres = cursor.fetchall()
    conn.close()
    
    return render_template('livres.html', livres=livres)  

# Route pour supprimer un livre
@app.route('/supprimer_livre/<int:livre_id>', methods=['POST'])
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
