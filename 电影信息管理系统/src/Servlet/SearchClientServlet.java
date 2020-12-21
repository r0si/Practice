package Servlet;

import java.io.IOException;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import Bean.Movie;
import Dao.MovieDao;

/**
 * Servlet implementation class SearchClientServlet
 */
public class SearchClientServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public SearchClientServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		//response.getWriter().append("Served at: ").append(request.getContextPath());
		String nm = request.getParameter("search");
		String sel = request.getParameter("select");
		Movie movie = new Movie(null, null, null, null, null, null);
		MovieDao md = new MovieDao();
		List<Movie> list = md.querySelect(sel, nm);
		if(list!=null) {
			  
		      request.setAttribute("list", list);
		      request.getRequestDispatcher("admin/clientMovie.jsp").forward(request,response);            
		} 
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
