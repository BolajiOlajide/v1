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

   Javascript