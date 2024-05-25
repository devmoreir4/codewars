function highAndLow(numbers){
    let nums = numbers.split(' ').map(Number)
    
    let max = Math.max(...nums);
    let min = Math.min(...nums);
    
    return `${max} ${min}`;
  }