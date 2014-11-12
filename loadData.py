import py2neo
from py2neo import neo4j
import csv

node = py2neo.node
rel  = py2neo.rel

rawData = []

users = []
songs = []
forNeo = []
with open("/home/devinj/neo4jData/ydata-ymusic-rating-study-v1_0-test.txt",'rb') as csvfile:
    csvreader = csv.reader(csvfile,delimiter='\t')
    for row in csvreader:
        rawData.append(row)
        if row[0] not in users:
            users.append(row[0])
            currentUser = node(uid=row[0])
            #forNeo.append(currentUser)
        if row[1] not in songs:
            songs.append(row[1])
            currentSong = node(songid=row[1])
            #forNeo.append(currentSong)
        forNeo.append(rel(currentUser,("RATED",{"rating": row[2]}),currentSong))


def head(data,i=9):
    for row in range(0,i):
        print data[row]

head(forNeo)

graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")
batch = neo4j.WriteBatch(graph_db)

graph_db.create(rel(currentUser,("RATED",{"rating": 5}),currentSong))

for row in range(0,1):
    graph_db.create(forNeo[row])

#neoStuff =  batch.submit()



#upload = graph_db.create(forNeo[0])



neo4j._add_header('X-Stream', 'true;format=pretty')



