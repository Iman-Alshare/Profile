package Player;

import Card.Card;

import java.util.ArrayList;
import java.util.Iterator;

public class Player {
    protected final String name;
    protected ArrayList<Card> cards;
    protected boolean human;
    public boolean isHuman(){return human;}
    public Player(String name, boolean human){
        this.name = name;
        cards = new ArrayList<>();
        this.human = human;
    }
    public String getName(){return name;}
    public void drawCard(Card card){cards.add(card);}
    public void putCard(Card card){cards.remove(card);};
    public Iterator<Card> getCardList(){return cards.iterator();}
    public int getCardListSize(){return cards.size();}
    public void sayUNO() {
        if(this.getCardListSize()==1){
            System.out.println("---------------\nPlayer "+name +": UNO!!");
        }
    }
    public void update(Card card){
        System.out.println("-Player: " +name +" current card on table is "+ card);
    }
    public void updateWinner(String player){
        System.out.println("-Winner player is "+ player);
    }
    public void puttedCard(Card card){
        System.out.println("-Putted Card is "+ card);
    }
    @Override
    public String toString() {
        return "-----------------------------------------\nCurrent Player name: " +
                name + '\n' +
                "cards list = " + cards;
    }
}
