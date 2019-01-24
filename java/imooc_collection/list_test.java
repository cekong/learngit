package imooc_collection;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

public class list_test {
	public List coursetoselect;
	public list_test() {
		this.coursetoselect=new ArrayList();
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
		
		course[] course1 = {new course("4","化学"),new course("5","物理")};
		coursetoselect.addAll(Arrays.asList(course1));
		course temp4 = (course) coursetoselect.get(3);
		course temp5 = (course) coursetoselect.get(4);
		System.out.println(temp4.id+temp4.name);
		System.out.println(temp5.id+temp5.name);
		
		course[] course2 = {new course("5","英语"),new course("6","政治")};
		coursetoselect.addAll(2,Arrays.asList(course2));
		course temp6 = (course) coursetoselect.get(2);
		course temp7 = (course) coursetoselect.get(3);
		System.out.println(temp6.id+temp6.name);
		System.out.println(temp7.id+temp7.name);
	
	}
	
	public void testget() {
		int size = coursetoselect.size();
		System.out.println("课程为：");
		for(int i=0;i<size;i++) {
			course cr=(course) coursetoselect.get(i);
			System.out.println(cr.id+cr.name);
		}		
	}
	
	public void testiterator() {
		Iterator it = coursetoselect.iterator();
		System.out.println("课程为：");
		while(it.hasNext()) {
			course cr = (course) it.next();
			System.out.println(cr.id+cr.name);
		}
	}
	public void foreach() {

		System.out.println("课程为：");
		for(Object obj:coursetoselect) {
			course cr = (course) obj;
			System.out.println(cr.id+cr.name);
		}
	}
	public void testmodify() {
		System.out.println("修改为：");
		coursetoselect.set(2,new course("7","毛概"));
	}
	public void testdel() {
		System.out.println("删除为：");
		course cr = (course) coursetoselect.get(2);
		System.out.println(cr.id+cr.name);
		coursetoselect.remove(cr);
		foreach();
		coursetoselect.remove(2);
		foreach();
		course[] course0 = {(course) coursetoselect.get(3),(course) coursetoselect.get(4)};
		coursetoselect.removeAll(Arrays.asList(course0));
		foreach();
	}
	
	public static void main(String[] args) {
		list_test lt = new list_test();
		lt.testadd();
		lt.testget();
		lt.testiterator();
		lt.testmodify();
		lt.foreach();
		lt.testdel();
		
	}
}
