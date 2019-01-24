package pukegame;

import java.util.HashSet;
import java.util.Set;


public class player {
	public String id;
	
	public String name;
	
	public Set<puke> pukes;
	
	public player(String id,String name) {
		
		this.id=id;
		
		this.name=name;
		
		this.pukes=new HashSet<puke>();
	}
}
