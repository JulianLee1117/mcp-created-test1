public class FileProcessor {
    /**
     * Process a filename using the common validation function
     * @param filename Name of the file to process
     * @return Processing status message
     */
    public String processFile(String filename) {
        if (CommonUtils.isValidString(filename)) {
            return "Processing file: " + filename;
        }
        return "Invalid filename provided";
    }
}