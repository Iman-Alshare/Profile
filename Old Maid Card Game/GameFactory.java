import java.util.ArrayList;

public class GameFactory {

    public static OldMaidGame getGameInstance(int numOfPlayers) {
        //System.out.println("Number of player in the game is "+numOfPlayers);
        return new OldMaidGame(numOfPlayers);
    }
}
