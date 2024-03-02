import java.util.Scanner;

public class Main {
	public static void main (String[] args) {

		Scanner input = new Scanner(System.in);

		Double a = input.nextDouble();
		Double b = input.nextDouble();
		input.close();

		Double result = 100*(b-a)/a;
		System.out.println(String.format("%.2f", result) + "%");
	}
}
