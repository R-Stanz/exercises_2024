import java.io.IOException;
import java.util.Scanner;
import java.util.HashSet;
import java.util.ArrayList;
 
/**
 * IMPORTANT: 
 *      O nome da classe deve ser "Main" para que a sua solução execute
 *      Class name must be "Main" for your solution to execute
 *      El nombre de la clase debe ser "Main" para que su solución ejecutar
 */
public class Main {
 
    public static void main(String[] args) throws IOException {
 
	    Scanner input = new Scanner(System.in);

	    ArrayList<Integer> queue = new ArrayList<Integer>();
	    Integer queueSize = input.nextInt();
	    for (int i = 0; i < queueSize; i++) {
		    Integer new_id = input.nextInt();
		    queue.add(new_id);
	    }

	    HashSet<Integer> exitedIds = new HashSet<Integer>();
	    Integer exitedSetSize = input.nextInt();
	    for (int i = 0; i < exitedSetSize; i++) {
		    Integer id = input.nextInt();
		    exitedIds.add(id);
	    }
	    input.close();

	    boolean printedFirstId = false;
	    for (Integer id : queue) {
		    if (!exitedIds.contains(id)) {
			    if (printedFirstId)
				    System.out.print(" ");
			    else
				    printedFirstId = !printedFirstId;
			System.out.print(id);
		    }
	    }
	    System.out.print("\n");
 
    }
 
}
