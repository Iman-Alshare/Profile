package UNO;

import Card.SpecialCard;
import GameEngine.Game;
import Player.Player;
import ActionHandler.*;
import java.util.ArrayList;

public class ClassicalUNOGame extends Game {
    public ClassicalUNOGame(int INIT_CARDS, ArrayList<Player> players){
    super(INIT_CARDS,players);
        System.out.println("Game is started!");
        distributeCards();
        currentCard = tableCards.getDeckCard();
        // don't want to start with skip, reverse or draw+2 cards
        while(currentCard.getValue().equalsIgnoreCase(SpecialCard.SKIP.name())|| currentCard.getValue().equalsIgnoreCase(SpecialCard.DRAWTwo.name()) || currentCard.getValue().equalsIgnoreCase(SpecialCard.REVERSE.name())) {
            tableCards.setDeckCard(currentCard);
            currentCard = tableCards.getDeckCard();
        }
        setCardHandler();
    }
    @Override
    protected void setCardHandler() {
        cardHandler = new NumberCardHandler();
        ActionHandler<Game> handler2 = new WildCardHandler();
        ActionHandler<Game> handler3 = new WildFourCardHandler();
        cardHandler.setNext(handler2);
        handler2.setNext(handler3);
    }

    @Override
    public void play()  {
        while (!winner){
            System.out.println(players.get(currentPlayerIndex));
            System.out.println("Current Card on table is :"+currentCard);
            cardHandler.handleRequest(this);
            currentPlayerIndex = (currentPlayerIndex+1)%players.size();
            sleep();
        }
        notifyWinner();
    }
    @Override
    protected void distributeCards() {
        for (int count=0;count<INIT_CARDS;count++){
        for(Player player : players){
            player.drawCard(tableCards.getDeckCard());
           }
        }
    }
}
