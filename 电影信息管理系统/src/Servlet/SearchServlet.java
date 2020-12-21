package Servlet;

import java.io.IOException;
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

import Bean.Movie;
import Dao.MovieDao;

/**
 * Servlet implementation class searchServlet
 */
public class SearchServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
   
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String nm = request.getParameter("search");
		String sel = request.getParameter("select");
		Movie movie = new Movie(null, null, null, null, null, null);
		MovieDao md = new MovieDao();
		List<Movie> list = md.querySelect(sel, nm);
		if(list!=null) {
			  
		      request.setAttribute("list", list);
		      request.getRequestDispatcher("admin/movie.jsp").forward(request,response);            
		} 
		/*
		Connection con=null;
  		ResultSet rs=null;
  		PreparedStatement pst=null;
  		List<Movie> list =new ArrayList<Movie>();
  		System.out.println(sel);
  		System.out.println(nm);
  		 try{
 			//1.加载驱动(java反射)
 			Class.forName("com.mysql.jdbc.Driver");
 			//2.建立连接
 			con = DriverManager.getConnection("jdbc:mysql://45.32.52.141:3306/movieManagement","Nadine","1835477566");

		        pst=con.prepareStatement("select * from movie where ?=?");
		        pst.setString(1, sel);
		        pst.setString(2, nm);
		        rs= pst.executeQuery(); 
		           while(rs.next())
		           {
		        	   String id=rs.getString("id");
				        String name=rs.getString("name");
				        String address=rs.getString("address");
				        String type=rs.getString("type");
				        String time=rs.getString("time");
				        String date=rs.getString("date");
				        Movie tl=new Movie( id,  name,  address,  type,time,date);
		                list.add(tl);
		            }
		           request.setAttribute("list", list);
		           request.getRequestDispatcher("admin/movie.jsp").forward(request, response);
		           //response.sendRedirect("admin/movie.jsp");
		            
		        } catch (Exception e) {
		            e.printStackTrace();
		        }finally {
					if(rs!=null) {
						try {
							rs.close();
						} catch (SQLException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
						}
					}
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
