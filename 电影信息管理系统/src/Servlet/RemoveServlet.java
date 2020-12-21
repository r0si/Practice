package Servlet;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.util.ArrayList;
import java.util.List;
import java.util.*;
import java.sql.*;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import Bean.Movie;
import Dao.MovieDao;
import Db.connectDb;
/**
 * Servlet implementation class RemoveServlet
 */
public class RemoveServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public RemoveServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		response.getWriter().append("Served at: ").append(request.getContextPath());
		String id=request.getParameter("id");
		MovieDao md = new MovieDao();
		boolean n = md.delete(id);
		if(n) {
		      //request.setAttribute("list", list);
		      //request.getRequestDispatcher("admin/movie.jsp").forward(request,response);
			response.sendRedirect("admin/movie.jsp");
		}
		/*
		Connection con=null;
 		ResultSet rs=null;
 		 int result=0;
 		PreparedStatement pst=null;
 		List<Movie> list =new ArrayList<Movie>();
 		PrintWriter out =response.getWriter();
 		System.out.print("delete");
 		try{
			//1.加载驱动(java反射)
			Class.forName("com.mysql.jdbc.Driver");
			//2.建立连接
		con = DriverManager.getConnection("jdbc:mysql://45.32.52.141:3306/movieManagement?useUnicode=true&characterEncoding=UTF-8","Nadine","1835477566");
			
		pst = con.prepareStatement("delete from movie where id=?");
		pst.setString(1, id);
		
		result = pst.executeUpdate();
		
		if(result>0){//成功插入
			System.out.println("删除文章成功");
			response.sendRedirect("admin/movie.jsp");
		}else{//失败
			System.out.println("删除文章失败");
			response.sendRedirect("admin/movie.jsp");
		}
	} catch (SQLException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}catch (Exception e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}finally{
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

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
