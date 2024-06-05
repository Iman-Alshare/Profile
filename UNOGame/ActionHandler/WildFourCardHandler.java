package ActionHandler;
import Card.*;
import GameEngine.*;

public class WildFourCardHandler extends ActionHandler<Game> {
    @Override
    public void handleRequest(Game game) {
        if(isWildFourCard(game.getCurrentCard()))
        {
            // find a match for the card
            for (int draw =0;draw<4;draw++){
                Card drawedCard = game.drawCardFromDeck();
                game.getCurrentPlayer().drawCard(drawedCard);
            }
            game.setPlayerIndex(1);
            System.out.println(game.getCurrentPlayer());
            System.out.println("Current Card on table is :"+game.getCurrentCard());
            (new WildCardHandler()).handleRequest(game);
            return;
        }
        if(nextHandler!=null)
        {
            nextHandler.handleRequest(game);
        } else
            System.out.println("Request cannot be handled");
    }
    private boolean isWildFourCard(Card currentCard){
        return currentCard.getValue().equalsIgnoreCase(SpecialCard.WILDFour.name());
    }
}