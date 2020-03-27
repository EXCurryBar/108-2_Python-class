import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Invoice {
    public static String data = "";

    public static void main(String[] args) {
        final cr c = new cr();
        c.start();
        try {
            c.join();
        } catch (InterruptedException e) {
            System.out.println(e.toString());
        }
        System.out.println(data.length() == 0 ? "no data" : data);
    }
}

class cr extends Thread {
    String r;
    Pattern pattern = Pattern.compile("<description>.*</description>");

    public void run() {
        try {
            URL url = new URL("http://invoice.etax.nat.gov.tw/invoice.xml");
            HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
            int responseCode = urlConnection.getResponseCode();
            if (responseCode == 200) {
                BufferedReader reader = new BufferedReader(
                        new InputStreamReader(urlConnection.getInputStream(), "utf-8"));
                if ((r = reader.readLine()) != null) {
                    Matcher matcher = pattern.matcher(r);
                    if (matcher.find()) {
                        // System.out.println(matcher.group());
                        Invoice.data = matcher.group();
                    }
                }
            } else {
                System.out.println("ResponseCode : " + responseCode);
            }
        } catch (Exception e) {
            System.out.println(e.toString());
        }
    }
}