package atm;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import com.mysql.jdbc.PreparedStatement;

public class UserDAO {

	//用户信息
	private User u = null;
	//数据库信息
	String driver = "org.gjt.mm.mysql.Driver";
	String url = "jdbc:mysql://localhost:3306/wzk";
	String utf8 = "?useUnicode=true&characterEncoding=utf-8";//设置参数
	String user = "root";
	String password = "";
	//jdbc对象
	Connection con = null;
	PreparedStatement pstmt = null;
	ResultSet re = null;


	public UserDAO()
	{
		//数据库插入操作
		try{
			//1.配置驱动
			Class.forName(driver);
			//2.建立连接
			con = DriverManager.getConnection(url+utf8, user, password);
		
		}catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	/*
	 * 关闭jdbc
	 */
	public void finalize()
	{
		try
		{
			if(null != con)
				con.close();
			if(null != pstmt)
				pstmt.close();
			if(null != re)
				re.close();			
		}catch(Exception e) {
			e.printStackTrace();
		}
	}

	/*
	 * 注册
	 */
	public boolean logon(String name, String psw)
	{
		try {
		//连接后设置预置操作对象
		String sql = "insert into user(name,password,money) values(?, ?, 0)";
		pstmt = (PreparedStatement) con.prepareStatement(sql);
		//设置预置对象占位符的值
		pstmt.setString(1, name);
		pstmt.setString(2, psw);
		//执行语句
		pstmt.executeUpdate();
		
		

		}catch(Exception e) {
			return false;
		}
		return true;
	}

	/*
	 * 登录
	 */
	public int login(String name, String psw)
	{
		String sql1 = "select id from user ";
		String sql2 = "where name = ? and password = ?";

		try {
			//返回id
			pstmt = (PreparedStatement) con.prepareStatement(sql1+sql2);
			pstmt.setString(1, name);
			pstmt.setString(2, psw);
			re = pstmt.executeQuery();
			
			int flag;
			if(re.next())//匹配标志
				flag = re.getInt(1);
			else
				flag = -1;;
			
			return flag;
		}catch(Exception e) {
			e.printStackTrace();
			return -1;
		}
	}

	/*
	 * 查询信用户息_通过id
	 */
	public User check(int id)
	{
		String sql1 = "select * from user ";
		String sql2 = "where id = ?";

		try {
			pstmt = (PreparedStatement) con.prepareStatement(sql1+sql2);
			pstmt.setInt(1, id);
			re = pstmt.executeQuery();
			if(re.next())
			{
				String name = re.getString(2);
				int money = re.getInt(4);
				
				u = new User(id, name, money);
			}
			else
				u = new User(-1);
			return u;
		}catch(Exception e) {
			e.printStackTrace();
		}
		return null;
	}
	/*
	 * 查询信用户息_通过name
	 */
	public User check(String name)
	{
		String sql1 = "select * from user ";
		String sql2 = "where name = ?";

		try {
			pstmt = (PreparedStatement) con.prepareStatement(sql1+sql2);
			pstmt.setString(1, name);
			re = pstmt.executeQuery();
			if(re.next())
			{
				int id = re.getInt(1);
				int money = re.getInt(4);
				
				u = new User(id, name, money);
			}
			else
				u = new User(-1);
			return u;
		}catch(Exception e) {
			e.printStackTrace();
		}
		return null;
		
	}
	
	/*
	 * 存钱
	 */
	public boolean in_money(int id, int addm)
	{
		String sql1 = "update user set money = money + ? ";
		String sql2 = "where id = ?";

		try {
			pstmt = (PreparedStatement) con.prepareStatement(sql1+sql2);
			pstmt.setInt(1, addm);
			pstmt.setInt(2, id);
			pstmt.executeUpdate();
			
			return true;
		}catch(Exception e) {
			e.printStackTrace();
		}
		return false;

	}
	
	/*
	 * 取钱
	 */
	public boolean out_money(int id, int minusm)
	{
		String sql1 = "update user set money = money - ? ";
		String sql2 = "where id = ?";
		if(check(id).getMoney() >= minusm)
			try {
				pstmt = (PreparedStatement) con.prepareStatement(sql1+sql2);
				pstmt.setInt(1, minusm);
				pstmt.setInt(2, id);
				pstmt.executeUpdate();
	
				return true;
			}catch(Exception e) {
				e.printStackTrace();
			}
		return false;
	}
	
	public boolean trans_moeny(int mid, int yid, int money)
	{

		if(out_money(mid, money))
			if(in_money(yid, money))
				return true;
		return false;
	}
}

