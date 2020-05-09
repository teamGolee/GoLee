<?php

$geturl = $_POST['text1'];
$db_conn=mysqli_connect("localhost", "goleeccit", "golee123#", "user");
$sql="SELECT * FROM url WHERE url='$geturl'";
$result=mysqli_query($db_conn, $sql);

if($result->num_rows==1){
	$row=$result->fetch_array(MYSQLI_ASSOC);
	$wob = $row['wob'];
	echo "$wob";
} else {
	echo "DB Connect Failed: ".mysqli_connect_error();
}
?>
