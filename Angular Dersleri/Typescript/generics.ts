function deger(x: number): number {
  return x;
}

let sayi = deger(10);
console.log(sayi);

function deger2<T>(x: T): T {
  return x;
}

let sayi3 = deger2<string>("Görkem");
console.log(sayi3);

let sayi2 = deger2<number>(2);
console.log(sayi2);

class GenericClass<T> {
  degisken: T;
  fonksiyon(parameter: T): T {
    return parameter;
  }
}
