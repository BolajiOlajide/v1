---
template: post
title: Javascript is weird?
slug: javascript-gotchas
draft: true
date: 2020-07-30T12:40:42.321Z
description: In this article, I try to explain some Javascript weirdness that
  confused me when I started writing javascript.
category: tech
tags:
  - javascript
  - gotchas
  - programming
---
I recently stumbled on a [tweet](https://twitter.com/Ashot_/status/1287818215465324546?s=20) about some of the things considered weird in Javascript. I decided to write this post to share some of the reasons why this things are in javascript. 

Understanding why they are, will lead to less confusion about the way the language handles operations across several data types.

1. **Why is the `typeof NaN === 'number'`?**

   `NaN` stands for `Not a Number` but suprisingly is a number. 

   This is one thing I considered weird when I started writing Javascript.

   I understood why that is after reading an article on [Ire Aderinokun's blog](https://bitsofco.de/javascript-typeof/#whatsthetypeofnan), I quote from her blog:

   > The type of `NaN`, which stands for Not a Number is, surprisingly, a number. The reason for this is, in computing, `NaN` is actually technically a numeric data type. However, it is a numeric data type whose value cannot be represented using actual numbers. So, the name "Not a Number", doesn't mean that the value is not numeric. It instead means that the value cannot be expressed with numbers.
2. **Why is 9999999999999999 converted to 10000000000000000 in JavaScript?**

   Javascript doesn't have integers. **9999999999999999** is treated internally as a floating point number and at this point has ran out of floating-point precision.

   Someone explained it beautifully on StackOverflow [here](https://stackoverflow.com/questions/13429451/why-is-9999999999999999-converted-to-10000000000000000-in-javascript#answer-13429506).
3. **0.1 + 0.2 !== 0.3**

      I remember having a chat with [Michael](https://twitter.com/mykeels) about this some months back. I was literally pulling my hair and cursing because it didn't make any sense to me. I decided to research more about it and I found a really helpful explanation [here](https://javascript.info/number).

   > A number is stored in memory in its binary form, a sequence of bits – ones and zeroes. But fractions like `0.1`, `0.2` that look simple in the decimal numeric system are actually unending fractions in their binary form.
   >
   > In other words, what is `0.1`? It is one divided by ten `1/10`, one-tenth. In decimal numeral system such numbers are easily representable. Compare it to one-third: `1/3`. It becomes an endless fraction `0.33333(3)`.
   >
   > So, division by powers `10` is guaranteed to work well in the decimal system, but division by `3` is not. For the same reason, in the binary numeral system, the division by powers of `2` is guaranteed to work, but `1/10` becomes an endless binary fraction.
   >
   > There’s just no way to store *exactly 0.1* or *exactly 0.2* using the binary system, just like there is no way to store one-third as a decimal fraction.
   >
   > The numeric format IEEE-754 solves this by rounding to the nearest possible number. These rounding rules normally don’t allow us to see that “tiny precision loss”, but it exists.

   Understanding the floating point arithmetic is very crucial to understanding why this is.

   ```javascript
   console.log(0.1.toFixed(20)); // 0.10000000000000000555

   // And when we sum two numbers, their “precision losses” add up.

   // That’s why 0.1 + 0.2 is not exactly 0.3.

   console.log(0.1 + 0.3) // 0.30000000000000004
   ```
4. **Math.max() === -Infiinity and Math.min() === Infinity**

      Weird right?

      The question I asked myself when I saw this is, **what exactly does Math.max() do?**

      I initially confused it with `Number.MAX_VALUE` which represents the maximum numeric value representable in JavaScript. Values greater than `Number.MAX_VALUE` are represented as Infinity.

   ```javascript
   Infinity > Number.MAX_VALUE // true
   ```

      `Math.max` is a function that returns the largest of the zero or more numbers given as input parameters, when we call `Math.max()` we pass in no arguments.

   ```javascript
   Math.max(1,4,2) // 4

   Math.min(2,1,3) // 1

   Math.min(1) // 1
   ```

   When we pass in just `1` into the `Math.min` function, the function returns `1` because that's the sole value passed into the function. Internally, the function needs something to compare values passed into it against, like a starting value, let's call this an `Identity` variable.

   These articles might help make things clearer:

   * [Math.min returns Infinity?](https://dev.to/dance2die/math-min-returns-infinity-1bi6)
   * [Why is Math.max() less than Math.min()?](https://charlieharvey.org.uk/page/why_math_max_is_less_than_math_min)
5. **\[] + \[] == ""**

      Adding two arrays returns an empty string, this happens because the \`+\` o[perator only exists for strings and numbers ](https://tc39.es/ecma262/#sec-addition-operator-plus)in javascript. When you try to add two arrays, Javascript tries to convert the array into a string by extracting the content of the array and converting it to a string, if the array is empty then it defaults to an empty string, hence why \`\[] + \[] == ""\`.

   ```javascript
   [] + [] // ""
   ['bol'] + ['aji'] // 'bolaji'
   ['bo', 'la'] + ['ji'] // bo,laji
   ```

   Javascript is basically calling the `toString` method on the array prototype and concatenating the result.
6. **\[] + {} === '\[object Object]'**

   From our understanding of the way the addition operator works so far we know the operator works mainly with strings and numbers. We can convert an array to a string using the `toString` method that exists on the Array prototype.

   ```javascript
   var arr = ['bol', 'aji']
   console.log(arr.toString()) // 'bol,aji'

   // we can also coerce it into a string using the `String` method in javscript
   console.log(String(arr)) // 'bol,aji'
   ```

   However, when we try to coerce an object the result is `'[object Object]'` and that's why `[] + {}` is equal to `'[object Object]'`.

   ```
   var arr1 = []
   var arr2 = ['proton']
   var obj = {}

   console.log(arr1 + obj) // '[object Object]'
   console.log(arr2 + obj) // 'proton[object Object]'
   ```