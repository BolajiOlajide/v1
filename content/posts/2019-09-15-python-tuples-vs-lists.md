---
template: post
title: Python Tuples vs Lists
slug: /posts/python-tuples-lists
draft: true
date: 2019-09-14T23:41:22.605Z
description: This article sheds light on the difference between a tuple and a list.
category: Tech
tags:
  - python
  - tuple
  - list
  - mutability
---
Tuples and Lists are commonly-used data structures used in Python. A lot of libraries and projects use them in different ways. They are both heterogeneous collections of items.

They are both very similar, some of the properties they have in common include:

* They can hold any data type (strings, integers, dictionaries etc can be stored in a tuple or a list)
* They both support indexing


Seeing how similar they are, what then is the difference between a tuple and a list?

### Tuples

Tuples are denoted with parentheses. Example:

```python
names = ('bolaji',)
items = ('apple', 'oranges', 'pineapple')
```

Notice when we are initialising a tuple with just one item, we append a trailing comma to it. The parenthesis don't automatically make them tuples. You have to add a comma after the string to indicate to python that it should be a tuple, however this isn't compulsory when you have more than one item in the tuple.

You can also create tuples using the `tuple` constructor, 

### Lists
A list are denoted with square brackets. It is somewhat similar to what you'll call an array in other programming languages like Javascript.

The main difference between a list and a tuple is that a list is mutable while a tuple is immutable.

Mutability refers to the liability or tendency for something to change.

Some folks get confused by what mutability means in this context as python doesn’t have the `const` keyword to define a variable that can’t be changed. I had this same thought when I was learning about tuples, coming from a JavaScript background. The concept of mutability here is concerning the index - an index in a list can be reassigned a new variable. 
We can shift items, pop them and so on, but in a tuple, we can’t do this because it’s immutable.
Take a look at the screenshot below to understand what happens when you try to mutate a tuple.

![immutability in tuples](/media/screenshot-2019-09-07-at-1.16.23-am.png)

From the screenshot above, you can see that overwriting the item at index 2 in the list is fine but when we try to do the same with a tuple we get an error. 

Tuples are used whenever we want to ensure immutability in a collection so no user action can overwrite the content at the index. However, we can reassign something else to the variable `store_tuple` because the variable is only a container that holds a reference to the tuple we created.

Did you find this helpful? Feel free to share a comment in the comment section below.
