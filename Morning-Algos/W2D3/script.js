/* 
Given a string,
return a new string with the duplicate characters excluded
Bonus: Keep only the last instance of each character.
*/

const str1 = "abcABCabcABCabcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";

//bonus
const str5 = "aba"
const expected5 = "ba"

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */
function stringDedupe(str) {
    //this is the string well return
    var newstr=''

    //this is the dictionary well utilize to check if we've seen this letter before
    var dict={}

    for(i of str){
        //if we haven't seen this character before, we add it to the dictionary and we also add it our return string.
        if(!dict.hasOwnProperty(i)){
            dict[i]=true
            newstr+=i
        }
    }
    return newstr
}

console.log(stringDedupe(str1));
console.log(stringDedupe(str2));
console.log(stringDedupe(str3));
console.log(stringDedupe(str4));
console.log(stringDedupe(str5));

/*****************************************************************************/

/* 
Given a string containing space separated words
Reverse each word in the string.
If you need to, use .split to start, then try to do it without.
*/

const strA = "hello";
const expectedA = "olleh";

const strB = "hello world";
const expectedB = "olleh dlrow";

const strC = "abc def ghi";
const expectedC = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */
function reverseWords(str) {
    newstr="";
    currentword="";
    for(i=0;i<str.length;i++){
        if(str[i]!=" "){
            currentword+=str[i];
            // console.log(i);
        }
        else{
            //this takes the current word and reverses it using array methods
            currentword=currentword.split('').reverse().join('')
            //this adds the current word to the new string, followed by a space
            newstr+=currentword+" "
            //this resets the currentword
            currentword=""
        }
    }
    //code from else follows here so we can grab the last word as there is no space following it
    currentword=currentword.split('').reverse().join('')
    newstr+=currentword
    currentword=""
    return newstr
}

// console.log(reverseWords(strA)) //expectedA: olleh
// console.log(reverseWords(strB)) //expectedB: olleh dlrow
// console.log(reverseWords(strC)) //expectedC: cba fed ihg

