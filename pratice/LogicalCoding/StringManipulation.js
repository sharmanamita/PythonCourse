function reverseString(str) {
  let reversed = "";

  for (let i = str.length - 1; i >= 0; i--) {
    reversed += str[i];
  }
  console.log(reversed);
  return reversed;
}

function findLargest(list) {
  let max = 0;
  for (let i = 0; i < list.length; i++) {
    if (max < list[i]) {
      max = list[i];
    }
  }
  console.log("Largest is ", max);
}

function findSmallest(list) {
  let min = list[0];
  for (let i = 0; i < list.length; i++) {
    if (min > list[i]) {
      min = list[i];
    }
  }
  console.log("Smallest is ", min);
}

function find2ndLargest(list) {
  let max1 = (max2 = 0);
  for (let i = 0; i < list.length; i++) {
    if (max1 < list[i]) {
      max2 = max1;
      max1 = list[i];
    } else if (max2 < list[i] && list[i] != max1) {
      max2 = list[i];
    }
  }

  console.log("2nd Largest is ", max2);
}

function countVowels(str) {
  let count = 0;
  for (let i = 0; i < str.length; i++) {
    if (
      str[i] == "a" ||
      str[i] == "e" ||
      str[i] == "i" ||
      str[i] == "o" ||
      str[i] == "u"
    ) {
      count++;
    } else if (
      str[i] == "A" ||
      str[i] == "E" ||
      str[i] == "I" ||
      str[i] == "O" ||
      str[i] == "U"
    ) {
      count++;
    }
  }
  console.log("Vowels count is ", count);
}

function isPalindrome(str) {
  let reversed = reverseString(str);
  if (str === reversed) {
    console.log("It is a palindrome");
  } else {
    console.log("It is not a palindrome");
  }
}

function checkAnagram(s1, s2) {
  if (s1.length !== s2.length) return false;
  s1 = [...s1];
  s2 = [...s2];

  return (
    s1.sort((a, b) => a.localeCompare(b)).join("") ==
    s2.sort((a, b) => a.localeCompare(b)).join("")
  );
}

reverseString("Hello World");
findLargest([14, 42, 53, 41, 45]);
findSmallest([14, 42, 53, 41, 45]);
find2ndLargest([14, 42, 53, 41, 45]);
countVowels("Hello World");
isPalindrome("madam");
console.log(checkAnagram("listen", "silent"));
