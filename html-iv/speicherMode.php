<?php
$q = $_REQUEST["q"];
$myfile = fopen("/var/www/vhosts/shisha-drive.de/httpdocs/html-iv/py/mode-werte.txt", "w");
fwrite($myfile, $q);
fclose($myfile);

$myfile2 = fopen("mode.txt", "w");
fwrite($myfile2, $q);
fclose($myfile2);
?> 