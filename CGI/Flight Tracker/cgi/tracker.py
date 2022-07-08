#!C:\Users\Teo\AppData\Local\Programs\Python\Python310\python.exe

import cgi,cgitb
import requests,json
import config
import csv
from datetime import datetime

######################################################################################

def airlines(rows):
    file = open("iata_airlines.csv")
    csvreader = csv.reader(file)
    
    for row in csvreader:
        rows.append(row)
    
    file.close()

def print_airline(rows, i):
    for x in range(len(response['data'][i]['airlines'])):
        for j in range(len(rows)):
            if(rows[j][0] == response['data'][i]['airlines'][x]):
            	print((rows[j][1]).title() + "<br>")

def printflight(dep_date, dep_time, arr_date, arr_time, duration, i, rows, price, lenght):
    print("""
          <tbody>
                    <tr style="height:150px;">
                      <td class="fw-bold ps-5 pe-5 table-responsive">
                        <table class="table table-borderless" style="text-align: center;">
                          <tbody>
                            <tr class="h4">""")
    print(f"<td class=\"text-success ps-1\" style=\"text-align: center;\" colspan=\"2\"> {response['data'][i]['cityFrom']} ({response['data'][i]['flyFrom']}) </td>")
    print(f"<td class=\"text-danger pe-7\" colspan=\"2\"> {response['data'][i]['cityTo']} ({response['data'][i]['flyTo']}) </td>")
    print(f"""</tr>
                            <tr>
                              <td>{dep_date}</td>
                              <td>{dep_time}</td>
                              <td>{arr_time}</td>
                              <td>{arr_date}</td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                      <td class="fw-bold">""")
    print_airline(rows, i)
    print(f"""</td>
                      <td style="color:greenyellow" class="fw-bold">{str(price)}&euro;</td>""")
    if(int(children) > 0):
        print(f"<td class=\"fw-bold\">{adults} Adulti {children} Bambini</td>")
    else:
        print(f"<td class=\"fw-bold\">{adults} Adulti</td>")
    print(f"""<td class="text-end pe-xl-5 fw-bold">{str(duration)} <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-hourglass-split" viewBox="0 0 16 16">
			<path d="M2.5 15a.5.5 0 1 1 0-1h1v-1a4.5 4.5 0 0 1 2.557-4.06c.29-.139.443-.377.443-.59v-.7c0-.213-.154-.451-.443-.59A4.5 4.5 0 0 1 3.5 3V2h-1a.5.5 0 0 1 0-1h11a.5.5 0 0 1 0 1h-1v1a4.5 4.5 0 0 1-2.557 4.06c-.29.139-.443.377-.443.59v.7c0 .213.154.451.443.59A4.5 4.5 0 0 1 12.5 13v1h1a.5.5 0 0 1 0 1h-11zm2-13v1c0 .537.12 1.045.337 1.5h6.326c.216-.455.337-.963.337-1.5V2h-7zm3 6.35c0 .701-.478 1.236-1.011 1.492A3.5 3.5 0 0 0 4.5 13s.866-1.299 3-1.48V8.35zm1 0v3.17c2.134.181 3 1.48 3 1.48a3.5 3.5 0 0 0-1.989-3.158C8.978 9.586 8.5 9.052 8.5 8.351z" />
			</svg>
		</td>
    """)

####################################################################################
 
rows = []
airlines(rows)

cgitb.enable()

form = cgi.FieldStorage()
airport_from = form.getvalue('departure')
airport_to = form.getvalue('arrival')
date_departure = form.getvalue('date')
adults = form.getvalue('quantity')
children = form.getvalue('quantity2')

url = "https://tequila-api.kiwi.com/v2/search?"

querystring = {
    "fly_from":airport_from,
    "fly_to":airport_to,
    "date_from":date_departure,
    "date_to":date_departure,
    "adults":adults,
    "children":children
}

header = {
	"apikey": config.API_KEY
}

response = requests.get(url, params=querystring, headers=header)
response = json.loads(response.text)

url = "https://serpapi.com/search.json?engine=google&q=" + response['data'][0]['cityTo'] + "&google_domain=google.com&tbm=isch&api_key=" + config.SERP_API

image = requests.get(url)
image = json.loads(image.text)

##############################################################################################################

print ("Content-type:text/html\n")
print("""
<!doctype html>
<html lang="en" class="dark-theme">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!--favicon-->
    <link rel="icon" href="assets/images/favicon-32x32.png" type="image/png" />
    <!--plugins-->
    <link href="assets/plugins/vectormap/jquery-jvectormap-2.0.2.css" rel="stylesheet" />
    <link href="assets/plugins/simplebar/css/simplebar.css" rel="stylesheet" />
    <link href="assets/plugins/perfect-scrollbar/css/perfect-scrollbar.css" rel="stylesheet" />
    <link href="assets/plugins/metismenu/css/metisMenu.min.css" rel="stylesheet" />
    <!-- loader-->
    <link href="assets/css/pace.min.css" rel="stylesheet" />
    <script src="assets/js/pace.min.js"></script>
    <!-- Bootstrap CSS -->
    <link href="assets/css/bootstrap.min.css" rel="stylesheet">
    <link href="assets/css/bootstrap-extended.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    <link href="assets/css/app.css" rel="stylesheet">
    <link href="assets/css/icons.css" rel="stylesheet">
    <!-- Theme Style CSS -->
    <link rel="stylesheet" href="assets/css/dark-theme.css" />
    <link rel="stylesheet" href="assets/css/semi-dark.css" />
    <link rel="stylesheet" href="assets/css/header-colors.css" />
	<style>
		html {
      cursor:url(assets/images/paper_plane.png), auto;
    }
		body {
      background-repeat: no-repeat;
  		background-attachment: fixed;
			background-size: cover;
   		opacity: 0.9;
			background-image: url('"""+image['images_results'][0]['original']+"""');
		}
	</style>
 	<link rel="icon" href="assets/images/icon.ico">
    <title>FlightTracker Supremo</title>
  </head>
  <body>
    <!--wrapper-->
    <div class="wrapper">
      <!--start header wrapper-->
      <div class="header-wrapper">
        <!--start header -->
        <header>
          <div class="topbar d-flex align-items-center">
            <nav class="navbar navbar-expand">
              <div class="navbar-brand justify-content-start">
                <div class="">
                  <img src="assets/images/icon.ico" class="d-inline-block col-2" alt="logo icon">
                </div>
                <!--			<div class=""><h4 class="logo-text col-2">FlightTracker Supremo</h4></div>-->
			
              </div>
              <div class="top-menu ms-auto">
                <ul class="navbar-nav align-items-center">
                  <div class="header-notifications-list">
                    <div class="header-message-list"></div>
                  </div>
                </ul>
              </div>
            </nav>
          </div>
        </header>
        <!--end header -->
        <!--navigation-->
        <div class="mobile-topbar-header">
          <div>
            <img src="assets/images/icon.ico" class="logo-icon" alt="logo icon">
          </div>
          <div>
            <h4 class="logo-text">FlightTracker Supremo</h4>
          </div>
          <div class="toggle-icon ms-auto">
            <i class='bx bx-arrow-to-left'></i>
          </div>
        </div>
        <!--end navigation-->
      </div>
      <!--end header wrapper-->
      <!--start page wrapper -->
      <div class="page-wrapper">
        <div class="page-content">
          <div class="card radius-4">
            <div class="card-body">
              <div class="d-flex">
                <div style="text-align:center;">
                  <h6 class="mb-0">Voli Disponibili</h6>
                  <br>
                </div>
              </div>
              <div class="table-responsive">
                <table class="table  mb-0 table-hover align-middle">
                  <thead class="table-dark">
                    <tr>
                      <th class="col-5" style="text-align: center;">Volo</th>
                      <th class="col-2">Compagnia Aerea</th>
                      <th class="col-1">Costo</th>
                      <th class="col-1">Passeggeri</th>
                      <th class="text-end pe-5 col-1">Durata</th>
                    </tr>
                  </thead>
""")

for i in range(len(response['data'])):
    dep = datetime.strptime(response['data'][i]['local_departure'], "%Y-%m-%dT%H:%M:%S.%fZ")
    dep_date = dep.strftime("%d/%m/%Y")
    dep_time = dep.strftime("%H:%M")
    #departure = datetime.strptime(departure, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%d/%m/%Y %H:%M:%S")
      
    arr = datetime.strptime(response['data'][i]['local_arrival'], "%Y-%m-%dT%H:%M:%S.%fZ")
    arr_date = arr.strftime("%d/%m/%Y")
    arr_time = arr.strftime("%H:%M")
    #arrival = datetime.strptime(arrival, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%d/%m/%Y %H:%M:%S")
    
    duration = arr - dep
    
    price = response['data'][i]['fare']['adults']*int(adults) + response['data'][i]['fare']['children']*int(children)
    
    lenght = len(response['data'][i]['route']) - 1
    
    printflight(dep_date, dep_time, arr_date, arr_time, duration, i, rows, price, lenght)


    
print("""
				</table>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!--end page wrapper -->
      <!--start overlay-->
      <div class="overlay toggle-icon"></div>
      <!--end overlay-->
      <!--Start Back To Top Button-->
      <a href="javaScript:;" class="back-to-top">
        <i class='bx bxs-up-arrow-alt'></i>
      </a>
      <!--End Back To Top Button-->
      <footer class="page-footer">
        <p class="mb-0">Broglio Matteo - Crepaldi Andrea - Gallo Riccardo - Galuzzi Sean</p>
      </footer>
    </div>
    <!--end wrapper-->
    <!--start switcher-->
    <div class="switcher-wrapper">
      <div class="switcher-btn">
        <i class='bx bx-cog bx-spin'></i>
      </div>
      <div class="switcher-body">
        <div class="d-flex align-items-center">
          <h5 class="mb-0 text-uppercase">Theme Customizer</h5>
          <button type="button" class="btn-close ms-auto close-switcher" aria-label="Close"></button>
        </div>
        <hr />
        <h6 class="mb-0">Theme Styles</h6>
        <hr />
        <div class="d-flex align-items-center justify-content-between">
          <div class="form-check">
            <input class="form-check-input" type="radio" name="flexRadioDefault" id="lightmode">
            <label class="form-check-label" for="lightmode">Light</label>
          </div>
          <div class="form-check">
            <input class="form-check-input" type="radio" name="flexRadioDefault" id="darkmode" checked>
            <label class="form-check-label" for="darkmode">Dark</label>
          </div>
          <div class="form-check">
            <input class="form-check-input" type="radio" name="flexRadioDefault" id="semidark">
            <label class="form-check-label" for="semidark">Semi Dark</label>
          </div>
        </div>
      </div>
    </div>
    <!--end switcher-->
    <!-- Bootstrap JS -->
    <script src="assets/js/bootstrap.bundle.min.js"></script>
    <!--plugins-->
    <script src="assets/js/jquery.min.js"></script>
    <script src="assets/plugins/perfect-scrollbar/js/perfect-scrollbar.js"></script>
    <!--app JS-->
    <script src="assets/js/app.js"></script>
  </body>
</html>      
""")