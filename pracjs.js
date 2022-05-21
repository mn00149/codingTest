// const re = /[\s.]/g
// const str = "나는 배짱이."
// let result = str.match(re)
// for(let aa of result) {
//     if(aa === ' '){
//         console.log('링딩동 링딩동 링딕디기')
//     }
//     if(aa === '.'){
//         console.log('링딩동 링딩동 링딩동 링딩동')
//     }
// }

const readline = require("readline");
 
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
let count = 0
rl.on("line", (line) => {
    count += 1
    if(count === 1){
        let attemp = line
    } else if(count === 2){
        let hit = line
    } else {
        rl.close();
    }
    
});
 
rl.on('close', () => {
        let temp = Math.floor((hit/attemp)*1000)
        let resultList = (temp + ' ').split(' ')
        let count = 0
        for(let i of resultList){
            count += 1
            if(i === '0'){
                continue;
            }
            if(count === 1){
                console.log(i + '할')
            }else if(count === 2){
                console.log(i + '푼')
            }else{
                console.log(i + '리')
            }
        }
        process.exit();
})