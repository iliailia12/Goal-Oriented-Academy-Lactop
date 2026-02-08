1) შექმენით 5 ელემენტიანი სია, .push() მეთოდის გამოყენებით სიაში ჩაამატეთ თქვენი სახელი.

2) იგივე სიის ბოლოდან ამოშალეთ ბოლო ელემენტი .pop() მეთოდის გამოყენებით.

3) .join() მეთოდის მეშვეობით გააერთიანეთ ეს სია space-ით string-ის სახით.

4) .slice() მეთოდის მეშვეობით სიიდან ამოიღეთ 0-ე ინდექსიდან 4-მდე ელემენტები და შესაბამისად დაბეჭდეთ.

5) .concat() მეთოდის გამოყენებით შეართეთ 2 სია ერთმანეთს და დაბეჭდეთ საბოლოო შედეგი.
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
