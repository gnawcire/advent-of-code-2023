import java.util.*;
import java.io.*;

public class Main {
  public static void main(String[] args) {
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
        String gameID = line.split(":")[0].substring(5);
        String[] rounds = line.split(":")[1].split(";");
        // System.out.println(gameID);
        Boolean valid = true;
        for (String round : rounds){
          // System.out.println(round);
          String[] scores = round.split(",");
          for (String score : scores){
            // System.out.println(score);
            // System.out.println(score.split(" ")[1]);
            if (score.contains("red")){
              if (Integer.parseInt(score.split(" ")[1]) > 12){
                valid = false;
              }
            } else if (score.contains("blue")){
              if (Integer.parseInt(score.split(" ")[1]) > 14){
                valid = false;
              }
            } else if (score.contains("green")){
              if (Integer.parseInt(score.split(" ")[1]) > 13){
                valid = false;
              }
            }
          }
        }
        if (valid){
          sum += Integer.parseInt(gameID);
        }
      }
    } catch (FileNotFoundException e) {
      e.printStackTrace();
    }
    return sum;
  }
  public static int part2(){
    int power = 0;
    try {
      File input = new File("input.txt");
      Scanner reader = new Scanner(input);
      while (reader.hasNextLine()){
        String line = reader.nextLine();
        int maxBlue = 0;
        int maxGreen = 0;
        int maxRed = 0;
        String[] rounds = line.split(":")[1].split(";");
        for (String round : rounds){
          // System.out.println(round);
          String[] scores = round.split(",");
          for (String score : scores){
            // System.out.println(score);
            // System.out.println(score.split(" ")[1]);
            if (score.contains("red")){
              if (Integer.parseInt(score.split(" ")[1]) > maxRed){
                maxRed = Integer.parseInt(score.split(" ")[1]);
              }
            } else if (score.contains("blue")){
              if (Integer.parseInt(score.split(" ")[1]) > maxBlue){
                maxBlue = Integer.parseInt(score.split(" ")[1]);
              }
            } else if (score.contains("green")){
              if (Integer.parseInt(score.split(" ")[1]) > maxGreen){
                maxGreen = Integer.parseInt(score.split(" ")[1]);
              }
            }
          }
        }
        power += maxBlue*maxGreen*maxRed;
      }
    } catch (FileNotFoundException e) {
      e.printStackTrace();
    }
    return power;
  }
}