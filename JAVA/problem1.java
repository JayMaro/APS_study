package Problem.src.problem1;

import java.util.ArrayList;
import java.util.Scanner;


public class problem1 {
	
	public static void main(String[] args) {
		
		Student std1 = new Student("�踶��", "2014310703");
		Student std2 = new Student("�踶��", "2014310704");
		Student std3 = new Student("�踶��", "2014310705");
		ArrayList <Student> lst = new ArrayList <Student>();
			
		lst.add(std1);
		lst.add(std2);
		lst.add(std3);
			
		for (Student std: lst) {
			System.out.println(std.getName());
			System.out.println(std.getNo());
		}
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("��� �˻��� �ϰ� �ʹٸ�y, �����ϰ� �ʹٸ� n");
		
		
		while (true) {
			String input = sc.next();
			
			if (input.equals("y")) {
				System.out.println("�˻�����");
				String name = sc.next();
				boolean flag = false;
				
				for (Student std: lst) {
					if (std.getName().equals(name)) {
						System.out.println("�й���: "+ std.getNo());
						flag = true;
					}
				
				}
				
				if (!flag) {
					System.out.println("�����ϴ�.");
				}
			}
			else if (input.equals("n")) {
				break;
			}
		}
		System.out.println("���α׷� ����");
	}
}
