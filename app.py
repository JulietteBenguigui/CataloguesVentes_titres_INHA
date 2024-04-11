# Importation des modules nécessaires depuis Flask et HTML
from flask import Flask, render_template, request
from html import escape

# Initialisation de l'application Flask
app = Flask(__name__)

# Route pour créer la page avec les formulaires à remplir
@app.route("/create_title_long")
def create_title_long():
    return render_template('add_titles_long.html')  # Renvoie à la page HTML dans notre dossier

# Route pour afficher les résultats après avoir rempli les formulaires et cliqué sur le bouton "submit"
@app.route('/results_long', methods=['POST'])
def results_long():
    # Initialisation des variables
    titles = []
    form_counter = 50  # Ajuster le nombre maximal de formulaires

    # Boucle pour récupérer les titres depuis les formulaires
    for i in range(1, form_counter + 1):
        title_key = f"title_long{i}"
        title_value = request.form.get(title_key, '')
        
        if title_value:
            titles.append(title_value)

    # Créer la liste des " [suivi de] "
    separators = [" [suivi de] "] * (len(titles) - 1)

    # Concaténer les titres avec les séparateurs
    concatenated_titles = "".join([title + sep for title, sep in zip(titles, separators)] + [titles[-1]])

    # Renvoyer les résultats à la page d'affichage
    return render_template('results_long.html', concatenated_titles=concatenated_titles)

# Vérifier si le script est exécuté directement (et non importé comme un module)
if __name__ == '__main__':
    # Lancer l'application en mode débogage
    app.run(debug=True)