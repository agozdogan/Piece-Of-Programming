// https://morioh.com/p/7639c262cbed/javascript-s-arrow-functions-explained-by-going-down-a-slide

function addTen(num) {
  return num + 10;
}

console.log(addTen(10));

let addTenT = num => num + 10;
console.log(addTenT(19));

let nums = [1, 4, 9];
let squares = nums.map(num => {
  return Math.sqrt(num);
});
console.log(squares);

let multiply = (num1, num2) => {
  return num1 * num2;
};
console.log(multipl(2, 10));
