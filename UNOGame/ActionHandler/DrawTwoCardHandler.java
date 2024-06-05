package ActionHandler;
import Card.Card;
import GameEngine.*;
import Card.*;
public class DrawTwoCardHandler extends ActionHandler<Game> {
    @Override
    public void handleRequest(Game game) {
            game.setPlayerIndex(1);
            for (int draw =0;draw<2;draw++){
                Card drawedCard = game.drawCardFromDeck();
                game.getCurrentPlayer().drawCard(drawedCard);
            }
            System.out.println(game.getCurrentPlayer());
    }
}
