// 2) შექმენი factory function რომელიც შექმნის ობიექტებს კუთვნილებებით: hobby1, hobby2, hobby3 და მეთოდით myHobbies() რომელიც გამოიტანს ერთ დიდ წინადადებას შენი ჰობიების შესახებ

function createHobbies(hobby1, hobby2, hobby3) {
    return {
    hobby1: hobby1,
    hobby2: hobby2,
    hobby3: hobby3,

    myHobbies: function () {
    console.log("My hobbies are " + this.hobby1 + ", " + this.hobby2 + " and " + this.hobby3 + ".") 

}
} 
}

const myHobbyObject = createHobbies("reading", "gaming", "football") 
myHobbyObject.myHobbies()