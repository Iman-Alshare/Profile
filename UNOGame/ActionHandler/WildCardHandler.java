package ActionHandler;
import Card.*;
import GameEngine.*;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Iterator;

public class WildCardHandler extends ActionHandler<Game> {
    @Override
    public void handleRequest(Game game) {
    if(isWildCard(game.getCurrentCard()))
    {
        Iterator<Card> it = game.getCurrentPlayer().getCardList();
        Card card = null;
        while(it.hasNext()){
            card = it.next();
            if (card!=null)
            {
                break;
            }
        }

        if (game.getCurrentCard().getColor().equalsIgnoreCase(card.getColor()) && card.getValue().equalsIgnoreCase(SpecialCard.DRAWTwo.name())) {
            new DrawTwoCardHandler().handleRequest(game);
        } else if (game.getCurrentCard().getColor().equalsIgnoreCase(card.getColor()) && card.getValue().equalsIgnoreCase(SpecialCard.SKIP.name())) {
            new SkipCardHandler().handleRequest(game);
        } else if (card.getColor().equalsIgnoreCase(game.getCurrentCard().getColor()) && card.getValue().equalsIgnoreCase(SpecialCard.REVERSE.name())) {
            new ReverseCardHandler().handleRequest(game);
        }
        else{
            game.addToDiscard(game.getCurrentCard());
            game.setCurrentCard(card);
            game.notifyUpdate();
        }
        game.getCurrentPlayer().puttedCard(card);
        game.getCurrentPlayer().puttedCard(card);
        if (game.getCurrentPlayer().getCardListSize()==1)
            game.getCurrentPlayer().sayUNO();
        if (game.getCurrentPlayer().getCardListSize()==0)
            game.setWinner();
        return;
    }
    if(nextHandler!=null)
    {
        nextHandler.handleRequest(game);
    } else
        System.out.println("Request cannot be handled");
}
    private boolean isWildCard(Card currentCard){
        return currentCard.getValue().equalsIgnoreCase(CardColor.WILD.name());
    }

}
