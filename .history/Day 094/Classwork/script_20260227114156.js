// 1) შექმენი ობიექტი სადაც გექნება გექნება ორი გასაღები, მათი მნიშვნელობა კი იყოს კი შენი საყვარელი მანქანის ბრენდი და მოდელი, დაამატე ახალი გასაღები რომელშიც შეინახავ გამოშვების წელს

const obj = {
    favCarBrand: 'honda civic 2017',
    model: '2017 or 2020'
}

// 2)შექმენი ობიექტი calculator, რომელსაც ექნება მეთოდი add(a, b) და დააბრუნებს ჯამს.

const calculator = {
    add(a,b){
        return a+b
    }
}

// 3) შექმენი ობიექტი user სადაც გექნება name და age. წაშალე age გასაღები და დაამატე weigth

const user = {
    name:'ilia',
    age:15
}
delete user.age
user.weight = 70
console.log(user)

// 4)შექმენი ობიექტი book და შეცვალე მისი title გასაღები.
const boock = {
    title:'48 Laws Of Power'
}
// 5)შექმენი ობიექტი და გამოიყენე for...in, რომ დაბეჭდო მხოლოდ keys.



const  user = {
    name:'ilia',
    'last name':'kviciani',
    age:15,
    height: 1.80,
    IsStudent:true,
    IsSingle:false,
    IsProgrammer:true,
    FavBoock: '48 Laws Of Power',
    hobby:'programming'
}

for (keys in user){
    c
}