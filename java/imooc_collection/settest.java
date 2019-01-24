package imooc_collection;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class settest {
	
	public List<course> coursetoselect;
	
	private Scanner console;
	
	public student student00;
	
	public settest() {
		coursetoselect = new ArrayList<course>();
		console=new Scanner(System.in);
	}
	public void testadd() {
		course cr1=new course("1","数学");
		coursetoselect.add(cr1);
		course temp = (course) coursetoselect.get(0);
		System.out.println(temp.id+temp.name);
		
		course cr2=new course("2","语文");
		coursetoselect.add(0,cr2);
		course temp2 = (course) coursetoselect.get(0);
		System.out.println(temp2.id+temp2.name);
		
		course cr3=new course("3","地理");
		coursetoselect.add(2,cr3);
		course temp3 = (course) coursetoselect.get(2);
		System.out.println(temp3.id+temp3.name);
		
		
	
	}
	public void foreach() {

		System.out.println("课程为：");
		for(Object obj:coursetoselect) {
			course cr = (course) obj;
			System.out.println(cr.id+cr.name);
		}
	}
	
	public static void main(String[] args) {
		settest st = new settest();
		st.testadd();
		st.foreach();
//		student student0 = new student("0","小明");
//		System.out.println("欢迎学生："+student0.name+"选课");
//		
//		Scanner console = new Scanner(System.in);
//		for(int i =0;i<3;i++) {
//			System.out.println("输入课程id");
//			String courseid=console.next();
//			for(course cr : st.coursetoselect) {
//				if(cr.id.equals(courseid)) {
//					student0.courses.add(cr);
//					student0.courses.add(cr);	
//				}
//			}
//		}
//		st.stforeach(student0);
//		st.testlistcontains();
		st.createstudentandselectcourse();
		

	}
	public void stforeach(student student0) {
		System.out.println(student0.courses.size());
		for(course cr : student0.courses) {
			System.out.println("学生选择的课程为："+cr.id+cr.name);
		}
	}
	public void testlistcontains() {
		course course0 = coursetoselect.get(0);
		System.out.println("课程"+course0.name);
		System.out.println("课程"+course0.name+
				coursetoselect.contains(course0));
		course cr1=new course(course0.id,course0.name);
		System.out.println("课程"+cr1.name);
		System.out.println("课程"+cr1.name+
				coursetoselect.contains(cr1));
		
		System.out.println("输入课程名称");
		String name = console.next();
		course cr2=new course();
		cr2.name = name;
		System.out.println("课程"+cr2.name);
		System.out.println("课程"+cr2.name+
				coursetoselect.contains(cr2));
	}
	public void createstudentandselectcourse() {
		student student0 = new student("0","小明");
		System.out.println("欢迎学生："+student0.name+"选课");
		for(int i =0;i<3;i++) {
			System.out.println("输入课程id");
			String courseid=console.next();
			for(course cr : coursetoselect) {
				if(cr.id.equals(courseid)) {
					student0.courses.add(cr);
					student0.courses.add(cr);	
				}
			}
		}
		stforeach(student0);
		testsetcontains(student0);
	}
	public void testsetcontains(student student0) {
		System.out.println("输入已选择的课程名称");
		String name=console.next();
		course course2=new course();
		course2.name = name;
		System.out.println("课程："+course2.name);
		System.out.println("课程："+course2.name+student0.courses.contains(course2));

		if(coursetoselect.contains(course2))
			System.out.println("课程\""+course2.name+"\"的索引位置为："+coursetoselect.indexOf(course2));
	}

}
