<html>
    <head>
        <title>Flight Search</title>
    </head>
    <body>
        <div class="track">
            <h1>Search Flight</h1>
            <form action="cgi/tracker.py" method="post">
                From <br><br>
                <div>
                    <datalist id="departure">
                        <?php
                            $file = fopen("iata_codes.csv", "r");
                            while(($data = fgetcsv($file, 1000, ",")) !== FALSE) {
                                echo "<option value='$data[0]'>$data[1]</option>";
                            }
                        ?>
                    </datalist>
                    <input  autoComplete="on" name="departure" list="departure"/> 
                </div> 
                <br><br>

                To <br><br>
                <div>
                    <datalist id="arrival">
                        <?php
                            $file = fopen("iata_codes.csv", "r");
                            while(($data = fgetcsv($file, 1000, ",")) !== FALSE) {
                                echo "<option value='$data[0]'>$data[1]</option>";
                            }
                        ?>
                    </datalist>
                    <input  autoComplete="on" name="arrival" list="arrival"/> 
                </div> 
                <br><br>

                Date <br><br>
                <input type="date" name="date" value="<?php echo date("Y-m-d"); ?>" min="<?php echo date("Y-m-d"); ?>"/>
                <br><br>
                
                <input type="submit" name="submit" value="Submit">
            </form>
        </div>
    </body>
</html>