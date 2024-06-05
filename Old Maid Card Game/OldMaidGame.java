import java.util.ArrayList;
import java.lang.InterruptedException;
import java.util.logging.Logger;
import java.util.logging.Level;
public class OldMaidGame{
  int numOfPlayers;
  Deck deck;
  ArrayList<Player> playersList;
  public static final Logger logger = Logger.getLogger(Main.class.getName());
  private static final Object lock = new Object();
  int currentPlayerID;
  int loserIndex;
  int totalCard;

  OldMaidGame(int numOfPlayers) {
    this.numOfPlayers = numOfPlayers;
    deck = new Deck();
    currentPlayerID = 0;
    playersList = new ArrayList<>();
    for (int idx = 0; idx < this.numOfPlayers; idx++) {
      playersList.add(new Player(idx));
    }
  }

  public void start() {

    /*
    1. run a thread to allow players picking from deck
        and find pairs in each player's card and remove
    2. run a thread to start playing by picking from previous player
     */

    Thread[] threads = new Thread [numOfPlayers];
    for (int idx=0; idx<numOfPlayers;idx++){
      int id = idx;
      threads[idx] = new Thread (() -> playerPicksFromDeck(id));
      threads[idx].start();
    }
    try {
      Thread.sleep(1000);
    } catch (InterruptedException e) {
      throw new RuntimeException(e);
    }
    synchronized (lock){
      lock.notifyAll();
    }
    for (int idx=0; idx<numOfPlayers;idx++){
        try {
          threads[idx].join();
        }
        catch(InterruptedException ex) {
          logger.log(Level.SEVERE,"Interrupt exception",ex);
        }
      }

    currentPlayerID = 0;
    for (int idx=0; idx<numOfPlayers;idx++) {
    totalCard += playersList.get(idx).getCardListLength();
    }

    for (int idx=0; idx<numOfPlayers;idx++){
      int id = idx;
      threads[idx] = new Thread (() -> playerTurn(id));
      threads[idx].start();
    }

    try {
      Thread.sleep(1000);
    } catch (InterruptedException e) {
      throw new RuntimeException(e);
    }
    synchronized (lock){
      lock.notifyAll();
    }

    for (int idx=0; idx<numOfPlayers;idx++){
      try {
        threads[idx].join();
      }
      catch(InterruptedException ex) {
        logger.log(Level.SEVERE,"Interrupt exception",ex);
      }
    }
    System.out.println("Total cards with all players is "+totalCard);
    totalCard = 0;
    System.out.println("Player "+loserIndex+ " is the loser and has card "+playersList.get(loserIndex).getCard() );
  }

  private void playerPicksFromDeck (int threadPlayerID) {
    Card card;
    while(true){
      synchronized (lock){
        while(threadPlayerID!=currentPlayerID) {
          try {
            lock.wait();
          } catch (InterruptedException ex) {
            logger.log(Level.SEVERE, "Interrupt exception", ex);
          }
        }
       if (deck.isEmpty()){
         // run match pair method and print it to the console
         currentPlayerID = (currentPlayerID + 1) % numOfPlayers;
         playersList.get(threadPlayerID).matchingPairs();
         lock.notifyAll();
         break;
       }
       else {
         card = deck.getCard();
         currentPlayerID = (currentPlayerID + 1) % numOfPlayers;
         playersList.get(threadPlayerID).addCard(card);
         lock.notifyAll();
       }
      }
    }
  }

  private void playerTurn(int threadPlayerID) {
    Card card;
    int previousPlayerID;// = (numOfPlayers + currentPlayerID - 1) % numOfPlayers;
    while(true){
      synchronized (lock){
        while(threadPlayerID!=currentPlayerID) {
          try {
            lock.wait();
          } catch (InterruptedException ex) {
            logger.log(Level.SEVERE, "Interrupt exception", ex);
          }
        }
        previousPlayerID = (numOfPlayers + currentPlayerID - 1) % numOfPlayers;
        if (totalCard==1){
          if (playersList.get(threadPlayerID).getCardListLength()==1){
            loserIndex = threadPlayerID;
          }
          // run match pair method and print it to the console
          currentPlayerID = (currentPlayerID + 1) % numOfPlayers;
          lock.notifyAll();
          break;
        }
        else {
          if (playersList.get(previousPlayerID).getCardListLength() != 0 ) {
              card = playersList.get(previousPlayerID).getCard();
              if (playersList.get(threadPlayerID).matchPair(card))
                totalCard -= 2;
          }
          currentPlayerID = (currentPlayerID + 1) % numOfPlayers;
          lock.notifyAll();
        }
        }
      }
    }
  }
