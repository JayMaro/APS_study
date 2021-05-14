package Problem.src.problem1;

import java.util.ArrayList;
import java.util.Scanner;


public class problem1 {
	
	public static void main(String[] args) {
		
		Student std1 = new Student("김마로", "2014310703");
		Student std2 = new Student("김마시", "2014310704");
		Student std3 = new Student("김마기", "2014310705");
		ArrayList <Student> lst = new ArrayList <Student>();
			
		lst.add(std1);
		lst.add(std2);
		lst.add(std3);
			
		for (Student std: lst) {
			System.out.println(std.getName());
			System.out.println(std.getNo());
		}
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("계속 검색을 하고 싶다면y, 종료하고 싶다면 n");
		
		
		while (true) {
			String input = sc.next();
			
			if (input.equals("y")) {
				System.out.println("검색시작");
				String name = sc.next();
				boolean flag = false;
				
				for (Student std: lst) {
					if (std.getName().equals(name)) {
						System.out.println("학번은: "+ std.getNo());
						flag = true;
					}
				
				}
				
				if (!flag) {
					System.out.println("없습니다.");
				}
			}
			else if (input.equals("n")) {
				break;
			}
		}
		System.out.println("프로그램 종료");
	}
}
