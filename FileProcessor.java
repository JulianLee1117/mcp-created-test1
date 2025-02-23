public class FileProcessor {
    /**
     * Process a filename using the common validation function and print each letter
     * @param filename Name of the file to process
     * @return Processing status message
     */
    public String processFile(String filename) {
        if (CommonUtils.isValidString(filename)) {
            System.out.println("Processing file: " + filename);
            // Print each character of the filename on a new line
            for (char c : filename.toCharArray()) {
                System.out.println(c);
            }
            return "Processing complete for file: " + filename;
        }
        return "Invalid filename provided";
    }
}