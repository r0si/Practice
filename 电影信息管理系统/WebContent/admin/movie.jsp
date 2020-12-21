<%@ page language="java" import="java.util.*,java.sql.*,Dao.*" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<%@page import="Bean.Movie"%>
<%@page import="Db.connectDb" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="https://www.bootcss.com/p/buttons/css/buttons.css">
<title>电影院信息管理系统</title>
<!--<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css"> -->
 <link rel="stylesheet" type="text/css" href="/zjf/w3.css"> 

<style>
	body{
		background-color: #f5f5d5;
	}
	* {
	box-sizing:border-box;
	
}
body {
	margin:0;
	padding:0;
	font-weight:500;
	font-family:"Microsoft YaHei","宋体","Segoe UI","Lucida Grande",Helvetica,Arial,sans-serif,FreeSans,Arimo;
}
#container {
	width:400px;
	height:320px;
	margin:0 auto;
}
div.search {
	padding:170px 0;
}
form {
	position:relative;
	width:300px;
	margin:0 auto;
}
input,button {
	border:none;
	outline:none;
}
input {
	width:100%;
	height:42px;
	padding-left:13px;
}
button {
	height:42px;
	width:42px;
	cursor:pointer;
	position:absolute;
}
.bar7 form {
	height:42px;
}
.bar7 input {
	width:350px;
	border-radius:42px;
	border:2px solid #324B4E;
	background:#F9F0DA;
	transition:.3s linear;
	float:right;
}
.bar7 input:focus {
	width:500px;
}
.bar7 button {
	background:none;
	top:-2px;
	right:20px;
}
.bar7 button:before {
	content:"Search";
	font-family:FontAwesome;
	color:#324b4e;
}
#btn{
	position:absolute;
	top:150px;
	left:1100px;
}
</style>
<style type="text/css">
	.header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background: #cc5350;
    color:#fff;
    z-index: 1000;
    height: 100px;
    overflow: hidden;
    -webkit-transition: height 0.3s;
    -moz-transition: height 0.3s;
    transition: height 0.3s;
    text-align:center;
    line-height:160px;

}
.header.shrink {
    height: 100px;
    line-height:80px;
}
.header h1
{
	margin:-30px;
    font-size:30px;
    font-weight:normal;
    -webkit-transition: all 0.3s;
    -moz-transition: all 0.3s;
    transition: all 0.3s;
}

.header.shrink h1
{
    font-size:24px;
    -webkit-transition: all 0.3s;
    -moz-transition: all 0.3s;
    transition: all 0.3s;
}
</style>
<style type="text/css">
	.btn {
       background-color: #4CAF50;
       border: none;
       color: white;
       padding: 1px;
       text-align: center;
       font-size: 16px;
       cursor: pointer;
       height: 30px;
       width: 50px;
   }
</style>
</head>
	
<body>
	<div class="header">
  <h1>电影院信息管理系统</h1>
</div>
<script class="cssdeck" src="//cdnjs.cloudflare.com/ajax/libs/jquery/1.8.0/jquery.min.js"></script>

	<div id="container">
	    <div class="search bar7">
        <form action="${pageContext.request.contextPath}/SearchServlet"  method="get">
            <input type="text" placeholder="请输入要查询的信息" name="search">
            <select name="select" style="margin-left:90px;" class="myselect">f
    			<option value="name">电影名称</option>
    			<option value="id">电影编号</option>
    			<option value="date">放映日期</option>
    			<option value="type">电影类型</option>
			</select>
            <button type="submit"></button>

        </form>
    </div>
   </div>
<div class="w3-container">
	<a href="/zjf/admin/addMovie.jsp" id="btn" class="button button-royal button-pill button-giant">添加电影</a>
	<a href="/zjf/login.jsp" style="position:absolute;top:230px;" id="btn" class="button button-royal button-pill button-giant">退出登录</a>
  <table class="w3-table-all w3-hoverable">
    <thead>
      <tr class="w3-light-grey">
        <th>电影编号</th>
        <th>电影名</th>
        <th>放映地址</th>
        <th>电影类型</th>
        <th>播放时长</th>
        <th>放映日期</th>
        <th>修改信息</th>
        <th>删除电影</th>
        <th>在线试看</th>
      </tr>
    </thead>
         <%
         /*
     		ResultSet rs=null;
     		List<Movie> list =new ArrayList<Movie>();
     		connectDb conn = new connectDb();
     		request.setCharacterEncoding("utf-8");
     		//String mv=request.getParameter("search");
		    //rs= conn.getResult("select * from movie");
		    String nm = request.getParameter("search");
			String sel = request.getParameter("select");
			rs= conn.getResult("select * from movie");
		    while(rs.next()) {
		    	String id=rs.getString("id");
		        String name=rs.getString("name");
		        String address=rs.getString("address");
		        String type=rs.getString("type");
		        String time=rs.getString("time");
		        String date=rs.getString("date");
		        Movie tl=new Movie( id,  name,  address,  type,  time,  date);
		        
		        if(nm==null)
	                list.add(tl);
	            else if(name.equals(nm))
	            	list.add(tl);
		        
		        //list.add(tl);
		    }
		    */
		    MovieDao mv=new MovieDao();
     		List<Movie> list=(List) request.getAttribute("list");
     		if(list==null ){
     		 list = mv.queryAll();
     		}
            for(Movie tl:list)
            {%>
           <script>
           		function crm()
           		{
           			if (confirm("确认删除？")) {
           				window.location.href = 'http://localhost:8080/zjf/RemoveServlet?id=<%=tl.getId() %>'
           			  } else {
           			    ;
           			  }
           		}
           </script>
           <tr>
               <td><%=tl.getId() %></td>
               <td><%=tl.getName() %></td>
               <td><%=tl.getAddress() %></td>
               <td><%=tl.getType() %></td>
               <td><%=tl.getTime() %></td>
               <td><%=tl.getDate() %></td>
               <td><button class="btn" onclick="window.location.href = 'http://localhost:8080/zjf/admin/editMovie.jsp?id=<%=tl.getId() %>'">修改</button>></td>
               <td><button class="btn" style="background-color: red;" onclick="crm()">删除</button>></td>
               <td><button class="btn" target="_blank" style="background-color: blue;" onclick="window.open('https://so.youku.com/search_video/q_<%=tl.getName() %>?searchfrom=3')">试看</button>></td>
               <!--<td><button class="btn" onclick="window.location.href = 'http://localhost:8080/zjf/RemoveServlet?id=<%=tl.getId() %>'">删除</button>></td>-->
           </tr>
             <%}
             %>
  </table>
</div>
</body>
</html>