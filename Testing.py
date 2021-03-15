#import
from tkinter import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import sqlite3
import sqlfile
from tkinter import messagebox as ms
from guiwidgets.listview import MultiListbox
from PIL import Image, ImageTk
import tkinter.font as font
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

global window
window = Tk()
width=400
height=310
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry("%dx%d+%d+%d" % (width, height, x, y))
window.overrideredirect(True)
window.resizable(0, 0)
topFrame = Frame(window, width=400, height=30, bg="#23232F")
bottomFrame = Frame(window, width=400, height=280, bg="#2B2B37")
topFrame.grid(row=0)
bottomFrame.grid(row=1)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Admin Database
conn = sqlite3.connect('admindata.db')
print("Open Database Successfully for admindata")

cursor = conn.cursor()
c = cursor.execute('CREATE TABLE IF NOT EXISTS ADMIN (username TEXT NOT NULL ,password TEXT NOT NULL);')
print("Table created successfully admindata")

conn.commit()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#userdatabase
conn1 = sqlite3.connect('userdatabase.db')
print("Open Database Successfully for userdata")
cursor1 = conn1.cursor()
    
c1 = cursor1.execute('CREATE TABLE IF NOT EXISTS USER (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,firstname TEXT NOT NULL ,lastname TEXT NOT NULL, username VARCHAR NOT NULL, emailid VARCHAR NOT NULL, years TEXT NOT NULL, branch TEXT NOT NULL, gender TEXT NOT NULL, mobile VARCHAR NOT NULL, college TEXT NOT NULL, setpass VARCHAR NOT NULL, confirmpass VARCHAR NOT NULL);')
print("Table created successfully userdata")
conn1.commit()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
conn2 = sqlite3.connect('eventsdatabase.db')
print("Open Database Successfully for eventsdatabase")
cursor2 = conn2.cursor()
c2 = cursor2.execute('CREATE TABLE IF NOT EXISTS EVENTS (eid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,username VARCHAR NOT NULL, event TEXT NOT NULL, fee TEXT NOT NULL);')
print("Table created successfully for events table")
conn2.commit()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
class WindowDraggable():

    def __init__(self, Frame):
        self.topFrame = topFrame
        topFrame.bind('<ButtonPress-1>', self.StartMove)
        topFrame.bind('<ButtonRelease-1>', self.StopMove)
        topFrame.bind('<B1-Motion>', self.OnMotion)

    def StartMove(self, event):
        self.x = event.x
        self.y = event.y

    def StopMove(self, event):
        self.x = None
        self.y = None
        
    def OnMotion(self,event):
        x = (event.x_root - self.x - self.topFrame.winfo_rootx() + self.topFrame.winfo_rootx())
        y = (event.y_root - self.y - self.topFrame.winfo_rooty() + self.topFrame.winfo_rooty())
        window.geometry("+%s+%s" % (x, y))


WindowDraggable(topFrame)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#loginvalidation
def Login():
    conn = sqlite3.connect('admindata.db')
    print("Connection Established Successfully")
    cursor = conn.cursor()
    
    insert_command = "INSERT OR IGNORE INTO ADMIN VALUES (?, ?)"
    c = cursor.execute(insert_command, ('admin', 'admin'))
    print("Records inserted successfully")
    conn.commit()
    find_user = ('SELECT * FROM ADMIN WHERE username=? AND password=?')
    c = cursor.execute(find_user,[(username.get()),(password.get())])
    print("Selection of data is done")
    conn.commit()
    result = cursor.fetchall()


    conn1 = sqlite3.connect('userdatabase.db')
    print("Open Database Successfully 2nd time")
    cursor1 = conn1.cursor()
        
    find_user1 = ('SELECT * FROM USER WHERE username=? AND setpass=?')
    u1 = cursor1.execute(find_user1,[(username.get()),(password.get())])
    conn1.commit()
    
    f1 = u1.fetchall()
    print("Fetching of data is done 2nd time")
         
    if result:
        ms.showinfo('CORRECT!','Login Successfull As Admin!')
        Admin() 
    elif f1:
        ms.showinfo('CORRECT!','Login Successfull As USER!')
        USERS()
    else:
        ms.showerror('Error!','Invalid Inputs!')
        
def CULTURAL():
    
    global windowcultural
    rootnew.withdraw()
    windowcultural = Toplevel()
    width=500
    height=470
    screen_width = windowcultural.winfo_screenwidth()
    screen_height = windowcultural.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    windowcultural.geometry("%dx%d+%d+%d" % (width, height, x, y))
    windowcultural.overrideredirect(True)
    windowcultural.resizable(0, 0)
    topFrame = Frame(windowcultural, width=500, height=30, bg="#23232F")
    bottomFrame = Frame(windowcultural, width=500, height=800, bg="#2B2B37")
    topFrame.grid(row=0)
    bottomFrame.grid(row=1)

    class WindowDraggableCultural():

        def __init__(self, Frame):
            self.topFrame = topFrame
            topFrame.bind('<ButtonPress-1>', self.StartMove)
            topFrame.bind('<ButtonRelease-1>', self.StopMove)
            topFrame.bind('<B1-Motion>', self.OnMotion)

        def StartMove(self, event):
            self.x = event.x
            self.y = event.y

        def StopMove(self, event):
            self.x = None
            self.y = None
        
        def OnMotion(self,event):
            x = (event.x_root - self.x - self.topFrame.winfo_rootx() + self.topFrame.winfo_rootx())
            y = (event.y_root - self.y - self.topFrame.winfo_rooty() + self.topFrame.winfo_rooty())
            windowcultural.geometry("+%s+%s" % (x, y))

    WindowDraggableCultural(topFrame)

    def onback(event=None):
        windowcultural.destroy()
        rootnew.deiconify()
        
    def onclose(event=None):
        windowcultural.destroy()

    def frame_mapped(event=None):
        windowcultural.update_idletasks()
        windowcultural.overrideredirect(True)
        windowcultural.state('normal')
    topFrame.bind("<Map>",frame_mapped)

    def onmin(event=None):
        windowcultural.update_idletasks()
        windowcultural.overrideredirect(False)
        windowcultural.state('iconic')
        
    def onClick():
        ms.showinfo("Zodiac Event's", "Event Added")

    def onClickMusicBand():
        ms.showinfo("Zodiac Event's", "Event Added")
        MusicBand()

    def MusicBand():
        btnproceednew.config(state=NORMAL)
        conn1 = sqlite3.connect('userdatabase.db')
        print("Open Database Successfully for userdata")
        cursor1 = conn1.cursor()
        cursor1.execute('SELECT * FROM USER')
        conn1.commit()
        fm = cursor1.fetchall()
        print("Fetching of data is done from userdatabase for music band")
        if fm:
            txtmusic =StringVar()
            txtmusic.set("Music Band")       
            conn2 = sqlite3.connect('eventsdatabase.db')
            print("Open Database Successfully for cultural events")
            cursor2 = conn2.cursor()
            insertcommand2 = "INSERT OR IGNORE INTO EVENTS VALUES (NULL, ?, ?, ?)"
            cursor2.execute(insertcommand2,(username.get(),txtmusic.get(),'150' ))
            print("Records inserted successfully")
            conn2.commit()

    def onClickDrama():
        ms.showinfo("Zodiac Event's", "Event Added")
        Drama()

    def Drama():
        btnproceednew.config(state=NORMAL)
        conn1 = sqlite3.connect('userdatabase.db')
        print("Open Database Successfully for userdata")
        cursor1 = conn1.cursor()
        cursor1.execute('SELECT * FROM USER')
        conn1.commit()
        fm = cursor1.fetchall()
        print("Fetching of data is done from userdatabase for drama")
        if fm:
            txtdrama =StringVar()
            txtdrama.set("Drama")       
            conn2 = sqlite3.connect('eventsdatabase.db')
            print("Open Database Successfully for cultural events")
            cursor2 = conn2.cursor()
            insertcommand2 = "INSERT OR IGNORE INTO EVENTS VALUES (NULL, ?, ?, ?)"
            cursor2.execute(insertcommand2,(username.get(),txtdrama.get(),'250' ))
            print("Records inserted successfully")
            conn2.commit()

    def onClickFashionShow(): 
        ms.showinfo("Zodiac Event's", "Event Added")
        FashionShow()

    def FashionShow():
        btnproceednew.config(state=NORMAL)
        conn1 = sqlite3.connect('userdatabase.db')
        print("Open Database Successfully for userdata")
        cursor1 = conn1.cursor()
        cursor1.execute('SELECT * FROM USER')
        conn1.commit()
        fm = cursor1.fetchall()
        print("Fetching of data is done from userdatabase for fashionshow")
        if fm:
            txtfashionshow =StringVar()
            txtfashionshow.set("Fashion Show")       
            conn2 = sqlite3.connect('eventsdatabase.db')
            print("Open Database Successfully for cultural events")
            cursor2 = conn2.cursor()
            insertcommand2 = "INSERT OR IGNORE INTO EVENTS VALUES (NULL, ?, ?, ?)"
            cursor2.execute(insertcommand2,(username.get(),txtfashionshow.get(),'200' ))
            print("Records inserted successfully")
            conn2.commit()

    def onClickSinging():
        ms.showinfo("Zodiac Event's", "Event Added")
        Singing()

    def Singing():
        btnproceednew.config(state=NORMAL)
        conn1 = sqlite3.connect('userdatabase.db')
        print("Open Database Successfully for userdata")
        cursor1 = conn1.cursor()
        cursor1.execute('SELECT * FROM USER')
        conn1.commit()
        fm = cursor1.fetchall()
        print("Fetching of data is done from userdatabase for singing")
        if fm:
            txtsinging =StringVar()
            txtsinging.set("Singing")       
            conn2 = sqlite3.connect('eventsdatabase.db')
            print("Open Database Successfully for cultural events")
            cursor2 = conn2.cursor()
            insertcommand2 = "INSERT OR IGNORE INTO EVENTS VALUES (NULL, ?, ?, ?)"
            cursor2.execute(insertcommand2,(username.get(),txtsinging.get(),'180' ))
            print("Records inserted successfully")
            conn2.commit()


    def onClickDance():
        ms.showinfo("Zodiac Event's", "Event Added")
        Dance()

    def Dance():
        btnproceednew.config(state=NORMAL)
        conn1 = sqlite3.connect('userdatabase.db')
        print("Open Database Successfully for userdata")
        cursor1 = conn1.cursor()
        cursor1.execute('SELECT * FROM USER')
        conn1.commit()
        fm = cursor1.fetchall()
        print("Fetching of data is done from userdatabase for dance")
        if fm:
            txtdance =StringVar()
            txtdance.set("Dance")       
            conn2 = sqlite3.connect('eventsdatabase.db')
            print("Open Database Successfully for cultural events")
            cursor2 = conn2.cursor()
            insertcommand2 = "INSERT OR IGNORE INTO EVENTS VALUES (NULL, ?, ?, ?)"
            cursor2.execute(insertcommand2,(username.get(),txtdance.get(),'300' ))
            print("Records inserted successfully")
            conn2.commit()

    def onClickMime():
        ms.showinfo("Zodiac Event's", "Event Added")
        Mime()

    def Mime():
        btnproceednew.config(state=NORMAL)
        conn1 = sqlite3.connect('userdatabase.db')
        print("Open Database Successfully for userdata")
        cursor1 = conn1.cursor()
        cursor1.execute('SELECT * FROM USER')
        conn1.commit()
        fm = cursor1.fetchall()
        print("Fetching of data is done from userdatabase for mime")
        if fm:
            txtmime =StringVar()
            txtmime.set("Mime")       
            conn2 = sqlite3.connect('eventsdatabase.db')
            print("Open Database Successfully for cultural events")
            cursor2 = conn2.cursor()
            insertcommand2 = "INSERT OR IGNORE INTO EVENTS VALUES (NULL, ?, ?, ?)"
            cursor2.execute(insertcommand2,(username.get(),txtmime.get(),'220' ))
            print("Records inserted successfully")
            conn2.commit()

    
    global musiccul
    musiccul = StringVar()
    #imageback
    image1 = Image.open("backlogo.png")
    image1 = image1.resize((18, 18), Image.ANTIALIAS) 
    photo1 = ImageTk.PhotoImage(image1)
    back1 = Button(topFrame, image=photo1, borderwidth=0, bg="#23232F",command=onback) # button with image binded to the same function 
    back1.grid(row=0)
    back1.place( x=10, y=6)
    #imageclose
    image2 = Image.open("close.png")
    image2 = image2.resize((18, 18), Image.ANTIALIAS)
    photo2 = ImageTk.PhotoImage(image2)
    close = Button(topFrame, image=photo2, borderwidth=0, bg="#23232F",command=onclose) # button with image binded to the same function
    close.grid(row=0)
    close.place( x=473, y=6)
    #imagemin
    image3 = Image.open("min1.png")
    image3 = image3.resize((18, 18), Image.ANTIALIAS)
    photo3 = ImageTk.PhotoImage(image3)
    min1 = Button(topFrame, image=photo3,  borderwidth=0, bg="#23232F",command=onmin)
    min1.grid(row=0)
    min1.place( x=452, y=6)

    font1 = font.Font(family='Haettenschweiler', size=14)
    image4 = Image.open("cultural_event_main.png")
    image4 = image4.resize((180, 80), Image.ANTIALIAS)
    photo4 = ImageTk.PhotoImage(image4)
    Title1=Label(windowcultural, image=photo4,  borderwidth=0, bg="#2B2B37" ,width=200,padx=70,pady=70)
    Title1.place(x=193,y=30)
    events1=Label(windowcultural,text="Events",font=font1,bg="#2B2B37",fg="#f64747")
    events1.place(x=350,y=98)

    image5 = Image.open("cultural_event.png")
    image5 = image5.resize((60, 60), Image.ANTIALIAS)
    photo5 = ImageTk.PhotoImage(image5)
    Title=Label(windowcultural, image=photo5,  borderwidth=0, bg="#2B2B37" ,width=100,padx=70,pady=70)
    Title.place(x=100,y=40)

    image6 = Image.open("cultural_music.png")
    image6 = image6.resize((50, 50), Image.ANTIALIAS)
    photo6 = ImageTk.PhotoImage(image6)
    cultural_music=Label(windowcultural, image=photo6,  borderwidth=0, bg="#2B2B37" ,width=100,padx=70,pady=70)
    cultural_music.place(x=30,y=140)
    cultural_music_Button=Button(windowcultural,text="Music Band",font=font1,borderwidth=0, bg="#2B2B37",fg="#f64747",command=onClickMusicBand)
    cultural_music_Button.place(x=105,y=160)

    image7 = Image.open("cultural_drama.png")
    image7 = image7.resize((50, 50), Image.ANTIALIAS)
    photo7 = ImageTk.PhotoImage(image7)
    cultural_drama_Label=Label(windowcultural, image=photo7,  borderwidth=0, bg="#2B2B37" ,width=100,padx=70,pady=70)
    cultural_drama_Label.place(x=30,y=230)
    cultural_drama_button=Button(windowcultural,text="Drama",font=font1,borderwidth=0, bg="#2B2B37",fg="#f64747",command=onClickDrama)
    cultural_drama_button.place(x=115,y=240)

    image8 = Image.open("cultural_fashion.png")
    image8 = image8.resize((50, 50), Image.ANTIALIAS)
    photo8 = ImageTk.PhotoImage(image8)
    cultural_fashion_Label=Label(windowcultural, image=photo8,  borderwidth=0, bg="#2B2B37" ,width=100,padx=70,pady=70)
    cultural_fashion_Label.place(x=30,y=320)
    cultural_fashion_button=Button(windowcultural,text="Fashion Show",font=font1,borderwidth=0, bg="#2B2B37",fg="#f64747",command=onClickFashionShow)
    cultural_fashion_button.place(x=105,y=330)

    image9 = Image.open("cultural_singing.png")
    image9 = image9.resize((50, 50), Image.ANTIALIAS)
    photo9 = ImageTk.PhotoImage(image9)
    cultural_singing_Label=Label(windowcultural, image=photo9,  borderwidth=0, bg="#2B2B37" ,width=100,padx=70,pady=70)
    cultural_singing_Label.place(x=260,y=140)
    cultural_singing_button=Button(windowcultural,text="Singing",font=font1,borderwidth=0, bg="#2B2B37",fg="#f64747",command=onClickSinging)
    cultural_singing_button.place(x=355,y=155)

    image10 = Image.open("cultural_dance.png")
    image10 = image10.resize((50, 50), Image.ANTIALIAS)
    photo10 = ImageTk.PhotoImage(image10)
    cultural_fashion_Label=Label(windowcultural, image=photo10,  borderwidth=0, bg="#2B2B37" ,width=100,padx=70,pady=70)
    cultural_fashion_Label.place(x=260,y=320)
    cultural_dance_button=Button(windowcultural,text="Dance",font=font1,borderwidth=0, bg="#2B2B37",fg="#f64747",command=onClickDance)
    cultural_dance_button.place(x=355,y=330)

    image11 = Image.open("cultural_mime.png")
    image11 = image11.resize((60, 60), Image.ANTIALIAS)
    photo11 = ImageTk.PhotoImage(image11)
    cultural_mime_Label=Label(windowcultural, image=photo11,  borderwidth=0, bg="#2B2B37" ,width=100,padx=70,pady=70)
    cultural_mime_Label.place(x=260,y=230)
    cultural_mime_button=Button(windowcultural,text="Mime",font=font1,borderwidth=0, bg="#2B2B37",fg="#f64747",command=onClickMime)
    cultural_mime_button.place(x=355,y=240)


    
    windowcultural.mainloop()

def SPORTS():
    global windowsports
    rootnew.withdraw()
    windowsports = Toplevel()
    width=500
    height=470
    screen_width = windowsports.winfo_screenwidth()
    screen_height = windowsports.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    windowsports.geometry("%dx%d+%d+%d" % (width, height, x, y))
    windowsports.overrideredirect(True)
    windowsports.resizable(0, 0)
    topFrame = Frame(windowsports, width=500, height=30, bg="#23232F")
    bottomFrame = Frame(windowsports, width=500, height=800, bg="#2B2B37")
    topFrame.grid(row=0)
    bottomFrame.grid(row=1)

    class WindowDraggableSports():

        def __init__(self, Frame):
            self.topFrame = topFrame
            topFrame.bind('<ButtonPress-1>', self.StartMove)
            topFrame.bind('<ButtonRelease-1>', self.StopMove)
            topFrame.bind('<B1-Motion>', self.OnMotion)

        def StartMove(self, event):
            self.x = event.x
            self.y = event.y

        def StopMove(self, event):
            self.x = None
            self.y = None
        
        def OnMotion(self,event):
            x = (event.x_root - self.x - self.topFrame.winfo_rootx() + self.topFrame.winfo_rootx())
            y = (event.y_root - self.y - self.topFrame.winfo_rooty() + self.topFrame.winfo_rooty())
            windowsports.geometry("+%s+%s" % (x, y))

    WindowDraggableSports(topFrame)

    #-----------------------------------------------------------------------------#
    #minimizebutton
    def back(event=None):
        windowsports.destroy()
        rootnew.deiconify()

    def close(event=None):
        windowsports.destroy()

    def frame_mapped(event=None):
        windowsports.update_idletasks()
        windowsports.overrideredirect(True)
        windowsports.state('normal')
    topFrame.bind("<Map>",frame_mapped)

    def minimize(event=None):
        windowsports.update_idletasks()
        windowsports.overrideredirect(False)
        windowsports.state('iconic')
        
    def onClickFootball():
        ms.showinfo("Zodiac Event's", "Event Added")
        Football()

    def Football():
        btnproceednew.config(state=NORMAL)
        conn1 = sqlite3.connect('userdatabase.db')
        print("Open Database Successfully for userdata")
        cursor1 = conn1.cursor()
        cursor1.execute('SELECT * FROM USER')
        conn1.commit()
        fm = cursor1.fetchall()
        print("Fetching of data is done from userdatabase for Football")
        if fm:
            txtfootball =StringVar()
            txtfootball.set("Football")       
            conn2 = sqlite3.connect('eventsdatabase.db')
            print("Open Database Successfully for cultural events")
            cursor2 = conn2.cursor()
            insertcommand2 = "INSERT OR IGNORE INTO EVENTS VALUES (NULL, ?, ?, ?)"
            cursor2.execute(insertcommand2,(username.get(),txtfootball.get(),'350' ))
            print("Records inserted successfully")
            conn2.commit()

    def onClickBadminton():    
        ms.showinfo("Zodiac Event's", "Event Added")
        Badminton()

    def Badminton():
        btnproceednew.config(state=NORMAL)
        conn1 = sqlite3.connect('userdatabase.db')
        print("Open Database Successfully for userdata")
        cursor1 = conn1.cursor()
        cursor1.execute('SELECT * FROM USER')
        conn1.commit()
        fm = cursor1.fetchall()
        print("Fetching of data is done from userdatabase for Badminton")
        if fm:
            txtbadminton =StringVar()
            txtbadminton.set("Badminton")       
            conn2 = sqlite3.connect('eventsdatabase.db')
            print("Open Database Successfully for cultural events")
            cursor2 = conn2.cursor()
            insertcommand2 = "INSERT OR IGNORE INTO EVENTS VALUES (NULL, ?, ?, ?)"
            cursor2.execute(insertcommand2,(username.get(),txtbadminton.get(),'150' ))
            print("Records inserted successfully")
            conn2.commit()
            
    def onClickCricket():
        ms.showinfo("Zodiac Event's", "Event Added")
        Cricket()

    def Cricket():
        btnproceednew.config(state=NORMAL)
        conn1 = sqlite3.connect('userdatabase.db')
        print("Open Database Successfully for userdata")
        cursor1 = conn1.cursor()
        cursor1.execute('SELECT * FROM USER')
        conn1.commit()
        fm = cursor1.fetchall()
        print("Fetching of data is done from userdatabase for Cricket")
        if fm:
            txtcricket =StringVar()
            txtcricket.set("Cricket")       
            conn2 = sqlite3.connect('eventsdatabase.db')
            print("Open Database Successfully for cultural events")
            cursor2 = conn2.cursor()
            insertcommand2 = "INSERT OR IGNORE INTO EVENTS VALUES (NULL, ?, ?, ?)"
            cursor2.execute(insertcommand2,(username.get(),txtcricket.get(),'550' ))
            print("Records inserted successfully")
            conn2.commit()

    def onClickSwimming():
        ms.showinfo("Zodiac Event's", "Event Added")
        Swimming()

    def Swimming():
        btnproceednew.config(state=NORMAL)
        conn1 = sqlite3.connect('userdatabase.db')
        print("Open Database Successfully for userdata")
        cursor1 = conn1.cursor()
        cursor1.execute('SELECT * FROM USER')
        conn1.commit()
        fm = cursor1.fetchall()
        print("Fetching of data is done from userdatabase for Swimming")
        if fm:
            txtswimming =StringVar()
            txtswimming.set("Swimming")       
            conn2 = sqlite3.connect('eventsdatabase.db')
            print("Open Database Successfully for cultural events")
            cursor2 = conn2.cursor()
            insertcommand2 = "INSERT OR IGNORE INTO EVENTS VALUES (NULL, ?, ?, ?)"
            cursor2.execute(insertcommand2,(username.get(),txtswimming.get(),'200' ))
            print("Records inserted successfully")
            conn2.commit()

    def onClickTennis():
        ms.showinfo("Zodiac Event's", "Event Added")
        Tennis()

    def Tennis():
        btnproceednew.config(state=NORMAL)
        conn1 = sqlite3.connect('userdatabase.db')
        print("Open Database Successfully for userdata")
        cursor1 = conn1.cursor()
        cursor1.execute('SELECT * FROM USER')
        conn1.commit()
        fm = cursor1.fetchall()
        print("Fetching of data is done from userdatabase for Tennis")
        if fm:
            txttennis =StringVar()
            txttennis.set("Tennis")       
            conn2 = sqlite3.connect('eventsdatabase.db')
            print("Open Database Successfully for cultural events")
            cursor2 = conn2.cursor()
            insertcommand2 = "INSERT OR IGNORE INTO EVENTS VALUES (NULL, ?, ?, ?)"
            cursor2.execute(insertcommand2,(username.get(),txttennis.get(),'250' ))
            print("Records inserted successfully")
            conn2.commit()

    def onClickVolleyBall():
        ms.showinfo("Zodiac Event's", "Event Added")
        VolleyBall()

    def VolleyBall():
        btnproceednew.config(state=NORMAL)
        conn1 = sqlite3.connect('userdatabase.db')
        print("Open Database Successfully for userdata")
        cursor1 = conn1.cursor()
        cursor1.execute('SELECT * FROM USER')
        conn1.commit()
        fm = cursor1.fetchall()
        print("Fetching of data is done from userdatabase for VolleyBall")
        if fm:
            txtVolleyBall =StringVar()
            txtVolleyBall.set("VolleyBall")       
            conn2 = sqlite3.connect('eventsdatabase.db')
            print("Open Database Successfully for cultural events")
            cursor2 = conn2.cursor()
            insertcommand2 = "INSERT OR IGNORE INTO EVENTS VALUES (NULL, ?, ?, ?)"
            cursor2.execute(insertcommand2,(username.get(),txtVolleyBall.get(),'500' ))
            print("Records inserted successfully")
            conn2.commit()

    #------------------------------------------------------------------------------#
    #imageback
    imageback = Image.open("backlogo.png")
    imageback = imageback.resize((18, 18), Image.ANTIALIAS) 
    photoback = ImageTk.PhotoImage(imageback)
    back0 = Button(windowsports, image=photoback, borderwidth=0, bg="#23232F",command=back) # button with image binded to the same function 
    back0.grid(row=0)
    back0.place( x=10, y=6)
    
    #imageclose
    image1 = Image.open("close.png")
    image1 = image1.resize((18, 18), Image.ANTIALIAS)
    photo1 = ImageTk.PhotoImage(image1)
    close = Button(windowsports, image=photo1, borderwidth=0, bg="#23232F", command=close) # button with image binded to the same function
    close.grid(row=0)
    close.place( x=470, y=6)

    #imagemin
    image2 = Image.open("min1.png")
    image2 = image2.resize((18, 18), Image.ANTIALIAS)
    photo2 = ImageTk.PhotoImage(image2)
    min1 = Button(windowsports, image=photo2,  borderwidth=0, bg="#23232F", command=minimize) # button with image binded to the same function
    min1.grid(row=0)
    min1.place( x=450, y=6)
    #------------------------------------------------------------------------------------

    font1 = font.Font(family='Haettenschweiler', size=14)
    image0 = Image.open("sports_event_main.png")
    image0 = image0.resize((180, 80), Image.ANTIALIAS)
    photo0 = ImageTk.PhotoImage(image0)
    Title=Label(windowsports, image=photo0,  borderwidth=0, bg="#2B2B37" ,width=200,padx=70,pady=70)
    Title.place(x=193,y=30)
    events=Label(windowsports,text="Events",font=font1,bg="#2B2B37",fg="#f64747")
    events.place(x=350,y=105)

    font1 = font.Font(family='Haettenschweiler', size=14)
    image3 = Image.open("sports.png")
    image3 = image3.resize((60, 60), Image.ANTIALIAS)
    photo3 = ImageTk.PhotoImage(image3)
    Title=Label(windowsports, image=photo3,  borderwidth=0, bg="#2B2B37" ,width=100,padx=70,pady=70)
    Title.place(x=103,y=40)

    image4 = Image.open("sports_football.png")
    image4 = image4.resize((50, 50), Image.ANTIALIAS)
    photo4 = ImageTk.PhotoImage(image4)
    cultural_music=Label(windowsports, image=photo4,  borderwidth=0, bg="#2B2B37" ,width=100,padx=70,pady=70)
    cultural_music.place(x=30,y=140)
    cultural_football_Button=Button(windowsports,text="Football",font=font1,borderwidth=0, bg="#2B2B37",fg="#f64747",command=onClickFootball)
    cultural_football_Button.place(x=107,y=155)

    image5 = Image.open("sports_badminton.png")
    image5 = image5.resize((50, 50), Image.ANTIALIAS)
    photo5 = ImageTk.PhotoImage(image5)
    cultural_drama_Label=Label(windowsports, image=photo5,  borderwidth=0, bg="#2B2B37" ,width=100,padx=70,pady=70)
    cultural_drama_Label.place(x=30,y=230)
    cultural_badminton_button=Button(windowsports,text="Badminton",font=font1,borderwidth=0, bg="#2B2B37",fg="#f64747",command=onClickBadminton)
    cultural_badminton_button.place(x=115,y=240)

    image6 = Image.open("sports_cricket.png")
    image6 = image6.resize((50, 50), Image.ANTIALIAS)
    photo6 = ImageTk.PhotoImage(image6)
    cultural_fashion_Label=Label(windowsports, image=photo6,  borderwidth=0, bg="#2B2B37" ,width=100,padx=70,pady=70)
    cultural_fashion_Label.place(x=30,y=320)
    cultural_cricket_button=Button(windowsports,text="Cricket",font=font1,borderwidth=0, bg="#2B2B37",fg="#f64747",command=onClickCricket)
    cultural_cricket_button.place(x=105,y=330)

    image7 = Image.open("sports_swimming.png")
    image7 = image7.resize((50, 50), Image.ANTIALIAS)
    photo7 = ImageTk.PhotoImage(image7)
    cultural_singing_Label=Label(windowsports, image=photo7,  borderwidth=0, bg="#2B2B37" ,width=100,padx=70,pady=70)
    cultural_singing_Label.place(x=260,y=140)
    cultural_singing_button=Button(windowsports,text="Swimming",font=font1,borderwidth=0, bg="#2B2B37",fg="#f64747",command=onClickSwimming)
    cultural_singing_button.place(x=355,y=155)

    image8 = Image.open("sports_tennis.png")
    image8 = image8.resize((50, 50), Image.ANTIALIAS)
    photo8 = ImageTk.PhotoImage(image8)
    cultural_fashion_Label=Label(windowsports, image=photo8,  borderwidth=0, bg="#2B2B37" ,width=100,padx=70,pady=70)
    cultural_fashion_Label.place(x=260,y=320)
    cultural_tennis_button=Button(windowsports,text="Tennis",font=font1,borderwidth=0, bg="#2B2B37",fg="#f64747",command=onClickTennis)
    cultural_tennis_button.place(x=355,y=330)

    image9 = Image.open("sports_volleyball.png")
    image9 = image9.resize((60, 60), Image.ANTIALIAS)
    photo9 = ImageTk.PhotoImage(image9)
    cultural_mime_Label=Label(windowsports, image=photo9,  borderwidth=0, bg="#2B2B37" ,width=100,padx=70,pady=70)
    cultural_mime_Label.place(x=260,y=230)
    cultural_volleyball_button=Button(windowsports,text="VolleyBall",font=font1,borderwidth=0, bg="#2B2B37",fg="#f64747",command=onClickVolleyBall)
    cultural_volleyball_button.place(x=355,y=240)


    windowsports.mainloop()

def TECHNICAL():
    global windowtechnical
    rootnew.withdraw()
    windowtechnical = Toplevel()
    width=500
    height=470
    screen_width = windowtechnical.winfo_screenwidth()
    screen_height = windowtechnical.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    windowtechnical.geometry("%dx%d+%d+%d" % (width, height, x, y))
    windowtechnical.overrideredirect(True)
    windowtechnical.resizable(0, 0)
    topFrame = Frame(windowtechnical, width=500, height=30, bg="#23232F")
    bottomFrame = Frame(windowtechnical, width=500, height=800, bg="#2B2B37")
    topFrame.grid(row=0)
    bottomFrame.grid(row=1)

    class WindowDraggableTechnical():

        def __init__(self, Frame):
            self.topFrame = topFrame
            topFrame.bind('<ButtonPress-1>', self.StartMove)
            topFrame.bind('<ButtonRelease-1>', self.StopMove)
            topFrame.bind('<B1-Motion>', self.OnMotion)

        def StartMove(self, event):
            self.x = event.x
            self.y = event.y

        def StopMove(self, event):
            self.x = None
            self.y = None
        
        def OnMotion(self,event):
            x = (event.x_root - self.x - self.topFrame.winfo_rootx() + self.topFrame.winfo_rootx())
            y = (event.y_root - self.y - self.topFrame.winfo_rooty() + self.topFrame.winfo_rooty())
            windowtechnical.geometry("+%s+%s" % (x, y))

    WindowDraggableTechnical(topFrame)
    #-----------------------------------------------------------------------------#
    def back(event=None):
        windowtechnical.destroy()
        rootnew.deiconify()
    def on_close(event=None):
        windowtechnical.destroy()

    def frame_mapped(event=None):
        windowtechnical.update_idletasks()
        windowtechnical.overrideredirect(True)
        windowtechnical.state('normal')
    topFrame.bind("<Map>",frame_mapped)

    def on_minimize(event=None):
        windowtechnical.update_idletasks()
        windowtechnical.overrideredirect(False)
        windowtechnical.state('iconic')


    def onClickPaperPresentation():
        ms.showinfo("Zodiac Event's", "Event Added")
        PaperPresentation()

    def PaperPresentation():
        btnproceednew.config(state=NORMAL)
        conn1 = sqlite3.connect('userdatabase.db')
        print("Open Database Successfully for userdata")
        cursor1 = conn1.cursor()
        cursor1.execute('SELECT * FROM USER')
        conn1.commit()
        fm = cursor1.fetchall()
        print("Fetching of data is done from userdatabase for PaperPresentation")
        if fm:
            txtPaperPresentation =StringVar()
            txtPaperPresentation.set("Paper Presentation")       
            conn2 = sqlite3.connect('eventsdatabase.db')
            print("Open Database Successfully for cultural events")
            cursor2 = conn2.cursor()
            insertcommand2 = "INSERT OR IGNORE INTO EVENTS VALUES (NULL, ?, ?, ?)"
            cursor2.execute(insertcommand2,(username.get(),txtPaperPresentation.get(),'150' ))
            print("Records inserted successfully")
            conn2.commit()

    def onClickTechnicalQuiz():
        ms.showinfo("Zodiac Event's", "Event Added")
        TechnicalQuiz()

    def TechnicalQuiz():
        btnproceednew.config(state=NORMAL)
        conn1 = sqlite3.connect('userdatabase.db')
        print("Open Database Successfully for userdata")
        cursor1 = conn1.cursor()
        cursor1.execute('SELECT * FROM USER')
        conn1.commit()
        fm = cursor1.fetchall()
        print("Fetching of data is done from userdatabase for TechnicalQuiz")
        if fm:
            txtTechnicalQuiz =StringVar()
            txtTechnicalQuiz.set("Technical Quiz")       
            conn2 = sqlite3.connect('eventsdatabase.db')
            print("Open Database Successfully for cultural events")
            cursor2 = conn2.cursor()
            insertcommand2 = "INSERT OR IGNORE INTO EVENTS VALUES (NULL, ?, ?, ?)"
            cursor2.execute(insertcommand2,(username.get(),txtTechnicalQuiz.get(),'200' ))
            print("Records inserted successfully")
            conn2.commit()

    def onClickBlindCoding():
        ms.showinfo("Zodiac Event's", "Event Added")
        BlindCoding()

    def BlindCoding():
        btnproceednew.config(state=NORMAL)
        conn1 = sqlite3.connect('userdatabase.db')
        print("Open Database Successfully for userdata")
        cursor1 = conn1.cursor()
        cursor1.execute('SELECT * FROM USER')
        conn1.commit()
        fm = cursor1.fetchall()
        print("Fetching of data is done from userdatabase for BlindCoding")
        if fm:
            txtBlindCoding =StringVar()
            txtBlindCoding.set("Blind Coding")       
            conn2 = sqlite3.connect('eventsdatabase.db')
            print("Open Database Successfully for cultural events")
            cursor2 = conn2.cursor()
            insertcommand2 = "INSERT OR IGNORE INTO EVENTS VALUES (NULL, ?, ?, ?)"
            cursor2.execute(insertcommand2,(username.get(),txtBlindCoding.get(),'100' ))
            print("Records inserted successfully")
            conn2.commit()

    def onClickCodeDebugging():
        ms.showinfo("Zodiac Event's", "Event Added")
        CodeDebugging()

    def CodeDebugging():
        btnproceednew.config(state=NORMAL)
        conn1 = sqlite3.connect('userdatabase.db')
        print("Open Database Successfully for userdata")
        cursor1 = conn1.cursor()
        cursor1.execute('SELECT * FROM USER')
        conn1.commit()
        fm = cursor1.fetchall()
        print("Fetching of data is done from userdatabase for CodeDebugging")
        if fm:
            txtCodeDebugging =StringVar()
            txtCodeDebugging.set("Code Debugging")       
            conn2 = sqlite3.connect('eventsdatabase.db')
            print("Open Database Successfully for cultural events")
            cursor2 = conn2.cursor()
            insertcommand2 = "INSERT OR IGNORE INTO EVENTS VALUES (NULL, ?, ?, ?)"
            cursor2.execute(insertcommand2,(username.get(),txtCodeDebugging.get(),'140' ))
            print("Records inserted successfully")
            conn2.commit()
    
    def onClickRoboWar():
        ms.showinfo("Zodiac Event's", "Event Added")
        RoboWar()

    def RoboWar():
        btnproceednew.config(state=NORMAL)
        conn1 = sqlite3.connect('userdatabase.db')
        print("Open Database Successfully for userdata")
        cursor1 = conn1.cursor()
        cursor1.execute('SELECT * FROM USER')
        conn1.commit()
        fm = cursor1.fetchall()
        print("Fetching of data is done from userdatabase for RoboWar")
        if fm:
            txtRoboWar =StringVar()
            txtRoboWar.set("Robo War")       
            conn2 = sqlite3.connect('eventsdatabase.db')
            print("Open Database Successfully for cultural events")
            cursor2 = conn2.cursor()
            insertcommand2 = "INSERT OR IGNORE INTO EVENTS VALUES (NULL, ?, ?, ?)"
            cursor2.execute(insertcommand2,(username.get(),txtRoboWar.get(),'300' ))
            print("Records inserted successfully")
            conn2.commit()

    def onClickModelExhibiton():
        ms.showinfo("Zodiac Event's", "Event Added")
        ModelExhibiton()

    def ModelExhibiton():
        btnproceednew.config(state=NORMAL)
        conn1 = sqlite3.connect('userdatabase.db')
        print("Open Database Successfully for userdata")
        cursor1 = conn1.cursor()
        cursor1.execute('SELECT * FROM USER')
        conn1.commit()
        fm = cursor1.fetchall()
        print("Fetching of data is done from userdatabase for ModelExhibiton")
        if fm:
            txtModelExhibiton =StringVar()
            txtModelExhibiton.set("Model Exhibiton")       
            conn2 = sqlite3.connect('eventsdatabase.db')
            print("Open Database Successfully for cultural events")
            cursor2 = conn2.cursor()
            insertcommand2 = "INSERT OR IGNORE INTO EVENTS VALUES (NULL, ?, ?, ?)"
            cursor2.execute(insertcommand2,(username.get(),txtModelExhibiton.get(),'350' ))
            print("Records inserted successfully")
            conn2.commit()

    
    #------------------------------------------------------------------------------#
    #imageback
    imageback = Image.open("backlogo.png")
    imageback = imageback.resize((18, 18), Image.ANTIALIAS) 
    photoback = ImageTk.PhotoImage(imageback)
    back0 = Button(windowtechnical, image=photoback, borderwidth=0, bg="#23232F",command=back) # button with image binded to the same function 
    back0.grid(row=0)
    back0.place( x=10, y=6)
    
    #imageclose
    image1 = Image.open("close.png")
    image1 = image1.resize((18, 18), Image.ANTIALIAS)
    photo1 = ImageTk.PhotoImage(image1)
    close = Button(windowtechnical, image=photo1, borderwidth=0, bg="#23232F", command=on_close) # button with image binded to the same function
    close.grid(row=0)
    close.place( x=470, y=6)

    #imagemin
    image2 = Image.open("min1.png")
    image2 = image2.resize((18, 18), Image.ANTIALIAS)
    photo2 = ImageTk.PhotoImage(image2)
    min1 = Button(windowtechnical, image=photo2,  borderwidth=0, bg="#23232F", command=on_minimize) # button with image binded to the same function
    min1.grid(row=0)
    min1.place( x=450, y=6)
    #------------------------------------------------------------------------------------
    
    font1 = font.Font(family='Haettenschweiler', size=14)
    image0 = Image.open("Technical_event_main.png")
    image0 = image0.resize((180, 70), Image.ANTIALIAS)
    photo0 = ImageTk.PhotoImage(image0)
    Title=Label(windowtechnical, image=photo0,  borderwidth=0, bg="#2B2B37" ,width=200,padx=70,pady=70)
    Title.place(x=193,y=40)
    events=Label(windowtechnical,text="Events",font=font1,bg="#2B2B37",fg="#f64747")
    events.place(x=350,y=105)

    font1 = font.Font(family='Haettenschweiler', size=14)
    image3 = Image.open("technical.png")
    image3 = image3.resize((60, 60), Image.ANTIALIAS)
    photo3 = ImageTk.PhotoImage(image3)
    Title=Label(windowtechnical, image=photo3,  borderwidth=0, bg="#2B2B37" ,width=100,padx=70,pady=70)
    Title.place(x=106,y=40)

    image4 = Image.open("Technical_PaperPresentation.png")
    image4 = image4.resize((50, 50), Image.ANTIALIAS)
    photo4 = ImageTk.PhotoImage(image4)
    cultural_music=Label(windowtechnical, image=photo4,  borderwidth=0, bg="#2B2B37" ,width=100,padx=70,pady=70)
    cultural_music.place(x=30,y=140)
    cultural_paper_Button=Button(windowtechnical,text="Paper Presentation",font=font1,borderwidth=0, bg="#2B2B37",fg="#f64747",command=onClickPaperPresentation)
    cultural_paper_Button.place(x=107,y=155)

    image5 = Image.open("Technical_Quiz.png")
    image5 = image5.resize((50, 50), Image.ANTIALIAS)
    photo5 = ImageTk.PhotoImage(image5)
    cultural_drama_Label=Label(windowtechnical, image=photo5,  borderwidth=0, bg="#2B2B37" ,width=100,padx=70,pady=70)
    cultural_drama_Label.place(x=30,y=230)
    cultural_quiz_button=Button(windowtechnical,text="Technical Quiz",font=font1,borderwidth=0, bg="#2B2B37",fg="#f64747",command=onClickTechnicalQuiz)
    cultural_quiz_button.place(x=115,y=240)

    image6 = Image.open("Technical_Blind.png")
    image6 = image6.resize((50, 50), Image.ANTIALIAS)
    photo6 = ImageTk.PhotoImage(image6)
    cultural_fashion_Label=Label(windowtechnical, image=photo6,  borderwidth=0, bg="#2B2B37" ,width=100,padx=70,pady=70)
    cultural_fashion_Label.place(x=30,y=320)
    cultural_blind_button=Button(windowtechnical,text="Blind Coding",font=font1,borderwidth=0, bg="#2B2B37",fg="#f64747",command=onClickBlindCoding)
    cultural_blind_button.place(x=110,y=330)

    image7 = Image.open("Technical_FindTheError.png")
    image7 = image7.resize((50, 50), Image.ANTIALIAS)
    photo7 = ImageTk.PhotoImage(image7)
    cultural_singing_Label=Label(windowtechnical, image=photo7,  borderwidth=0, bg="#2B2B37" ,width=100,padx=70,pady=70)
    cultural_singing_Label.place(x=260,y=140)
    cultural_code_button=Button(windowtechnical,text="Code Debugging",font=font1,borderwidth=0, bg="#2B2B37",fg="#f64747",command=onClickCodeDebugging)
    cultural_code_button.place(x=348,y=155)

    image8 = Image.open("Tecnical_RoboWar.png")
    image8 = image8.resize((50, 50), Image.ANTIALIAS)
    photo8 = ImageTk.PhotoImage(image8)
    cultural_fashion_Label=Label(windowtechnical, image=photo8,  borderwidth=0, bg="#2B2B37" ,width=100,padx=70,pady=70)
    cultural_fashion_Label.place(x=265,y=320)
    cultural_robo_button=Button(windowtechnical,text="Robo War",font=font1,borderwidth=0, bg="#2B2B37",fg="#f64747",command=onClickRoboWar)
    cultural_robo_button.place(x=358,y=330)

    image9 = Image.open("Technical_Exhibitions_option.png")
    image9 = image9.resize((60, 60), Image.ANTIALIAS)
    photo9 = ImageTk.PhotoImage(image9)
    cultural_mime_Label=Label(windowtechnical, image=photo9,  borderwidth=0, bg="#2B2B37" ,width=100,padx=70,pady=70)
    cultural_mime_Label.place(x=260,y=230)
    cultural_model_button=Button(windowtechnical,text="Model Exhibiton",font=font1,borderwidth=0, bg="#2B2B37",fg="#f64747",command=onClickModelExhibiton)
    cultural_model_button.place(x=355,y=240)


   
    windowtechnical.mainloop()


    
                        
def USERS():
    global rootnew
    window.withdraw()
    rootnew = Toplevel()
    width=1000
    height=620
    screen_width = rootnew.winfo_screenwidth()
    screen_height = rootnew.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    rootnew.geometry("%dx%d+%d+%d" % (width, height, x, y))
    rootnew.overrideredirect(True)
    rootnew.resizable(0, 0)
    topFrame = Frame(rootnew, width=1200, height=30, bg="#23232F")
    bottomFrame = Frame(rootnew, width=1200, height=590, bg="#2B2B37")
    topFrame.grid(row=0)
    bottomFrame.grid(row=1)

    class WindowDraggableUser():

        def __init__(self, Frame):
            self.topFrame = topFrame
            topFrame.bind('<ButtonPress-1>', self.StartMove)
            topFrame.bind('<ButtonRelease-1>', self.StopMove)
            topFrame.bind('<B1-Motion>', self.OnMotion)

        def StartMove(self, event):
            self.x = event.x
            self.y = event.y

        def StopMove(self, event):
            self.x = None
            self.y = None
        
        def OnMotion(self,event):
            x = (event.x_root - self.x - self.topFrame.winfo_rootx() + self.topFrame.winfo_rootx())
            y = (event.y_root - self.y - self.topFrame.winfo_rooty() + self.topFrame.winfo_rooty())
            rootnew.geometry("+%s+%s" % (x, y))

    WindowDraggableUser(topFrame)
    #-----------------------------------------------------------------------------#
    #minimizebutton
    def on_back(event=None):
        rootnew.destroy()
        window.deiconify()
        
    def on_close(event=None):
        rootnew.destroy()

    def frame_mapped(event=None):
        rootnew.update_idletasks()
        rootnew.overrideredirect(True)
        rootnew.state('normal')
    topFrame.bind("<Map>",frame_mapped)

    def on_minimize(event=None):
        rootnew.update_idletasks()
        rootnew.overrideredirect(False)
        rootnew.state('iconic')
        
    def onclickProceed():
        rootnew.withdraw()
        global winrules
        winrules = Toplevel()
        width=770
        height=560
        screen_width = winrules.winfo_screenwidth()
        screen_height = winrules.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        winrules.geometry("%dx%d+%d+%d" % (width, height, x, y))
        winrules.overrideredirect(True)
        winrules.resizable(0, 0)
        topFrame = Frame(winrules, width=770, height=30, bg="#23232F")
        bottomFrame = Frame(winrules, width=770, height=570, bg="#2B2B37")
        topFrame.grid(row=0)
        bottomFrame.grid(row=1)
        class WindowDraggableRules():
            def __init__(self, Frame):
                self.topFrame = topFrame
                topFrame.bind('<ButtonPress-1>', self.StartMove)
                topFrame.bind('<ButtonRelease-1>', self.StopMove)
                topFrame.bind('<B1-Motion>', self.OnMotion)

            def StartMove(self, event):
                self.x = event.x
                self.y = event.y

            def StopMove(self, event):
                self.x = None
                self.y = None
        
            def OnMotion(self,event):
                x = (event.x_root - self.x - self.topFrame.winfo_rootx() + self.topFrame.winfo_rootx())
                y = (event.y_root - self.y - self.topFrame.winfo_rooty() + self.topFrame.winfo_rooty())
                winrules.geometry("+%s+%s" % (x, y))


        WindowDraggableRules(topFrame)
        def onback(event=None):
            winrules.destroy()
            rootnew.deiconify()
        
        def on_close(event=None):
            winrules.destroy()

        def frame_mapped(event=None):
            winrules.update_idletasks()
            winrules.overrideredirect(True)
            winrules.state('normal')
        topFrame.bind("<Map>",frame_mapped)

        def on_minimize(event=None):
            winrules.update_idletasks()
            winrules.overrideredirect(False)
            winrules.state('iconic')
        #imageback
        image1 = Image.open("backlogo.png")
        image1 = image1.resize((18, 18), Image.ANTIALIAS) 
        photo1 = ImageTk.PhotoImage(image1)
        back1 = Button(winrules, image=photo1, borderwidth=0, bg="#23232F",command=onback) # button with image binded to the same function 
        back1.grid(row=0)
        back1.place( x=10, y=6)
        #imageclose
        image2 = Image.open("close.png")
        image2 = image2.resize((18, 18), Image.ANTIALIAS)
        photo2 = ImageTk.PhotoImage(image2)
        close = Button(winrules, image=photo2, borderwidth=0, bg="#23232F", command=on_close) # button with image binded to the same function
        close.grid(row=0)
        close.place( x=744, y=6)
        #imagemin
        image3 = Image.open("min1.png")
        image3 = image3.resize((18, 18), Image.ANTIALIAS)
        photo3 = ImageTk.PhotoImage(image3)
        min1 = Button(winrules, image=photo3,  borderwidth=0, bg="#23232F", command=on_minimize) # button with image binded to the same function
        min1.grid(row=0)
        min1.place( x=722, y=6)
        #heading
        image0 = Image.open("Rules and regulations.png")
        image0 = image0.resize((275, 50), Image.ANTIALIAS)
        photo0 = ImageTk.PhotoImage(image0)
        Title=Label(winrules, image=photo0,  borderwidth=0, bg="#2B2B37" ,width=500,padx=30,pady=70)
        Title.place(x=150,y=40)
        helv3634 = font.Font(family='Helvetica', size=13, weight='bold')
        fontlatest = font.Font(family='Bookman Old Style', size=11, weight='bold')
        Rules=Label(winrules,text='\n✨ TECHNICAL FEST OR EVENT ✨'
                          '\n'
                          '\n■ Participants need to carry their identity card.'
                          '\n■ No cheating should be done.Mobile Phones are not allowed.'
                          '\n■ Winner will be declared as per the new innovation.'
                          '\n■ Decision of Judges will be final.'

                         '\n\n✨ CULTURAL FEST OR EVENT ✨\n'
                          '\n■ Participants will be disqualified for disobeying the rules. '
                          '\n■ No vulgar comedy,play,words should be told.'
                         '\n■ Marks awarded on the basis of content, presentation, language.'
                         '\n■ Judgment will be on the basis of content, creativity & catchy lines.'
  
                        '\n\n✨ SPORTS FEST OR EVENT ✨\n'
                        '\n■ Players must have their identity cards.'
                        '\n■ Only individual participation is allowed for cricket and football 11 players are allowed. '
                        '\n■ The players should get their racquets and kit for rest of the game.\n'
        ,bg="#23232F",fg="#f64747",font=helv3634)
        Rules.place(x=50,y=100)
        def decline():
            winaccept.withdraw()
            window.deiconify()
        def verified():
            winaccept.withdraw()
            global winproceed
            winproceed = Toplevel()
            width=1000
            height=620
            screen_width = winproceed.winfo_screenwidth()
            screen_height = winproceed.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            winproceed.geometry("%dx%d+%d+%d" % (width, height, x, y))
            winproceed.overrideredirect(True)
            winproceed.resizable(0, 0)
            topFrame = Frame(winproceed, width=1000, height=30, bg="#23232F")
            bottomFrame = Frame(winproceed, width=1000, height=590, bg="#2B2B37")
            topFrame.grid(row=0)
            bottomFrame.grid(row=1)

            if username.get() != "":
                conn = sqlite3.connect("eventsdatabase.db")
                print("Connection Established Successfully in search method in events table")
                cursor = conn.cursor() 
                cursor.execute("SELECT * FROM `EVENTS` WHERE `username` LIKE ? OR `event` LIKE ?", ('%'+str(username.get())+'%', '%'+str(username.get())+'%'))
                fetchnewevent = cursor.fetchall()
                if fetchnewevent:   
                    mlb = MultiListbox(winproceed,(('EID',5),('USERNAME',20),('EVENT',23),('COST',23)))
                    mlb.not_focus()
                    mlb.place(x=1, y=150, width=1000, height=466)
        
                    mlb.delete(0,END)
                    for row in fetchnewevent:
                        print("Successfully inserted data into eventsinfotable")
                        mlb.insert(END, (int (row[0]), row[1], row[2], row[3]))
                        mlb.selection_set(0)
                else:
                    ms.showerror('OOPS','No Events Selected!')

                    
            class WindowDraggableEvents():

                def __init__(self, Frame):
                    self.topFrame = topFrame
                    topFrame.bind('<ButtonPress-1>', self.StartMove)
                    topFrame.bind('<ButtonRelease-1>', self.StopMove)
                    topFrame.bind('<B1-Motion>', self.OnMotion)

                def StartMove(self, event):
                    self.x = event.x
                    self.y = event.y

                def StopMove(self, event):
                    self.x = None
                    self.y = None
        
                def OnMotion(self,event):
                    x = (event.x_root - self.x - self.topFrame.winfo_rootx() + self.topFrame.winfo_rootx())
                    y = (event.y_root - self.y - self.topFrame.winfo_rooty() + self.topFrame.winfo_rooty())
                    winproceed.geometry("+%s+%s" % (x, y))

            WindowDraggableEvents(topFrame)

            def onbackevents(event=None):
                winproceed.destroy()
                rootnew.deiconify()
        
            def oncloseevents(event=None):
                winproceed.destroy()

            def frame_mapped(event=None):
                winproceed.update_idletasks()
                winproceed.overrideredirect(True)
                winproceed.state('normal')
            topFrame.bind("<Map>",frame_mapped)

            def onminimizeevents(event=None):
                winproceed.update_idletasks()
                winproceed.overrideredirect(False)
                winproceed.state('iconic')

            def viewdataevents():
                if username.get() != "":
                    conn = sqlite3.connect("eventsdatabase.db")
                    print("Connection Established Successfully in search method in events table")
                    cursor = conn.cursor() 
                    cursor.execute("SELECT * FROM `EVENTS` WHERE `username` LIKE ? OR `event` LIKE ?", ('%'+str(username.get())+'%', '%'+str(username.get())+'%'))
                    fetchnew12 = cursor.fetchall()
                    mlb.delete(0,END)
                    for row in fetchnew12:
                        mlb.insert(END,row)

            def deleteevents():
                sqlfile.deleteeventseid(mlb.item_selected[1])
                mlb.delete(0,END)

            
            
        
    
            #-----------------------------------------------------------------------------------------------------------------------------  
                
        
        
            #imageback
            imagenew = Image.open("backlogo.png")
            imagenew= imagenew.resize((18, 18), Image.ANTIALIAS) 
            photonew = ImageTk.PhotoImage(imagenew)
            backnew = Button(topFrame, image=photonew, borderwidth=0, bg="#23232F", command=onbackevents) # button with image binded to the same function 
            backnew.grid(row=0)
            backnew.place( x=10, y=6)
            #imageclose
            image1 = Image.open("close.png")
            image1 = image1.resize((18, 18), Image.ANTIALIAS)
            photo1 = ImageTk.PhotoImage(image1)
            close = Button(topFrame, image=photo1, borderwidth=0, bg="#23232F", command=oncloseevents) # button with image binded to the same function
            close.grid(row=0)
            close.place( x=970, y=6)
            #imagemin
            image2 = Image.open("min1.png")
            image2 = image2.resize((18, 18), Image.ANTIALIAS)
            photo2 = ImageTk.PhotoImage(image2)
            min1 = Button(topFrame, image=photo2,  borderwidth=0, bg="#23232F", command=onminimizeevents)
            min1.grid(row=0)
            min1.place( x=950, y=6)
            #imagedelete
            image4 = Image.open("delete.png")
            image4 = image4.resize((22, 22), Image.ANTIALIAS) 
            photo4 = ImageTk.PhotoImage(image4)
            delete = Button(bottomFrame, image=photo4, borderwidth=0, bg="#2B2B37", command=deleteevents) # button with image binded to the same function 
            delete.grid(row=0)
            delete.place( x=10, y=85)
            #imagerefresh
            image5 = Image.open("refresh.png")
            image5 = image5.resize((25, 25), Image.ANTIALIAS) 
            photo5 = ImageTk.PhotoImage(image5)
            refresh = Button(bottomFrame, image=photo5, borderwidth=0, bg="#2B2B37", command=viewdataevents) # button with image binded to the same function 
            refresh.grid(row=0)
            refresh.place( x=44, y=85)
        
            Events_Module = Image.open("Events_module.png")
            Events_Module = Events_Module.resize((420, 50), Image.ANTIALIAS) 
            Events_Module_photo = ImageTk.PhotoImage(Events_Module)
            font5 = font.Font(family='Helvetica', size=22, weight='bold')
            labelevents = Label(winproceed,image=Events_Module_photo,bg="#2B2B37", fg="#f64747")
            labelevents.place(x=330,y=50)

            winproceed.mainloop()
        def nextwin():
            winrules.withdraw()
            global winaccept
            winaccept = Toplevel()
            width=300
            height=200
            screen_width = winaccept.winfo_screenwidth()
            screen_height = winaccept.winfo_screenheight()
            x = (screen_width/2) - (width/2)
            y = (screen_height/2) - (height/2)
            winaccept.geometry("%dx%d+%d+%d" % (width, height, x, y))
            winaccept.overrideredirect(True)
            winaccept.resizable(0, 0)
            topFrame = Frame(winaccept, width=300, height=30, bg="#23232F")
            bottomFrame = Frame(winaccept, width=300, height=170, bg="#2B2B37")
            topFrame.grid(row=0)
            bottomFrame.grid(row=1)
    
            def onbackaccept(event=None):
                winaccept.destroy()
                winrules.deiconify()
        
            def oncloseaccept(event=None):
                winaccept.destroy()

            def frame_mapped(event=None):
                winaccept.update_idletasks()
                winaccept.overrideredirect(True)
                winaccept.state('normal')
            topFrame.bind("<Map>",frame_mapped)

            def onminimizeaccept(event=None):
                winaccept.update_idletasks()
                winaccept.overrideredirect(False)
                winaccept.state('iconic')
            #imageback
            image1 = Image.open("backlogo.png")
            image1 = image1.resize((18, 18), Image.ANTIALIAS) 
            photo1 = ImageTk.PhotoImage(image1)
            back1 = Button(winaccept, image=photo1, borderwidth=0, bg="#23232F",command=onbackaccept) # button with image binded to the same function 
            back1.grid(row=0)
            back1.place( x=10, y=6)
            #imageclose
            image2 = Image.open("close.png")
            image2 = image2.resize((18, 18), Image.ANTIALIAS)
            photo2 = ImageTk.PhotoImage(image2)
            close = Button(winaccept, image=photo2, borderwidth=0, bg="#23232F", command=oncloseaccept) # button with image binded to the same function
            close.grid(row=0)
            close.place( x=270, y=6)
            #imagemin
            image3 = Image.open("min1.png")
            image3 = image3.resize((18, 18), Image.ANTIALIAS)
            photo3 = ImageTk.PhotoImage(image3)
            min1 = Button(winaccept, image=photo3,  borderwidth=0, bg="#23232F", command=onminimizeaccept) # button with image binded to the same function
            min1.grid(row=0)
            min1.place( x=250, y=6)

            helv36 = font.Font(family='Helvetica', size=13, weight='bold')
            image4 = Image.open("accept.png")
            image4 = image4.resize((13, 13), Image.ANTIALIAS)
            photo4 = ImageTk.PhotoImage(image4)
            image5 = Image.open("decline.png")
            image5 = image5.resize((13, 13), Image.ANTIALIAS)
            photo5 = ImageTk.PhotoImage(image5)
            btnaccept = Button(winaccept, text=" Accept" , image=photo4, compound=LEFT,font=helv36, bg="#2B2B37", fg="#f64747",command=verified)
            btnaccept.place(x=30,y=100,width=100,height=40)
            btndecline = Button(winaccept, text=" Decline", image=photo5, compound=LEFT, font=helv36, bg="#2B2B37", fg="#f64747",command=decline)
            btndecline.place(x=180,y=100,width=100,height=40)
            class WindowDraggableAccept():

                def __init__(self, Frame):
                    self.topFrame = topFrame
                    topFrame.bind('<ButtonPress-1>', self.StartMove)
                    topFrame.bind('<ButtonRelease-1>', self.StopMove)
                    topFrame.bind('<B1-Motion>', self.OnMotion)

                def StartMove(self, event):
                    self.x = event.x
                    self.y = event.y

                def StopMove(self, event):
                    self.x = None
                    self.y = None
        
                def OnMotion(self,event):
                    x = (event.x_root - self.x - self.topFrame.winfo_rootx() + self.topFrame.winfo_rootx())
                    y = (event.y_root - self.y - self.topFrame.winfo_rooty() + self.topFrame.winfo_rooty())
                    winaccept.geometry("+%s+%s" % (x, y))

            WindowDraggableAccept(topFrame)
            winaccept.mainloop()


        def accept():
            if var.get() == 1:
                Proceedbtn.configure(state=NORMAL)
                Proceedbtn.configure(command=nextwin)
        
            else:
                Proceedbtn.configure(state=DISABLED)

        
        var = IntVar()
        helv363 = font.Font(family='Helvetica', size=13, weight='bold')
        helv3633 = font.Font(family='Helvetica', size=13, weight='bold')
        proceed_check = Checkbutton (winrules,text = ' Yes, I Accept the Above Terms and Conditions. ',variable=var,font=helv3633,bg="#23232F",activebackground="#23232F",activeforeground="#f64747",fg="#f64747",state = ACTIVE,command=accept)
        proceed_check.place(x=50,y=510)
        Proceedbtn=Button(winrules,text="NEXT",bg="#23232F",fg="#f64747",state=DISABLED,font=helv363,pady=0.1)
        Proceedbtn.place(x=627,y=515,width=80)
        winrules.mainloop()

    def onclickEventsInfo():
        rootnew.withdraw()
        global wineventsinfo
        wineventsinfo = Toplevel()
        width=1000
        height=620
        screen_width = wineventsinfo.winfo_screenwidth()
        screen_height = wineventsinfo.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        wineventsinfo.geometry("%dx%d+%d+%d" % (width, height, x, y))
        wineventsinfo.overrideredirect(True)
        wineventsinfo.resizable(0, 0)
        topFrame = Frame(wineventsinfo, width=1000, height=30, bg="#23232F")
        bottomFrame = Frame(wineventsinfo, width=1000, height=590, bg="#2B2B37")
        topFrame.grid(row=0)
        bottomFrame.grid(row=1)
        class WindowDraggableEventsInfo():

                def __init__(self, Frame):
                    self.topFrame = topFrame
                    topFrame.bind('<ButtonPress-1>', self.StartMove)
                    topFrame.bind('<ButtonRelease-1>', self.StopMove)
                    topFrame.bind('<B1-Motion>', self.OnMotion)

                def StartMove(self, event):
                    self.x = event.x
                    self.y = event.y

                def StopMove(self, event):
                    self.x = None
                    self.y = None
        
                def OnMotion(self,event):
                    x = (event.x_root - self.x - self.topFrame.winfo_rootx() + self.topFrame.winfo_rootx())
                    y = (event.y_root - self.y - self.topFrame.winfo_rooty() + self.topFrame.winfo_rooty())
                    winproceed.geometry("+%s+%s" % (x, y))
                    
        WindowDraggableEventsInfo(topFrame)
        def onbackeventsinfo(event=None):
            wineventsinfo.destroy()
            rootnew.deiconify()

                
        def oncloseeventsinfo(event=None):
            wineventsinfo.destroy()

        def frame_mapped(event=None):
            wineventsinfo.update_idletasks()
            wineventsinfo.overrideredirect(True)
            wineventsinfo.state('normal')
        topFrame.bind("<Map>",frame_mapped)

        def onminimizeeventsinfo(event=None):
            wineventsinfo.update_idletasks()
            wineventsinfo.overrideredirect(False)
            wineventsinfo.state('iconic')

        def viewdataeventsinfo():
            if username.get() != "":
                conn = sqlite3.connect("eventsdatabase.db")
                print("Connection Established Successfully in search method in events table")
                cursor = conn.cursor() 
                cursor.execute("SELECT * FROM `EVENTS` WHERE `username` LIKE ? OR `event` LIKE ?", ('%'+str(username.get())+'%', '%'+str(username.get())+'%'))
                fetchnew1 = cursor.fetchall()
                mlb.delete(0,END)
                for row in fetchnew1:
                    mlb.insert(END,row)

        def deleteeventsinfo():
            sqlfile.deleteeventseidinfo(mlb.item_selected[1])
            mlb.delete(0,END)
        
        if username.get() != "":
            conn = sqlite3.connect("eventsdatabase.db")
            print("Connection Established Successfully in search method in events table")
            cursor = conn.cursor() 
            cursor.execute("SELECT * FROM `EVENTS` WHERE `username` LIKE ? OR `event` LIKE ?", ('%'+str(username.get())+'%', '%'+str(username.get())+'%'))
            fetchnew = cursor.fetchall()
            if fetchnew:   
                mlb = MultiListbox(wineventsinfo,(('EID',5),('USERNAME',20),('EVENT',23),('COST',23)))
                mlb.not_focus()
                mlb.place(x=1, y=150, width=1000, height=466)
        
                mlb.delete(0,END)
                for row in fetchnew:
                    print("Successfully inserted data into eventsinfotable")
                    mlb.insert(END, (int (row[0]), row[1], row[2], row[3]))
                    mlb.selection_set(0)
            else:
                ms.showerror('OOPS','No Events Selected!')


        #imageeventsheading
        Events_Module = Image.open("Events_module.png")
        Events_Module = Events_Module.resize((420, 50), Image.ANTIALIAS) 
        Events_Module_photo = ImageTk.PhotoImage(Events_Module)
        font5 = font.Font(family='Helvetica', size=22, weight='bold')
        labelevents = Label(wineventsinfo,image=Events_Module_photo,bg="#2B2B37", fg="#f64747")
        labelevents.place(x=330,y=50)
        #imageback
        imagenew = Image.open("backlogo.png")
        imagenew= imagenew.resize((18, 18), Image.ANTIALIAS) 
        photonew = ImageTk.PhotoImage(imagenew)
        backnew = Button(topFrame, image=photonew, borderwidth=0, bg="#23232F", command=onbackeventsinfo) # button with image binded to the same function 
        backnew.grid(row=0)
        backnew.place( x=10, y=6)
        #imageclose
        image1 = Image.open("close.png")
        image1 = image1.resize((18, 18), Image.ANTIALIAS)
        photo1 = ImageTk.PhotoImage(image1)
        close = Button(topFrame, image=photo1, borderwidth=0, bg="#23232F", command=oncloseeventsinfo) # button with image binded to the same function
        close.grid(row=0)
        close.place( x=970, y=6)
        #imagemin
        image2 = Image.open("min1.png")
        image2 = image2.resize((18, 18), Image.ANTIALIAS)
        photo2 = ImageTk.PhotoImage(image2)
        min1 = Button(topFrame, image=photo2,  borderwidth=0, bg="#23232F", command=onminimizeeventsinfo)
        min1.grid(row=0)
        min1.place( x=950, y=6)
        #imagedelete
        image4 = Image.open("delete.png")
        image4 = image4.resize((22, 22), Image.ANTIALIAS) 
        photo4 = ImageTk.PhotoImage(image4)
        delete = Button(bottomFrame, image=photo4, borderwidth=0, bg="#2B2B37", command=deleteeventsinfo) # button with image binded to the same function 
        delete.grid(row=0)
        delete.place( x=10, y=85)
        #imagerefresh
        image5 = Image.open("refresh.png")
        image5 = image5.resize((25, 25), Image.ANTIALIAS) 
        photo5 = ImageTk.PhotoImage(image5)
        refresh = Button(bottomFrame, image=photo5, borderwidth=0, bg="#2B2B37", command=viewdataeventsinfo) # button with image binded to the same function 
        refresh.grid(row=0)
        refresh.place( x=44, y=85)

        wineventsinfo.mainloop()
      
    #------------------------------------------------------------------------------#
    #imageback
    image7 = Image.open("backlogo.png")
    image7 = image7.resize((18, 18), Image.ANTIALIAS) 
    photo7 = ImageTk.PhotoImage(image7)
    back7 = Button(topFrame, image=photo7, borderwidth=0, bg="#23232F", command=on_back) # button with image binded to the same function 
    back7.grid(row=0)
    back7.place( x=10, y=6)
    #imageclose
    image1 = Image.open("close.png")
    image1 = image1.resize((18, 18), Image.ANTIALIAS)
    photo1 = ImageTk.PhotoImage(image1)
    close = Button(rootnew, image=photo1, borderwidth=0, bg="#23232F", command=on_close) # button with image binded to the same function
    close.grid(row=0)
    close.place( x=970, y=6)

    #imagemin
    image2 = Image.open("min1.png")
    image2 = image2.resize((18, 18), Image.ANTIALIAS)
    photo2 = ImageTk.PhotoImage(image2)
    min1 = Button(rootnew, image=photo2,  borderwidth=0, bg="#23232F", command=on_minimize)
    min1.grid(row=0)
    min1.place( x=950, y=6)

    #TitleLabel
    image3 = Image.open("zodiac_f.png")
    image3 = image3.resize((200, 100), Image.ANTIALIAS)
    photo3 = ImageTk.PhotoImage(image3)
    font1 = font.Font(family='Haettenschweiler', size=14)
    font2 = font.Font(family='Haettenschweiler', size=20)
    Title=Label(rootnew, image=photo3,  borderwidth=0, bg="#23232F" ,width=200,padx=70,pady=70)
    Title.place(x=390,y=40)
    events=Label(rootnew,text="events",font=font1,bg="#2B2B37",fg="#f64747")
    events.place(x=540,y=125)
    #dance
    image4 = Image.open("danceicon.png")
    image4 = image4.resize((250, 250), Image.ANTIALIAS)
    photo4 = ImageTk.PhotoImage(image4)
    dance=Button(rootnew, image=photo4,  borderwidth=0, bg="#23232F" ,width=300,height=310,padx=70,pady=70,command=CULTURAL)
    dance.place(x=20,y=200)

    events_cultural=Label(rootnew,text="CULTURAL",font=font1,bg="#23232F",fg="#f64747")
    events_cultural.place(x=255,y=480)

    #sports
    image5 = Image.open("sportsicon.png")
    image5 = image5.resize((252, 252), Image.ANTIALIAS)
    photo5 = ImageTk.PhotoImage(image5)
    dance=Button(rootnew, image=photo5,  borderwidth=0,bg="#23232F" ,width=300,height=310,padx=70,pady=70,command=SPORTS)
    dance.place(x=350,y=200)
    events_sports=Label(rootnew,text="SPORTS",font=font1,bg="#23232F",fg="#f64747")
    events_sports.place(x=595,y=480)

    #technical
    image6 = Image.open("technicalicon.png")
    image6 = image6.resize((250, 250), Image.ANTIALIAS)
    photo6 = ImageTk.PhotoImage(image6)
    dance=Button(rootnew, image=photo6,  borderwidth=0, bg="#23232F" ,width=300,height=310,padx=70,pady=70,command=TECHNICAL)
    dance.place(x=680,y=200)

    events_tech=Label(rootnew,text="TECHNICAL",font=font1,bg="#23232F",fg="#f64747")
    events_tech.place(x=912,y=480)
    global btnproceednew
    proceed_button = Image.open("proceed_events.png")
    proceed_button = proceed_button.resize((60, 60), Image.ANTIALIAS)
    proceed_button_photo = ImageTk.PhotoImage(proceed_button)
    btnproceednew = Button(rootnew,borderwidth=0,image=proceed_button_photo,text="Proceed", state=DISABLED, compound=LEFT,font=font2, bg="#2B2B37",fg="#f64747", command=onclickProceed)
    btnproceednew.place(x=560,y=540)

    information_button = Image.open("information_events.png")
    information_button = information_button.resize((60, 60), Image.ANTIALIAS)
    information_button_photo = ImageTk.PhotoImage(information_button)
    btnviewevents = Button(rootnew,image=information_button_photo,text="  Information",compound=LEFT,font=font2,borderwidth=0,fg="#f64747", bg="#2B2B37", command=onclickEventsInfo)
    btnviewevents.place(x=300,y=540)

    def logouteventsinfo(event=None):
        rootnew.destroy()
        window.deiconify()
        username.delete(0, 'end')
        password.delete(0, 'end')

    logout_button = Image.open("logout.png")
    logout_button = logout_button.resize((30, 30), Image.ANTIALIAS)
    logout_button_photo = ImageTk.PhotoImage(logout_button)
    logoutbtn = Button(rootnew,image=logout_button_photo,font=font2,borderwidth=0,fg="#f64747", bg="#2B2B37", command=logouteventsinfo)
    logoutbtn.place(x=945,y=40)
    
    rootnew.mainloop()

    
#Admin
def Admin():
    global eventswindow
    window.withdraw()
    eventswindow = Toplevel()
    width=1700
    height=720
    screen_width = eventswindow.winfo_screenwidth()
    screen_height = eventswindow.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    eventswindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    eventswindow.overrideredirect(True)
    eventswindow.resizable(0, 0)

    topFrame = Frame(eventswindow, width=1700, height=30, bg="#23232F")
    middleFrame = Frame(eventswindow, width=1700, height=70, bg="#2B2B37")    
    bottomFrame = Frame(eventswindow, width=1700, height=620, bg="#2B2B37")
    topFrame.grid(row=0)
    middleFrame.grid(row=1)
    bottomFrame.grid(row=2)
   


    conn1 = sqlite3.connect('userdatabase.db')
    print("Open Database Successfully 4th time in admin page ....")
    cursor1 = conn1.cursor()
    
    find_user1 = "SELECT * FROM USER "
    u1 = cursor1.execute(find_user1)
    
    f1 = u1.fetchall()
    print("Fetching of data is done 4th time in admin page...")

    if f1:
        mlb = MultiListbox(bottomFrame,(('ID',5),('FIRSTNAME',23),('LASTNAME',23),('USERNAME',23),('EMAILID',35),('YEAR',23),('BRANCH',23),('GENDER',23),('MOBILE NO.',23),('COLLEGE NAME',23),('SETPASS',23),('CONFIRMPASS',23)))
        mlb.not_focus()
        mlb.place(x=1, y=70, width=1700, height=530)
        mlb.delete(0,END)
        for row in f1:
            mlb.insert(END, (int (row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7],  row[8], row[9], row[10], row[11]))
            mlb.selection_set(0)
    else:
        ms.showinfo('OOPS!','Login Failed DUE VALUES NOT INSERTED!')
            
  



    class WindowDraggableAdmin():

        def __init__(self, Frame):
            self.topFrame = topFrame
            topFrame.bind('<ButtonPress-1>', self.StartMove)
            topFrame.bind('<ButtonRelease-1>', self.StopMove)
            topFrame.bind('<B1-Motion>', self.OnMotion)

        def StartMove(self, event):
            self.x = event.x
            self.y = event.y

        def StopMove(self, event):
            self.x = None
            self.y = None
        
        def OnMotion(self,event):
            x = (event.x_root - self.x - self.topFrame.winfo_rootx() + self.topFrame.winfo_rootx())
            y = (event.y_root - self.y - self.topFrame.winfo_rooty() + self.topFrame.winfo_rooty())
            eventswindow.geometry("+%s+%s" % (x, y))

    WindowDraggableAdmin(topFrame)
    #----------------------------------------------------------------------------------------------------------------------------   
    #minimizebutton
    def on_back(event=None):
        eventswindow.destroy()
        window.deiconify()
        
    def on_close(event=None):
        eventswindow.destroy()
    
    def on_minimize(event=None):
        eventswindow.update_idletasks()
        eventswindow.overrideredirect(False)
        eventswindow.state('iconic')
    
    def frame_mapped(event=None):
        eventswindow.update_idletasks()
        eventswindow.overrideredirect(True)
        eventswindow.state('normal')
    topFrame.bind("<Map>",frame_mapped)

    def viewdata():
        mlb.delete(0,END)
        for row in sqlfile.viewalldata():
            mlb.insert(END,row)

    def delete():
        sqlfile.delete(mlb.item_selected[1])
        mlb.delete(0,END)

    def on_entry_click_search(event):
        """function that gets called whenever entry is clicked"""
        if entrysearch.get() == 'Search Here':
           entrysearch.delete(0, "end") # delete all the text in the entry
           entrysearch.insert(0, '') #Insert blank for user input
    def on_focus_out_search(event):
        """function that gets called whenever entry is clicked"""
        if entrysearch.get() == '':
           entrysearch.insert(0, 'Search Here') #Insert blank for user input
           
    def search():
        if SEARCH.get() != "":
            conn = sqlite3.connect("userdatabase.db")
            print("Connection Established Successfully in search method")
            cursor = conn.cursor() 
            cursor.execute("SELECT * FROM `USER` WHERE `firstname` LIKE ? OR `lastname` LIKE ?", ('%'+str(SEARCH.get())+'%', '%'+str(SEARCH.get())+'%'))
            fetch = cursor.fetchall()
        
            mlb.delete(0,END)
            for row in fetch:
                mlb.insert(END,row)
            cursor.close()
            conn.close()

        
    
    #-----------------------------------------------------------------------------------------------------------------------------  
    #imageback
    image1 = Image.open("backlogo.png")
    image1 = image1.resize((18, 18), Image.ANTIALIAS) 
    photo1 = ImageTk.PhotoImage(image1)
    back = Button(topFrame, image=photo1, borderwidth=0, bg="#23232F", command=on_back) # button with image binded to the same function 
    back.grid(row=0)
    back.place( x=10, y=6)
    #imageclose
    image2 = Image.open("close.png")
    image2 = image2.resize((18, 18), Image.ANTIALIAS) 
    photo2 = ImageTk.PhotoImage(image2)
    close = Button(topFrame, image=photo2, borderwidth=0, bg="#23232F", command=on_close) # button with image binded to the same function 
    close.grid(row=0)
    close.place( x=1674, y=6)
    #imagemin
    image3 = Image.open("min1.png")
    image3 = image3.resize((18, 18), Image.ANTIALIAS) 
    photo3 = ImageTk.PhotoImage(image3)
    min1 = Button(topFrame, image=photo3,  borderwidth=0, bg="#23232F", command=on_minimize) # button with image binded to the same function 
    min1.grid(row=0)
    min1.place( x=1652, y=6)
    #imagedelete
    image4 = Image.open("delete.png")
    image4 = image4.resize((22, 22), Image.ANTIALIAS) 
    photo4 = ImageTk.PhotoImage(image4)
    delete = Button(bottomFrame, image=photo4, borderwidth=0, bg="#2B2B37", command=delete) # button with image binded to the same function 
    delete.grid(row=0)
    delete.place( x=10, y=30)
    #imagerefresh
    image5 = Image.open("refresh.png")
    image5 = image5.resize((25, 25), Image.ANTIALIAS) 
    photo5 = ImageTk.PhotoImage(image5)
    refresh = Button(bottomFrame, image=photo5, borderwidth=0, bg="#2B2B37", command=viewdata) # button with image binded to the same function 
    refresh.grid(row=0)
    refresh.place( x=44, y=30)
    #imagesearch
    image6 = Image.open("search.png")
    image6 = image6.resize((25, 25), Image.ANTIALIAS) 
    photo6 = ImageTk.PhotoImage(image6)
    searchbtn = Button(bottomFrame, image=photo6, borderwidth=0, bg="#2B2B37", command=search) # button with image binded to the same function 
    searchbtn.grid(row=0)
    searchbtn.place( x=1410, y=30)
    #imagetitle
    image7 = Image.open("Admin_Module.jpg")
    image7 = image7.resize((420, 50), Image.ANTIALIAS) 
    photo7 = ImageTk.PhotoImage(image7)
    TitleAdmin=Label(bottomFrame, image=photo7,  borderwidth=0, bg="#2B2B37" ,width=500, pady=20)
    TitleAdmin.place(x=630,y=1)
    #----------------------------------------------------------------------------------------------------------------------------

    #labels
    #font1 = font.Font(family='Helvetica', size=18, weight='bold')
    #label1 = Label(middleFrame, font=font1, text="WELCOME TO ADMIN MODULE", bg="#2B2B37", fg="#f64747")
    #label1.place(x=640, y=40)
    #----------------------------------------------------------------------------------------------------------#
    #buttons
    helv36 = font.Font(family='Helvetica', size=16, weight='bold')
    font2 = font.Font(family='Helvetica', size=10, weight='bold')

    SEARCH = StringVar()
    entrysearch = Entry(bottomFrame, font=font2, bg="#2B2B37", fg="grey", textvariable=SEARCH)
    entrysearch.insert(0, 'Search Here')
    entrysearch.bind('<FocusIn>', on_entry_click_search)
    entrysearch.bind('<FocusOut>', on_focus_out_search)
    entrysearch.place( x=1450, y=30, width=200, height=25)
    
    eventswindow.mainloop()

#SignUp
def SignUp():
    global root
    window.withdraw()
    root = Toplevel()
    width=440
    height=580
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.overrideredirect(True)
    root.resizable(0, 0)
    topFrame = Frame(root, width=440, height=30, bg="#23232F")
    bottomFrame = Frame(root, width=440, height=550, bg="#2B2B37")
    topFrame.grid(row=0)
    bottomFrame.grid(row=1)

    class SimpleApp(object):
        def __init__(self, master, filename, **kwargs):
            self.master = master
            self.filename = filename
            self.canvas = Canvas(master, width=230, height=230 ,bg="#2B2B37")
            self.canvas.pack()

            self.update = self.draw().__next__
            master.after(100, self.update)

        def draw(self):
            image = Image.open(self.filename)
            angle = 0
            while True:
                tkimage = ImageTk.PhotoImage(image.rotate(angle))
                canvas_obj = self.canvas.create_image(117, 70, image=tkimage)
                self.master.after_idle(self.update)
                yield
                self.canvas.delete(canvas_obj)
                angle += 0.5
                angle %= 360
    

    
    
    class WindowDraggableSignup():

        def __init__(self, Frame):
            self.topFrame = topFrame
            topFrame.bind('<ButtonPress-1>', self.StartMove)
            topFrame.bind('<ButtonRelease-1>', self.StopMove)
            topFrame.bind('<B1-Motion>', self.OnMotion)

        def StartMove(self, event):
            self.x = event.x
            self.y = event.y

        def StopMove(self, event):
            self.x = None
            self.y = None
        
        def OnMotion(self,event):
            x = (event.x_root - self.x - self.topFrame.winfo_rootx() + self.topFrame.winfo_rootx())
            y = (event.y_root - self.y - self.topFrame.winfo_rooty() + self.topFrame.winfo_rooty())
            root.geometry("+%s+%s" % (x, y))

    WindowDraggableSignup(topFrame)
    #----------------------------------------------------------------------------------------------------------------------------   
    #minimizebutton
    def on_close(event=None):
        root.destroy()
    
    def on_minimize(event=None):
        root.update_idletasks()
        root.overrideredirect(False)
        root.state('iconic')
    
    def frame_mapped(event=None):
        root.update_idletasks()
        root.overrideredirect(True)
        root.state('normal')
    topFrame.bind("<Map>",frame_mapped)

    def on_entry_click_fname(event):
        """function that gets called whenever entry is clicked"""
        if entryfname.get() == 'First Name':
           entryfname.delete(0, "end") # delete all the text in the entry
           entryfname.insert(0, '') #Insert blank for user input
    def on_focus_out_fname(event):
        """function that gets called whenever entry is clicked"""
        if entryfname.get() == '':
           entryfname.insert(0, 'First Name') #Insert blank for user input

       
    def on_entry_click_lname(event):
        if entrylname.get() == 'Last Name':
           entrylname.delete(0, "end") # delete all the text in the entry
           entrylname.insert(0, '') #Insert blank for user input
    def on_focus_out_lname(event):
        """function that gets called whenever entry is clicked"""
        if entrylname.get() == '':
           entrylname.insert(0, 'Last Name') #Insert blank for user input

       
    def on_entry_click_usname(event):
        if entryusname.get() == 'User Name':
           entryusname.delete(0, "end") # delete all the text in the entry
           entryusname.insert(0, '') #Insert blank for user input
    def on_focus_out_usname(event):
        """function that gets called whenever entry is clicked"""
        if entryusname.get() == '':
           entryusname.insert(0, 'User Name') #Insert blank for user input

    def on_entry_click_email(event):
        if entryemail.get() == 'Email id':
           entryemail.delete(0, "end") # delete all the text in the entry
           entryemail.insert(0, '') #Insert blank for user input
    def on_focus_out_email(event):
        """function that gets called whenever entry is clicked"""
        if entryemail.get() == '':
           entryemail.insert(0, 'Email id') #Insert blank for user input

    def on_entry_click_mobile(event):
        if entrymobile.get() == 'Mobile Number':
           entrymobile.delete(0, "end") # delete all the text in the entry
           entrymobile.insert(0, '') #Insert blank for user input
    def on_focus_out_mobile(event):
        """function that gets called whenever entry is clicked"""
        if entrymobile.get() == '':
           entrymobile.insert(0, 'Mobile Number') #Insert blank for user input
           

    def on_entry_click_setpass(event):
        if entrysetpass.get() == 'Set A Password':
           entrysetpass.delete(0, "end") # delete all the text in the entry
           entrysetpass.insert(0, '') #Insert blank for user input
    def on_focus_out_setpass(event):
        """function that gets called whenever entry is clicked"""
        if entrysetpass.get() == '':
           entrysetpass.insert(0, 'Set A Password') #Insert blank for user input

    def on_entry_click_confirmpass(event):
        if entryconfirmpass.get() == 'Confirm Password':
           entryconfirmpass.delete(0, "end") # delete all the text in the entry
           entryconfirmpass.insert(0, '') #Insert blank for user input
    def on_focus_out_confirmpass(event):
        """function that gets called whenever entry is clicked"""
        if entryconfirmpass.get() == '':
           entryconfirmpass.insert(0, 'Confirm Password') #Insert blank for user input
           
    def BackToLogin():
        root.destroy()
        window.deiconify()

    def getEmail():
        winddone.withdraw()
        print("Mail SENT")
        # Create the root message and fill in the from, to, and subject headers
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = 'Zodiac Registration Info'
        msgRoot['From'] = "zodiacrgitportal@gmail.com"
        msgRoot['To'] = emailid.get()
        msgRoot.preamble = 'This is a multi-part message in MIME format.'
        # Encapsulate the plain and HTML versions of the message body in an
        # 'alternative' part, so message agents can decide which they want to display.
        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)

        msgText = MIMEText('This is the alternative plain text message.')
        msgAlternative.attach(msgText)

        # We reference the image in the IMG SRC attribute by the ID we give it below
        msgText = MIMEText('<h1>KINDLY NOTE THE EVENTS INFO </h1><br><img src="cid:image1"><br>', 'html')
        msgAlternative.attach(msgText)

        # This example assumes the image is in the current directory
        fp = open('zodiacpass.jpg', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        # Define the image's ID as referenced above
        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        #Next, log in to the server
        server.login("zodiacrgitportal@gmail.com", "mctrgitzodiac@123")
        #Send the mail
        msg = "successfull!" 
        server.sendmail("zodiacrgitportal@gmail.com", emailid.get(), msgRoot.as_string())
        
        window.after(10,window.deiconify)
        
    def done():   
        global winddone
        winddone = Toplevel()
        width=230
        height=230
        screen_width = winddone.winfo_screenwidth()
        screen_height = winddone.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        winddone.geometry("%dx%d+%d+%d" % (width, height, x, y))
        winddone.overrideredirect(True)
        bottomFrame = Frame(winddone, width=230, height=230, bg="#2B2B37")
        bottomFrame.grid(row=1)
        font12 = font.Font(family='Haettenschweiler', size=25)
        fontemail = font.Font(family='Helvetica', size=13, weight="bold")
        image6 = Image.open("Done2.png")
        image6 = image6.resize((80, 80), Image.ANTIALIAS)
        photo6 = ImageTk.PhotoImage(image6)
        label6 = Label(winddone, image=photo6, borderwidth=0, bg="#2B2B37")
        label6.image = photo6
        label6.place(x=75, y=30)
        Label1 = Label(winddone, text="Registered", bg="#2B2B37", fg="#f64747", font=font12)
        Label1.place(x=55, y=115)
        email_button = Image.open("emailicon.png")
        email_button = email_button.resize((30, 30), Image.ANTIALIAS)
        email_photo = ImageTk.PhotoImage(email_button)
        btnemailme = Button(winddone,borderwidth=0,image=email_photo,text=" GET EMAIL",compound=LEFT,bg="#2B2B37", fg="#f64747", font=fontemail, command=getEmail)
        btnemailme.place(x=60,y=174)
        root.destroy()
        winddone.mainloop()
        

    def notdone():
        global windnotdone
        windnotdone = Toplevel()
        width=230
        height=230
        screen_width = windnotdone.winfo_screenwidth()
        screen_height = windnotdone.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        windnotdone.geometry("%dx%d+%d+%d" % (width, height, x, y))
        windnotdone.overrideredirect(True)
        bottomFrame = Frame(windnotdone, width=230, height=230, bg="#2B2B37")
        bottomFrame.grid(row=1)
        font13 = font.Font(family='Haettenschweiler', size=17)
        image6 = Image.open("Not Registered.png")
        image6 = image6.resize((60, 60), Image.ANTIALIAS)
        photo6 = ImageTk.PhotoImage(image6)
        label6 = Label(windnotdone, image=photo6, borderwidth=0, bg="#2B2B37" )
        label6.image = photo6
        label6.place(x=80, y=40)
        Label1 = Label(windnotdone, text=" ✗ \n Invalid \n  Information...", bg="#2B2B37", fg="#f64747", font=font13)
        Label1.place(x=62, y=120)
        root.withdraw()
        windnotdone.after(3000, windnotdone.destroy)
        root.after(4000, root.deiconify)
        windnotdone.mainloop()
       


    def Data():
        conn1 = sqlite3.connect('userdatabase.db')
        print("Open Database Successfully 2nd time")
        cursor1 = conn1.cursor()
    
        insert_command1 = "INSERT OR IGNORE INTO USER VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        c1 = cursor1.execute(insert_command1, (fname.get(),lname.get(),uname.get(),emailid.get(),years.get(),branch.get(),gendervar.get(),mobile.get(),college.get(),setpass.get(),confirmpass.get()))

        print("Records inserted successfully into user")
        conn1.commit()

        global rootsubmit
        rootsubmit = Toplevel()
        width=230
        height=230
        screen_width = rootsubmit.winfo_screenwidth()
        screen_height = rootsubmit.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        rootsubmit.geometry("%dx%d+%d+%d" % (width, height, x, y))
        rootsubmit.overrideredirect(True)
        app = SimpleApp(rootsubmit, 'check1.png')
        font14 = font.Font(family='Haettenschweiler', size=18)
        Label1=Label(rootsubmit,text="Checking Status......." ,bg="#2B2B37",fg="#f64747",font=font14)
        Label1.place(x=57,y=140)
        rootsubmit.after(2000, rootsubmit.destroy)
    
        if (setpass.get() == confirmpass.get() and fname.get()!="" and lname.get()!="" and uname.get()!="" and emailid.get()!="" and years.get()!="--Select Year--" and branch.get()!="--Select Branch--" and gendervar.get()!="" and mobile.get()!="" and college.get()!="--Select College--" and setpass.get()!=""and confirmpass.get()!=""):  
            done()
        else:
            notdone()

        rootsubmit.mainloop()



        
    #-----------------------------------------------------------------------------------------------------------------------------  
    #imageclose
    image1 = Image.open("close.png")
    image1 = image1.resize((18, 18), Image.ANTIALIAS) 
    photo1 = ImageTk.PhotoImage(image1)
    close = Button(root, image=photo1, borderwidth=0, bg="#23232F", command=on_close) # button with image binded to the same function 
    close.grid(row=0)
    close.place( x=410, y=6)
    #imagemin
    image2 = Image.open("min1.png")
    image2 = image2.resize((18, 18), Image.ANTIALIAS) 
    photo2 = ImageTk.PhotoImage(image2)
    min1 = Button(root, image=photo2,  borderwidth=0, bg="#23232F", command=on_minimize) # button with image binded to the same function 
    min1.grid(row=0)
    min1.place( x=390, y=6)
    #fnameicon
    image3 = Image.open("usericon.png")
    image3 = image3.resize((23, 23), Image.ANTIALIAS) 
    photo3 = ImageTk.PhotoImage(image3)
    label3 = Label(root, image=photo3,  borderwidth=0, bg="#2B2B37")
    label3.image = photo3 
    label3.place( x=26, y=108)
    #usericon
    image4 = Image.open("usericon.png")
    image4 = image4.resize((23, 23), Image.ANTIALIAS) 
    photo4 = ImageTk.PhotoImage(image4)
    label4 = Label(root, image=photo4,  borderwidth=0, bg="#2B2B37")
    label4.image = photo4 
    label4.place( x=26, y=148)
    #emailicon
    image5 = Image.open("emailicon.png")
    image5 = image5.resize((20, 20), Image.ANTIALIAS) 
    photo5 = ImageTk.PhotoImage(image5)
    label5 = Label(root, image=photo5,  borderwidth=0, bg="#2B2B37")
    label5.image = photo5
    label5.place( x=26, y=190)
    #maleicon
    image6 = Image.open("malelogo.png")
    image6 = image6.resize((23, 23), Image.ANTIALIAS) 
    photo6 = ImageTk.PhotoImage(image6)
    label6 = Label(root, image=photo6,  borderwidth=0, bg="#2B2B37")
    label6.image = photo6
    label6.place( x=150, y=284)
    #femaleicon
    image7 = Image.open("femalelogo.png")
    image7 = image7.resize((23, 23), Image.ANTIALIAS) 
    photo7 = ImageTk.PhotoImage(image7)
    label7 = Label(root, image=photo7,  borderwidth=0, bg="#2B2B37")
    label7.image = photo7
    label7.place( x=150, y=316)
    #setpassicon
    image8 = Image.open("passicon.png")
    image8 = image8.resize((19, 19), Image.ANTIALIAS) 
    photo8 = ImageTk.PhotoImage(image8)
    label8 = Label(root, image=photo8,  borderwidth=0, bg="#2B2B37")
    label8.image = photo8
    label8.place( x=26, y=391)
    #confirmpassicon
    image9 = Image.open("passicon.png")
    image9 = image9.resize((19, 19), Image.ANTIALIAS) 
    photo9 = ImageTk.PhotoImage(image9)
    label9 = Label(root, image=photo9,  borderwidth=0, bg="#2B2B37")
    label9.image = photo9
    label9.place( x=26, y=429)
    #imageback
    image10 = Image.open("backlogo.png")
    image10 = image10.resize((18, 18), Image.ANTIALIAS) 
    photo10 = ImageTk.PhotoImage(image10)
    back = Button(root, image=photo10, borderwidth=0, bg="#23232F", command=BackToLogin) # button with image binded to the same function 
    back.grid(row=0)
    back.place( x=10, y=6)
    #mobileicon
    image11 = Image.open("mobileicon.png")
    image11 = image11.resize((23, 23), Image.ANTIALIAS) 
    photo11 = ImageTk.PhotoImage(image11)
    label11 = Label(root, image=photo11,  borderwidth=0, bg="#2B2B37")
    label11.image = photo11
    label11.place( x=26, y=350)
    #----------------------------------------------------------------------------------------------------------------------------

    #labels
    font1 = font.Font(family='Helvetica', size=15, weight='bold')
    label1 = Label(root, font=font1, text="Sign Up For Free", bg="#2B2B37", fg="#f64747")
    label1.grid(row=1)
    label1.place(x=140, y=40)

    #----------------------------------------------------------------------------------------------------------------------------
    #entry for fname
    fname = StringVar()
    lname = StringVar()
    uname= StringVar()
    emailid = StringVar()
    mobile = StringVar()
    setpass = StringVar()
    confirmpass = StringVar()
    
    font2 = font.Font(family='Helvetica', size=10, weight='bold')
    entryfname = Entry(root, font=font2, bg="#2B2B37", fg="grey", textvariable=fname)
    entryfname.insert(0, 'First Name')
    entryfname.bind('<FocusIn>', on_entry_click_fname)
    entryfname.bind('<FocusOut>', on_focus_out_fname)
    entryfname.place( x=50, y=108, width=150, height=25)
    #entry for lname
    entrylname = Entry(root, font=font2, bg="#2B2B37",fg="grey", textvariable=lname)
    entrylname.insert(0, 'Last Name')
    entrylname.bind('<FocusIn>', on_entry_click_lname)
    entrylname.bind('<FocusOut>', on_focus_out_lname)
    entrylname.place( x=240, y=108, width=150, height=25)
    #entry for usname
    entryusname = Entry(root, font=font2, bg="#2B2B37",fg="grey", textvariable=uname)
    entryusname.insert(0, 'User Name')
    entryusname.bind('<FocusIn>', on_entry_click_usname)
    entryusname.bind('<FocusOut>', on_focus_out_usname)
    entryusname.place( x=50, y=148, width=340, height=25)
    #entry for emailid
    global entryemail
    entryemail = Entry(root, font=font2, bg="#2B2B37", fg="grey", textvariable=emailid)
    entryemail.insert(0, 'Email id')
    entryemail.bind('<FocusIn>', on_entry_click_email)
    entryemail.bind('<FocusOut>', on_focus_out_email)
    entryemail.place( x=50, y=188, width=340, height=25)

    #Year==List
    Year_List=["First Year","Second Year","Third Year","Last Year"]
    years = StringVar()
    years.set("--Select Year--")#(Year_List[0])
    Year_dropDown=OptionMenu(root,years,*Year_List)
    Year_dropDown.config(bg="#2B2B37",activebackground="#2B2B37",fg="grey" ,relief="sunken")
    Year_dropDown.place(x=50,y=238,width=150,height=25)

    #Branch==List
    Branch_List=["Computer Engg","Mechanical Engg","Electronics Engg","Information & Technology"]
    branch = StringVar()
    branch.set("--Select Branch--")
    Branch_dropDown=OptionMenu(root,branch,*Branch_List)
    Branch_dropDown.config(bg="#2B2B37",activebackground="#2B2B37",fg="grey")
    Branch_dropDown.place(x=240,y=238,width=150,height=25)

    #Gender==RadioButton
    Gender_Label=Label(root,text="Gender :",font="Verdana 12 bold",bg="#2B2B37",activebackground="#2B2B37",fg="grey")
    Gender_Label.place(x=40,y=278,width=100,height=40)
    gendervar = StringVar()
    Gender_radioButton_Male=Radiobutton(root,text="Male",value="Male",variable=gendervar,bg="#2B2B37",fg="grey")
    Gender_radioButton_Female=Radiobutton(root,text="Female",value="Female",variable=gendervar,bg="#2B2B37",fg="grey")
    Gender_radioButton_Male.place(x=174,y=278,width=50,height=40)
    Gender_radioButton_Female.place(x=174,y=310,width=60,height=40)

    #entrymobilenumber
    entrymobile = Entry(root, font=font2, bg="#2B2B37", fg="grey", textvariable=mobile)
    entrymobile.insert(0, 'Mobile Number')
    entrymobile.bind('<FocusIn>', on_entry_click_mobile)
    entrymobile.bind('<FocusOut>', on_focus_out_mobile)
    entrymobile.place( x=50, y=350, width=150, height=25)

    #College==List
    College_List=["Rajiv Gandhi","Sardar Patel","Thakur","Thadomal","DJ Sanghvi"]
    college = StringVar()
    college.set("--Select College--")
    College_dropDown=OptionMenu(root,college,*College_List)
    College_dropDown.config(bg="#2B2B37",activebackground="#2B2B37",fg="grey")
    College_dropDown.place(x=240,y=350,width=150,height=25)

    #entry for setpass
    entrysetpass = Entry(root, font=font2, bg="#2B2B37", fg="grey", textvariable=setpass)
    entrysetpass.insert(0, 'Set A Password')
    entrysetpass.bind('<FocusIn>', on_entry_click_setpass)
    entrysetpass.bind('<FocusOut>', on_focus_out_setpass)
    entrysetpass.place( x=50, y=388, width=340, height=25)

    #entry for confirmpass
    entryconfirmpass = Entry(root, font=font2, bg="#2B2B37", fg="grey", textvariable=confirmpass)
    entryconfirmpass.insert(0, 'Confirm Password')
    entryconfirmpass.bind('<FocusIn>', on_entry_click_confirmpass)
    entryconfirmpass.bind('<FocusOut>', on_focus_out_confirmpass)
    entryconfirmpass.place( x=50, y=426, width=340, height=25)

   
    #----------------------------------------------------------------------------------------------------------------------------
    #buttons
    font3 = font.Font(family='Helvetica', size=14, weight='bold')
    submit = Button(root, font=font3, text="GET STARTED", bg="#2B2B37", fg="#f64747", command=Data)
    submit.place( x=50, y=482, width=340, height=50)
    #----------------------------------------------------------------------------------------------------------------------------
    root.mainloop()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#minimizebutton
def on_close(event=None):
    window.destroy()

def frame_mapped(event=None):
    window.update_idletasks()
    window.overrideredirect(True)
    window.state('normal')
topFrame.bind("<Map>",frame_mapped)

def on_minimize(event=None):
    window.update_idletasks()
    window.overrideredirect(False)
    window.state('iconic') 

#------------------------------------------------------------------------------#
#image
image = Image.open("userlogo.png")
image = image.resize((80, 80), Image.ANTIALIAS) 
photo = ImageTk.PhotoImage(image)
label = Label(window, image=photo,  borderwidth=0, bg="#2B2B37")
label.image = photo # keep a reference!
label.place( x=166, y=38)

#imageclose
image1 = Image.open("close.png")
image1 = image1.resize((18, 18), Image.ANTIALIAS) 
photo1 = ImageTk.PhotoImage(image1)
close = Button(window, image=photo1, borderwidth=0, bg="#23232F", command=on_close) # button with image binded to the same function 
close.grid(row=0)
close.place( x=370, y=6)

#imagemin
image2 = Image.open("min1.png")
image2 = image2.resize((18, 18), Image.ANTIALIAS) 
photo2 = ImageTk.PhotoImage(image2)
min1 = Button(window, image=photo2,  borderwidth=0, bg="#23232F", command=on_minimize) # button with image binded to the same function 
min1.grid(row=0)
min1.place( x=348, y=6)

#usericon
image3 = Image.open("usericon.png")
image3 = image3.resize((23, 23), Image.ANTIALIAS) 
photo3 = ImageTk.PhotoImage(image3)
label3 = Label(window, image=photo3,  borderwidth=0, bg="#2B2B37")
label3.image = photo3 
label3.place( x=60, y=160)

#passicon
image4 = Image.open("passicon.png")
image4 = image4.resize((23, 23), Image.ANTIALIAS) 
photo4 = ImageTk.PhotoImage(image4)
label4 = Label(window, image=photo4,  borderwidth=0, bg="#2B2B37")
label4.image = photo4 
label4.place( x=60, y=198)
#----------------------------------------------------------------------------------------------------------#

warn = Label(window, font=("bold", 10), bg="#2B2B37" )
warn.place( x=100, y=227 )

#buttons
imagevisible = Image.open("visible.png")
imagevisible = imagevisible.resize((20, 20), Image.ANTIALIAS) 
photvisible = ImageTk.PhotoImage(imagevisible)
imageinvisible = Image.open("invisible.png")
imageinvisible = imageinvisible.resize((20, 20), Image.ANTIALIAS)
photoinvisible = ImageTk.PhotoImage(imageinvisible)

def btnpressed(event=None):
    password.config(show="")
    btnaction.configure(image=photvisible)
               
def btnreleased(event=None):
    password.configure(show="•")
    btnaction.configure(image=photoinvisible)

#entry
helv36 = font.Font(family='Helvetica', size=13, weight='bold')
username = StringVar()
password = StringVar()

username = Entry(window, textvariable=username, font=helv36, bg="#2B2B37", fg="grey")
username.place( x=90, y=158, width=230, height=25)

password = Entry(window, textvariable=password, font=helv36, show="•", bg="#2B2B37", fg="grey")
password.place( x=90, y=198, width=230, height=25)

btnaction = Button(window,image=photvisible, bg="#2B2B37", width=20, height=20)

btnaction.bind('<Double-Button-1>',btnpressed)
btnaction.bind('<Button-1>',btnreleased)
btnaction.place(x=330,y=198)

loginButton = Button(window, font=helv36 , text="LOGIN", bg="#2B2B37", fg="#f64747", command=Login)
loginButton.place( x=120, y=260, width=80, height=30 )
signupButton = Button(window, font=helv36, text="SIGN UP", bg="#2B2B37", fg="#f64747", command=SignUp)
signupButton.place( x=215, y=260,  width=80, height=30)
#---------------------------------------------------------------------------------------------------------------#
window.mainloop()
