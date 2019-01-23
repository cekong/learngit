package imooc_collection;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class collectionstest {
	
	public void testsort1() {
		List<Integer> intlist = new ArrayList<Integer>();
		Random random = new Random();
		Integer k;
		for (int i=0;i<10;i++) {
			do {
				k=random.nextInt(100);
			}while(intlist.contains(k));
			intlist.add(k);
			System.out.println("成功添加整数："+k);
		}
		System.out.println("--------排序前---------");
		for (Integer integer : intlist) {
			System.out.println("元素："+integer);
		}
		Collections.sort(intlist);
		System.out.println("--------排序后---------");
		for (Integer integer : intlist) {
			System.out.println("元素："+integer);
		}
	}
	public void testsort2() {
		List<String> strlist = new ArrayList<String>();
		strlist.add("egg");
		strlist.add("color");
		strlist.add("blue");
		strlist.add("dog");
		
		System.out.println("--------排序前---------");
		for (String str : strlist) {
			System.out.println("元素："+str);
		}
		Collections.sort(strlist);
		System.out.println("--------排序后---------");
		for (String str : strlist) {
			System.out.println("元素："+str);
		}
	}
	public void testsort3() {
		List<String> strlist = new ArrayList<String>();
		Random random = new Random();
		String randomStr = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"; 
		Integer k;
		for (int i=0;i<10;i++) {
			k=random.nextInt(10);
			StringBuilder builStr = new StringBuilder(); 
			for(int j=0;j<k;j++) {
				char tempC = randomStr.charAt(random.nextInt(randomStr.length()));
				builStr.insert(j, tempC);
			}
			String tempStr = builStr.toString(); 
			strlist.add(tempStr);
		}
		
		System.out.println("--------排序前---------");
		for (String str : strlist) {
			System.out.println("元素："+str);
		}
		Collections.sort(strlist);
		System.out.println("--------排序后---------");
		for (String str : strlist) {
			System.out.println("元素："+str);
		}
	}
	public void testsort4() {
		List<student> stulist = new ArrayList<student>();
		Random random = new Random();
		stulist.add(new student(random.nextInt(10)+"","jim"));
		stulist.add(new student(random.nextInt(10)+"","lim"));
		stulist.add(new student(random.nextInt(10)+"","tom"));
		stulist.add(new student(11+"","sam"));
		System.out.println("--------排序前---------");
		for (student str : stulist) {
			System.out.println("元素："+str.name+str.id);
		}
		Collections.sort(stulist);
		System.out.println("--------id排序后---------");
		for (student str : stulist) {
			System.out.println("元素："+str.name+"，"+str.id);
		}
		System.out.println("--------name排序后---------");
		Collections.sort(stulist,new stucomparator());
		for (student str : stulist) {
			System.out.println("元素："+str.name+"，"+str.id);
		}
	}
	
	public static void main(String[] args) {
		collectionstest ct = new collectionstest();
//		ct.testsort1();
//		ct.testsort2();
//		ct.testsort3();
		ct.testsort4();
	}
}
