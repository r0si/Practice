package Db;

import java.sql.*;

public class connectDb {
	Connection conn=null;
	Statement stat=null;
	ResultSet rs=null;
	PreparedStatement ps=null;
	public Connection getConn() {
		try {
			Class.forName("com.mysql.jdbc.Driver").newInstance();
			conn = DriverManager.getConnection("jdbc:mysql://45.32.52.141:3306/movieManagement?useUnicode=true&characterEncoding=UTF-8","Nadine","1835477566");
		} catch(InstantiationException e) {
			e.printStackTrace();
		} catch (IllegalAccessException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return conn;
	}
	public void release() {
		try {
			if (rs != null)
				rs.close();
			if (stat != null)
				stat.close();
			if (conn != null)
				conn.close();
		} catch(SQLException e) {
			e.printStackTrace();
		}
	}
	public ResultSet getResult(String sql, String []args) {
		rs = null;
		if (conn == null)
			conn = this.getConn();
		try {
			ps = conn.prepareStatement(sql);
			for(int i=0;i<args.length;i++) {
				ps.setString(i+1,args[i]);
			}
			rs=ps.executeQuery();
		} catch(SQLException e) {
			e.printStackTrace();
		}
		return rs;
	}
	public ResultSet getResult(String sql) {
		rs = null;
		if (conn == null)
			conn = this.getConn();
		try {
			stat = conn.createStatement();
			rs=stat.executeQuery(sql);
		} catch(SQLException e) {
			e.printStackTrace();
		}
		return rs;
	}
	public int update(String sql) {
		if (conn == null)
			conn = this.getConn();
		try {
			stat = conn.createStatement();
			return stat.executeUpdate(sql);
		} catch(SQLException e) {
			e.printStackTrace();
		}
		return 0;
	}
	public int update(String sql, String []args) {
		if (conn == null)
			conn = this.getConn();
		try {
			ps = conn.prepareStatement(sql);
			for(int i=0;i<args.length;i++) {
				ps.setString(i+1,args[i]);
			}
			return ps.executeUpdate();
		} catch(SQLException e) {
			e.printStackTrace();
		}
		return 0;
	}
}
