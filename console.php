<?php 

$command = escapeshellcmd('/path/to/file/ibm_discovery.py');
$output = shell_exec($command);
echo $output;

#Send to Perl.
#open(SECRETLOG, ">", "log.txt");
#print SECRETLOG "accessed.";
#close(SECRETLOG);


?>
