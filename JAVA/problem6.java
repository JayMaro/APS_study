package problem;

import java.util.Scanner;

public class problem6 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt();
		int y = sc.nextInt();
		if (x < y) {
			int tmp;
			tmp = x;
			x = y;
			y = tmp;
		}
		
		int gcd = 0;
		while (true) {
			if (x % y == 0) {
				gcd = y;
				break;
			} else {
				int tmp = x % y;
				x = y;
				y = tmp;
			}
		}
		System.out.println(gcd);
		
	}
}
