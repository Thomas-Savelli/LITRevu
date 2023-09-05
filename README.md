# LITRevu - Application Web de critiques de Livres et d'Articles   


Ce programme a pour objectif de faciliter la tâche de suivi des prix des livres d'occasion sur les sites web de concurrents de Books Online. Il s'agit d'un scraper développé en Python qui extrait les informations tarifaires d'autres librairies en ligne. Dans cette version bêta, le programme se concentre sur la récupération des prix chez un revendeur de livres en ligne nommé Books to Scrape, au moment de son exécution. L'application est développée pour être exécutable à la demande et ne surveille pas les prix en temps réel sur la durée. Il permettra à Books Online de gagner du temps et de rester compétitif sur le marché.

## **Pour commencer - le téléchargement**

Télécharger l’intégralité du repository sur : https://github.com/Thomas-Savelli/LITRevu.git

Pour ce faire, veuillez ouvrir votre Terminal de Commande: 

1. Grace à la commande cd , dirigez vous vers le répertoire ou vous voulez installer le repository exemple : ```cd Desktop``` *(pour l'installer sur le Desktop de votre ordinateur)*.

2. Par la suite, entrez dans votre terminal la commande : 
```
git clone https://github.com/Thomas-Savelli/LITRevu.git
```
puis appuyer sur entrée afin de créer votre clone local.

## **2/ Installation des dépendances / packages**

Une fois le repository téléchargé et stocké localement, rendez vous dans le dossier LITRevu/. Pour cela utiliser la commande : ```cd LITRevu```
- Créer un environnement virtuel afin de récupérer les dépendances et packages du projet.  
*exemple procedure* : ```python -m venv env```
- Contrôler avec ```ls``` que vous disposez maintenant d’un dossier env. Si ce n’est pas le cas, réitérer cette étape en contrôlant la syntaxe de la ligne de commande. Sinon activer votre nouvel environnement virtuel.
  
    exemple procédure : 
    - (PowerShell): ```.\env\Scripts\activate``` 
    - (Windows): ```.\env\Scripts\activate.bat```
    - (autres): ```source env/bin/activate```

*Si vous rencontrez des difficultés vous pouvez vous référer sur le site :* https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows/18713789#18713789
  
  Pour contrôler la réussite de cette manœuvre, vous devriez avoir un ```(env)``` devant votre ligne de commande. Par exemple :

```(env) PS C:\Users\thoma\Desktop\OpenClassrooms\Parcours DA PYTHON\Projet_9\LITRevu>```
  
  PS : Taper seulement ```deactivate``` pour fermer ce dernier.

Pour finir, télécharger avec pip les packages et dépendances requis pour le bon fonctionnement du code avec le requirements.txt en entrant la commande suivante *(dans votre environnement virtuel !)* 

```pip install -r requirements.txt``` 

Une fois le téléchargement effectué et l'installation terminée, vous êtes prêt à exécuter le code.

## **3/ Activation du Serveur en Local**

Afin de pouvoir visiter et tester l'application web de LITRevu, vous devez lancer un serveur local. Pour ce faire, vous devez :

- dans votre terminal, vous situez dans le dossier de l'application LITRevu
- activer votre environnement virtuel (env)
- Lancer le serveur local avec la commande :
``` python manage.py runserver```

Votre serveur local est maintenant lancé. Vous pouvez entrer l'adresse url *(qui s'affiche dans votre terminal)* dans votre navigateur afin de naviguer dans l'aplication.

## **4/ Se connecter à la plateforme Administrative**
En plus de l'application web qui est accessible à travers la création d'un compte utilisateur, vous avez la possibilité de vous connecter en tant que super utilisateur à la plateforme administrative mise en place par le Framework Django. Pour ce faire entrer dans votre navigateur l'url fournie par votre serveur local et ajoutez ```admin``` à la fin de celle ci.

exemple : ```http://127.0.0.1:8000/admin```

Un super utilisateur à déja été créé afin de réaliser des tests. Vous pouvez utiliser ces informations afin de vous connecter à travers ce compte super utilisateur :

- id : thomas 
- password : poimlknbv0

Sinon vous pouvez créer un autre super utilisateur en tapant dans votre terminal *(en étant situé dans le dossier de l'application avec l'environnement virtuel activé)* :

```python manage.py createsuperuser```

Par la suite, suivez les instructions du terminal et quand cela est fini, vous n'avez plus qu'à vous connecter sur l'interface admin.


## Dévellopé avec

* Python - 3.11.1 - [*https://docs.python.org/fr/3/tutorial/index.html*]
* Django - 4.2.4 - [*https://pypi.org/project/Django/*]
* Django-sass - 1.1.0 - [*https://pypi.org/project/django-sass/*]
* Pillow - 10.0.0 - [*https://pypi.org/project/Pillow/*]
* IDE - [*https://code.visualstudio.com/*] - Visual Studio Code     
* PowerShell - [*https://learn.microsoft.com/fr-fr/powershell/scripting/overview?view=powershell-7.3*]  
* GitHub - [*https://github.com/*]   

## Versions

**Dernière version stable :** Beta 1.0  
**Dernière version :** Beta 1.0  

## Auteur  
* **Thomas Savelli** [https://github.com/Thomas-Savelli] - ``Devellopeur Python -Junior- Full Stack - LITRevu``  