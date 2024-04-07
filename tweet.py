import tweepy as tw
import keys
import mysql_connexion as sql
import re
import scraping


query_ex = "INSERT INTO ex_articles (titres, resumes, metas, liens) VALUES (%s,%s,%s,%s)"

client = tw.Client(keys.Bearer_token, keys.API_key, keys.API_key_secret, keys.Access_token, keys.Access_token_secret)
auth = tw.OAuth1UserHandler(keys.API_key, keys.API_key_secret, keys.Access_token, keys.Access_token_secret)
api = tw.API(auth)


for i in range(len(sql.titresTweeter)):
    t = str(sql.titresTweeter[i]) +"\n" +"\n"+ str(sql.metasTweeter[i])+"\n"+"\n"+"Read >>> "+str(sql.liensTweeter[i])
    #regex pour remplacer '[]()' par ''
    tweet = re.sub("[()']","",t)
    client.create_tweet(text = tweet)
    sql.mycursor.execute(query_ex, (scraping.titresTweeter, scraping.metasTweeter, scraping.liensTweeter))
    sql.db.commit()


sql.titresTweeter = []
sql.metasTweeter = []
sql.liensTweeter = []