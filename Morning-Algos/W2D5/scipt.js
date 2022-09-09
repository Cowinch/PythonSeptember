/* 
  String: Rotate String
  Create a standalone function that accepts a string and an integer,
  and rotates the characters in the string to the right by that given
  integer amount.
*/

const str = "Hello World";

const rotateAmnt1 = 0;
const expected1 = "Hello World";

const rotateAmnt2 = 1;
const expected2 = "dHello Worl";

const rotateAmnt3 = 2;
const expected3 = "ldHello Wor";

const rotateAmnt4 = 4;
const expected4 = "orldHello W";

const rotateAmnt5 = 13;
const expected5 = "ldHello Wor";
/* 
Explanation: this is 2 more than the length so it ends up being the same
as rotating it 2 characters because after rotating every letter it gets back
to the original position.
*/

/**
 * Rotates a given string's characters to the right by the given amount,
 * wrapping characters to the beginning.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @param {number} amnt The amount of characters in the given str to rotate to the
 *    right.
 * @returns {string} The string rotated by the given amount.
 */


//this code is insanely innefficient, as each one of those methods is their own loop. So everytime we run this loop we run multiple loops
function rotateStr(str, amount) {
    var currentStr=str
    for(i=0;i<amount;i++){
        //this line of code grabs the most recent character in the string
        let currentChar=currentStr[currentStr.length-1];

        //this line of code turns the string, temporarily, into an array so we can take advantage of reverseing it
        currentStr=currentStr.split('').reverse().join('');

        //the method slice removes the first letter in a string. We reversed the array so now its removing the last string in our array
        currentStr=currentStr.slice(1);

        //now we add the currentcharacter back to the end of the string
        currentStr+=currentChar;

        //reversing the string again puts everything back in order, with our newest character at the front and our "sliced" character that we've replaced coming from the back of the string.
        currentStr=currentStr.split('').reverse().join('');
    }
    return currentStr
}
console.log(rotateStr(str, 1))
console.log(rotateStr(str, 2))
console.log(rotateStr(str, 3))
console.log(rotateStr(str, 4))
console.log(rotateStr(str, 5))
console.log(rotateStr(str, 13))

/* 
    Create the function isRotation(str1,str2) that
    returns whether the second string is a rotation of the first.
*/

const two_strA1 = "ABCD";
const two_strB1 = "CDAB";
// Explanation: if you start from A in the 2nd string, the letters are in the same order, just rotated
const two_expected1 = true;

const two_strA2 = "ABCD";
const two_strB2 = "CDBA";
// Explanation: all same letters in 2nd string, but out of order
const two_expected2 = false;

const two_strA3 = "ABCD";
const two_strB3 = "BCDAB";
// Explanation: same letters in correct order but there is an extra letter.
const two_expected3 = false;

/**
 * Determines whether the second string is a rotated version of the first.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether the second string is a rotated version of the 1st.
 */

//very efficient code, courtesy of instructor Tyler Thibault
function isRotation(s1, s2) {
    if(s1.length !== s2.length) return false;

    return (s1+s1).includes(s2)
}

console.log(isRotation(two_strA1,two_strB1))
console.log(isRotation(two_strA2,two_strB2))
console.log(isRotation(two_strA3,two_strB3))