/* 
Given an array of strings
return the number of times each string occurs (a frequency / hash table)
*/

const arr1 = ["a", "a", "a"];
const expected1 = {
    a: 3,
};

const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
const expected2 = {
    a: 2,
    b: 1,
    c: 3,
    B: 1,
    d: 1,
};

const arr3 = [];
const expected3 = {};

/**
 * Builds a frequency table based on the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} arr
 * @returns {Object<string, number>} A frequency table where the keys are items
 *    from the given arr and the values are the amnt of times that item occurs.
 *  Possible hint: .hasOwnProperty() <- Don't know it? Google it as a group!
 */
function makeFrequencyTable1(array) {
    //we're going to create two arrays, one holding the character and one holding the frequency, and then at the end well combine them into a dictionary for the end result.
    let characters = [],
        frequency = [],
        arr = [...array], // clone array so we don't change the original when using .sort()
        prev, //this variable holds the previous element we tested
        newDict={};

    arr.sort(); // its important the array is sorted for the math in the for loop below
    for (let element of arr) {
        // i=0;i<arr.length;i++ does not work here, as we want the dictionary key to display the character. OF is what gives us the element of the array, if we wrote IN then we would get the indices like with traditional for loops
        if (element !== prev) { //if it doesnt equal the previous element, then we add the character to the character string, and we start the number off as 1
            characters.push(element);
            frequency.push(1);
        }
        //if the previous element is equal to the current one, we increase the freqeuncy variable for that character. This is why sorting it was important. We find the correct frequency index to increment by finding the most previous index in the frequency array
        else frequency[frequency.length - 1]++;
        prev = element;
    }
    //this is where we generate the dictionary. when we set a value in a dictionary and there is no key, it will create the key.
    for(i=0;i<characters.length;i++){
        newDict[characters[i]]=frequency[i]
    }

    return newDict;
}

function makeFrequencyTable(array){
    let table={}
    for(let elem of array){
        if (table.hasOwnProperty(elem)){
            table[elem]+=1
        } else {
            table[elem]=1
        }
    }
    return table;
}

//this is just a condensed version of the previous function. With ? acting as an if,else/true,false. if true, runs the first line. if false/else runs the line after the colon ':'
function makeFrequencyTable3(array){
    let table={}
    for(let elem of array){
        table.hasOwnProperty(elem) ? table[elem]++ : table[elem]=1
    }
    return table
}
console.log(makeFrequencyTable(arr1))
console.log("Expected: ", expected1);
console.log(makeFrequencyTable(arr2))
console.log("Expected: ", expected2);
console.log(makeFrequencyTable(arr3))
console.log("Expected: ", expected3);

/* 
Given a non-empty array of odd length containing ints where every int but one
has a matching pair (another int that is the same)
return the only int that has no matching pair.
*/

const numsA = [1];
const expectedA = 1;

const numsB = [5, 4, 5];
const expectedB = 4;

const numsC = [5, 4, 3, 4, 3, 4, 5];
const expectedC = 4; // there is a pair of 4s but one 4 has no pair.

const numsD = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];
const expectedD = 1;

function oddOccurrencesInArray(nums) {
    let object=makeFrequencyTable3(nums);
    for(key in object){
        if(object[key]%2!=0){ //we're checking if the remainder of being divided by 2 is NOT equal to 0. ALL odd numbers return a remainder when divided by 2.
            return parseInt(key);
        }
    }
    return false;
}

console.log(oddOccurrencesInArray(numsA), "should equal", expectedA);
console.log(oddOccurrencesInArray(numsB), "should equal", expectedB);
console.log(oddOccurrencesInArray(numsC), "should equal", expectedC);
console.log(oddOccurrencesInArray(numsD), "should equal", expectedD);