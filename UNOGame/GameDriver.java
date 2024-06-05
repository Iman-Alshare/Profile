// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
import GameEngine.GameFactory;
import GameEngine.Game;

public class GameDriver {
    public static void main(String[] args) throws InterruptedException {
    Game game = new GameFactory().createGame("ClassicalUNO");
    game.play();
    }
}