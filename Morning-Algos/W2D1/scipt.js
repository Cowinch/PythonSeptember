// You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

// Increment the large integer by one and return the resulting array of digits.

// Example 1:

// Input: digits = [1,2,3]
// Output: [1,2,4]
// Explanation: The array represents the integer 123.
// Incrementing by one gives 123 + 1 = 124.
// Thus, the result should be [1,2,4].
// Example 2:

// Input: digits = [4,3,2,1]
// Output: [4,3,2,2]
// Explanation: The array represents the integer 4321.
// Incrementing by one gives 4321 + 1 = 4322.
// Thus, the result should be [4,3,2,2].
// Example 3:

// Input: digits = [9]
// Output: [1,0]
// Explanation: The array represents the integer 9.
// Incrementing by one gives 9 + 1 = 10.
// Thus, the result should be [1,0].

// Constraints:

// 1 <= digits.length <= 100
// 0 <= digits[i] <= 9
// digits does not contain any leading 0's.

arr1=[1,2,3]
arr2=[4,3,2,1]
arr3=[9]
arr4=[4,4,4,4,5,6,7,8,4,3,4,6,7,8,9,6,4,3,2,5]

function incrementArray(array){
    let increment=parseInt(array.join(''))+1;
    increment=String(increment).split('')
    // for(i=0;i<array.length;i++){
    //     increment[i]=parseInt(array[i])
    // }
    return increment
}

function incrementBrokeDown(array){
    let increment='';//this line defines our temp variable
    console.log(increment)

    increment=parseInt(array.join(''));//join function takes a string an array and turns it into a string. its wrapped around parseInt to then turn the string into an int so we can increment it
    console.log(increment)

    increment++; //this is the int being incremented
    console.log(increment)

    increment=String(increment).split(''); //String class is used to turn the int back into a string. split method is used to turn a string back into an array
    console.log(increment)

    // for(i=0;i<array.length;i++){
    //     increment[i]=parseInt(array[i])
    // } //this for loop is responsible for turning the strings inside of the array back into ints. this for loop actually starts behaving VERY weirdly
    // console.log(increment)
    return increment;
}

var plusOne = function(digits) { //teachers solution
    let end = digits.length-1 // let end be the last index of the array of digits
    digits[end] += 1 // increase the digit in the last index by one
    
    while (digits[end] > 9 ){ // loop runs while last digit greater than 9 (ie is 10 and needs to carry over)
        digits[end] = 0; // set current digit to 0
        end--; // move to next digit (in order to "carry the one")
        if (end < 0){ // if end is less than zero, we need to add an index at front with a 1
            return [1, ...digits] // makes a new array with 1 and then everything in digits
        }
        else { //otherwise
            digits[end] += 1 // we carry the one
        }
    }
    return digits
};
// console.log(incrementArray(arr1))
// console.log(incrementBrokeDown(arr1))
// console.log(incrementArray(arr2))
console.log(incrementBrokeDown(arr3))
console.log(PlusOne(arr3));