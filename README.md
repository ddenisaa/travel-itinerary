# Planificator de călătorii

O aplicație web construită cu Python, Flask și scikit-learn pentru generarea itinerariilor de călătorie bazate pe preferințe (buget, tip de vacanță, durată). Proiectul folosește un algoritm de similaritate cosinus pentru recomandări personalizate.

## Funcționalități
- Introduceți bugetul, tipul de vacanță (cultural, plajă, aventură) și durata.
- Primești un itinerar sugerat cu destinație, cost și durată.
- Interfață web simplă și prietenoasă, cu gestionare a erorilor.

## Tehnologii
- **Backend**: Python, Flask, pandas, scikit-learn
- **Frontend**: HTML/CSS
- **Date**: Fișier CSV static (`destinations.csv`)

## Instalare
1. Clonează repository-ul: `git clone https://github.com/ddenisaa/travel-itinerary.git`
2. Navighează în director: `cd travel-itinerary`
3. Creează un mediu virtual: `python -m venv venv`
4. Activează mediul virtual: `venv\Scripts\activate` (Windows)
5. Instalează dependințele: `pip install flask pandas scikit-learn`
6. Rulează aplicația: `python app.py`
7. Accesează: `http://127.0.0.1:5000` în browser.

## Utilizare
- Completează formularul cu buget (USD), tip de vacanță și durată (zile).
- Apasă „Generează itinerar” pentru a vedea recomandarea.

## Autor
Denisa Dinu
[LinkedIn sau alt link de contact, dacă dorești] 
