package imooc_collection;

import java.util.ArrayList;
import java.util.List;

public class testgeneric {
	
	public List<course> courses;
	
	public testgeneric() {
		this.courses = new ArrayList<course>();
	}
	
	public void testadd() {
		course cr1 = new course("1","数学");
		courses.add(cr1);
//		courses.add("添加字符串");
		course cr2 = new course("2","语文");
		courses.add(cr2);
	}
	public void foreach() {

		System.out.println("课程为：");
		for(course cr:courses) {
			System.out.println(cr.id+cr.name);
		}
	}
	public void testchild() {
		childcourse ccr = new childcourse();
		ccr.id="3";
		ccr.name="子类";
		courses.add(ccr);
	}
	public void testbasictype() {
		List<Integer> list =new ArrayList<Integer>();
		list.add(1);
		System.out.println(list.get(0));
	}
	public static void main(String[] args) {
		testgeneric tg = new testgeneric();
		tg.testadd();
		tg.testchild();
		tg.foreach();
		tg.testbasictype();
	}
	
}
