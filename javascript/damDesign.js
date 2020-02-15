

/**
 * 
 * @param {*} wallPositions 
 * @param {*} wallHeights 
 * 
 * @Problem : https://fizzbuzzer.com/mud-walls/
 */

function maxHeight(wallPositions, wallHeights) {
  let n = wallPositions.length;
  let m = wallHeights.length;
  let max = 0;
  for (let i = 0; i < n - 1; i++) {
    if (wallPositions[i] < wallPositions[i + 1] - 1) {
      // We have a gap
      let heightDiff = Math.abs(wallHeights[i + 1] - wallHeights[i]);
      let gapLen = wallPositions[i + 1] - wallPositions[i] - 1;
      let localMax = 0;
      if (gapLen > heightDiff) {
        let low = Math.max(wallHeights[i + 1], wallHeights[i]) + 1;
        let remainingGap = gapLen - heightDiff - 1;
        localMax = low + remainingGap / 2;

      } else {
        localMax = Math.min(wallHeights[i + 1], wallHeights[i]) + gapLen;
      }

      max = Math.max(max, localMax);
    }
  }
  return Math.floor(max);
}

/**
 * 
 * @param {*} wallPositions 
 * @param {*} wallHeights 
 * Mathematical Solution.
 */
function maxHeightGeometry(wallPositions, wallHeights) {
  const result = wallPositions.reduce((acc, el, index) => {
    if (index > 0) {
      const hole = el - wallPositions[index - 1] - 1;
      if (hole) {
        const leftHeight = wallHeights[index - 1]
        const rightHeight = wallHeights[index]
        const leftIndex = wallPositions[index - 1]
        const rightIndex = el
        let x = Math.floor((rightHeight + rightIndex - leftHeight + leftIndex) / 2)
        let mud = 0;
        if (x >= rightIndex) {
          x = rightIndex - 1
          mud = leftHeight + x - leftIndex;
        }
        else if (x <= leftIndex) {
          x = leftIndex + 1
          mud = rightHeight + + x - leftIndex;
        }
        else {
          mud = leftHeight + x - leftIndex;
        }
        // const mud = Math.floor((leftHeight - leftIndex + rightHeight + rightIndex)/2)
        if (mud > 50000) {
          console.log(mud, leftIndex, leftHeight, rightIndex, rightHeight)
        }
        acc = Math.max(acc, mud)
      }
    }
    return acc
  }, 0)
  return result
}