package Problem.src.problem4;

import java.util.Scanner;

public class problem4 {
	public static void main(String[] args) {
	
		Scanner sc = new Scanner(System.in);
		int i_num = sc.nextInt();
		int[] binary_num = new int[100];
		int i = 0;
		
		while (i_num != 0) {
			binary_num[i] = i_num % 2;
			i_num /= 2;
			i++;
		}
		
		i--;
		for (;i>=0;i--) {
			System.out.print(binary_num[i]);
		}
		
	}
	
	
}
