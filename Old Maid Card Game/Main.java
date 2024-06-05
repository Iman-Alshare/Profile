import java.util.Scanner;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        System.out.print("Enter number f players: ");
        int numOfPlayers = sc.nextInt();
        while(numOfPlayers<2 || numOfPlayers>8){
            System.out.print("Enter number f players: ");
            numOfPlayers = sc.nextInt();
        }
        OldMaidGame game = GameFactory.getGameInstance(numOfPlayers);//2 + (int) (Math.random() * 7));
        game.start();
        }
}