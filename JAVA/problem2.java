package problem;

import java.util.Scanner;


public class problem2 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		int[] fibo = new int[num+1];
		fibo[1] = 1;
		fibo[2] = 1;
		for (int i = 3; i < num+1; i++) {
			fibo[i] = fibo[i-1] + fibo[i-2];
		}
		System.out.println(fibo[num]);
		
		
	}
}
