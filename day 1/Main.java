import java.io.*;
import java.util.*;
// part 1
public class Main {
    public static void main(String[] args){
        System.out.println("Part 1: " + part1());
        System.out.println("Part 2: " + part2());
    }
    public static int part1(){
        int sum = 0;
        try {
            File input = new File("input.txt");
            Scanner reader = new Scanner(input);
            while (reader.hasNextLine()){
                String line = reader.nextLine();
                String number = "";
                int i = 0;
                while (!Character.isDigit(line.charAt(i))){
                    i++;
                }
                number = number + line.charAt(i);
                i = line.length()-1;
                while (!Character.isDigit(line.charAt(i))){
                    i--;
                }
                number = number + line.charAt(i);
                sum += Integer.parseInt(number);
            }
            reader.close();
        } catch(FileNotFoundException e) {
            e.printStackTrace();
        }
        return sum;
    }
    private static String checkNumber(String line, int index){
            if (index+3 <= line.length() && line.substring(index, index+3).equals("one")){
                return "1";
            }
            else if (index+3 <= line.length() && line.substring(index, index+3).equals("two")){
                return "2";
            }
            else if (index+5 <= line.length() &&line.substring(index, index+5).equals("three")){
                return "3";
            }
            else if (index+4 <= line.length() &&line.substring(index, index+4).equals("four")){
                return "4";
            }
            else if (index+4 <= line.length() && line.substring(index, index+4).equals("five")){
                return "5";
            }
            else if (index+3 <= line.length() && line.substring(index, index+3).equals("six")){
                return "6";
            }
            else if (index+5 <= line.length() && line.substring(index, index+5).equals("seven")){
                return "7";
            }
            else if (index+5 <= line.length() && line.substring(index, index+5).equals("eight")){
                return "8";
            }
            else if (index+4 <= line.length() && line.substring(index, index+4).equals("nine")){
                return "9";
            }
            return "null";
        }
    public static int part2(){
        
        int sum = 0;
        try {
            File input = new File("input.txt");
            Scanner reader = new Scanner(input);
            while (reader.hasNextLine()){
                String line = reader.nextLine();
                String number = "";
                int i = 0;
                while (!Character.isDigit(line.charAt(i))){
                    if (checkNumber(line, i) != "null"){
                        number = number + checkNumber(line, i);
                        break;
                    }
                    i++;
                }
                if (Character.isDigit(line.charAt(i))){
                    number = number + line.charAt(i);
                }
                i = line.length()-1;
                while (!Character.isDigit(line.charAt(i))){
                    if (checkNumber(line, i) != "null"){
                        number = number + checkNumber(line, i);
                        break;
                    }
                    i--;
                }
                if (Character.isDigit(line.charAt(i))){
                    number = number + line.charAt(i);
                }
                // tests
                // System.out.println("Line: " + line);
                // System.out.println("Number obtained: " + number);
                sum += Integer.parseInt(number);
            }
            reader.close();
        } catch(FileNotFoundException e) {
            e.printStackTrace();
        }
        return sum;
    }
}