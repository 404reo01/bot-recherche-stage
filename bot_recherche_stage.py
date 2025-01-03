import os
import re
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import csv
import datetime

options = ChromeOptions()# options.add_argument('--headless')  # Mode sans interface graphique



def get_pages(count):




    driver = webdriver.Chrome(options=options)  # initialiser un simulateur de navigateur

    pages = []

    for page_nb in range(1, count + 1):  # on voudra utiliser plusieurs pages donc boucle pour chaque page
        page_url = f"https://www.welcometothejungle.com/fr/jobs?refinementList%5Boffices.country_code%5D%5B%5D=FR&refinementList%5Boffices.state%5D%5B%5D=Ile-de-France&refinementList%5Bcontract_type%5D%5B%5D=internship&query=data&pages={page_nb}&aroundQuery=%C3%8Ele-de-France%2C%20France"
        driver.get(page_url)

        time.sleep(12)  # pour attendre 12 sec après chaque chargement de page pour éviter d'être bloqué

        pages.append(driver.page_source.encode("utf-8"))  # récupère résultats des pages

    driver.quit()  # Ferme le navigateur après avoir terminé

    return pages

#extraire le lien des annonces dans la page
def recup_lien(page):
    urls = []
    soup = BeautifulSoup(page, "html.parser")
    prefixe = "https://www.welcometothejungle.com"

    lien = soup.findAll("a", {"mode" : "grid"})

    for i in lien:
        url = prefixe + i["href"]
        print(url)
        urls.append(url)
    return urls

def recup_annonce(url):
    #recuperer les infos pour remplir l'annnonce
    #return l'annonce
    driver = webdriver.Chrome(options=options)
    annonce = {"url": url}
    driver.get(url)
    time.sleep(5)  # pour attendre 12 sec après chaque chargement de page pour éviter d'être bloqué
    soup = BeautifulSoup(driver.page_source.encode("utf-8"), "html.parser")
    titre = soup.find("h2").text
    localisation = soup.findAll("div",{"class": "sc-fKWMtX lpfkog"})[1].text
    nom_entreprise = soup.find("div", {"class": "sc-bXCLTC dPVkkc"}).text
    date = soup.findAll("div", {"class": "sc-bXCLTC dPVkkc"})[1].text
    competences =  {
    "python": False,
    "sql": False,
    "analyse de données": False,
    "mongodb": False,
    "excel": False,
    "scrapping": False,
    "power bi": False,
    }

    texte_annonce = soup.find("div", {"data-testid":"job-section-description"}).text.lower()
    for competence in competences:
        if competence in texte_annonce:
            competences[competence] = True




    annonce["competences"] = competences
    annonce["titre"] = titre
    annonce["localisation"] = localisation
    annonce["nom_ent"] = nom_entreprise
    annonce["date"] = date
    annonce["récolté le :"] = datetime.datetime.now().strftime("%c")
    driver.quit()

    return annonce

##ecrire annonce dans un fichier csv


def enregistrer_annonces_csv(annonces, nom_fichier):
    # Convertir la liste des annonces en DataFrame
    df = pd.DataFrame(annonces)
    # Enregistrer le DataFrame dans un fichier CSV sans les index
    df.to_csv(nom_fichier, index=False)
    print(f"Les annonces ont été enregistrées dans {nom_fichier}")







def main():
    liens = []
    annonces = []
    pages = get_pages(1)
    for page in pages:
        liens = liens + recup_lien(page)
    for url in liens:
        annonces.append(recup_annonce(url))
    enregistrer_annonces_csv(annonces,"annonces_stage.csv")




main()













