public enum CardType {
    Spades,
    Clubs ,
    Diamonds,
    Hearts;
    final static CardType[]values = CardType.values();
    public static int getLength(){return values.length;}
    public static CardType getValue(int idx){return values[idx];}
}
