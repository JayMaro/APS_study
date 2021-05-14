package problem;

import java.util.Scanner;
import java.util.Arrays;

public class problem5 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// Áß¿ä!!+++++++++++++
		char[] arr;
		arr = sc.nextLine().toCharArray();
		// ++++++++++++++++++
		
		System.out.println(Arrays.toString(arr));
		
		for (int i=0; i<arr.length; i++) {
			if (arr[i] >= 'a' && arr[i] <= 'z') {
				arr[i] = (char)(arr[i] - 32);
			}
			else {
				arr[i] = (char)(arr[i] + 32);
			}
			
		}
		System.out.println(arr);
	}
}
