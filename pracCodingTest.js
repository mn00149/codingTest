const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let fruits = [];

rl.on('line', (line) => {
    fruits = line.split(' ');
    rl.close();
  })
  .on('close', () => {
    fruits.filter((item) => item !== '콩' )
    console.log(fruits)
    process.exit();
  });