
<?php

$rcn = mysql_connect("localhost","root",""); 

mysql_select_db("bolejka"); 

$termid = "";
$last = "order by `mesuredatetime`";
$day = "";
$from = "";
$to = "";

if (isset($_GET['termid'])) $termid=" and `sensorid` = ".$_GET['termid'];
if (isset($_GET['last'])) $last="order by `mesuredatetime` desc, 'termid' 
limit ".$_GET['last'];
if (isset($_GET['day'])) $day=" and DAY(`mesuredatetime`) = ".$_GET['day'];
if (isset($_GET['from'])) $from=" and `mesuredatetime` >= ".$_GET['from'];
if (isset($_GET['to'])) $to=" and `mesurementdatetime` <= ".$_GET['to'];
//printf("ZZ".$_POST['zz']);

$sqlstr = "SELECT unix_timestamp(`mesuredatetime`)*1000 as javadatetime, ROUND(`value`,1) as value 
FROM `mesurements` 
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
