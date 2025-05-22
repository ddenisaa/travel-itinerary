#Ce face acest cod?
#Folosește LabelEncoder pentru a transforma categoria (ex. „cultural”, „beach”) în numere.
#Creează un vector pentru preferințele utilizatorului (buget, durată, categorie codificată).
#Compară acest vector cu vectorii destinațiilor folosind similaritatea cosinus.
#Alege destinația cu cea mai mare similaritate, dar verifică dacă respectă constrângerile (buget, categorie, durată).

from flask import Flask, request, render_template
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__)

# Citește datele și gestionează erorile
try:
    destinations = pd.read_csv('destinations.csv')
except FileNotFoundError:
    destinations = pd.DataFrame()
    error_message = "Eroare: Fișierul 'destinations.csv' nu a fost găsit. Te rugăm să verifici și să repornești aplicația."
except Exception as e:
    destinations = pd.DataFrame()
    error_message = f"Eroare la citirea datelor: {e}. Te rugăm să verifici fișierul CSV."
else:
    error_message = None

# Preprocesare pentru IA (dacă datele sunt disponibile)
if not destinations.empty:
    try:
        le = LabelEncoder()
        destinations['category_encoded'] = le.fit_transform(destinations['category'])
    except Exception as e:
        error_message = f"Eroare la preprocesare: {e}. Te rugăm să verifici formatul datelor."
        destinations = pd.DataFrame()
else:
    le = LabelEncoder()  # Inițializăm pentru a evita erori

@app.route('/')
def home():
    return render_template('index.html', error=error_message)

@app.route('/itinerary', methods=['POST'])
def generate_itinerary():
    if destinations.empty or error_message:
        return render_template('itinerary.html', itinerary=error_message)

    try:
        budget = float(request.form['budget'])
        category = request.form['category']
        duration = int(request.form['duration'])
        if budget <= 0 or duration <= 0:
            return render_template('itinerary.html', itinerary="Bugetul și durata trebuie să fie mai mari decât 0.")
    except (ValueError, KeyError):
        return render_template('itinerary.html', itinerary="Te rugăm să introduci valori valide pentru buget și durată.")

    category_encoded = le.transform([category])[0]
    user_vector = np.array([[budget, duration, category_encoded]])
    destination_vectors = destinations[['cost', 'duration', 'category_encoded']].values
    similarities = cosine_similarity(user_vector, destination_vectors)[0]
    best_index = np.argmax(similarities)
    best_destination = destinations.iloc[best_index]

    if (best_destination['cost'] <= budget) and (best_destination['category'] == category) and (best_destination['duration'] <= duration):
        itinerary = f"Itinerar sugerat: {best_destination['city']} - Cost: {best_destination['cost']} USD, Durata: {best_destination['duration']} zile"
    else:
        itinerary = "Nicio destinație găsită pentru preferințele tale."

    return render_template('itinerary.html', itinerary=itinerary)

if __name__ == '__main__':
    app.run(debug=True)