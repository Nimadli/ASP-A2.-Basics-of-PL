import java.awt.image.BufferedImage;
import java.io.File;
import javax.imageio.ImageIO;

public class MatrixSlice {
    public static void main(String[] args) throws Exception {
        BufferedImage img = ImageIO.read(new File("sample.jpg"));

        int rowStart = 100, rowEnd = 400;
        int colStart = 150, colEnd = 450;

        int width = colEnd - colStart;
        int height = rowEnd - rowStart;

        BufferedImage sliced = img.getSubimage(colStart, rowStart, width, height);

        ImageIO.write(sliced, "jpg", new File("slicedImage.jpg"));
    }
}
