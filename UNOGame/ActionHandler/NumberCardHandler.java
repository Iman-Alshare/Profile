package ActionHandler;
import GameEngine.*;
import Card.*;

import java.util.Iterator;

public class NumberCardHandler extends ActionHandler<Game> {
    @Override
    public void handleRequest(Game game) {
        if (isNumberCard(game.getCurrentCard())) {
            if (!game.getCurrentPlayer().isHuman())
            {
                Card playedCard = findMatch(game);
                if (playedCard == null) {
                    playedCard = game.drawCardFromDeck();
                    if (matchCard(playedCard,game.getCurrentCard())==null) {
                        // add to player cards
                        game.getCurrentPlayer().drawCard(playedCard);
                        return;
                    }
                    else{
                    // set currentCard to playedCard
                    update(game,playedCard);
                    }
                }
                else{
                    game.getCurrentPlayer().putCard(playedCard);
                    if (game.getCurrentPlayer().getCardListSize()==1)
                        game.getCurrentPlayer().sayUNO();
                    if (game.getCurrentPlayer().getCardListSize()==0)
                        game.setWinner();
                    update(game,playedCard);
                }
            }
            return;
        }
        if (nextHandler != null) {
            nextHandler.handleRequest(game);
        } else
            System.out.println("Request cannot be handled");
    }
    private boolean isNumberCard(Card currentCard) {
        return NumberCard.contains(currentCard.getValue());
    }
    private Card findMatch(Game game) {
        Card playedCared = null;
        Iterator<Card> it = game.getCurrentPlayer().getCardList();
        while (it.hasNext()) {
            Card card = it.next();
            if (game.getCurrentCard().isEqual(card)) {
                playedCared = card;
               break;
            }
            playedCared = matchCard(card,game.getCurrentCard());
        }
        // it will return matched color and value card or last matched card
        return playedCared;
    }

    private Card matchCard(Card card, Card currentCard) {
        Card playedCared = null;
        if (card == null) return playedCared;
        if (card.isEqual(currentCard)){
            return card;
        } else if (card.getValue().equalsIgnoreCase(SpecialCard.WILDFour.name())) {
            playedCared = card;
        } else if (card.getValue().equalsIgnoreCase(SpecialCard.WILD.name())) {
            playedCared = card;
        } else if (card.getColor().equalsIgnoreCase(currentCard.getColor()) && card.getValue().equalsIgnoreCase(SpecialCard.DRAWTwo.name())) {
            playedCared = card;
        } else if (card.getColor().equalsIgnoreCase(currentCard.getColor()) && card.getValue().equalsIgnoreCase(SpecialCard.SKIP.name())) {
            playedCared = card;
        } else if (card.getColor().equalsIgnoreCase(currentCard.getColor()) && card.getValue().equalsIgnoreCase(SpecialCard.REVERSE.name())) {
            playedCared = card;
        }
        return playedCared;
    }
    private void update(Game game, Card playedCard){
        game.getCurrentPlayer().puttedCard(playedCard);
        if (playedCard.getValue().equalsIgnoreCase(SpecialCard.DRAWTwo.name())) {
            game.addToDiscard(playedCard);
            (new DrawTwoCardHandler()).handleRequest(game);
            return;
        } else if (playedCard.getValue().equalsIgnoreCase(SpecialCard.SKIP.name())) {
            game.addToDiscard(playedCard);
            (new SkipCardHandler()).handleRequest(game);
            return;
        } else if (playedCard.getValue().equalsIgnoreCase(SpecialCard.REVERSE.name())) {
            game.addToDiscard(playedCard);
            (new ReverseCardHandler()).handleRequest(game);
            return;
        }
        game.addToDiscard(game.getCurrentCard());
        game.setCurrentCard(playedCard);
        game.notifyUpdate();
    }
}