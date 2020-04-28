	package atm;

	public class User {
		private int id;
		private String name;
		private int money;
				
		public int getId() {
			return id;
		}

		public void setId(int iD) {
			id = iD;
		}

		public String getName() {
			return name;
		}

		public void setName(String name) {
			this.name = name;
		}

		public int getMoney() {
			return money;
		}

		public void setMoney(int money) {
			this.money = money;
		}
		
		public User(int iD)//不存在的账户
		{
			id = iD;//ID == -1
			name = "";
			money = -1;
		}
		
		public User(int iD, String name, int money)
		{
			id = iD;
			this.name = name;
			this.money = money;
		}
	}

