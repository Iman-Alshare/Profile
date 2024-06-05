import java.util.HashMap;

public class Card {
    private final String name;
    private final String type;
    private final static HashMap<String, String> typeMap = new HashMap<String, String>();
    public Card(String name, String type){
        this.name = name;
        this.type = type;
        typeMap.put("Spades", "Clubs");
        typeMap.put("Diamonds", "Hearts");
        typeMap.put("Clubs", "Spades");
        typeMap.put("Hearts", "Diamonds");
        typeMap.put("Joker","Joker");

    }
   public Boolean Equal(Card another){
        return name.equalsIgnoreCase(another.name) && typeMap.get(type).equalsIgnoreCase(another.type);
   }

    @Override
    public String toString() {
        return "name='" + name + '\'' + ", type='" + type + '\'' ;
    }


}
