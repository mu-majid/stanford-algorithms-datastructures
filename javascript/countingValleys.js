// Complete the countingValleys function below.
// Tracks Every step
function countingValleys(n, s) {

  let valleys = 0;
  let valleyEntered, valleyExited;
  const elevations = { 'D': -1, 'U': 1 }
  const seaLevel = 0;
  let currentLevel = 0; // starting at sea level

  [...s].forEach(c => {
    currentLevel = currentLevel + elevations[c];
    if (currentLevel < seaLevel && (currentLevel - elevations[c]) === seaLevel) { // valley entered
      valleyEntered = true;
    }
    if (currentLevel === seaLevel && (currentLevel - elevations[c]) < seaLevel) { // valley exited
      valleyExited = true;
    }
    if (valleyEntered && valleyExited) {
      valleys++;
      valleyEntered = valleyExited = false;
    }
  });

  return valleys;
}

// More Efficient
function countingValleys2(n, s) {

  let valleys = 0;
  let currentLevel = 0; // starting at sea level

  [...s].forEach(c => {
    if (c === 'U') currentLevel++
    if (c === 'D') currentLevel--
    if(currentLevel === 0 && c === 'U') valleys++;
  });

  return valleys;
}


console.log(countingValleys(8, 'UDDDUDUU'));
console.log(countingValleys2(8, 'UDDDUDUU'));
