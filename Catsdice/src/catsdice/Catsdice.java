/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package catsdice;

import java.awt.event.MouseEvent;
import javafx.application.Application;
import static javafx.application.Application.launch;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;



/**
 *
 * @author Imperator
 */
public class Catsdice extends Application {
   @Override
   public void start(Stage stage) throws Exception {
      Parent Root = 
         FXMLLoader.load(getClass().getResource("Catsdice.fxml"));
      
     Scene scene = new Scene(Root); // attach scene graph to scene
     stage.setTitle("Catsdice"); // displayed in window's title bar
     stage.setScene(scene); // attach scene to stage
     stage.show(); // display the stage
   }
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        launch(args); 
    }
    
}