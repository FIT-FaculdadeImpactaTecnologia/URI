import java.io.IOException;
import java.util.Scanner;
import java.lang.StringBuffer;

public class Risada {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        String vog = "aeiou";
        String rs = "", aux = "",resp = "N";

        rs = s.nextLine();

        for(int i = 0; i < rs.length() ; i++){
            if( !(vog.contains( Character.toString(rs.charAt(i)) ))){
              aux = Character.toString(rs.charAt(i)); 
              rs = rs.replace( aux , "");     
            }
        }
        StringBuffer sb = new StringBuffer(rs);

        if ( rs.equals(sb.reverse().toString())){
            resp = "S";
        }
        // else{
            // System.out.println("erro");
            // resp = "erro";
        // }       
        
        //rs = sb.reverse().toString();

        // System.out.println(sb + " " + sb.reverse());
        System.out.println(resp);
    }
}   