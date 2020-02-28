function greeter(name:string){
    return "Merhaba" + name;
}

let mesaj = greeter("Görky");

console.log(mesaj);

enum Renk {
    Kirmizi=1,
    Mavi,
    Siyah
}

let renk : Renk = Renk.Mavi;
console.log(renk)

function selam(){
    console.log("Merhaba");
}
