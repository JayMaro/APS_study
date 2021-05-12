package Problem.src.problem3;

import java.util.Scanner;
import java.util.Arrays;

public class problem3 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] num_lst = new int[10];
		for (int i=0; i<10; i++) {
			num_lst[sc.nextInt()] += 1;
		}
		System.out.println(Arrays.toString(num_lst));
	}
}
