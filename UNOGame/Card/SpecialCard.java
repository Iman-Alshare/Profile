package Card;

public enum SpecialCard {
    REVERSE,
    SKIP,
    DRAWTwo,
    WILD,
    WILDFour;
    final static SpecialCard [] values = SpecialCard.values();
    public static SpecialCard getValue(int idx){return values[idx];}
    public static int getLength(){return values.length;}
}
