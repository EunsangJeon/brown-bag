function f(x) {
    if (x) {
        var y = 9;
    }
    else {
        y = 99;
    }
    return y;
}

console.log(f(true));
console.log(f(false));
