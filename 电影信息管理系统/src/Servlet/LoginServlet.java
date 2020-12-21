package Servlet;

import java.io.IOException;
import java.sql.ResultSet;
import java.sql.SQLException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import Db.connectDb;

/**
 * Servlet implementation class LoginServlet
 */
@WebServlet("/LoginServlet")
public class LoginServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public LoginServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doPost(request,response);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	static boolean check(String name, String passwd) {
		connectDb conn = new connectDb();
		ResultSet data = conn.getResult("select * from admin");
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
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		String userName=request.getParameter("userName");
		String userPwd=request.getParameter("userPwd");
		
		HttpSession session=request.getSession();
		
		if(userName==null||userPwd==null) {
			response.sendRedirect("login.jsp");
		}else if(check(userName,userPwd)) {
			session.setAttribute("username", userName);
			session.setAttribute("userpwd", userPwd);
			response.sendRedirect("admin/movie.jsp");
			//request.getRequestDispatcher("admin/movie.jsp").forward(request, response);
		}else {
			response.sendRedirect("login.jsp");
		}
	}

}
