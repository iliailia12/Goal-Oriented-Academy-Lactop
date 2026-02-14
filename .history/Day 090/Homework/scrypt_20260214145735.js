// ===============================
// .forEach() დავალებები
// ===============================

// თითოეული რიცხვის დაბეჭდვა
const numbers1 = [1, 2, 3, 4, 5];

numbers1.forEach(function(number) {
  console.log(number);
});


// მისალმება თითოეულ სახელზე
const names1 = ["John", "Sarah", "Mike"];

names1.forEach(function(name) {
  console.log("Hello, " + name);
});


//  რიცხვების ჯამის გამოთვლა
const numbers2 = [1, 2, 3, 4, 5];

let sum = 0;

numbers2.forEach(function(number) {
  sum += number;
});

console.log("Sum:", sum);


//  სიტყვის და მისი სიგრძის დაბეჭდვა
const words = ["javascript", "is", "awesome"];

words.forEach(function(word) {
  console.log(word + " - " + word.length);
});


//  სახელის და ინდექსის დაბეჭდვა
const students = ["John", "Sarah", "Mike"];

students.forEach(function(name, index) {
  console.log(index + " - " + name);
});


// ===============================
//  .map() დავალებები
// ===============================

//  ყველა რიცხვის გამრავლება 2-ზე
const numbers3 = [1, 2, 3, 4, 5];

const doubled = numbers3.map(function(number) {
  return number * 2;
});

console.log(doubled);


//  ცელსიუსიდან ფარენჰეიტში გადაყვანა
const celsius = [0, 10, 20, 30];

const fahrenheit = celsius.map(function(temp) {
  return temp * 9/5 + 32;
});

console.log(fahrenheit);


// სახელების გადაყვანა დიდ ასოებში
const names2 = ["John", "Sarah", "Mike"];

const upperNames = names2.map(function(name) {
  return name.toUpperCase();
});

console.log(upperNames);


//  მხოლოდ სახელების მიღება ობიექტებიდან
const users = [
  { name: "John", age: 20 },
  { name: "Sarah", age: 25 }
];

const onlyNames = users.map(function(user) {
  return user.name;
});

console.log(onlyNames);


// ტექსტის ფორმატის შექმნა
const numbers4 = [1, 2, 3, 4, 5];

const formatted = numbers4.map(function(number) {
  return "Number: " + number;
});

console.log(formatted);
