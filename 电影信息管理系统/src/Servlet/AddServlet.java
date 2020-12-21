package Servlet;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.sql.*;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import Bean.Movie;
import Dao.MovieDao;

/**
 * Servlet implementation class searchServlet
 */
public class AddServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
   
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String id = request.getParameter("id");
		String name = request.getParameter("name");
		String address = request.getParameter("address");
		String type = request.getParameter("type");
		String time = request.getParameter("time");
		String date = request.getParameter("date");
		Movie movie = new Movie(id, name, address, type, time, date);
		MovieDao md = new MovieDao();
		
		boolean n = md.insert(movie);
		if(n) {
		      //request.setAttribute("list", list);
		      //request.getRequestDispatcher("admin/movie.jsp").forward(request,response);
			response.sendRedirect("admin/movie.jsp");
		}
		/*Connection con=null;
  		ResultSet rs=null;
  		PreparedStatement ps=null;
  		List<Movie> list =new ArrayList<Movie>();
  		System.out.print(name);
  		String sql ="insert into movie (id,name,address, type,time,date) value(?,?,?,?,?,?)";
  	    int n =0;
  		 try{
  			Class.forName("com.mysql.jdbc.Driver");
			//2.建立连接
  			con = DriverManager.getConnection("jdbc:mysql://45.32.52.141:3306/movieManagement?useUnicode=true&characterEncoding=UTF-8","Nadine","1835477566");
  			ps = con.prepareStatement(sql);
  			ps.setString(1, id);
  		        ps.setString(2, name);
  			ps.setString(3, address);
  			ps.setString(4, type);
  			ps.setString(5, time);
  			ps.setString(6, date);
  			//ps.setString(5, classes);
  			n=ps.executeUpdate();
 			//1.加载驱动(java反射)
  			response.sendRedirect("admin/movie.jsp");
  			//request.getRequestDispatcher("admin/movie.jsp").forward(request, response);
  		 }catch (Exception e) {
	            e.printStackTrace();
	        }
  		 finally {
		if(rs!=null) {
			try {
				rs.close();
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		if(ps!=null){
			try {
				ps.close();
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
