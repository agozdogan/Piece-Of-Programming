var Ev = /** @class */ (function () {
    function Ev(odaSayisi, pencereSayisi, kat) {
        this._kat = kat;
        this._odaSayisi = odaSayisi;
        this._pencereSayisi = pencereSayisi;
    }
    Ev.prototype.yemekYe = function () {
        console.log("Yemek yiyildi.");
    };
    return Ev;
}());
var ev = new Ev(3, 4, 5);
console.log(ev._pencereSayisi);
ev.yemekYe();
