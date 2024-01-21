package org.fizzbuzz;


public class App {
    public static void main(String[] args) {
        if (args.length != 1) {
            printUsageAndExit();
        }

        try {
            int input = Integer.parseInt(args[0]);
            System.out.println(new App().getMessage(input));
        }
        catch (NumberFormatException e) {
            printUsageAndExit();
        }
    }

    public String getMessage(int value) {
        String result = "";
        
        if (value % 3 == 0) {
            result = result + "Fizz";
        }

        if (value % 5 == 0) {
            result = result + "Buzz";
        }

        if (result.equals("")) {
            result = Integer.toString(value);
        }

        return result;
    }

    private static void printUsageAndExit() {
        System.err.println("Usage: java App <integer>");
        System.exit(1);
    }
}
