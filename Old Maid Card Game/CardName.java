public enum CardName {
    KING,
    QUEEN,
    JACK,
    ACE,
    TWO,
    THREE,
    FOUR,
    FIVE,
    SIX,
    SEVEN,
    EIGHT,
    NINE,
    TEN;
    final static CardName[]values = CardName.values();
    public static int getLength(){return values.length;}
    public static CardName getValue(int idx){return values[idx];}
}
