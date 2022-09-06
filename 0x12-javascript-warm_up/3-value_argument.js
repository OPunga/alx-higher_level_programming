#!/usr/bin/node

let args = process.argv;
let count = 0

for (i in args){
	count += 1
}
if (count === 2){
	console.log("No argument");
}
else if (count > 2){
	console.log(args[2]);
}
