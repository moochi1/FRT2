
import MySQLdb

from MySQLdb import cursors




db= MySQLdb.connect(host="localhost",user="root",passwd="root",db="test")
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM marks")

# print all the first cell of all the rows

result=cur.fetchall()
print (result)












current = 0

diff=0

for row in result:
	i=db.cursor()
	previous=current

	current= row[1]

	difference=int(current-previous)
	print (type(row[0]))
	print (type(difference))
	print ("UPDATE marks SET diff=" +str(difference) + " where name = \'"+ row[0] + "\'")
	
	i.execute("UPDATE marks SET diff=" +str(difference) + " where name = \'"+ row[0] + "\'")
	db.commit()


db.close()
