# bot recherche stage

Un bot Python permettant de rechercher des offres de stage en Île-de-France sur le site [Welcome to the Jungle](https://www.welcometothejungle.com/fr). Ce script utilise Selenium et BeautifulSoup pour récupérer les annonces et les enregistrer dans un fichier CSV.

## Fonctionnalités

- **Navigation automatisée** : Utilise Selenium pour parcourir les pages d'offres de stage.
- **Extraction de liens d'annonces** : Identifie et récupère les URLs des annonces de stage.
- **Scrapping des détails des annonces** : Extrait les informations clés telles que le titre, la localisation, l'entreprise, la date de publication et les compétences recherchées.
- **Enregistrement des données** : Stocke les annonces récupérées dans un fichier CSV pour une consultation ultérieure.

## Prérequis

- Python 3.x
- [Selenium](https://pypi.org/project/selenium/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [pandas](https://pandas.pydata.org/)
- Un navigateur Chrome et le [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/)

## Installation

1. Clonez le dépôt :

    ```sh
    git clone https://github.com/404reo01/bot-recherche-stage.git
    ```



2. Assurez-vous d'avoir le bon `chromedriver` pour votre version de Chrome et placez-le dans le dossier approprié.

## Utilisation

1. Modifiez le script `bot_recherche_stage.py` si nécessaire pour ajuster les paramètres de recherche (par exemple, le nombre de pages à parcourir).
2. Exécutez le script :

    ```sh
    bot_recherche_stage.py
    ```

3. Les annonces seront enregistrées dans le fichier `annonces_stages.csv` dans le répertoire courant.

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request si vous avez des suggestions ou des améliorations.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
