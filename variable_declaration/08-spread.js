let first = [1, 2];
let second = [3, 4];
let bothPlus = [0, ...first, ...second, 5];

console.log(bothPlus);

let defaults = {
	name: "Eunsang Jeon",
	knox: "eunsang.jeon",
	org: "Service S/W Lab"
};

let result0 = { ...defaults};
let result1 = { ...defaults, org: "SS3" };
let result2 = { org:"SS3", ...defaults};

console.log(result0);
console.log(result1);
console.log(result2);
