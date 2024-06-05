package UNO;

import Card.*;
import java.util.*;

public class ClassicalUnoDeck extends Deck {

    public ClassicalUnoDeck() {
        this.deckCards = new LinkedList<>();
        this.discardedCards = new Stack<>();
        deckInitialization();
    }

    @Override
    protected void deckInitialization() {
        for (int colortIdx = 0; colortIdx < CardColor.getLength() - 1; colortIdx++) {
            this.setDeckCard(new Card(NumberCard.getValue(0).name(), CardColor.getValue(colortIdx).name()));
            for (int cardIdx = 1; cardIdx < NumberCard.getLength(); cardIdx++) {
                this.setDeckCard(new Card(NumberCard.getValue(cardIdx).name(), CardColor.getValue(colortIdx).name()));
                this.setDeckCard(new Card(NumberCard.getValue(cardIdx).name(), CardColor.getValue(colortIdx).name()));
            }

            for (int cardIdx = 0; cardIdx < 3; cardIdx++) {
                this.setDeckCard(new Card(SpecialCard.getValue(cardIdx).name(), CardColor.getValue(colortIdx).name()));
                this.setDeckCard(new Card(SpecialCard.getValue(cardIdx).name(), CardColor.getValue(colortIdx).name()));
            }
        }
        for (int cardIdx = 3; cardIdx < SpecialCard.getLength(); cardIdx++) {
            for (int count = 0; count < 4; count++) {
                this.setDeckCard(new Card(SpecialCard.getValue(cardIdx).name(), CardColor.getValue(CardColor.getLength() - 1).name()));
            }
        }
        LinkedList<Card> temp = new LinkedList<>(this.deckCards);
        Collections.shuffle(temp);
        this.deckCards = temp;
        temp = null;
    }

    @Override
    protected void fillDeck() {
        copy();
        this.discardedCards.clear();
    }
}