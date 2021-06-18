<?php
//check connection
//이주석 만 지우시면 예전 코드 똑같습니다.
$db = mysqli_connect("127.0.0.1","root","autoset","kmsprj");
if(mysqli_connect_errno()){
	echo "Failed to connect to MySQL: " . mysqli_connect_error();
}else{
}
?>
