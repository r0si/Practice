<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>登录</title>
    <link rel="stylesheet" href="demo.css">
    <script type="text/javascript" src="http://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script>
    <style type="text/css">
    	
body {
    margin: 0px;
    padding: 0px;
    font-family: sans-serif;
    background: cornsilk;
    background-size: cover;
}

.box {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    /*实现块元素百分比下居中*/
    width: 450px;
    padding: 50px;
    background: rgba(0, 0, 0, .8);
    box-sizing: border-box;
    box-shadow: 0px 15px 25px rgba(0, 0, 0, .5);
    border-radius: 15px;
}

.box h2 {
    margin: 0 0 30px;
    padding: 0;
    color: #fff;
    text-align: center;
}

.box .inputbox {
    position: relative;
}

.box .inputbox input {
    width: 100%;
    padding: 10px 0;
    font-size: 16px;
    color: #fff;
    letter-spacing: 1px;
    margin-bottom: 30px;
    border: none;
    border-bottom: 1px solid #fff;
    outline: none;
    background: transparent;
}

.box .inputbox label {
    position: absolute;
    top: 0px;
    left: 0px;
    padding: 10px 0;
    font-size: 16px;
    color: #fff;
    pointer-events: none;
    transition: .5s;
}

.box .inputbox input:focus ~ label,
.box .inputbox input:valid ~ label {
    top: -18px;
    left: 0;
    color: #03a9f4;
    font-size: 14px;
}

.box input[type="submit"] {
    background: transparent;
    border: none;
    outline: none;
    font-size: 16px;
    color: #fff;
    background: #03a9f4;
    padding: 15px 20px;
    cursor: pointer;
    border-radius: 10px;
    display: block;
    margin: 0 auto;
}
    </style>
</head>
<body>
<script type="text/javascript">
    $(document).ready(
        function () {
            document.onkeydown = function () {
                var r = parseInt(Math.random() * 256);
                var g = parseInt(Math.random() * 256);
                var b = parseInt(Math.random() * 256);
                document.body.style.backgroundColor = "rgb(" + r + "," + g + "," + b + ")";
            }
        }
    )
</script>
<form action="${pageContext.request.contextPath}/LoginServlet" method="post">
    <div class="box">
        <h2>Login</h2>
        <form>
            <div class="inputbox">
                <input type="text" name="userName" required="">
                <label>Username</label>
            </div>
            <div class="inputbox">
                <input type="password" name="userPwd" required="">
                <label>Password</label>
            </div>
            <input type="submit" name="" value="submit">
        </form>
    </div>
</form>
</body>
</html>