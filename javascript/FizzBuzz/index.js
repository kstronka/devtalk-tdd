import { fizzBuzz } from "./src/fizzbuzz.js";

const printUsageAndExit = () => {
    console.log("Usage: yarn start <integer>");
    process.exit(1);
};

if (process.argv.length !== 3) {
    printUsageAndExit()
}

const input = parseInt(process.argv[2]);

if (isNaN(input)) {
    printUsageAndExit()
}

console.log(fizzBuzz(input));