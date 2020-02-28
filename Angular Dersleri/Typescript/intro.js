function greeter(name) {
    return "Merhaba" + name;
}
var mesaj = greeter("Görky");
console.log(mesaj);
var Renk;
(function (Renk) {
    Renk[Renk["Kirmizi"] = 1] = "Kirmizi";
    Renk[Renk["Mavi"] = 2] = "Mavi";
    Renk[Renk["Siyah"] = 3] = "Siyah";
})(Renk || (Renk = {}));
var renk = Renk.Mavi;
console.log(renk);
