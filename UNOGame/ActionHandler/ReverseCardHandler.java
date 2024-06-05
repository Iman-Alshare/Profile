package ActionHandler;
import GameEngine.*;
import Card.*;
public class ReverseCardHandler extends ActionHandler<Game> {
    @Override
    public void handleRequest(Game game) {
            game.reversePlayersList();
    }

}
