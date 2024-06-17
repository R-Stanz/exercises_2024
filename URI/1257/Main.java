import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		int test_cases = input.nextInt();
		int[] results = new int[test_cases];

		for (int k = 0; k < test_cases; k++) {
			int numb_of_lines = input.nextInt();

			for (int line = 0; line < numb_of_lines; line++) {
				String str = input.next();
				results[k] += hash_a_line(line, str);
			}
		}

		input.close();

		for (int i : results) {
			System.out.println(i);
		}
	}

	private static int hash_a_line(int line, String str) {
		return hash_a_line(line, str, 0, 0);
	}

	private static int hash_a_line(int line, String str, int pos, int hash) {
		if (str.length() > pos) {
			hash += (int) str.charAt(pos) - (int) 'A' + line + pos;
			return hash_a_line(line, str, pos + 1, hash);
		}
		return hash;
	}
}
