import py2neo
import csv

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
            currentUser = py2neo.node(uid=row[0])
        if row[1] not in songs:
            songs.append(row[1])
            currentSong = py2neo.node(songid=row[1]) 
        forNeo.append(py2neo.rel(currentUser,("RATED",{"rating":row[2]}),currentSong))


def head(data,i=9):
    for row in range(0,i):
        print data[row]




head(forNeo)
print type(forNeo[0])
