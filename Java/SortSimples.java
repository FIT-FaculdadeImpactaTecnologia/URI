/*
Leia 3 valores inteiros e ordene-os em ordem crescente. OK
No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.
*/
import java.util.Scanner;
import java.io.IOException;
public class SortSimples {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        int[] arr = new int[3];
        // int[] arr2 = new int[3];
        int aux = 0;
        String ex = "";
        ex = s.nextLine();

        String strArr[] = ex.split(" "); 

        arr[0] = Integer.parseInt(strArr[0]);
        arr[1] = Integer.parseInt(strArr[1]);
        arr[2] = Integer.parseInt(strArr[2]);

        int[] arrOr = new int[3];    
        // arr[0] = s.nextInt();
        // arr[1] = s.nextInt();
        // arr[2] = s.nextInt();
        for(int i = 0 ; i < 3 ; i++ ){
            arrOr[i] = arr[i];
        }    

        for(int i = 0 ; i < 3 ; i++ ){
        
            for(int j = i + 1 ; j < 3 ; j++ ){
                if(arr[i] > arr[j]){
                    aux = arr[i];
                    arr[i] = arr[j];
                    arr[j] = aux;
                }      
            }
            
        }
        

        for(int i = 0 ; i < 3 ; i++ ){
            System.out.println(arr[i]);
        }

        System.out.println("");
        
        for(int i = 0 ; i < 3 ; i++ ){
            System.out.println(arrOr[i]);
        }

        

        //System.out.println("SOMA = " + soma);
    }
}