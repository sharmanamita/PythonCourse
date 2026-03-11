function ObjectFromArrays(keysArr, valuesArr) {
  if (keysArr.length !== valuesArr.length) {
    console.warn("Arrays length mismatch");
  }

  return Object.fromEntries(
    keysArr.map((key, i) => [key || "end", valuesArr[i] ?? 0]),
  );
}

const keys = ["a", "b", "c", "d"];
const vals = [1, 2, 3, 4, 5];
const result = ObjectFromArrays(keys, vals);
console.log(result);

function flattenArray(arr) {
  let result = [];

  for (let i = 0; i < arr.length; i++) {
    console.log(typeof arr[i]);

    if (Array.isArray(arr[i])) {
      result = [...result, ...flattenArray(arr[i])];
    } else {
      result.push(arr[i]);
    }
  }
  console.log(result);
  return result;
}

const arr = [1, [2, 3], [4, [5, 6]], 7];
flattenArray(arr);

// function RotateArray(arr, position) {
//   // var result = arr.splice(arr.length / 2);
//   while (position) {
//     for (let i = 0; i < arr.length; i++) {
//       if (arr.length - 1 !== i) {
//         [arr[i + 1], arr[i]] = [arr[i], arr[i + 1]]; // clockwise direction
//       }
//     }
//     position--;
//   }
//   console.log(arr);
// }

function RotateArray(arr, k) {
  const n = arr.length;
  if (n == 0 || k == 0) return;

  k %= n;

  function reverse(nums, start, end) {
    while (start < end) {
      [nums[start], nums[end]] = [nums[end], nums[start]];
      start++;
      end--;
    }
  }

  reverse(arr, 0, n - 1);
  console.log("reverse", arr);
  reverse(arr, 0, k - 1);
  console.log("after reverse", arr);
  reverse(arr, k, n - 1);
  console.log("final", arr);
}

RotateArray([1, 2, 3, 4, 5], 2);
