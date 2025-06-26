import numpy as np
import requests
import pandas as pd
import pickle

zahlen = [1,18,99]

def simple_pandas_stats():
    daten = {
        "Name": ["Max", "Anna", "Tim"],
        "Punkte": [10, 20, 15]
    }
    
    df = pd.DataFrame(daten)
    print("Datenübersicht:")
    print(df)

    durchschnitt = df["Punkte"].mean()
    print(f"\nDurchschnittliche Punktzahl: {durchschnitt}")



def average(numbers):
    result = np.mean(numbers)
    print(f"Der Mittelwert ist: {result}")



def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        joke = response.json()
        print(f"{joke['setup']} — {joke['punchline']}")
    else:
        print("Fehler beim Abrufen des Witzes.")


def erstelle_dataframe():
    daten = {
        "Name": ["Lena", "Tom", "Eva"],
        "Alter": [25, 30, 22]
    }
    df = pd.DataFrame(daten)
    print("Erstellter DataFrame:")
    print(df)
    return df

def speichere_mit_pickle(df, dateiname):
    with open(dateiname, "wb") as f:
        pickle.dump(df, f)
    print(f"\nDataFrame wurde als '{dateiname}' gespeichert.")

def lade_mit_pickle(dateiname):
    with open(dateiname, "rb") as f:
        df = pickle.load(f)
    print(f"\nGeladener DataFrame aus '{dateiname}':")
    print(df)


    


simple_pandas_stats()
average(zahlen)
get_joke()
df = erstelle_dataframe()
speichere_mit_pickle(df, "personen.pkl")
lade_mit_pickle("personen.pkl")