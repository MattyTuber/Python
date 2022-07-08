#!C:\Users\Teo\AppData\Local\Programs\Python\Python310\python.exe

import cgi,cgitb
import requests,json
import config

import sys
sys.stdout.reconfigure(encoding='utf-8') #configura l'output in utf-8

###############################################################################

cgitb.enable() #abilito la cartella all'uso del CGI

form = cgi.FieldStorage() #prendi in input i valori del form (barra di ricerca)

url = "https://serpapi.com/search.json?engine=youtube&gl=it&hl=it&search_query=" + form.getvalue("search") + "&api_key=" + config.API_KEY #url chiamata all'API

response = requests.get(url) #chiamata effetiva all'API
response = json.loads(response.text) #converto il risultato in un json

###############################################################################

print ("Content-type:text/html\n") #tipo di contenuto
print(f"""
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!-- Material Icons -->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" />
    <!-- CSS File -->
    <link rel="stylesheet" href="Style/style.css" />
    <link rel="icon" href="YouTube.ico">
    <title>Youtube API</title>
  </head>
  <body>
    <!-- Header Starts -->
    <div class="header">
      <div class="header__left">
        <i id="menu" class="material-icons">menu</i>
        <a href="index.html"> <img src="https://i.ibb.co/vhFms13/Presentation1-removebg-preview.png" alt="" /> </a>
      </div>
      <div class="header__search">
        <form action="index.py" method="post">
          <input type="text" name="search" value="{form.getvalue("search")}"/>
          <button>
            <i class="material-icons">search</i>
          </button>
        </form>
      </div>
      <div class="header__icons">
        <i class="material-icons display-this">search</i>
        <i class="material-icons">videocam</i>
        <i class="material-icons">apps</i>
        <i class="material-icons">notifications</i>
        <i class="material-icons display-this">account_circle</i>
      </div>
    </div>
    <!-- Header Ends -->
    <!-- Main Body Starts -->
    <div class="mainBody">
      <!-- Sidebar Starts -->
      <div class="sidebar">
        <div class="sidebar__categories">
          <div class="sidebar__category">
            <i class="material-icons">home</i>
            <span>Home</span>
          </div>
          <div class="sidebar__category">
            <i class="material-icons">local_fire_department</i>
            <span>Trending</span>
          </div>
          <div class="sidebar__category">
            <i class="material-icons">subscriptions</i>
            <span>Subcriptions</span>
          </div>
        </div>
        <hr />
        <div class="sidebar__categories">
          <div class="sidebar__category">
            <i class="material-icons">library_add_check</i>
            <span>Library</span>
          </div>
          <div class="sidebar__category">
            <i class="material-icons">history</i>
            <span>History</span>
          </div>
          <div class="sidebar__category">
            <i class="material-icons">play_arrow</i>
            <span>Your Videos</span>
          </div>
          <div class="sidebar__category">
            <i class="material-icons">watch_later</i>
            <span>Watch Later</span>
          </div>
          <div class="sidebar__category">
            <i class="material-icons">thumb_up</i>
            <span>Liked Videos</span>
          </div>
        </div>
        <hr />
      </div>
      <!-- Sidebar Ends -->
      <!-- Videos Section -->
      <div class="videos">
        <h1>Results</h1>
        <div class="videos__container">
          <!-- Single Video starts -->""")
for i in range(len(response["video_results"])):
    try:
      print(f"""
            <div class="video">
                <div class="video__thumbnail">
                <a href="{response["video_results"][i]["link"]}"><img src="{response["video_results"][i]["thumbnail"]["static"]}" /></a>
                </div>
                <div class="video__details">
                <div class="author">
                    <a href="{response["video_results"][i]["channel"]["link"]}"><img src="{response["video_results"][i]["channel"]["thumbnail"]}" /></a>
                </div>
                <div class="title">
                    <a href="{response["video_results"][i]["link"]}"><h3> {response["video_results"][i]["title"]} </h3> </a>
                    <a href="{response["video_results"][i]["channel"]["link"]}">{response["video_results"][i]["channel"]["name"]}</a>
                    <span>{response["video_results"][i]["views"]} &bull; {response["video_results"][i]["published_date"]}</span>
                </div>
                </div>
            </div>
    """)
    except:
      pass
print("""
          <!-- Single Video Ends -->
        </div>
      </div>
    </div>
    </div>
    <script src="Script/script.js"></script>
    <!-- Main Body Ends -->
  </body>undefined
</html>
""")