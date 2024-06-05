package Card;

public class Card {
    private final String value;
    private final String color;

    public Card(String value, String color) {
        this.value = value;
        this.color = color;
    }
    public boolean isEqual(Card card){
        return this.getValue().equalsIgnoreCase(card.getValue())||this.getColor().equalsIgnoreCase(card.getColor());
    }

    public String getValue() {
        return this.value;
    }

    public String getColor() {
        return this.color;
    }
//    public abstract void action();

    @Override
    public String toString() {
        return value + '_' +color ;
    }
}
