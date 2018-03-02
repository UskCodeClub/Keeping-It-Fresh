# User Interface
from guizero import *
import time
from datetime import datetime

# Database
import sqlite3
dbfile = sqlite3.connect('kif.db')
db = dbfile.cursor()
db.execute('''CREATE TABLE IF NOT EXISTS pantry (food text, bbdate text)''')

# Twitter
# Need to add own Twitter app keys
from twython import Twython
app_key = "xxxxxxxxxxEcrUJkcghvWP6ts"
app_secret = "xxxxxxxxxx9qJpkRsSIB7JH8c78bO7Mmomf2NWZWHzIGAZdSEL"
oauth_token = "xxxxxxxxxx99451137-PiajpZmSh5AoXzIzBDB11M1xM27c1bq"
oauth_token_secret = "xxxxxxxxxxqPVl53xmFAoebHKplVDhYRxnu0xl6Wyhf3s"
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

thetime = datetime.now().strftime('%-I:%M%P on %d-%m-%Y')

# Global Variables
food = ''
bbdate = ''


# Find Food Going Off Tomorrow, Tweet Recipe, Remove From Pantry
# Remove coments from twitter lines when correct authorisation keys in place

for row in dbfile.execute("SELECT * FROM pantry WHERE food='Bacon' AND bbdate=date('now','+1 day')"):
    print (row)
    #twitter.update_status(status="Your bacon is approaching its best before date. Here's a link to some recipes you might like. https://www.bbcgoodfood.com/search/recipes?query=bacon" + " " + thetime)
    
for row in dbfile.execute("SELECT * FROM pantry WHERE food='Tomatoes' AND bbdate=date('now','+1 day')"):
    print (row)
    #twitter.update_status(status="Your tomatoes are approaching their best before date. Here's a link to some recipes you might like. https://www.bbcgoodfood.com/search/recipes?query=tomatoes" + " " + thetime)
 
for row in dbfile.execute("SELECT * FROM pantry WHERE food='Chicken' AND bbdate=date('now','+1 day')"):
    print (row)
    #twitter.update_status(status="Your chicken is approaching its best before date. Here's a link to some recipes you might like. https://www.bbcgoodfood.com/search/recipes?query=chicken" + " " + thetime)
     
for row in dbfile.execute("SELECT * FROM pantry WHERE food='Milk' AND bbdate=date('now','+1 day')"):
    print (row)
    #twitter.update_status(status="Your milk is approaching its best before date. Here's a link to some recipes you might like. https://www.bbcgoodfood.com/search/recipes?query=milk" + " " + thetime)

for row in dbfile.execute("SELECT * FROM pantry WHERE food='Broccoli' AND bbdate=date('now','+1 day')"):
    print (row)
    #twitter.update_status(status="Your broccoli is approaching its best before date. Here's a link to some recipes you might like. https://www.bbcgoodfood.com/search/recipes?query=broccoli" + " " + thetime)
    
for row in dbfile.execute("SELECT * FROM pantry WHERE food='Peppers' AND bbdate=date('now','+1 day')"):
    print (row)
    #twitter.update_status(status="Your peppers are approaching their best before date. Here's a link to some recipes you might like. https://www.bbcgoodfood.com/search/recipes?query=peppers" + " " + thetime)
     
for row in dbfile.execute("SELECT * FROM pantry WHERE food='Potatoes' AND bbdate=date('now','+1 day')"):
    print (row)
    #twitter.update_status(status="Your potatoes are approaching their best before date. Here's a link to some recipes you might like. https://www.bbcgoodfood.com/search/recipes?query=potatoes" + " " + thetime)
   
for row in dbfile.execute("SELECT * FROM pantry WHERE food='Eggs' AND bbdate=date('now','+1 day')"):
    print (row)
    #twitter.update_status(status="Your eggs are approaching their best before date. Here's a link to some recipes you might like. https://www.bbcgoodfood.com/search/recipes?query=eggs" + " " + thetime)
    
for row in dbfile.execute("SELECT * FROM pantry WHERE food='Leeks' AND bbdate=date('now','+1 day')"):
    print (row)
    #twitter.update_status(status="Your leeks are approaching their best before date. Here's a link to some recipes you might like. https://www.bbcgoodfood.com/search/recipes?query=leeks" + " " + thetime)
       
for row in dbfile.execute("SELECT * FROM pantry WHERE food='Carrots' AND bbdate=date('now','+1 day')"):
    print (row)
    #twitter.update_status(status="Your carrots are approaching their best before date. Here's a link to some recipes you might like. https://www.bbcgoodfood.com/search/recipes?query=carrots" + " " + thetime)
    
dbfile.execute("DELETE FROM pantry WHERE bbdate<=date('now')");


# Add To Pantry

def add_to_pantry():

    global food, bbdate

    bbdate = y_combo.value + "-" + m_combo.value + "-" + d_combo.value

    if d_combo.value == 'Day' or m_combo.value == 'Month' or y_combo.value == 'Year' :
        print ("You haven't set a best before date")

    elif food == '' :
        print ("You haven't tapped a food icon")

    else :
        print ("Adding " +food +" to pantry with best before date " +bbdate)
        q = "INSERT INTO pantry VALUES ('"
        q += food
        q += "', '"
        q += bbdate
        q += "')"
        db.execute(q)
        dbfile.commit()


# Button Commands
                
def add_carrots():
        global food 
        food = 'Carrots'
           
def add_bacon():
        global food
        food = 'Bacon'
             
def add_chicken():
        global food
        food = 'Chicken'

def add_Eggs():
        global food
        food = 'Eggs'
        
def add_potatoes():
        global food
        food = 'Potatoes'
 
def add_tomatoes():
        global food
        food = 'Tomatoes'
         
def add_broccoli():
        global food
        food = 'Broccoli'
        
def add_leeks():
        global food
        food = 'Leeks'
        
def add_peppers():
        global food
        food = 'Peppers'
         
def add_milk():
        global food
        food = 'Milk'


# Build User Interface

app = App(title="Keeping It Fresh", height=600, width=820)

box = Box(app, layout="grid")

t01 = Text(box, text="Welcome to Keeping It Fresh", font="20", grid=[0,1,5,1])

t02 = Text(box, text="Please tap a food icon", font="20", grid=[0,2,5,1])

# First row of buttons

b01 = PushButton (box, command=add_carrots,  icon="carrots.gif",  grid=[0,3])
b02 = PushButton (box, command=add_bacon,    icon="bacon.gif",    grid=[1,3])
b03 = PushButton (box, command=add_chicken,  icon="chicken.gif",  grid=[2,3])
b04 = PushButton (box, command=add_Eggs,     icon="Eggs.gif",     grid=[3,3])
b05 = PushButton (box, command=add_potatoes, icon="potatoes.gif", grid=[4,3])

# Second Row of Buttons

b06 = PushButton (box, command=add_tomatoes, icon="tomatoes.gif", grid=[0,4])
b07 = PushButton (box, command=add_broccoli, icon="broccoli.gif", grid=[1,4])
b08 = PushButton (box, command=add_leeks,    icon="leeks.gif",    grid=[2,4])
b09 = PushButton (box, command=add_peppers,  icon="peppers.gif",  grid=[3,4])
b10 = PushButton (box, command=add_milk,     icon="milk.gif",     grid=[4,4])

t03 = Text(box, text="Please set a best before date", font="20", grid=[0,5,5,1])

# Calendar Combo Boxes

d_combo = Combo(box, options=["Day", 
	"01", "02", "03", "04", "05", "06", "07", "08", "09", "10", 
	"11", "12", "13", "14", "15", "16", "17", "18", "19", "20", 
	"21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
	"31", ], grid=[1,6] )

m_combo = Combo(box, options=["Month", 
	"01", "02", "03", "04", "05", "06",
	"07", "08", "09", "10", "11", "12", ], grid=[2,6] )

y_combo = Combo(box, options=["Year", "2018", "2019", "2020", ], grid=[3,6] )

t04 = Text(box, text="Please tap add to pantry", font="20", grid=[0,7,5,1])

# Add to Pantry Button

b11 = PushButton (box, command=add_to_pantry, text="Add To Pantry", grid=[2,8])

# Display the App

app.display()
