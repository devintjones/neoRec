LOAD CSV FROM 'file:///home/devinj/neo4jData/ydata-ymusic-rating-study-v1_0-test.txt' AS line
FIELDTERMINATOR '\t'
MERGE (users:Users {userId : toInt(line[0])})
WITH line, users
MERGE (items:Items {itemId : toInt(line[1])})
WITH items, users, line



