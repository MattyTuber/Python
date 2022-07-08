<!DOCTYPE html>
<html>
<head>
  <!-- Basic -->
  <meta charset="utf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <!-- Mobile Metas -->
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
  <!-- Site Metas -->
  <meta name="keywords" content="" />
  <meta name="description" content="" />
  <meta name="author" content="" />
  <title>
    FlightTracker Supremo
  </title>

  <!-- plus minus button -->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
  <script type="text/javascript" src="js/PlusMinusButton.js"></script>
  <link rel="stylesheet" type="text/css" href="css/bootstrap.css" />
  <link href="https://fonts.googleapis.com/css?family=Poppins:400,600,700&display=swap" rel="stylesheet" />
  <link href="css/style.css" rel="stylesheet" />
  
  <!-- responsive style -->
  <link href="css/responsive.css" rel="stylesheet" />
  <link rel="icon" href="images/icon.ico">
  <style>
    body {
      cursor:url(cgi/assets/images/paper_plane.png), auto;
    }
  </style>
</head>

<body>
<section class="trip_section layout_padding" id="bookTrip">
    <div class="container ">
      <div class="box container-bg">
        <div class="img-box">
          <img src="images/form-img.png" alt="">
        </div>
        <div class="form_container">
          <form action="cgi\tracker.py" method="post">

 <!-- FROM -->                 
            <div class="form-group">
              <label for="example">From</label>
              <div class="input-group ">
                <div class="input-group-prepend">       
                  <div class="input-group-text">
                    <img src="images/location.png" alt="">        
                  </div>
                </div>
                <datalist id="departure">
                  <?php
                  $file = fopen("iata_codes.csv", "r");
                  while (($data = fgetcsv($file, 1000, ",")) !== false) {
                      echo "<option value='$data[0]'>$data[1]</option>";
                  }
                  ?>
                </datalist>
                <input name="departure" list="departure" autoComplete="on" class="form-control" id="inputDestination" placeholder="City or Airport"                                                        ">
              </div>
            </div>
<!-- END FROM -->

<!-- TO -->
            <div class="form-group">
              <label for="example">To</label>
              <div class="input-group ">
                <div class="input-group-prepend">
                  <div class="input-group-text">
                    <img src="images/location.png" alt="">       
                  </div>
                </div>
                <input name="arrival" list="arrival" autoComplete="on" class="form-control" id="inputDestination" placeholder="City or Airport"                                                        ">
                <datalist id="arrival">
                  <?php
                  $file = fopen("iata_codes.csv", "r");
                  while (($data = fgetcsv($file, 1000, ",")) !== false) {
                      echo "<option value='$data[0]'>$data[1]</option>";
                  }
                  ?>
                </datalist>              
              </div>
            </div>
<!-- END TO -->

<!-- DATE -->
            <div class="form-group">
              <label for="example">Date</label>
              <div class="input-group">
                <div class="input-group-prepend">
                  <div class="input-group-text">
                    <img src="images/location.png" alt="">       
                  </div>
                </div>
                <input  class="form-control"  type="date" name="date" value="<?php echo date("Y-m-d"); ?>" min="<?php echo date("Y-m-d"); ?>"/>
              </div>
            </div>
<!-- END DATE -->

<!-- Plus Minus Button -->

            <div id='adults' style="text-align: left; padding: 5px; margin: 2%;" method='POST' action='#'>
              Adults
              <input type='button' value='-' class='qtyminus' field='quantity' />
              <input type='text' name='quantity' value='1' class='qty1' style=" width: 40px; height: 25px; text-align: center;"/> 
              <input type='button' value='+' class='qtyplus' field='quantity' /> 
            </div>
<!-- end Plus Minus Button -->


            <div id='children' style=" text-align: left; padding: 5px; margin: 2%;" method='POST' action='#'>
                Children
            <input type='button' value='-' class='chdminus' field='quantity2' />
            <input type='text' name='quantity2' value='0' class='qty' style=" width: 40px; height: 25px; text-align: center;"/> 
            <input type='button' value='+' class='chdplus' field='quantity2' /> 
            </div>

<!-- submit Button -->     
            <div class="btn-box">
              <button style="background: #041f3d;" type="submit" class="button">Submit</button>  
            </div>
          </form>
        </div>
      </div>
    </div>
  </section>
</body>
</html>