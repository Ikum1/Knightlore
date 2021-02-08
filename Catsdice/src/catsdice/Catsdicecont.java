/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package catsdice;
import java.awt.event.MouseEvent;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.text.NumberFormat;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import java.util.Random;
import javafx.animation.PathTransition;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.image.ImageView;
import javafx.scene.shape.Circle;
import javafx.util.Duration;
import javafx.scene.shape.Line;

/**
 *
 * @author Imperator
 */
public class Catsdicecont {
    
    @FXML
    private TextField d20q;
    
    @FXML
   private TextField d20res;
    
   @FXML
   private ImageView cat;
   

   @FXML
   private void move(MouseEvent a){
   Line abcd = new Line(10,10,100,10);
           
   PathTransition moves = new PathTransition();
   moves.setDuration(Duration.seconds(3));
   moves.setNode(cat);
   
   moves.setPath(abcd);
   moves.play();
   }
   
   
           
           
  @FXML
   
    private void count(ActionEvent event){
        int resultcount = 0;
        double a = Double.parseDouble(d20q.getText());
        int d20num = (int)a;
        Random rand = new Random(); 
        int totald20 =0;
        int[] arr; 
        arr = new int[d20num];
        String allint = "";
        int temp;
        String finald20;
        

    for(int i =0; i < d20num; i++){
        temp = rand.nextInt(20)+1;
        allint = allint + " , "+ String.valueOf(temp);
        totald20 = totald20+ temp;
        }
    finald20 = allint +"( "+String.valueOf(totald20)+")";
    d20res.setText(finald20);
    
    }
          public void initialize() {

           }
    
    
    
            
            
            
}
