package Bean;

public class Movie {
	private String id;
	private String name;
	private String address;
	private String type;
	private String time;
	private String date;

	public Movie(String id, String name, String address, String type, String time, String date) {
		super();
		this.id = id;
		this.name = name;
		this.address = address;
		this.type = type;
		this.time = time;
		this.date = date;
	}
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getAddress() {
		return address;
	}
	public void setAddress(String address) {
		this.address = address;
	}
	public String getType() {
		return type;
	}
	public void setType(String type) {
		this.type = type;
	}
	public String getTime() {
		return time;
	}
	public void setTime(String time) {
		this.time = time;
	}
	public String getDate() {
		return date;
	}
	public void setDate(String date) {
		this.date = date;
	}

}
