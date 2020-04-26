// Complete the sockMerchant function below.

// Naive Approach
function sockMerchant(n, ar) {
  const colors = {}
  let pairs = 0;
  for (let i = 0; i < ar.length; i++) {

    if (!colors.hasOwnProperty(ar[i])) {
      colors[ar[i]] = 1
    }
    else {
      colors[ar[i]] += 1
    }

  }

  for (const color in colors) {
    if (colors.hasOwnProperty(color)) {
      let socks = colors[color];
      if (socks % 2 === 0) { // even
        pairs = pairs + socks / 2
      }
      else {
        socks = socks - 1
        pairs = pairs + socks / 2
      }
    }
  }
  return pairs
}

// O(n) Approach
function sockMerchant2(n, ar) {
  const colors = new Map();
  let pairs = 0;
  for (let i = 0; i < ar.length; i++) {

    if (!colors.has(ar[i])) {
      colors.set(ar[i], 1);
    }
    else {
      pairs += 1;
      colors.delete(ar[i]);
    }

  }
  return pairs;
}


console.log(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]));
console.log(sockMerchant(20, [4, 5, 5, 5, 6, 6, 4, 1, 4, 4, 3, 6, 6, 3, 6, 1, 4, 5, 5, 5]));
console.log()
console.log(sockMerchant2(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]));
console.log(sockMerchant2(20, [4, 5, 5, 5, 6, 6, 4, 1, 4, 4, 3, 6, 6, 3, 6, 1, 4, 5, 5, 5]));


