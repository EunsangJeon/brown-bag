let array = [1, 2];
let [first, second] = array;

console.log(first);
console.log(second);

[first, second] = [second, first];

console.log(first);
console.log(second);

let [one, ...rest] = [1, 2, 3, 4];

console.log(one);
console.log(rest);

let [, two, , four] = [1, 2, 3, 4];

console.log(two);
console.log(four);
