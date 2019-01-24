package pukegame;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.Scanner;
import java.util.Set;


public class game {
	
	public Scanner console;
	public Map<String,player> players;
	public List<puke> pukepai ;
	public String[] hslist= {"红桃","黑桃","梅花","方片"};
	public List<puke> playerpuke;
	public game() {
		pukepai = new ArrayList<puke>();
		playerpuke = new ArrayList<puke>();
		this.players = new HashMap<String,player>();
		console=new Scanner(System.in);
	}
	
	public void pukeadd() {
		String hs = "";
		String dx = "";
		for (String strhs: hslist ) {
			for(int j=1;j<=13;j++) {
				hs=strhs;
				dx=j+"";
				puke pk = new puke(hs,dx);
				pukepai.add(pk);
			}
		}	
	}
	
	public void foreach() {

		System.out.println("扑克牌为：");
		for(Object obj:pukepai) {
			puke cr = (puke) obj;
			System.out.print(cr.hs+cr.dx+" ");
		}	
	}
	
	public void createplayer() {
		System.out.println("");	
		System.out.println("欢迎选手加入游戏");
		for(int i =1;i<3;i++) {
			String id = i +"";
			player per = players.get(id);
			if(per==null) {
				System.out.println("请输入第"+i+"名选手姓名");
				String name = console.next();
				player newper= new player(id, name);
				players.put(id, newper);
				System.out.println("成功添加第"+i+"名选手"+players.get(id).name);
			}else {
				System.out.println("该选手id已被占用");
				continue;
			}
		}
	}
	
	public void fapai() {
		System.out.println("开始发牌");
		
		for(int i=1;i<3;i++) {
			String stri = i +"";
			player pl = players.get(stri);
			
			if(pl !=null) {
				for(int j =0;j<2;j++) {
					puke temp=new puke();
					do {
						Random random = new Random();
						int intid = random.nextInt(52);
						temp=pukepai.get(intid);
					}while(playerpuke.contains(temp));
					playerpuke.add(temp);	
				}
			}	
		}
		int i=0;
		for(puke cr : playerpuke) {
			if(i<2)
				System.out.println("玩家1获得的牌为："+cr.hs+cr.dx);
			else
				System.out.println("玩家2获得的牌为："+cr.hs+cr.dx);
			i++;
		}
	}
	public void startgame() {
		int j=0;
		int[] temp =new int[2];
		for(int i=0;i<2;i++) {
			if(Integer.valueOf(playerpuke.get(i+j).dx).intValue()>=Integer.valueOf(playerpuke.get(i+j+1).dx).intValue()) {
				System.out.println("玩家"+(j+1)+"最大牌为："+playerpuke.get(i+j).hs+playerpuke.get(i+j).dx);
				temp[j]=Integer.valueOf(playerpuke.get(i+j).dx).intValue();
			}
				
			else {
				System.out.println("玩家"+(j+1)+"最大牌为："+playerpuke.get(i+j+1).hs+playerpuke.get(i+j+1).dx);
				temp[j]=Integer.valueOf(playerpuke.get(i+j+1).dx).intValue();
			}
			System.out.println(j);
			j++;		
		}
		if(temp[0]>temp[1])
			System.out.println("玩家1获胜");
		else
			System.out.println("玩家2获胜");
		
	}
	
	
	public static void main(String[] args) {
		game pkg = new game();
		pkg.pukeadd();
		pkg.foreach();
		pkg.createplayer();
		pkg.fapai();
		pkg.startgame();
	}

}
