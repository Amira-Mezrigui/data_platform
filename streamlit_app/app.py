import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests


# Titre de l'application
st.title('Brief application')

# function to load data 
def fetch_data():
    response = requests.get("http://flask_app:5000/data")
    return response.json()

data = fetch_data()
df = pd.DataFrame(data)
st.write(df)

# Générer des données aléatoires
st.write("Voici un graphique généré aléatoirement :")
data = pd.DataFrame({
    'x': np.arange(1, 11),
    'y': np.random.rand(10)
})

# Afficher le graphique
fig, ax = plt.subplots()
ax.plot(data['x'], data['y'], marker='o')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Graphique des valeurs aléatoires')
st.pyplot(fig)