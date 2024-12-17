import java.io.File;
import java.awt.image.BufferedImage;
import java.awt.Color;
import java.util.Arrays;
import javax.imageio.ImageIO;

public class SeamCarving{
    // Attribut représentant l'image comme une matrice de pixels
    int[][] pixels;

    // Constructeur initialisant pixels à partir du nom
    // d'un fichier représentant une image au format PNG
    public SeamCarving(String fileName){
        try{
            
            BufferedImage img=ImageIO.read(new File(fileName));
            int width = img.getWidth();
            int height = img.getHeight();
            pixels = new int[height][width];
            for (int i = 0; i < width; i++) {
                for (int j = 0; j < height; j++) {
                    pixels[j][i] = img.getRGB(i, j) & 0xFF;
                }
            }
        }catch(Exception e){
            System.out.println("Erreur lors du chargement de \""+fileName+"\" : "+e);
        }
    }

    // Complexité : O(n carré) avec n = m*p les dimensions de tab
    public double max2DArray(double[][] tab){
        double currentMax = tab[0][0];

        for(int i = 0; i < tab.length; i++){
            for(int j = 0; j < tab[0].length; j++){
                if (tab[i][j] > currentMax){
                    currentMax = tab[i][j];
                }
            }
        }

        return currentMax;
    }

    // Complexité : O(n) avec n = la dimension de tab
    public double minArray(double[] tab){
        double currentMin = tab[0];

        for(int i = 0; i < tab.length; i++){
            if (tab[i] < currentMin){
                currentMin = tab[i];
            }
        }

        return currentMin;
    }

    // Complexité : O(n) avec n = m*p les dimensions de tab
    public void fillBorder(double[][] tab, double x){
        // remplace les contours de l'image tab par
        // la valeur x

        for (int i = 0; i < tab[0].length-1; i++){
            tab[0][i] = x;
            tab[tab.length-1][i] = x;
        }
        for (int i = 0; i < tab.length; i++){
            tab[i][0] = x;
            tab[i][tab[0].length-1] = x;
        }
    }

    // Complexité : O(n carré) avec n la complexité avec n = m*p les dimensions de pixels
    public double[][] energie(){
        double[][] res = new double[pixels.length][pixels[0].length];   // Matrice contenant les énergies de chaque pixel

        for (int i = 1; i < pixels.length-1; i++){
            for (int j = 1; j < pixels[i].length-1; j++){
                res[i][j] = Math.sqrt(Math.pow(pixels[i][j-1] - pixels[i][j+1], 2) + Math.pow(pixels[i-1][j] - pixels[i+1][j], 2));
            }
        }

        double maxEnergy = max2DArray(res);      // Maximum des valeurs de la matrice d'énergie
        fillBorder(res, maxEnergy);     // Affecte aux bordures la valeur maxEnergy

        return res;
    }

    // Complexité : O(n carré) avec n = m*p les dimensions de pixels
    private void suppressionNaive(){
        double[][] matriceEnergie = this.energie();

        for (int i = 0; i < matriceEnergie.length; i++) {

            double minCurrentLine = minArray(matriceEnergie[i]);

            for (int j = 0; j < pixels[i].length; j++) {
                if (matriceEnergie[i][j] == minCurrentLine){
                    this.supprimePixel(i, j);
                    break;
                }
            }
        }
    }

    // Complexité : O(...)
    public void suppressionNaiveK(int k){
        for (int i = 0; i < k; i++) {
            this.suppressionNaive();
        }
    }

    // Complexité : O(n carré) avec n = n*p les dimensions de l'image
    public double[][] tableauCouture(double[][] energies){
        // pour chaque énergie c[i][j] on part de ce pixel et on additionne la plus petite energie parmi les 3 au dessus

        double[][] c = new double[energies.length][energies[0].length];

        // On recopie la ligne du haut (cf Q7 en bas du programme)
        c[0] = Arrays.copyOf(energies[0], energies[0].length);

        // pour chaque énergie c[i][j] on part de ce pixel et on additionne la plus petite energie parmi les 3 au dessus
        for (int i = 1; i < c.length; i++) {
            for (int j = 0; j < c[0].length; j++) {
                double minAbove = 0;
                if (j == 0){    // cas de la bordure gauche
                    minAbove = minArray(new double[]{c[i - 1][j], c[i - 1][j+1]});
                } else if (j == c[0].length - 1) {  // cas de la bordure droite
                    minAbove = minArray(new double[]{c[i - 1][j-1], c[i - 1][j]});
                } else {
                    minAbove = minArray(new double[]{c[i - 1][j - 1], c[i - 1][j], c[i - 1][j + 1]});
                }

                c[i][j] = energies[i][j] + minAbove;
            }
        }

        return c;
    }

    // Complexité : O(n carré) avec n = m*p les dimensions de l'image
    public int[][] tableauCouturePrec(double[][] energies){

        int[][] prec = new int[energies.length][energies[0].length];

        // On remplit la première ligne de -1
        for (int j = 0; j < prec[0].length; j++) {
            prec[0][j] = - 1;
        }

        double[][] c = tableauCouture(energies);

        for (int i = 1; i < prec.length; i++) {
            for (int j = 0; j < prec[0].length; j++) {

                // On prend le minimum au dessus et on regarde à quel indice il correspond
                double minAbove = 0;
                if (j == 0){    // cas de la bordure gauche
                    minAbove = minArray(new double[]{c[i - 1][j], c[i - 1][j+1]});
                    if (minAbove == c[i-1][j]){
                        prec[i][j] = j;
                    } else {
                        prec[i][j] = j+1;
                    }

                } else if (j == c[0].length - 1) {  // cas de la bordure droite
                    minAbove = minArray(new double[]{c[i - 1][j-1], c[i - 1][j]});
                    if (minAbove == c[i-1][j]) {
                        prec[i][j] = j;
                    } else {
                        prec[i][j] = j-1;
                    }

                } else {
                    minAbove = minArray(new double[]{c[i - 1][j - 1], c[i - 1][j], c[i - 1][j + 1]});
                    if (minAbove == c[i-1][j]) {
                        prec[i][j] = j;
                    } else if (minAbove == c[i-1][j+1]) {
                        prec[i][j] = j+1;
                    } else {
                        prec[i][j] = j-1;
                    }
                }
            }
        }

        return prec;
    }

    // Complexité : O(n) avec n la hauteur de l'image
    private int[] extractCout(int[][] prec, int j){
        int[] couture = new int[prec.length];

        couture[couture.length - 1] = j;

        for (int i = prec.length - 1; i >= 1 ; i--) {
            couture[i-1] = prec[i][j];
            j = prec[i][couture[i]];
        }

        return couture;
    }

    // Complexité : O(n) avec n la largeur de l'image
    private void supprimePixel(int i, int j){
        int[] newLine = new int[pixels[i].length - 1];

        for (int k = 0; k < newLine.length; k++) {
            if (k < j){
                newLine[k] = pixels[i][k];
            } else{
                newLine[k] = pixels[i][k+1];
            }
        }

        pixels[i] = newLine;

    }

    // Complexité : O(n carré) avec n = m*p les dimensions de l'image (on utilise
    // m fois la fonction supprimePixel en O(p) d'où O(n carré) )
    private void supprimeCouture(int[] cout){
        for (int i = 0; i < pixels.length; i++) {
            supprimePixel(i, cout[i]);
        }
    }

    // Complexité : O(n carré) avec n = m*m les dimensions de l'image
    private void supprimeCoutureMin(){

        double[][] energies = this.energie();
        int[][] prec = tableauCouturePrec(energies);
        double[][] energiesTableau = this.tableauCouture(energies);
        double[] energiesCoutures = Arrays.copyOf(energiesTableau[energiesTableau.length - 1], energiesTableau[energiesTableau.length - 1].length);


        // On prend la couture d'énergie minimale et on la supprime
        double minEnergiesCoutures = minArray(energiesCoutures);

        for (int j = 0; j < energiesCoutures.length; j++) {
            if (energiesCoutures[j] == minEnergiesCoutures){
                supprimeCouture(extractCout(prec, j));
                break;
            }
        }
    }

    // Complexité : O(n carré) avec n = k*m*p <=> k*les dimensions de l'image
    public void seamCarving(int k){
        for (int i = 0; i < k; i++) {
            this.supprimeCoutureMin();
        }
    }

    // fonction permettant d'exporter une matrice de double vers un fichier
    // fileName représentant une image au format PNG.
    //
    // (utile pour exporter la matrice des énergies)
    //
    // Si le fichier est existant, il sera écrasé, sinon il sera créé.
    public static void exportToPng(String fileName, double[][] pixs){
        int[][] pixs2 = new int[pixs.length][pixs[0].length];
        double maxi = 0.;
        for(int i=0; i<pixs.length; i++) {
            for(int j=0; j<pixs[i].length; j++) {
                maxi = Math.max(maxi, pixs[i][j]);
            }
        }
        for(int i=0; i<pixs.length; i++) {
            for(int j=0; j<pixs[i].length; j++) {
                pixs2[i][j] = (int) (255*pixs[i][j]/maxi);
            }
        }
        exportToPng(fileName, pixs2);
    }

    // fonction permettant d'exporter une matrice de int vers un fichier
    // fileName représentant une image au format PNG.
    //
    // (utile pour exporter pixels)
    //
    // Si le fichier est existant, il sera écrasé, sinon il sera créé.
    public static void exportToPng(String fileName, int[][] pixs){
        try {
            BufferedImage image = new BufferedImage(pixs[0].length, pixs.length, BufferedImage.TYPE_INT_ARGB);
            for(int i=0; i<pixs.length; i++) {
                for(int j=0; j<pixs[i].length; j++) {
                    int a = pixs[i][j];
                    Color newColor = new Color(a,a,a);
                    image.setRGB(j,i,newColor.getRGB());
                }
            }
            File output = new File(fileName);
            ImageIO.write(image, "PNG", output);
        }catch(Exception e){
            System.out.println("Erreur lors de l'export vers \""+fileName+"\" : "+e);
        }
    }

    // fonction privée auxiliaire pour toString
    private static String threeDigitInt(int n){
        if(n < 10){
            return "  "+n;
        }else if(n < 100){
            return " "+n;
        }else{
            return ""+n;
        }
    }

    // fonction permettant d'afficher la matrice pixels
    // de manière lisible
    public String toString(){
        String res = "[";
        for(int i = 0; i < pixels.length;i++){
            if(i != 0){
                res+=",\n ";
            }
            res+="[ "+threeDigitInt(pixels[i][0]);
            for(int j = 1; j < pixels[i].length;j++){
                res+=", "+threeDigitInt(pixels[i][j]);
            }
            res+=" ]";
        }
        return res+"]";
    }


    public static void main(String[] args) {
        SeamCarving carvingBird = new SeamCarving("./src/oiseau.png");
        carvingBird.seamCarving(240);
        exportToPng("oiseau_out.png", carvingBird.pixels);

    }
}

// _____Réponse aux questions_____ :
// Q6 :
// On observe un décalage incohérent entre les lignes. Cela est du
// au fait qu'on ne regarde que l'énergie minimale du pixel de chaque
// ligne sans tenir compte de sa cohérence par rapport à celui du
// dessus.
//
// Q7 :
// Tous les c[0][j] sont égales à leur propre énergie (qui est 266.2
// pour tous les c[0][j].
//
// Q8 :
// c[i][j] = c[i][j] + min(c[i-1][j-1], c[i-1][j], c[i-1][j+1]
//
// Q15 :
// On pourrait ne recalculer l'énergie que de la partie à droite
// de la couture supprimée.