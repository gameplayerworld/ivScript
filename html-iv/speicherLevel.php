<?php
$q = $_REQUEST["q"];
echo $q;
$myfile = fopen("/var/www/vhosts/shisha-drive.de/httpdocs/html-iv/py/level-werte.txt", "w");
fwrite($myfile, $q);
fclose($myfile);

$myfile2 = fopen("level.txt", "w");
fwrite($myfile2, $q);
fclose($myfile2);
?> 