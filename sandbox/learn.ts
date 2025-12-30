type bigType = {
    name: string
}


type smallType = {
    name: string
    age: number
}


const bt: bigType = {
    name: 'kostya',
}

const st: smallType = {
    name: 'Petr',
    age: 22
}


const check: bigType = st
console.log(check)

enum Color {
    RED = 'red'
}


function setColor(color: Color): Color {
    return color
}

console.log(setColor(Color.RED))