// <!-- 1)შექმენი ორი ობიექტი, ორივე ობიექტში შეინახე მანქანის ბრენდი და მოდელი, ორივე ობიექტში დაამატე ერთ და იგივე ფუნქცია სახელად aboutCar(), რომელიც გამოძახებისას გამოიტანს წინადადებას "this is (brand)(model)" იმ მანქანაზე რომლის ობიექტშიც გამოვიძახეთ -->

const car1 = {
    brand: 'BMW',
    model: 'M5',

    abautCar: function(){
        console.log('this is'+this.brand+''+this.model)
    }
}

const car2 = {
    bra
}