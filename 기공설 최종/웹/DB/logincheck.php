<?php
 if(!isset($_SESSION)) 
    { 
        session_start(); 
    } 
$username=$_POST['username'];
$userpw=$_POST['userpw'];
//echo "<script>alert('$username');</script>";
require "dbconfig.php";
$sql_new = "SELECT * from user where id = '$username'";
//print_r($sql_new);
//history.go(-1);

if($result = mysqli_query($db, $sql_new)){

	$row = $result->fetch_assoc();
	print_r($row);
	if($row['pw'] =='')
		echo"<script>alert('ID가 존재 하지 않습니다. ');history.go(-1);</script>";
	else
	{
		if($row['pw'] == $userpw)
		{
			echo"<script>alert('로그인에 성공 하였습니다. ');location.href='../admin.php?id=".$username."';</script>";
		}
		else
		{
			echo"<script>alert('비밀번호가 틀렸습니다. ');history.go(-1);</script>";
		}
	}
	
} 
else{
	echo mysqli_connect_error();
    echo "<script>alert('ERROR: DB connect error ~');</script>";
    
}

mysqli_close($db);

?>