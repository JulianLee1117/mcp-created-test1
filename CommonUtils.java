public class CommonUtils {
    /**
     * A common utility function to validate string input
     * @param input String to validate
     * @return true if string is valid (not null and not empty), false otherwise
     */
    public static boolean isValidString(String input) {
        return input != null && !input.trim().isEmpty();
    }
}