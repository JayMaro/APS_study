package problem;


import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class problem7 {
    public static void main(String[] args) {
        int numbers[] = new int[10001];
        List<Integer> prime = new ArrayList<>();
        prime.add(2);
        for (int i=3; i<=100; i++) {
            if (numbers[i] == 0) {
                prime.add(i);
                for (int j=i; j<=10000; j+=i) {
                    numbers[j] = 1;
                }
            }
        }
        for (int i=100; i<10000; i++) {
            if (numbers[i] == 0) {
                prime.add(i);
            }
        }
        System.out.println(prime);

        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        if (prime.contains(x)) System.out.println(x+"는 소수입니다.");
        else System.out.println(x+"는 소수가 아닙니다.");

    }
}
