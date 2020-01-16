let obj1 = {
    a: "foo",
    b: 9,
    c: "none"
};

let { a, b } = obj1;

console.log(a);
console.log(b);

let obj2 = {
    d: "foo",
    e: 9,
    f: "none"
};


let { d, ...rest} = obj2;

console.log(d);
console.log(rest);

let { d: newName, ...others} = obj2;

console.log(newName);
