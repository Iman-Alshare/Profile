import java.util.ArrayList;
import java.util.Collections;

public class Deck {

    ArrayList<Card> deck ;
    public Deck(){
        deck = new ArrayList<>();
        for (int nametIdx = 0; nametIdx< CardName.getLength(); nametIdx++) {
            for (int typeIdx = 0; typeIdx< CardType.getLength(); typeIdx++){
                deck.add(new Card(CardName.getValue(nametIdx).name(), CardType.getValue(typeIdx).name()));
            }
        }
        deck.add(new Card("Joker","Joker"));
        Collections.shuffle(deck);
    }
    public Card getCard(){
        int idx = deck.size()-1;
        Card card = deck.get(idx);
        deck.remove(idx);
        Collections.shuffle(deck);
        return card;
    }
    public int getDeckSize(){
        return deck.size();
    }

    public boolean isEmpty(){
        return deck.isEmpty();
    }
}
