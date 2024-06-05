package Utils;

import Player.Player;

import java.util.ArrayList;
import java.util.Scanner;
import Player.*;
public class Utils {
    public static ArrayList<Player> ScanPlayer(){
        ArrayList<Player> players= new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        System.out.println("Please enter player names on one line: ");
        String names = sc.nextLine();
        String[] namesArray = names.split(" ");
        for (String name : namesArray)
        {
            players.add(new Player(name,false));
        }
        if (players.size()<2 || players.size()>10){
            throw new IllegalArgumentException("Number of players must be more than 1 and less than 11");}
        return players;
    }

}
