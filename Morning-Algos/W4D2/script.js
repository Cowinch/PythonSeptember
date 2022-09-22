/* 
    Recursive Factorial
    Input: integer
    Output: integer, product of ints from 1 up to given integer
    
    If less than zero, treat as zero.
    Bonus: If not integer, truncate (remove decimals).
    
    Experts tell us 0! is 1.
    
    rFact(3) = 6 (1*2*3)
    rFact(6.8) = 720 (1*2*3*4*5*6)
*/

const num1 = 3;
const expected1 = 6;
// Explanation: 1*2*3 = 6

const num2 = 6.8;
const expected2 = 720;
// Explanation: 1*2*3*4*5*6 = 720

const num3 = 0;
const expected3 = 1;

function factorial(n) {
    if(n<=0){
        return 1;
    }
    return factorial(Math.floor(n-1))*Math.floor(n);
}

/*****************************************************************************/
console.log("Factoial of num1 is "+factorial(num1)) // 6
console.log("Factoial of num2 is "+factorial(num2)) // 720
console.log("Factoial of num3 is "+factorial(num3)) // 1
console.log("\n")

/*
    Sum To One Digit
    Implement a function sumToOne(num)​ that,
    given a number, sums that number’s digits
    repeatedly until the sum is only one digit. Return
    that final one digit result.
    Tips:
    to access digits from a number, need to convert it .toString() to access each digit via index
    parseInt(arg) returns arg parsed as an integer, or NaN if it couldn't be converted to an int
    isNaN(arg) used to check if something is NaN
*/

const numA = 5;
const expectedA = 5;

const numB = 10;
const expectedB = 1;

const numC = 25;
const expectedC = 7;

const numD = 999;// 9+9+9 = 27, 2 + 7 = 9
const expectedD = 9;

/**
 * Sums the given number's digits until the number becomes one digit.
 * @param {number} num The number to sum to one digit.
 * @returns {number} One digit.
 */
function oldsumToOneDigit(num) {

    //Base case?
    //once a number is less than 10 its a single digit, so we can just return it and start the recursive process there.
    if(num<10){
        return num;
    }

    // Logic ?
    //the number is converted into a string and num is defined. A for loop iterates through the string.
    str=num.toString()
    sum=0;

    for(i=0;i<str.length;i++){
        sum+=parseInt(str[i])
    }

    // Recursive call / return
    return sumToOneDigit(sum)
}


function sumToOneDigit(num) {

    //Base case?
    //once a number is less than 10 its a single digit, so we can just return it and start the recursive process there.
    if(num<10){
        return num;
    }

    // %10 returns the last number
    let last=num%10;

    let remaining=Math.floor(num/10);
    return sumToOneDigit(last + sumToOneDigit(remaining))
    //this code is honestly bulkier on the recursive side, and is harder to trace through.
}

console.log("sum to one digit of numA is "+sumToOneDigit(numA)) // 5
console.log("sum to one digit of numB is "+sumToOneDigit(numB)) // 1
console.log("sum to one digit of numC is "+sumToOneDigit(numC)) // 7
console.log("sum to one digit of numD is "+sumToOneDigit(numD)) // 9
/*****************************************************************************/