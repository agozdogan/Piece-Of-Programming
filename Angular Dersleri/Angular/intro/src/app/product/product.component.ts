import { Component, OnInit } from "@angular/core";

@Component({
  selector: "app-product",
  template: `
    <p>{{ productName }} worksa!</p>
  `,
  styleUrls: ["./product.component.css"]
})
export class ProductComponent implements OnInit {
  constructor() {}
  productName = "Laptop";
  ngOnInit(): void {}
}
