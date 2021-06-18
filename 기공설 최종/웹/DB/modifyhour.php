<?php
$idx = $_GET['idx'];
$hour = $_GET['hour'];

require "dbconfig.php";
if($result = mysqli_query($db,"SELECT * FROM lecture where idx = ".$idx.";") )
{
	$row = $result->fetch_assoc();
	$sql = "UPDATE lecture SET beforehour='$hour' WHERE idx='$idx'";
    if ($db->query($sql) === TRUE) {
    echo"<script>alert('변경했습니다');window.close();</script>";
} 
} 

//require "dbconfig.php";
//$sql_new = "SELECT * from userlist where id = BINARY('$username')";
//print_r($sql_new);
//history.go(-1);
mysqli_close($db);

?>