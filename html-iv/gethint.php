
<?php

// get the q parameter from URL
$q = $_REQUEST["q"];
echo $q;
$myfile = fopen("/var/www/vhosts/shisha-drive.de/httpdocs/html-iv/py/iv-werte.txt", "w");
$txt = $q;
fwrite($myfile, $txt);
fclose($myfile);

$myfile2 = fopen("data.txt", "w");
fwrite($myfile2, $txt);
fclose($myfile2);

?> 