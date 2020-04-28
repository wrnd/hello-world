package atm;

import java.util.*;

public class Atm 
{
	static Scanner input = new Scanner(System.in);
	//系统信息
	private boolean flag;//系统继续运行
	private int u;//当前用户id
	UserDAO uDao;

	public Atm()
	{
		flag = true;
		u = -1;//未登录状态
		uDao = new UserDAO();
	}
	
	public void begin()//开始菜单
	{
		do {
			System.out.println("欢迎使用东软ATM自动提款机");
			System.out.println("请 1.登录 2.注册 3.退出");
			int n = input.nextInt();
			switch(n)
			{
			case 1:
				login();
				break;
			case 2:
				logon();
				break;
			case 3:
				logout();
				return;
			default:
				System.out.println("输入有误，请重新输入！");
				break;					
			}
		}while(-1 == u);
		

		do{
			System.out.println("请选择以下功能:\n"
					+ "1.查询 2.存款 3.取款 4.转账 5.切换账户 6.退出 ");
			int n = input.nextInt();
			switch(n)				
			{
			case 1:
				cheak();
				break;
			case 2:
				in_money();
				break;
			case 3:
				out_money();
				break;
			case 4:
				trans_moeny();
				break;
			case 5:
				login();
				break;
			case 6:
				logout();//退出
				break;
			default:
				System.out.println("输入有误，请重新输入！");
				break;
			}
		}while(flag);
	}
	
	public void login()//登录
	{
//		Scanner input = new Scanner(System.in);
		
		System.out.println("请输入用户名：");
		String name = input.next();
		System.out.println("请输入密码：");
		String password = input.next();
		 
		u = uDao.login(name, password);

		if(-1 == u)
			System.out.println("卡号、密码错误！请重试！");
		else
			System.out.println("登录成功！");			
	}
	
	public void logon()//注册
	{
		System.out.println("请输入卡号：");
		String name = input.next();
		String psw1;
		do{
			System.out.println("请输入密码：");
			psw1 = input.next();
			System.out.println("请再次输入密码：");
			String psw2 = input.next();
			if(psw1.equals(psw2))
				break;
			else
				System.out.println("两次密码输入不一致！");
		}while(true);
		
		if(uDao.logon(name, psw1))
			System.out.println("注册成功！");
		else
			System.out.println("注册失败！-已有用户注册此名！");
	}
	
	public void logout()//退出
	{
		u = -1;
		flag = false;
		System.out.println("欢迎下次使用！");
	}

	public void cheak()//查询
	{
		if(-1 == u)//检查登录状态
		{
			System.out.println("错误！-未登录！");
			return;
		}
		
		User t = uDao.check(u);
		System.out.println("****************");
		System.out.println("卡号:"+t.getId());
		System.out.println("姓名:"+t.getName());
		System.out.println("余额:"+t.getMoney());
		System.out.println("****************");
	}
	
	public void in_money()//存款
	{
		if(-1 == u)//检查登录状态
		{
			System.out.println("错误！-未登录！");
			return;
		}
		
		System.out.println("请输入存款数：");
		int t = input.nextInt();
		
		if(uDao.in_money(u, t))
		{
			System.out.println("存款成功！");
			System.out.println("当前余额为："+uDao.check(u).getMoney());
		}
		
	}
	
	public void out_money()//取钱
	{
		if(-1 == u)//检查登录状态
		{
			System.out.println("错误！-未登录！");
			return;
		}
		
		System.out.println("请输入所取金额：");
		int t = input.nextInt();		
		
		if(uDao.out_money(u, t))
			System.out.println("取出成功！");

		else
			System.out.println("取出失败！-余额不足！");
		System.out.println("当前余额为："+uDao.check(u).getMoney());
		
	}
	
	
	public void trans_moeny()//转账
	{
		if(-1 == u)//检查登录状态
		{
			System.out.println("错误！-未登录！");
			return;
		}
		
		System.out.println("请输入对方卡号：");//输入的是name
		String name = input.next();
		
		int Id = uDao.check(name).getId();
		if(-1 == Id)
		{
			System.out.println("失败！-未找到对方卡号！");
			return;
		}
		else if(Id == u)
			System.out.println("失败！-不可转账给自己！");
		else//对方卡号正确
		{
			System.out.println("请输入转账金额：");
			int t = input.nextInt();
			
			if(uDao.trans_moeny(u, Id, t))
			{
				System.out.println("转账成功！");				
				System.out.println("当前余额为："+uDao.check(u).getMoney());
			}
			else
				System.out.println("失败！-余额不足");
				return;
		}
	}
	

}

