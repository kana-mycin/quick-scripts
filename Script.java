/* Strips autograder emails of line numbering. For use with integration tests
*  and stingy autograders.
*/
import java.io.PrintWriter;
import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;

public class Script {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the name of the file to process: ");
        String test = input.nextLine();
        try {
            Scanner s = new Scanner(new File(test));
            PrintWriter writer = new PrintWriter(test + "-clean");
            while (s.hasNextLine()) {
                String line = s.nextLine();
                int space = line.indexOf(" ");
                if (space == -1) {
                    writer.println();
                } else {
                    if (space == 0) {
                        space = line.substring(2).indexOf(" ") + 2;
                    }
                    writer.println(line.substring(space + 1));
                }
            }
            writer.close();
            s.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found.");
        }
    }

}