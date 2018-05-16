<?php 

$command = escapeshellcmd('/path/to/file/ibm_discovery.py');
$output = shell_exec($command);
echo $output;

?>