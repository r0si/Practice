package Servlet;

import java.io.IOException;
import java.sql.ResultSet;
import java.sql.SQLException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import Db.connectDb;

/**
 * Servlet implementation class LoginClientServlet
 */
public class LoginClientServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public LoginClientServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		response.getWriter().append("Served at: ").append(request.getContextPath());
	}
	static boolean check(String name, String passwd) {
		connectDb conn = new connectDb();
		ResultSet data = conn.getResult("select * from client");
		try {
			while (data.next()) {
				String a = data.getString(1), b = data.getString(2);
				if (a.equals(name) && b.equals(passwd))
					return true;
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return false;
		}
		return false;
	}
	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
		String userName=request.getParameter("userName");
		String userPwd=request.getParameter("userPwd");
		System.out.println(userName);
		System.out.println(userPwd);
		HttpSession session=request.getSession();
		
		if(userName==null||userPwd==null) {
			response.sendRedirect("clientlogin.jsp");
		}else if(check(userName,userPwd)) {
			session.setAttribute("username", userName);
			session.setAttribute("userpwd", userPwd);
			response.sendRedirect("admin/clientMovie.jsp");
			//request.getRequestDispatcher("admin/movie.jsp").forward(request, response);
		}else {
			response.sendRedirect("clientlogin.jsp");
		}
	}

}
