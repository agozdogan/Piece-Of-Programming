class Ev {
  _odaSayisi: number;
  _pencereSayisi: number;
  _kat: number;
  constructor(odaSayisi: number, pencereSayisi: number, kat: number) {
    this._kat = kat;
    this._odaSayisi = odaSayisi;
    this._pencereSayisi = pencereSayisi;
  }

  yemekYe() {
    console.log("Yemek yendi.");
  }
}

let ev = new Ev(3, 4, 5);

console.log(ev._pencereSayisi);
ev.yemekYe();
