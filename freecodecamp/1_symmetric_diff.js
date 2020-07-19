/* Create function that calculates symmetric difference

Test 1: 
a=[1,2,3]
b=[1,3,5]

Symmetric difference of a and b is [2,5]

We need to remove common elements between arrays and also ignore duplicate elements within same array

Test 2: 
a=[1,2,3]
b=[1,3,5]
c=[2,4,6]
Symmetric difference of a, b and c is [4,5, 6]

First calculate sym diff of a and b and then use result and c to get final symmetric difference

*/
function sym(...args) {
    if(args.length > 0){
      let diff = new Set(args[0]);
      for(let i=1 ; i<args.length;i++){
        let arr = [...new Set(args[i])]
        for(let j=0; j<arr.length;j++){
            if(!diff.has(arr[j])){
              diff.add(arr[j]);
            }else{
              diff.delete(arr[j]);
            }
        }
      }
      return Array.from(diff);
    }
  
    return args;
  }
  
  let result = sym([1, 2, 3], [5, 2, 1, 4]);
  console.log(result);