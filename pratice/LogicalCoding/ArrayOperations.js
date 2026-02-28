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

function loop() {}

const arr = [1, [2, 3], [4, [5, 6]], 7];
flattenArray(arr);
