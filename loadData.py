from py2neo import neo4j, node, rel
import csv


def head(data,i=9):
    for row in range(0,i):
        print data[row]
def tail(data,i=9):
    for row in range(len(data)-i,len(data)):
        print data[row]

ratings = []
with open("/home/devinj/neo4jData/ydata-ymusic-rating-study-v1_0-test.txt",'rb') as csvfile:
    csvreader = csv.reader(csvfile,delimiter='\t')
    for row in csvreader:
        ratings.append(row)

#takes a columns of [user, item, rating] and preps for neo node & relationship creation
def prepForNeo(data):
    from py2neo import neo4j, node, rel
    users   = []
    ratings = []
    songs   = []
    useridx = 0
    songidx = 0
    userdict = {}
    songdict = {}

    for row in data:
        ratings.append(row)
        if row[0] not in userdict:
            users.append(node(uid=row[0]))
            userdict[row[0]]=useridx
            useridx += 1
        if row[1] not in songdict:
            songs.append(node(songid=row[1]))
            songdict[row[1]]=songidx
            songidx += 1

    neoRatings = []
    for rating in ratings:
        neoRatings.append(rel(userdict[rating[0]],("RATED",{"rating":rating[2]}),songdict[rating[1]]))

    allTogether = users + songs + neoRatings
    
    return allTogether


allTogether = prepForNeo(ratings)









graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

#batch = neo4j.WriteBatch(graph_db)
#neoStuff =  batch.submit()


#upload = graph_db.create(*allTogether)

neo4j._add_header('X-Stream', 'true;format=pretty')



