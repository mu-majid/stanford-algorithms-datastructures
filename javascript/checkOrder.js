/**
 * Students are asked to stand in non-decreasing order of heights for an annual photo.

 * Return the minimum number of students that must move in order for all students
 * to be standing in non-decreasing order of height.

 * Example 1:
 * Input: heights = [1,1,4,2,1,3]
 * Output: 3
 */

var heightChecker = function (heights) {
  let sorted = heights.slice(0);
  sorted = sorted.sort((a, b) => { return a - b });
  let count = 0;

  for (let i = 0; i < heights.length; i++) {
    if (heights[i] !== sorted[i]) count++
  }
  return count;
};