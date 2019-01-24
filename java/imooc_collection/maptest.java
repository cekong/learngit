package imooc_collection;

import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Scanner;
import java.util.Set;

public class maptest {

	public Map<String,student> students;
	
	public maptest() {
		this.students = new HashMap<String,student>();
	}
	
	public void testput() {
		Scanner	console = new Scanner(System.in);
		int i = 0 ;
		while(i<3) {
			System.out.println("请输入学生id");
			String id = console.next();
			student st = students.get(id);
			if(st==null) {
				System.out.println("请输入学生姓名");
				String name = console.next();
				student newst= new student(id, name);
				students.put(id, newst);
				System.out.println("成功添加学生"+i+students.get(id).name);
				i++;
			}else {
				System.out.println("该学生id已被占用");
				continue;
			}
		}
	}
	public void testkeyset() {
		Set<String> keyset=students.keySet();
		for(String stuid : keyset) {
			student st = students.get(stuid);
			if(st != null) {
				System.out.println("学生姓名"+st.name);
			}
		}
	}
	public void testentryset() {
		Set<Entry<String,student>> entryset = students.entrySet();
		for(Entry<String,student> entry : entryset) {
			System.out.println("key:"+entry.getKey());
			System.out.println("value:"+entry.getValue().name);
		}
	}	
	public void testdel() {
		while(true) {
			System.out.println("要删除的学生的id：");
			Scanner	console = new Scanner(System.in);
			String id = console.next();
			student st = students.get(id);
			
			if(st == null) {
				System.out.println("学生id不存在");
				continue;
			}
			students.remove(id);
			System.out.println("成功删除学生："+st.name);
			break;
		}
	}
	
	public void testmodify() {
		System.out.println("要修改的学生的id：");
		Scanner	console = new Scanner(System.in);
		while(true) {
			String id = console.next();
			student st = students.get(id);
			if(st == null) {
				System.out.println("学生id不存在,请重新输入");
				continue;
			}
			System.out.println("所对应的学生姓名"+st.name);
			System.out.println("请输入新的学生姓名");
			String name = console.next();
			student newst = new student(id,name);
			students.put(id, newst);
			System.out.println("修改成功");
			break;	
		}
		
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		maptest mp = new maptest();
		mp.testput();
		mp.testkeyset();
//		mp.testdel();
//		mp.testentryset();
//		mp.testmodify();
//		mp.testentryset();
		mp.testcontainkeyorvalue();
	}
	public void testcontainkeyorvalue() {
		Scanner	console = new Scanner(System.in);
		System.out.println("请输入学生id");
		String id = console.next();
		System.out.println("您输入学生id为"+id+",存在吗？"+students.containsKey(id));
		if(students.containsKey(id))
			System.out.println("对应的学生为“："+students.get(id).name);
		
		System.out.println("请输入学生name");
		String name = console.next();
		
		if(students.containsValue(new student(null,name)))
			System.out.println("存在学生"+name);
		else
			System.out.println("不存在学生"+name);
	}

}
