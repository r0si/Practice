package Dao;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;
import java.sql.*;
import java.util.*;
import Bean.Movie;
import Db.connectDb;
/**
 * 实现文章的增加、删除、更新、添加等操作
 * @author Administrator
 *
 */

public class MovieDao {
		PreparedStatement ps = null;
		connectDb con=new connectDb();
		ResultSet rs=null;
		
//添加功能	
		
public boolean insert(Movie movie) {
    String sql ="insert into movie (id,name,address, type,time,date) value(?,?,?,?,?,?)";
    int n =0;
    try{
	ps = con.getConn().prepareStatement(sql);
	ps.setString(1, movie.getId());
	ps.setString(2, movie.getName());
	ps.setString(3, movie.getAddress());
	ps.setString(4, movie.getType());
	ps.setString(5, movie.getTime());
	ps.setString(6, movie.getDate());
	n=ps.executeUpdate();
	}catch (Exception e) {
	    e.printStackTrace();
	}
	 return n>0;
		}	
	
//删除功能
		
public boolean delete(String id) {
   String sql ="delete from movie where id=?";
   int n=0;
   try{
	ps=con.getConn().prepareStatement(sql);
	ps.setString(1, id);
	n=ps.executeUpdate();
	}
	catch (Exception e) {
	e.printStackTrace();
	}
	return n>0;
		}

//修改功能
public boolean update(Movie movie) {
   String sql = "update movie set id=?,name=?, address=? , type=?,time=?,date=? where id=?";
   int n = 0;
   try{
	//ps=con.getConnection().prepareStatement(sql);
	ps=con.getConn().prepareStatement(sql);
	ps.setString(1, movie.getId());
	ps.setString(2, movie.getName());
	ps.setString(3, movie.getAddress());
	ps.setString(4, movie.getType());
	ps.setString(5, movie.getTime());
	ps.setString(6, movie.getDate());
	ps.setString(7, movie.getId());
	n=ps.executeUpdate();
	}
	catch(Exception e){
		e.printStackTrace();
	}
	return n>0;
		}
	 
		
/**
*查询所有信息
*/

public List<Movie> queryAll() {
   String sql="select * from movie";
   List<Movie> list = new ArrayList<Movie>();
   try{
	ps=con.getConn().prepareStatement(sql);
	rs=ps.executeQuery();
	while(rs.next()){
	Movie movie = new Movie(null, null, null, null, null, null);
	movie.setId(rs.getString("id"));
	movie.setName(rs.getString("name"));
	movie.setAddress(rs.getString("address"));
	movie.setType(rs.getString("type"));
	movie.setTime(rs.getString("time"));
	movie.setDate(rs.getString("date"));	
	list.add(movie);
	}
}catch (Exception e) {
	e.printStackTrace();
			}
			return list;
		}
public List<Movie> querySelect(String sel,String nm) {
	   //String sql="select * from movie where ? like ?";
		//String sql="select * from movie where date="+"'2020-12-16'";	
		String sql="select * from movie where "+sel+" like '%"+nm+"%'";
	   List<Movie> list = new ArrayList<Movie>();
	   System.out.println(sel);
	   System.out.println(nm);
	   System.out.println(sql);
	   try{
		   String select=sel;
		   String name="%"+nm+ "%";
		ps=con.getConn().prepareStatement(sql);
		//ps.setString(1, select);
	    //ps.setString(2, name);
	    //ps.setString(1, "10000");
		//ps.setString(2, "10000");
		rs=ps.executeQuery();
		while(rs.next()){
		Movie movie = new Movie(null, null, null, null, null, null);
		movie.setId(rs.getString("id"));
		movie.setName(rs.getString("name"));
		movie.setAddress(rs.getString("address"));
		movie.setType(rs.getString("type"));
		movie.setTime(rs.getString("time"));
		movie.setDate(rs.getString("date"));
		list.add(movie);
		}
	}catch (Exception e) {
		e.printStackTrace();
				}
				return list;
			}
/*	 
//按作者姓名查询
public List<Movie> queryByAuthor(Movie Movie) {
    String sql = "select * from Movie where author=?";
    List<Movie> list = new ArrayList<Movie>();
   try{
	ps =con.getConn().prepareStatement(sql);
        ps.setString(1, Movie.getAuthor());
	ResultSet rs = ps.executeQuery();
	while(rs.next()){
	Movie = new Movie();
	Movie.setNo(rs.getInt("no"));
	Movie.setType(rs.getString("type"));
	Movie.setTitle(rs.getString("title"));
	Movie.setContent(rs.getString("content"));
	Movie.setAuthor(rs.getString("author"));
	Movie.setTime (rs.getDate("time"));
	list.add(Movie);				
		}
			}catch(Exception e){
				e.printStackTrace();
			}
			return list;
		}
 */
//按文章序号查询

public Movie queryByNo(String id) {
	String sql = "select * from movie where id=?";
    Movie	movie = new Movie(null, null, null, null, null, null);
	try{
	ps =con.getConn().prepareStatement(sql);
	ps.setString(1, id);
	ResultSet rs = ps.executeQuery();
    while(rs.next()){
	movie.setId(rs.getString("id"));
	movie.setName(rs.getString("name"));
	movie.setAddress(rs.getString("address"));
	movie.setType(rs.getString("type"));
	movie.setTime(rs.getString("time"));
	movie.setDate(rs.getString("date"));	
	}
	}catch(Exception e){
		e.printStackTrace();
	}
	return movie;
	}
	
}
