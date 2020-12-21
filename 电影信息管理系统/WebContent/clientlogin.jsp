<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"> 
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>电影院用户登录</title>
	<link rel="stylesheet" type="text/css" href="/zjf/styles.css">
	<script src="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.js"></script>
	<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/toastr.min.css">
	<!--[if IE]>
		<script src="http://libs.baidu.com/html5shiv/3.7/html5shiv.min.js"></script>
	<![endif]-->
</head>
<body>
	<div class="jq22-container" style="padding-top:100px">
		<div class="login-wrap">
			<div class="login-html">
				<input id="tab-1" type="radio" name="tab" class="sign-in" checked><label for="tab-1" class="tab">Sign In</label>
				<input id="tab-2" type="radio" name="tab" class="sign-up"><label for="tab-2" class="tab">Sign Up</label>
				<div class="login-form">
				<form action="${pageContext.request.contextPath}/LoginClientServlet" method="post">
					<div class="sign-in-htm">
						<div class="group">
							<label for="user" class="label">Username</label>
							<input id="user" name="userName" type="text" class="input">
						</div>
						<div class="group">
							<label for="pass" class="label">Password</label>
							<input id="pass" name="userPwd" type="password" class="input" data-type="password">
						</div>
						<div class="group">
							<input id="check" type="checkbox" class="check" checked>
							<label for="check"><span class="icon"></span> Keep me Signed in</label>
						</div>
						<div class="group">
							<input type="submit" class="button" value="Sign In">
						</div>
						<div class="hr"></div>
						<div class="foot-lnk">
							<a href="#forgot">Forgot Password?</a>
						</div>
					</div>
					</form>
					<script type="text/javascript">
						function check(){
							var password = document.getElementById("password").value;
							var repeatpass = document.getElementById("repeatpass").value;
							console.log(pass,repeatpass);
							if(password != repeatpass){
								alert("两次密码输入不一致！")
							}
						}
						function success(){
							toastr.success('注册成功');
							
						}
					</script>
					<form action="${pageContext.request.contextPath}/ClientRegServlet" method="post">
					<div class="sign-up-htm">
						<div class="group">
							<label for="user" class="label">Username</label>
							<input id="user" name="userName" type="text" class="input">
						</div>
						<div class="group">
							<label for="pass" class="label">Password</label>
							<input id="password" name="userPwd" type="password" class="input" data-type="password">
						</div>
						<div class="group">
							<label for="pass"  class="label">Repeat Password</label>
							<input id="repeatpass" name="repeatUserPwd" type="password" class="input" data-type="password">
						</div>
						<div class="group">
							<label for="pass"  class="label">Email Address</label>
							<input id="pass" name="email" onclick="check();" type="text" class="input">
						</div>
						<div class="group">
							<input type="submit" onclick="success()" class="button" value="Sign Up">
						</div>
						<div class="hr"></div>
						<div class="foot-lnk">
							<label for="tab-1">Already Member?</a>
						</div>
					</div>
					</form>
				</div>
			</div>
		</div>
	</div>
	
</body>
</html>