import sqlite3

def connect():
   conn1 = sqlite3.connect('userdatabase.db')
   print("Open Database Successfully for userdata")
   cursor1 = conn1.cursor()
    
   c1 = cursor1.execute('CREATE TABLE IF NOT EXISTS USER (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,firstname TEXT NOT NULL ,lastname TEXT NOT NULL, username VARCHAR NOT NULL, emailid VARCHAR NOT NULL, years TEXT NOT NULL, branch TEXT NOT NULL, gender TEXT NOT NULL, mobile int NOT NULL, college VARCHAR NOT NULL, setpass VARCHAR NOT NULL, confirmpass VARCHAR NOT NULL);')
   print("Table created successfully userdata")
   conn1.commit()

   conn2 = sqlite3.connect('eventsdatabase.db')
   print("Open Database Successfully for eventsdatabase")
   cursor2 = conn2.cursor()
   c2 = cursor2.execute('CREATE TABLE IF NOT EXISTS EVENTS (eid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,username VARCHAR NOT NULL, event TEXT NOT NULL, fee TEXT NOT NULL);')
   print("Table created successfully for events table")
   conn2.commit()

def viewalldata():
   conn1 = sqlite3.connect('userdatabase.db')
   print("Open Database Successfully for userdata")
   cursor1 = conn1.cursor()
   cursor1.execute("SELECT * FROM USER")
   rows = cursor1.fetchall()
   conn1.close()
   return rows

def search(firstname=""):
    conn1 = sqlite3.connect('userdatabase.db')
    print("Open Database Successfully 4th time in admin page ....")
    cursor1 = conn1.cursor()
    find_user1 = ("SELECT * FROM USER WHERE firstname=?",(firstname))
    u1 = cursor1.execute(find_user1)
    conn1.close()
    return u1

def searchevents(username=""):
    conn2 = sqlite3.connect('eventsdatabase.db')
    print("Open Database Successfully 4th time in admin page ....")
    cursor2 = conn2.cursor()
    find_user2 = ("SELECT * FROM EVENTS WHERE username=?",(username))
    u2 = cursor2.execute(find_user2)
    conn2.close()
    return u2
   
def delete(id):
    conn1 = sqlite3.connect('userdatabase.db')
    print("Open Database Successfully 4th time in admin page ....")
    cursor1 = conn1.cursor()
    cursor1.execute("DELETE FROM USER WHERE id=?",(id,))
    conn1.commit()
    print("DELETION DONE FROM ADMIN MODULE.....")
    conn1.close()

def deleteeventseid(eid):
    conn2 = sqlite3.connect('eventsdatabase.db')
    print("Open Database Successfully in sqlfile ....")
    cursor2 = conn2.cursor()
    cursor2.execute("DELETE FROM EVENTS WHERE eid=?",(eid,))
    conn2.commit()
    print("DELETION DONE FROM EVENTS MODULE.....")
    conn2.close()

def deleteeventseidinfo(eid):
    conn2 = sqlite3.connect('eventsdatabase.db')
    print("Open Database Successfully in sqlfile ....")
    cursor2 = conn2.cursor()
    cursor2.execute("DELETE FROM EVENTS WHERE eid=?",(eid,))
    conn2.commit()
    print("DELETION DONE FROM EVENTS MODULE.....")
    conn2.close()

    
connect()
