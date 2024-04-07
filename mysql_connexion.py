import mysql.connector
import scraping as s
from getpass4 import getpass

db = mysql.connector.connect(
    host = "localhost",
    user = input("Username: "),
    password = getpass("password: "), 
    database="vegBiotech"
)

mycursor = db.cursor()

#Une première requête pour vérifier si l'article est déjà présent. 
checkQuery = "SELECT * FROM Articles WHERE titres = %s"

#Une seconde requête pour enregistrer un article en BDD.
query = "INSERT INTO Articles (titres, resumes, metas, liens) VALUES (%s,%s,%s,%s)"

#mycursor.execute("CREATE TABLE Articles (article_id BIGINT NOT NULL AUTO_INCREMENT, titres VARCHAR(250), resumes VARCHAR(500), metas VARCHAR(250), liens VARCHAR(250), PRIMARY KEY (`article_id`))")
#mycursor.execute("CREATE TABLE ex_articles (article_id BIGINT NOT NULL AUTO_INCREMENT, titres VARCHAR(250), resumes VARCHAR(500), metas VARCHAR(250), liens VARCHAR(250), PRIMARY KEY (`article_id`))")
#mycursor.execute("DESCRIBE Articles")


for i in range(len(s.titresDuJour)):
    mycursor.execute(checkQuery, (s.titresDuJour[i],))
    #fetchone() permet de récupérer la réponse de la requête 1. 
    resultCheckQuery = mycursor.fetchone()
    #Si l'article est déjà présent en BDD alors pas d'ajout. -> à ce jour j'ai un souci ici. 
    if resultCheckQuery == None :
        mycursor.execute(query, (s.titresDuJour[i], s.resumesDuJour[i], s.metasDuJour[i], s.liensDuJour[i]))
        db.commit()
    else :
        print("rien d'neuf")


#On récupère les titres en vue des les tweeter.
mycursor.execute("SELECT titres FROM articles")
result = mycursor.fetchall()
titresTweeter = []
for i in result:
    titresTweeter.append(i)

#On récupère les resumes en vue des les tweeter.
mycursor.execute("SELECT resumes FROM articles")
result = mycursor.fetchall()
resumesTweeter = []
for i in result:
    resumesTweeter.append(i)

#On récupère les metas en vue des les tweeter.
mycursor.execute("SELECT metas FROM articles")
result = mycursor.fetchall()
metasTweeter = []
for i in result:
    metasTweeter.append(i)

#On récupère les liens en vue des les tweeter.
mycursor.execute("SELECT liens FROM articles")
result = mycursor.fetchall()
liensTweeter = []
for i in result:
    liensTweeter.append(i)



db.close()

