import java.util.ArrayList;

public class Player {
    int  id;
    ArrayList<Card> ownCards;
    public Player(int id){
        this.id = id;
        ownCards = new ArrayList<>();
    }
    public void addCard(Card card) {
        this.ownCards.add(card);
    }
    public int getCardListLength(){
        return ownCards.size();
    }
    public Card getCard(){
        int idx = (int) (Math.random() * ownCards.size());
        Card c = ownCards.get(idx);
        ownCards.remove(idx);
        return c;
    }
    public boolean matchPair(Card card){

        for (int idx =0;idx<getCardListLength();idx++) {
            if (card.Equal(ownCards.get(idx))) {
                System.out.println(("Player " + id + " has matched pair: " + card + " and " + ownCards.get(idx)));
                ownCards.remove(idx);
                return true;
            }
        }
        ownCards.add(card);
        return false;
    }

    public void matchingPairs(){

        for (int i = 0; i < ownCards.size(); i++) {
            Card card1 = ownCards.get(i);

            for (int j = i + 1; j < ownCards.size(); j++) {

                Card card2 = ownCards.get(j);

                if (card1.Equal(card2)) {

                    System.out.println(("Player " + id + " has matched pair: " + card1 + " and " + card2));

                    ownCards.remove(j);
                    ownCards.remove(i);

                    i--;

                    break;
                }
            }
        }
    }
}
