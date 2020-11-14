<?php
/*
 * $servername = "45.32.52.141";
 * $username = "root";
 * $password = "1835477566";
 * $conn = mysqli_connect($servername,$username,$password);
 * if ($conn->connect_error){
 *     die("连接失败: ".$conn->connect_error);
 *     }
 *     echo "success";
 *     echo $_GET["search"];
 *     */
print (phpinfo());
$ip = "47.94.165.228";
$user = "system";
$pass = "oracle";
$conn = oci_connect('system','oracle','47.94.165.228:1521/XE');
echo "连接oracle成功！";
?>
