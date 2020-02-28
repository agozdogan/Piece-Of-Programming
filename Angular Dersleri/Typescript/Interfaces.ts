interface Product{
    id:number;
    name:string;
    unitPrice:number;
}

function save(product:Product){
    console.log(product.name + " Kaydedildi");
}

save({id:1,name:"Laptop",unitPrice:10})

interface PersonService{
    save();
}

class CustomerService implements PersonService{
    save() {
        throw new Error("Method not implemented.");
    }

}