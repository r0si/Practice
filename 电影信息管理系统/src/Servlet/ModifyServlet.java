package Servlet;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import Bean.Movie;
import Dao.MovieDao;

/**
 * Servlet implementation class ModifyServlet
 */
public class ModifyServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
   
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String id=request.getParameter("id");
		String name=request.getParameter("name");
		String address=request.getParameter("address");
		String type=request.getParameter("type");
		String time=request.getParameter("time");
		String date=request.getParameter("date");
		Movie movie = new Movie(id, name, address, type, time, date);
		MovieDao md = new MovieDao();
		System.out.println("modify");
		System.out.println(type);
		boolean r = md.update(movie);
		if(r) {
			  
		      //request.getRequestDispatcher("admin/movie.jsp").forward(request,response);
			response.sendRedirect("admin/movie.jsp");
		 } 
		/*HttpSession session=request.getSession();
		String s=session.getAttribute("num").toString();
		int no=Integer.parseInt(s);
		Connection con=null;
 		//ResultSet rs=null;
 		PreparedStatement pst=null;
 		List<Movie> list =new ArrayList<Movie>();
 		PrintWriter out =response.getWriter();
 		System.out.print("modify");
 		 try{

			//1.加载驱动(java反射)
			Class.forName("com.mysql.jdbc.Driver");
			//2.建立连接
			con = DriverManager.getConnection("jdbc:mysql://45.32.52.141:3306/movieManagement?useUnicode=true&characterEncoding=UTF-8","Nadine","1835477566");
	        pst=con.prepareStatement("update movie set id=?,name=?,address=?,type=?,time=?,date=? where id=?");
	        pst.setString(1, id);
	        pst.setString(2, name);
	        pst.setString(3, address);
	        pst.setString(4, type);
	        pst.setString(5, time);
	        pst.setString(6, date);
	        pst.setString(7, id);
	        int r= pst.executeUpdate(); 
	        if(r!=0) { 
	        	out.print("修改成功！");
	        	response.sendRedirect("admin/movie.jsp");
	        }else {
	        	out.print("修改失败！");
	        	response.sendRedirect("admin/movie.jsp");
	        }
 		 }
	        catch (Exception e) {
	            e.printStackTrace();
	        }finally {
				
				if(pst!=null){
					try {
						pst.close();
					} catch (SQLException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
				if(con!=null){
					try {
						con.close();
					} catch (SQLException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
				}
	        }*/
	}

	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
