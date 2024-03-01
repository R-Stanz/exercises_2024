import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		Integer n = input.nextInt();
		for (int i = 0; i < n; i++) {
			Integer year = input.nextInt();
			if (year < 2015) {
				Integer diff = 2015 - year;
				System.out.println(diff.toString() + " D.C.");
			}
			else {
				Integer diff = year - 2014;
				System.out.println(diff.toString() + " A.C.");
			}
		}
		input.close();
	}
}
