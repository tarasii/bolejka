<?php

$rcn = mysql_connect("localhost","root",""); 

mysql_select_db("bolejka"); 

$termid = "";
$last = "order by `measuredatetime`";
$day = "";
$from = "";
$to = "";

if (isset($_GET['termid'])) $termid=" and `sensorid` = ".$_GET['termid'];
if (isset($_GET['last'])) $last="order by `measuredatetime` desc, 'termid' 
limit ".$_GET['last'];
if (isset($_GET['day'])) $day=" and DAY(`measuredatetime`) = ".$_GET['day'];
if (isset($_GET['from'])) $from=" and `measuredatetime` >= ".$_GET['from'];
if (isset($_GET['to'])) $to=" and `measurementdatetime` <= ".$_GET['to'];
//printf("ZZ".$_POST['zz']);

$sqlstr = "SELECT `measuredatetime`,ROUND(`value`,1) as value 
FROM `temperatures` 
WHERE 1 ".$termid." ".$day."  ".$from."  ".$to." 
".$last;

$res = mysql_query($sqlstr); 
//limit 3");
//WHERE `thermometerid` = 2
//order by `measurementdatetime` desc



$number = mysql_num_rows($res);
printf("[");
//printf(""+$number);

$first = false;

if ($number > 0) 
{
  while ($row=mysql_fetch_array($res)) {
    if ($first) printf(",");
    printf("[");
    printf($row['javadatetime']);
    printf(", ");
    printf($row['value']);
    printf("]");
    $first = true;
  }
} 
printf("]");

mysql_close();
?>
