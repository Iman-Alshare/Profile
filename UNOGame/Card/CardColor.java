package Card;

public enum CardColor {
    RED,
    GREEN,
    BLUE,
    YELLOW,
    WILD;
    final static CardColor[]values = CardColor.values();
    public static CardColor getValue(int idx){return values[idx];}
    public static int getLength(){return values.length;}
}