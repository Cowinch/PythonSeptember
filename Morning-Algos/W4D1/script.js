/* 
Recursive Sigma
Input: integer
Output: sum of integers from 1 to Input integer
*/

const num1 = 5;
const expected1 = 15;
// Explanation: (1+2+3+4+5)

const num2 = 2.5;
const expected2 = 3;
// Explanation: (1+2)

const num3 = -1;
const expected3 = 0;

/**
 * Recursively sum the given int and every previous positive int.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} num
 * @returns {number}
 */
function recursiveSigma(num) {
    //Your code here
    //Santize value?

    //Base case?
    // we start with num < 1 because we are only looking at integers and we are trying to reach the int 1 recursively
    if (num < 1) {
        return 0
    }
    
    //Recursive call?
    //math.floor because we only want integers.
    return recursiveSigma(Math.floor(num - 1)) + Math.floor(num)
}

console.log(recursiveSigma(num1)); // 15
console.log(recursiveSigma(num2)); // 3
console.log(recursiveSigma(num3)); // 0

/*****************************************************************************/

/* 
Recursively sum an arr of ints
*/

const numsA = [1, 2, 3];
const expectedA = 6;

const numsB = [1];
const expectedB = 1;

const numsC = [];
const expectedC = 0;

/**
 * Add params if needed for recursion <-------
 * Recursively sums the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The sum of the given nums.
 */
function sumArr(nums, i = 0) {
    //Your code here
    //Base case?
    if (i === nums.length) {
        return 0
    }
    //Any more logic?
    //Recursive call?
    return sumArr(nums, i + 1) + nums[i]
}

// console.log(sumArr(numsA)) // 6
// console.log(sumArr(numsB)) // 1
// console.log(sumArr(numsC)) // 0
/*****************************************************************************/