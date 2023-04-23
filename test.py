
import requests

val = requests.get("https://api.adzuna.com/v1/api/jobs/fr/search/5?app_id=7d943028&app_key=d65e648bb664af69fe8a73941514bbe8").json()


val['results'][0]["location"]["display_name"]
val['results'][0]["description"]

import pymysql
connection = pymysql.connect(host='db',
                             user='root',
                             password='root',
                             port=3306)


dbcreate = "CREATE DATABASE IF NOT EXISTS EMPLOI"
tablecreate = "CREATE TABLE IF NOT EXISTS offre_emploi (location varchar(250), description varchar(1000));"
dbselect = "USE EMPLOI;"

connection.cursor().execute(dbcreate)
connection.commit()
connection.cursor().execute(dbselect)
connection.commit()
connection.cursor().execute(tablecreate)
connection.commit() 




for i in val['results']:
    location = i["location"]["display_name"]
    description = i["description"].replace("é","e").replace("è","e")
    req = """INSERT INTO offre_emploi (location, description)
         VALUES (%s, %s)"""
    connection.cursor().execute(req, (location, description))
    connection.commit()
    print("une ligne inserer")