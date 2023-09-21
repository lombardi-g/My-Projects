class IPod {
    public void play() {
        System.out.println("Playing.");
    }

    public void pause() {
        System.out.println("Paused.");
    }

    public void selectSong(String song) {
        System.out.println("Now playing: " + song);
    }
}

class Phone {
    public void call(String phoneNumber) {
        System.out.println("Calling: " + phoneNumber);
    }

    public void answer() {
        System.out.println("Call answered.");
    }

    public void startVoiceMail() {
        System.out.println("Starting voicemail.");
    }
}

class Browser {
    public void showPage(String url) {
        System.out.println("Displaying page: " + url);
    }

    public void newTab() {
        System.out.println("Opening a new tab.");
    }

    public void refreshPage() {
        System.out.println("Refreshing the page.");
    }
}

public class IOSimulator {
    public static void main(String[] args) {
        IPod iPod = new IPod();
        iPod.play();
        iPod.pause();
        iPod.selectSong("The Beatles");

        Phone phone = new Phone();
        phone.call("12 34567-8910");
        phone.answer();
        phone.startVoiceMail();

        Browser browser = new Browser();
        browser.showPage("https://github.com/lombardi-g/");
        browser.newTab();
        browser.refreshPage();
    }
}
