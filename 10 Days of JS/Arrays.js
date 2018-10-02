/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    return Array.from(new Set(nums)).sort(function(a, b){return b - a})[1];
}