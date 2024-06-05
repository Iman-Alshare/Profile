package ActionHandler;
import GameEngine.*;
import Card.*;
public class SkipCardHandler extends ActionHandler<Game> {
    @Override
    public void handleRequest(Game game) {
            game.setPlayerIndex(1);
    }
}

