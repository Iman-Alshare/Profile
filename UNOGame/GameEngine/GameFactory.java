package GameEngine;

import Player.Player;
import UNO.*;
import Utils.Utils;

import java.util.ArrayList;

public class GameFactory {

    public Game createGame(String UnoVariation){
        ArrayList<Player> players = Utils.ScanPlayer();
        if (UnoVariation.equalsIgnoreCase("ClassicalUNO")){
           return new ClassicalUNOGame(7, players);
        }
       return null; // add new uno variation
    }
}
