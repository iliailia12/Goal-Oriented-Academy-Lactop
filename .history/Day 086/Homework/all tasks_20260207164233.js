
let arr = [1, 2, 3, 4, 5];
arr.push("1920");
console.log(arr);

// 2) 
arr.pop();
console.log(arr);

// 3) 
let joinedString = arr.join(" ");
console.log(joinedString);

// 4)
let slicedArr = arr.slice(0, 4);
console.log(slicedArr);

// 5
let arr2 = ["a", "b", "c"];
let finalArr = arr.concat(arr2);
console.log(finalArr);
