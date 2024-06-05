package GameEngine;

import Card.Card;
import Player.Player;
import Card.Deck;
import UNO.ClassicalUnoDeck;
import ActionHandler.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.concurrent.TimeUnit;
public abstract class Game {
    protected final int INIT_CARDS;
    protected ActionHandler<Game> cardHandler;
    protected Deck tableCards;
    protected ArrayList<Player>players;
    protected Card currentCard;
    protected int currentPlayerIndex;
    protected boolean winner = false;
    public void setPlayerIndex(int skipCount)
    {
        currentPlayerIndex = (Math.abs(currentPlayerIndex+skipCount))%players.size();
    }
    public void setWinner(){winner=!winner;}
    public Game(int INIT_CARDS,ArrayList<Player>players){

        this.INIT_CARDS = INIT_CARDS;
        tableCards = new ClassicalUnoDeck();
        this.players = new ArrayList<>();
        currentPlayerIndex = 0;
        this.players.addAll(players);
    }
    protected abstract void setCardHandler();
    public void setCurrentCard(Card card){currentCard = card;}
    public Card getCurrentCard(){return currentCard;}

    public abstract void play() throws InterruptedException;
    protected abstract void distributeCards();
    public void notifyUpdate() {
        System.out.println("\n--------------------\nNotify Players: ");
        for (Player player : players) {
            player.update(currentCard);
        }
    }
    public void notifyWinner() {
        System.out.println("\n--------------------\nNotify Players whose wins: ");
        setPlayerIndex(-1);
        for (Player player : players) {
            player.updateWinner(players.get(currentPlayerIndex).getName());
        }
    }
    public Player getCurrentPlayer() {
        return players.get(currentPlayerIndex);
    }
    public void sleep(){
        TimeUnit timeUnit = TimeUnit.SECONDS;
        long sleepTimeInSeconds = 10;
        try {
            timeUnit.sleep(sleepTimeInSeconds);
        }catch(InterruptedException  e) {}

    }
    public void reversePlayersList()
    {
        Collections.reverse(players);
        currentPlayerIndex = (players.size()-currentPlayerIndex-1);
    }

    public Card drawCardFromDeck(){
        return tableCards.getDeckCard();
    }
    public void addToDiscard(Card card){
        tableCards.addToDiscard(card);
    }
}
