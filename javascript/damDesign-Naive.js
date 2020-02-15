function isWall(elem) {
  return elem && elem !== 0
}

function isMud(elem) {
  return elem === 0;
}

function maxHeight2(wallPositions, wallHeights) {
  let numberOfWalls = wallPositions.length;
  let numberOfMudSegs = 0;
  let maxHt = 0;
  let damHeights = [];
  let mudIndexes = [];
  let damHeightsCopy;
  
  for (let i = 0; i < numberOfWalls; i++) {

    damHeights.push(wallHeights[i])
    numberOfMudSegs = wallPositions[i + 1] - wallPositions[i] - 1;
    for (let j = 0; j < numberOfMudSegs; j++) {
      damHeights.push(0);
    }

    mudIndexes = damHeights.reduce(function (a, e, i) {
      if (e === 0)
        a.push(i);
      return a;
    }, []);

    damHeightsCopy = damHeights.slice();
  }

  for (let heightIndex = 0; heightIndex < damHeightsCopy.length; heightIndex++) {
    const currentElem = damHeights[heightIndex];
    const nextElem = damHeights[heightIndex + 1];
    const prevElem = damHeights[heightIndex - 1];

    if (isWall(currentElem)) {
      if (nextElem === 0) { // mud segment
        damHeightsCopy[heightIndex + 1] = currentElem + 1;
      }
      else {
        continue;
      }
    }
    else {

      if (isWall(prevElem) && isWall(nextElem)) {
        let mudHeight = Math.min(damHeightsCopy[heightIndex-1], damHeightsCopy[heightIndex+1]) + 1;
        damHeightsCopy[heightIndex] = mudHeight;
      }
      else if (isMud(prevElem) && isWall(nextElem)) {

        let mudHeight = Math.min(damHeightsCopy[heightIndex-1], damHeightsCopy[heightIndex+1]) + 1;
        damHeightsCopy[heightIndex] = mudHeight;
        if (Math.abs(mudHeight - prevElem) > 1) {
          damHeightsCopy[heightIndex - 1] = mudHeight + 1;
        }
      }
      else if (isMud(prevElem) && isMud(nextElem)) {
        damHeightsCopy[heightIndex] = damHeightsCopy[heightIndex-1] + 1;
      }
      else if (isWall(prevElem) && isMud(nextElem)) {
        continue;
      }
    }

  }

  damHeightsCopy.forEach((elem, index) => {
    if(mudIndexes.includes(index)) {
      if(maxHt < elem) {
        maxHt = elem;
      }
    }
  })


  return maxHt
}