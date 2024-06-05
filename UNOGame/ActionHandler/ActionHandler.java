package ActionHandler;
public abstract class ActionHandler<Game> {
    protected ActionHandler nextHandler = null;
    public void setNext(ActionHandler nextHandler){
        if(nextHandler == null)
            throw new IllegalArgumentException();
        this.nextHandler = nextHandler;
    }
    public abstract void handleRequest(Game game);
}
