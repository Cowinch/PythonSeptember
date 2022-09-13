// const arrA1 = [1, 2, 3];
// const arrB1 = ['a', 'b', 'c'];
// const expected1 = [1, 'a', 2, 'b', 3, 'c'];

// const arrA2 = [1, 3];
// const arrB2 = [2, 4, 6, 8];
// const expected2 = [1, 2, 3, 4, 6, 8];

// const arrA3 = [1, 3, 5, 7];
// const arrB3 = [2, 4];
// const expected3 = [1, 2, 3, 4, 5, 7];

// const arrA4 = [];
// const arrB4 = [42, 0, 6];
// const expected4 = [42, 0, 6];

/*
* Interleaves two arrays into a new array. Interleaving means laternating
* the items starting from the first array.
* - Time: 0(?)
* - Space: 0(?)
* @param {Array<any>} arr1
* @param {Array<any>} arr2
* @returns {Array<any>} A new array of interleaved items
*/

function interleaveArrays(arr1, arr2) {
    var newArr = [];
    //this first for loop will successfully lace both arrays for as long as they are of the same length. The next two if for loops will catch the remainder
    for (i = 0; i < arr1.length && i < arr2.length; i++) {
        newArr.push(arr1[i]);
        newArr.push(arr2[i]);
    }
    //we use both if statements to determine which is the bigger string, and then act accordingly. We add up the total length of both arrays, and then subtract the largest array length from the sum to get our iterative variable starting point.
    if (arr1.length < arr2.length) {
        for (i = (arr2.length + arr1.length) - arr2.length; i < arr2.length; i++) {
            newArr.push(arr2[i]);
        }
    }
    else if (arr2.length < arr1.length) {
        for (i = (arr2.length + arr1.length) - arr1.length; i < arr1.length; i++) {
            newArr.push(arr1[i]);
        }
    }
    return newArr
}

// console.log(interleaveArrays(arrA1, arrB1));
// console.log(interleaveArrays(arrA2, arrB2));
// console.log(interleaveArrays(arrA3, arrB3));
// console.log(interleaveArrays(arrA4, arrB4));

/* 
Array: Binary Search (non recursive)
Given a sorted array and a value, return whether the array contains that value.
Do not sequentially iterate the array. Instead, ‘divide and conquer’,
taking advantage of the fact that the array is sorted .
Bonus (alumni interview): 
    first complete it without the bonus, because they ask for additions
    after the initial algo is complete
    return how many times the given number occurs
*/

const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true; //1 for bonus

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true; //1 for bonus

// bonus, how many times does the search num appear?
const nums4 = [2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9];
const searchNum4 = 2;
const expected4 = 4;

/**
 * Efficiently determines if the given num exists in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the given num exists in the given array.
 */

function binarySearch(sortedNums, searchNum){
    let low=0
    let high=sortedNums.length-1
    let mid=0;
    while (high-low>1){
        let mid=(high+low)/2;
        if(sortedNums[mid]<searchNum){
            low=mid+1;
        } else {
            high=mid;
        }
    }
    if(sortedNums[low]==searchNum){
        return true
    }
    else if(sortedNums[high]==searchNum){
        return true
    } else {
        return false
    }
}






function wrongBinarySearch(sortedNums, searchNum) {
    var start=Math.floor(sortedNums.length/2)
    var count=0
    if (sortedNums[start]==searchNum){
        return true
    } 
    else if (sortedNums[start]>searchNum){
        for(i=0;i<=sortedNums.length/2;i++){
            if (sortedNums[i]==searchNum){
                count++
            }
        }
    } else {
        for(i=sortedNums.length-1;i>=sortedNums.length/2;i--){
            if (sortedNums[i]==searchNum){
                count++
            }
        }
    }
    if(count>0){
        return "This is how many times we found "+searchNum+": "+count
    } else {
        return false
    }
}


console.log(binarySearch(nums1, searchNum1)); // false
console.log(binarySearch(nums2, searchNum2)); // true (1 for bonus)
console.log(binarySearch(nums3, searchNum3)); // true (1 for bonus)

//bonus, how many times does the search num appear?
console.log(binarySearch(nums4, searchNum4)); // 4