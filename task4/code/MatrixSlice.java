import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import javax.imageio.ImageIO;

public class MatrixSlice {

    public static int[][] sliceMatrix2D(int[][] matrix, int rowStart, int rowEnd, int colStart, int colEnd) {
        int height = matrix.length;
        int width = matrix[0].length;

        if (rowStart < 0 || rowEnd > height || colStart < 0 || colEnd > width || rowStart >= rowEnd || colStart >= colEnd) {
            throw new IllegalArgumentException("Invalid slice boundaries for matrix dimensions " + height + "x" + width);
        }

        int slicedHeight = rowEnd - rowStart;
        int slicedWidth = colEnd - colStart;
        int[][] sliced = new int[slicedHeight][slicedWidth];

        for (int r = 0; r < slicedHeight; r++) {
            for (int c = 0; c < slicedWidth; c++) {
                sliced[r][c] = matrix[rowStart + r][colStart + c];
            }
        }

        return sliced;
    }

    public static void processImageSlice(String inputFilename, int rowStart, int rowEnd, 
                                         int colStart, int colEnd, String outputFilename) {
        try {
            Path inputPath = Paths.get(inputFilename).toAbsolutePath();
            File inputFile = inputPath.toFile();

            if (!inputFile.exists()) {
                throw new IOException("Could not find file at path: " + inputPath);
            }

            BufferedImage img = ImageIO.read(inputFile);
            int height = img.getHeight();
            int width = img.getWidth();

            System.out.println("Original Image Dimensions: " + height + "x" + width + " (Rows x Columns)");

            int sliceWidth = colEnd - colStart;
            int sliceHeight = rowEnd - rowStart;
            BufferedImage slicedImg = img.getSubimage(colStart, rowStart, sliceWidth, sliceHeight);

            System.out.println("Sliced Image Dimensions:   " + slicedImg.getHeight() + "x" + slicedImg.getWidth());

            File outputFile = new File(outputFilename);
            ImageIO.write(slicedImg, "jpg", outputFile);

        } catch (IOException e) {
            System.err.println("Error processing image slice: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        int[][] numMatrix = {
            {10, 11, 12, 13, 14},
            {20, 21, 22, 23, 24},
            {30, 31, 32, 33, 34},
            {40, 41, 42, 43, 44}
        };

        int[][] numSlice = sliceMatrix2D(numMatrix, 1, 3, 2, 5);

        System.out.println("Sliced 2D Sub-Matrix (Rows 1:3, Cols 2:5):");
        for (int[] row : numSlice) {
            for (int val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }

        processImageSlice("sample.jpg", 100, 400, 150, 450, "slicedImage.jpg");
    }
}