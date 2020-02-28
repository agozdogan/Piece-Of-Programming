abstract class KrediBase{
    constructor(){

    }

    kaydet():void{
        console.log("Kaydedildi");
    }

    abstract hesapla():void;
}

class TuketiciKredi extends KrediBase{
    constructor(){
        super();
    }

    hesapla():void{
        console.log("Tüketici kredisine göre hesap yapıldı")
    }
}

class KonutKredi extends KrediBase{
    constructor(){
        super();
    }

    hesapla():void{
        console.log("Konut kredisine göre hesap yapıldı")
    }
    baskabiroperasyon():void{
        console.log("Konut kredisine göre hesap yapıldı")
    }
}

let tuketiciKredisi =  new TuketiciKredi();
tuketiciKredisi.hesapla();
tuketiciKredisi.kaydet();


let konutKredisi = new KonutKredi();
konutKredisi.hesapla();
konutKredisi.kaydet();
konutKredisi.baskabiroperasyon();