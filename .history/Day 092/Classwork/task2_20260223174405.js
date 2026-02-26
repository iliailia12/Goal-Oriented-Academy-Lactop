// 2)შექმენით სახელების სია და გამოიტანე ახალი სია სადაც მხოლოდ ის სახელებია რომელიც იწყება ასო ს-ზე

const nameList = ['ილია','ლაშა','საბა'];

const result = nameList.filter(name => name.startsWith('ს'));

console.log(result);