package Dao;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;
import java.sql.*;
import java.util.*;
import Bean.Client;
import Db.connectDb;
/**
 * 实现文章的增加、删除、更新、添加等操作
 * @author Administrator
 *
 */

public class UserDao {
		PreparedStatement ps = null;
		connectDb con=new connectDb();
		ResultSet rs=null;
		
//添加功能	
		
public boolean register(Client client) {
    String sql ="insert into client (username,password,email) value(?,?,?)";
    int n =0;
    try{
	ps = con.getConn().prepareStatement(sql);
	ps.setString(1, client.getUsername());
	ps.setString(2, client.getPassword());
	ps.setString(3, client.getEmail());
	n=ps.executeUpdate();
	}catch (Exception e) {
	    e.printStackTrace();
	}
	 return n>0;
		}
}