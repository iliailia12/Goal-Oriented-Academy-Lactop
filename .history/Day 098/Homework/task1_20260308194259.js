// 1)შექმენი ორი ობიექტი, ორივე ობიექტში შეინახე ტელეფონის ბრენდი და მოდელი, ორივე ობიექტში დაამატე ერთ და იგივე ფუნქცია სახელად aboutTelephone(), რომელიც გამოძახებისას გამოიტანს წინადადებას "this is (brand)(model)" იმ ტელეფონზე რომლის ობიექტშიც გამოვიძახეთ

let phone1 = {
    brand: 'Apple',
    model: 'Iphone 18',
    aboutTelephone: function() {
    console.log("this is " + this.brand + " " + this.model)

}
}

let phone2 = {
    brand: "Samsung",
    model: "Galaxy S23",
    aboutTelephone: function() {
    console.log("this is " + this.brand + " " + this.model)

}
}

