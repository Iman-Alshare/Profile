package Card;

public enum NumberCard {
    ZERO,
    ONE,
    TWO,
    THREE,
    FOUR,
    FIVE,
    SIX,
    SEVEN,
    EIGHT,
    NINE;
    final static NumberCard[]values = NumberCard.values();
    public static NumberCard getValue(int idx){return values[idx];}
    public static int getLength(){return values.length;}
    public static boolean contains(String value) {
        try {
            NumberCard.valueOf(value);
            return true;
        } catch (IllegalArgumentException e) {
            return false;
        }
    }
}
