from bs4 import BeautifulSoup as bfs
import requests as req
from requests_html import HTMLSession

url = "https://link.springer.com/search?facet-sub-discipline=%22Plant+Pathology%22&facet-sub-discipline=%22Plant+Genetics+and+Genomics%22&facet-discipline=%22Life+Sciences%22&facet-content-type=Article&facet-sub-discipline=%22Plant+Physiology%22&facet-sub-discipline=%22Plant+Sciences%22&facet-sub-discipline=%22Biotechnology%22&facet-language=%22En%22&date-facet-mode=between&facet-start-year=1990&previous-start-year=1952&facet-end-year=2023&previous-end-year=2023"

        
session = HTMLSession()
response = session.get(url)

#Executer le JS avec render. https://requests.readthedocs.io/projects/requests-html/en/latest/#javascript-support   
#On peut y ajouter des conditions telles que : render(sleep = 1, keep_page = True, scrolldown=1)
response.html.render()
soup = bfs(response.text, 'html.parser')

#Gestion des erreurs. 
try:
    response = req.get(url)
    response.raise_for_status()
except req.exceptions.HTTPError as errh:
    print("Http Error:", errh)
except req.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
except req.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except req.exceptions.RequestException as err:
    print("Else? Error", err)

#Récupère les balises 'a' de class = 'title' contenant les titres des articles. titles = <class 'bs4.element.ResultSet'>.
try:
    titles = soup.find_all('a', class_='title')
except AttributeError as e:
    print("Impossible de trouver la balise a")
    raise AttributeError from e
    
#Récupère l'ensemble des abstracts    
try:     
    abstracts = soup.find_all("a", class_ = "snippet")
except AttributeError as e:
    print("Impossible de trouver la p.snippet")
    raise AttributeError from e

#Récupère l'ensemble des auteurs et journaux. 
try:
    authorsAndJournals = soup.find_all("p", class_ = "meta")
except AttributeError as e:
    print("Impossible de trouver la p.meta")
    raise AttributeError from e
    
titresDuJour = []
resumesDuJour = []
metasDuJour = []
liensDuJour = []

n=0
for i in abstracts:
    n+=1
    print(n)


n=0 # n = 20 normalement. 
for i in titles:
    if "QTL" in i.text:
        if i.text not in titresDuJour:
            titresDuJour.append(titles[n].text)
            resumesDuJour.append(abstracts[n].text)
            metasDuJour.append(authorsAndJournals[n].text)
            liensDuJour.append("https://link.springer.com"+titles[n].get('href').encode('utf-8').decode('utf-8'))

    n+=1

print(titles)



