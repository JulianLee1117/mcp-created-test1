public class DataAnalyzer {
    /**
     * Analyze data using the common validation function
     * @param data Data string to analyze
     * @return Analysis result
     */
    public String analyzeData(String data) {
        if (CommonUtils.isValidString(data)) {
            return "Analyzing data: " + data;
        }
        return "Invalid data provided";
    }
}