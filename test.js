let x=1;
let b=2055
let m=2579
let power = b%m;
let n="101010"
for (let i=5; i>=0; i--) {
    if (n[i]===1) {
        x=(x*power) % m
    }

    power = (power*power) % m
}

console.log(x)