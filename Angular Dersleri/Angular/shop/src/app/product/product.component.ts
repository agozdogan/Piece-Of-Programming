import { Component, OnInit } from "@angular/core";
import { Product } from "./product";
declare let alertify: any;

@Component({
  selector: "app-product",
  templateUrl: "./product.component.html",
  styleUrls: ["./product.component.css"]
})
export class ProductComponent implements OnInit {
  constructor() {}
  title = "Ürün Listesi";
  filterText = "";
  products: Product[] = [
    {
      id: 1,
      productName: "Laptop",
      price: 2500,
      categoryId: 1,
      description: "Asus Zenbook",
      imageUrl:
        "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60"
    },
    {
      id: 2,
      productName: "Mouse",
      price: 150,
      categoryId: 2,
      description: "Razer Mouse",
      imageUrl:
        "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60"
    },
    {
      id: 4,
      productName: "Klavye",
      price: 650,
      categoryId: 2,
      description: "Razer Klavye",
      imageUrl:
        "https://images.unsplash.com/photo-1561112078-7d24e04c3407?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60"
    },
    {
      id: 3,
      productName: "Süpürge",
      price: 250,
      categoryId: 3,
      description: "Dyson Süpürge",
      imageUrl:
        "https://images.unsplash.com/photo-1551731494-e17c67304912?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60"
    },
    {
      id: 5,
      productName: "Demlik",
      price: 150,
      categoryId: 2,
      description: "Paslanmaz Demlik",
      imageUrl:
        "https://images.unsplash.com/uploads/141156683569128f190a0/6efc090d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60"
    }
  ];
  ngOnInit(): void {}

  addToCart(product) {
    alertify.success("added");
  }
}
