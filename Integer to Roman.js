var intToRoman = function(num) {
    const M = ['', 'M', 'MM', 'MMM'];
    // const M = ['', '1000', '2000', '3000']
    const C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'];
    // const C = ['', '100', '200', '300', '400', '500', '600', '700', '800', '900']
    const X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'];
    // const X = ['', '10', '20', '30', '40', '50', '60', '70', '80', '90']
    const I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'];
    // const I = ['', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  
  return M[Math.floor(num / 1000)] + C[Math.floor((num % 1000) / 100)] + X[Math.floor((num % 100) / 10)] + I[Math.floor(num % 10)];
  
  };