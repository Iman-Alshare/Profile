package Card;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Queue;
import java.util.Stack;

public abstract class Deck {
    protected Queue<Card> deckCards ;
    protected Stack<Card> discardedCards ;
    protected abstract void deckInitialization();
    public Card getDeckCard(){
        if (deckCards.isEmpty())
            fillDeck();
        Card currentCard = deckCards.poll();
        return currentCard;
    }
    public void addToDiscard(Card currentCard){
        discardedCards.push(currentCard);
    }
    public void setDeckCard(Card card){
        deckCards.offer(card);
    }
    protected abstract void fillDeck();
    protected void copy(){
        Collections.shuffle(discardedCards);
        while (!discardedCards.empty()) {
            deckCards.offer(discardedCards.pop());
        }
    }
}
