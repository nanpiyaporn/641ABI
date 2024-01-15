# Set, tuple, and disctionary

- [Set, tuple, and disctionary](#set-tuple-and-disctionary)
  - [1. Sets](#1-sets)
    - [Defining sets](#defining-sets)
    - [List and set](#list-and-set)
  - [2. Set Methods and Operations](#2-set-methods-and-operations)
    - [`add()` method](#add-method)
    - [`union()` method and `|` operator](#union-method-and--operator)
    - [`intersection()` method and `&` operator](#intersection-method-and--operator)
    - [`difference()` method and `-` operator](#difference-method-and---operator)
  - [3. Modifying a Set](#3-modifying-a-set)
  - [4. Tuple](#4-tuple)
    - [Defining tuples](#defining-tuples)
    - [Slice operator](#slice-operator)
    - [Tuples are immutable](#tuples-are-immutable)
  - [5. Tuple assignment](#5-tuple-assignment)
  - [6. Lists and tuples](#6-lists-and-tuples)
    - [`zip()` function](#zip-function)
    - [`enumerate()` function](#enumerate-function)
  - [7. Practice questions - 1: Set and tuple](#7-practice-questions---1-set-and-tuple)
  - [8. A dictionary is a mapping](#8-a-dictionary-is-a-mapping)
  - [9. Lookup](#9-lookup)
  - [10. Dictionary and list/tuple](#10-dictionary-and-listtuple)
  - [11. Practice questions 2: dictionary](#11-practice-questions-2-dictionary)


## 1. Sets
### Defining sets
- Sets are another collection/container, like lists, which contain multiple values. 
- The **key differences** are
	- **Sets don't hold order**
	- **Sets don't allow duplicate elements**
- We can define a set using curly bracket, for example
    ```python
    >>> universities = {'Rutgers', 'NYU', 'Princeton'}
    >>> universities
    {'Rutgers', 'Princeton', 'NYU'}
    ```

**Set size**
- List lists, `len()` returns set size.
    ```python
    >>> universities = {'Rutgers', 'NYU', 'Princeton'}
    >>> len(universities)
    3
    ```

**`in` Operation**
- Like lists, sets also have `in` operation.
    ```python
    universities = {'Rutgers', 'NYU', 'Princeton'}

    x = 'NYU'
    if x in universities:
        print(f'{x} is in the set.')
    else:
        print(f'{x} isn't in the set.')
    ```

### List and set
- Set and list are interchangeable. It would be very useful to delete the duplicates by transforming a list to a set.
    ```python
    >>> l = [2, 0, 2, 3]
    >>> s = set(l)
    >>> s
    {0, 2, 3}
    >>> l_new = list(s)
    [0, 2, 3]
    ```
## 2. Set Methods and Operations
### `add()` method
- We can use `add()` method to add an element into a set. But **the new element could be anywhere in the set** since sets don't keep order.
    ```python
    >>> universities = {'Rutgers', 'NYU', 'Princeton'}
    >>> universities.add('Columbia')
    >>> universities
    {'Rutgers', 'Columbia', 'Princeton', 'NYU'}
    ```
- If we try to do it again, that is, add 'Columbia' again, we will get the same results. **It is because sets don't allow duplicate elements.**

### `union()` method and `|` operator
- Set union can combine sets. 
    ```python
    >>> set_1 = {1, 2, 3} 
    >>> set_2 = {2, 3, 4}
    >>> set_1.union(set_2)
    {1, 2, 3, 4}
    ```
- More than two sets may be specified with the method.
    ```python
    >>> set_1 = {1, 2, 3} 
    >>> set_2 = {2, 3, 4}
    >>> set_3 = {5, 6, 7}
    >>> set_1.union(set_2, set_3)
    {1, 2, 3, 4, 5, 6, 7}
    ```
- We can also use `|` operator to get the same result
    ```python
    >>> set_1 = {1, 2, 3} 
    >>> set_2 = {2, 3, 4}
    >>> set_3 = {5, 6, 7}
    >>> set_1|set_2|set_3
    {1, 2, 3, 4, 5, 6, 7}
    ```
### `intersection()` method and `&` operator
- `intersection()` computes the intersection of two or more sets.
- `&` operator also computes the intersection.
    ```python
    >>> set_1 = {1, 2, 3} 
    >>> set_2 = {2, 3, 4}
    >>> set_1.intersection(set_2)
    {2, 3}
    >>> set_1 & set_2
    ```

### `difference()` method and `-` operator
- `difference()` and `-` operator compute the difference between two or more sets.
    ```python
    >>> set_1 = {1, 2, 3} 
    >>> set_2 = {2, 3, 4}
    >>> set_3 = {5, 6, 7}

    >>> set_1.difference(set_2)
    {1}
    >>> set_1.difference(set_2, set_3)
    {1}
    >>> set_1 - set_2 - set_3
    {1}

    >>> set_2 - set_1
    {4}
    ```
- `set_1.difference(set_2)` or `set_1 - set_2` returns a set containing elements that are in `set_1` but not in `set_2`.

## 3. Modifying a Set
**`remove()` method**
- To delete an element, we can use `remove()` methods.
    ```python
    >>> universities = {'Rutgers', 'NYU', 'Princeton'}
    >>> universities.remove('NYU')
    >>> universities
    {'Rutgers', 'Princeton'}
    ```
- If we try to remove an element that doesn't exist in the set, there would be an error.
    ```python
    >>> universities = {'Rutgers', 'NYU', 'Princeton'}
    >>> universities.remove('Harvard')
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    KeyError: 'Harvard'
    ```

**`discard()` method**
- `x.discard(<elem>)` also removes `<elem>` from `x`. However, if `<elem>` is not in `x`, this method quietly does nothing instead of raising an exception.
    ```python
    >>> universities = {'Rutgers', 'NYU', 'Princeton'}
    >>> universities.discard('Harvard')
    ```

## 4. Tuple
### Defining tuples
- A tuple is a comma-separated list. We can define a tuple like this:
    ```python
    >>> t = 'a', 'b', 'c', 'd'
    >>> t
    ('a', 'b', 'c', 'd')
    ```
- We can also enclose tuples in parentheses:
    ```python
    >>> t = ('a', 'b', 'c', 'd')
    >>> t
    ('a', 'b', 'c', 'd')
    ```
- Specially, to create a tuple with a single element, you have to include a final comma:
    ```python 
    >>> t1 = 'a',
    >>> t1
    ('a',)
    ```
- The comma is a must, otherwise it is a string, not a tuple. Even we put a single element in parentheses without comma, it is still not a tuple.
    ```python
    >>> t1 = ('a')
    >>> type(t1)
    <class 'str'>
    ```

### Slice operator
- The slice operator selects a range of elements.
    ```python
    >>> t = ('a', 'b', 'c', 'd')
    >>> t[0]
    'a'
    >>> t[1:3]
    ('b', 'c')
    ```

### Tuples are immutable
- Tuples are immutable, and you cannot modify the elements.
    ```python
    >>> t = ('a', 'b', 'c', 'd')
    >>> t[0] = 'A'
    TypeError: 'tuple' object does not support item assignment
    ```

## 5. Tuple assignment
- We often need to define several similar variables and assign values to the variables.
    ```python
    a = 1
    b = 2
    c = 3
    ```
- The conventional method works fine. But with tuple assignment, we can make the code more elegant.
    ```python
    a, b, c = 1, 2, 3
    ```
- Sometimes we need to swap the values of two variables. For example, we would like to swap the values in variables `a` and `b`. It can be done like this:
    ```python
    a = 1
    b = 2

    temp = a
    a = b
    b = temp

    print(a)
    print(b)
    ```
- The above solution seems cumbersome. **Tuple assignment** is more elegant:
    ```python
    a = 1
    b = 2

    a, b = b, a

    print(a)
    print(b)
    ```
- In the tuple assignment, `a, b = b, a`, the left side is a tuple of variables; the right side is a tuple of expressions. Each value is assigned to its respective variable. All the expressions on the right side are evaluated before any of the assignments.
- Note: *The number of variables on the left and the number of values on the right have to be the same.*
    ```python
    >>> a, b = 1, 2, 3
    ValueError: too many values to unpack
    ```
- Tuple assignment is very useful when we would like to assign values to several variables simultaneously. For example, we learned this code before, which is to extract information from an address string.
    ```python
    address = "100 Rockafeller Rd, Piscataway, NJ"
    address_list = address.split(', ')

    street = address_list[0]
    city = address_list[1]
    state = address_list[2]
    ```
- With tuple assignment, we can finish it elegantly.
    ```python
    address = "100 Rockafeller Rd, Piscataway, NJ"
    address_list = address.split(', ')

    street, city, state = address_list
    ```
- We can see that Python is not that strict. In the last line, the left side is a tuple, while the right slide is a list. It works well, which means that Python transform a list into a tuple automatically. For sure, the above code can be further improved as follows.
    ```python
    address = "100 Rockafeller Rd, Piscataway, NJ"
    street, city, state = address.split(', ')
    ```

**Tuples as return values**
- Strictly speaking, a function can only return one value, but if **the value is a tuple**, the effect is the same as returning multiple values. 
- For example, if you want to divide two integers and compute the quotient and remainder, it is inefficient to compute x//y and then x%y as follows. 
    ```python
    def get_quotient(x, y):
        return x//y

    def get_remainder(x, y):
        return x%y

    x, y = 7, 3
    quot, rem = get_quotient(x, y), get_remainder(x, y)
    ```
- It is better to compute them both at the same time.
    ```python
    def get_quot_rem(x, y):
        return x//y, x%y

    x, y = 7, 3
    quot, rem = get_quot_rem(x, y)
    ```

## 6. Lists and tuples
### `zip()` function
- `zip()` is a built-in function that takes two or more sequences and interleaves them. The name of the function refers to a zipper, which interleaves two rows of teeth.
- Sometimes we would like to collect information for different items. For example, we have lists about County, City, and Zipcode. 
    ```python
    counties = ['MIDDLESEX', 'MIDDLESEX', 'SOMERSET']
    cities = ['Piscataway', 'HIGHLAND PARK', 'FLAGTOWN']
    zipcodes = ['08854', '08904', '08821']

    print(zip(counties, cities, zipcodes))

    ```
- We will get
    ```python
    <zip object at xxxx090xxxxxx>
    ```
- The result is a zip object that knows how to iterate through the pairs. The most common use of zip is in a `for` loop or transform it to a list:
    ```python
    counties = ['MIDDLESEX', 'MIDDLESEX', 'SOMERSET']
    cities = ['Piscataway', 'HIGHLAND PARK', 'FLAGTOWN']
    zipcodes = ['08854', '08904', '08821']

    for pair in zip(counties, cities, zipcodes):
        print(pair)
    ```
- We will get
    ```python
    ('MIDDLESEX', 'Piscataway', '08854')
    ('MIDDLESEX', 'HIGHLAND PARK', '08904')
    ('SOMERSET', 'FLAGTOWN', '08821')
    ```
- We can also transform it to a list
    ```python
    counties = ['MIDDLESEX', 'MIDDLESEX', 'SOMERSET']
    cities = ['Piscataway', 'HIGHLAND PARK', 'FLAGTOWN']
    zipcodes = ['08854', '08904', '08821']

    l_pairs = list(zip(counties, cities, zipcodes))

    print(l_pairs)
    ```
- We will get a list with three tuples.
    ```python
    [('MIDDLESEX', 'Piscataway', '08854'), ('MIDDLESEX', 'HIGHLAND PARK', '08904'), ('SOMERSET', 'FLAGTOWN', '08821')]
    ```

### `enumerate()` function
- The result from `enumerate()` is an enumerate object, which iterates a sequence of pairs; each pair contains an index (starting from 0) and an element from the given sequence.
- For example:
    ```python
    universities = ["Princeton", "MIT", "Harvard", "Stanford"]

    for i, university in enumerate(universities):
        print(i+1, university)
    ```

## 7. Practice questions - 1: Set and tuple


1. We've provided you with a list of lottery players, and also with 6 random lottery numbers. The random lottery numbers are generated like this:
    ```python
    import random
    lottery_numbers = set(random.sample(list(range(22)), 6))
    ```
    And the list of players we've given you are:

    ```python
    players = [
    ("Rolf", {1, 3, 5, 7, 11, 20}),
    ("Charlie", {2, 7, 9, 5, 12, 15}),
    ("Anna", {7, 8, 1, 3, 13, 16}),
    ("Jen", {4, 7, 3, 5, 12, 21})
    ]
    ```
    Try to find out the number of winnings for each person. For example, if the lottery number is  `6, 8, 9, 13, 16, 19`, you need to print:
    ```python
    Rolf won 0.
    Charlie won 1.
    Anna has won 3.
    Jen has won 0.
    ```

2. Try to create a function, which can take variable-length arguments and return the square root of the arguments.

3. Summary data. Create a function, named `summarize_data`, which takes a list of numbers and returns a tuple containing the minimum, mean, and the maximum values. For example, given `[1, 2, 5]`, it would return `1, 2.6666, 5`.
	- You may use some built-in functions, like `sum`, `min`, and `max` .

4. **(Optional)** Letter frequency. Create a function, named `letter_frequency`, which takes a string and prints the letters in the string (case-insensitive, or just use upper case) and corresponding frequency. For example, 
	- Given 'Rutgers, RBS', the function would print `[('G', 1), ('U', 1), ('B', 1), ('T', 1), ('R', 3), (',', 1), ('E', 1), ('S', 2)]`


## 8. A dictionary is a mapping

**Dictionary**
- A dictionary is like a list, but more general.
- In a list, there are values and corresponding indices. For example, in a list, `l = ['a', 'b', 'c']`, the values are  'a', 'b', and 'c', and the indices are 0, 1, 2, and 3.
- In a dictionary, the indices can be (almost) any type.
- A dictionary contains a collection of indices, which are called *keys*, and a collection of values. Each key is associated with a single value. 
- The association of a key and a value is called *Key-value pair* or sometime an *item*.

**Defining Dictionary**
- We can *define a dictionary* in the following way.
	```python
	>>> eng2arabic = {'one': 1, 'two': 2, 'three': 3}
	```

- We can *add new items*
	```python
	>>> eng2arabic = {'one': 1, 'two': 2, 'three': 3}
	>>> eng2arabic['four'] = 4
	>>> eng2arabic
	{'one': 1, 'two': 2, 'three': 3, 'four': 4}
	```
- Define an empty dictionary, then add items.
	```python
	>>> d = dict() # d would be an empty dictionary
	>>> d['one'] = 1
	>>> d['two'] = 2
	>>> d
	{'one': 1, 'two': 2}
	```

## 9. Lookup

**`len` function**
- The `len` function works on dictionaries; it returns the number of key-value pairs:
	```python
	>>> eng2arabic = {'one': 1, 'two': 2, 'three': 3}
	>>> len(eng2arabic)
	3
	```

**Lookup**
- Then we can *access the values* via the keys.
	```python
	>>> eng2arabic = {'one': 1, 'two': 2, 'three': 3}
	>>> eng2arabic['one']
	1
	```

**`in` operator**
- The in operator works on dictionaries, too; it tells you whether something appears as a *key* in the dictionary.
	```python
	>>> eng2arabic = {'one': 1, 'two': 2, 'three': 3}
	>>> 'one' in eng2arabic
	True
	>>> 1 in eng2arabic
	False
	```

**Get keys and values**
- We can get keys and values using the following code.
	```python
	>>> eng2arabic = {'one': 1, 'two': 2, 'three': 3}
	>>> eng2arabic.keys()
	dict_keys(['one', 'two', 'three'])
	>>> eng2arabic.values()
	dict_values([1, 2, 3])
	```
- For sure, we can transform them into lists by using `list()` function
	```python
	>>> eng2arabic = {'one': 1, 'two': 2, 'three': 3}
	>>> list(eng2arabic.keys())
	['one', 'two', 'three']
	>>> list(eng2arabic.values())
	[1, 2, 3]
	```
- Then, we can print the pairs in the dictionary.
	```python
	eng2arabic = {'one': 1, 'two': 2, 'three': 3}

	for key in eng2arabic.keys():
		print(key, eng2arabic[key])
	```

## 10. Dictionary and list/tuple 
- We mentioned that tuples are useful for collecting data that are highly correlated. 
	```python
	cities = ['PISCATAWAY', 'HIGHLAND PARK', 'FLAGTOWN']
	zipcodes = ['08854', '08904', '08821']

	l_pairs = list(zip(cities, zipcodes))

	print(l_pairs)
	```
- The output would be as follows. It is a list with three tuples. In each tuple, there are city names and the corresponding zip-code.
	```python
	[('PISCATAWAY', '08854'), ('HIGHLAND PARK', '08904'), ('FLAGTOWN', '08821')]
	```
- We can also use dictionary, which is more convenient for us to loop up.
	```python
	cities = ['PISCATAWAY', 'HIGHLAND PARK', 'FLAGTOWN']
	zipcodes = ['08854', '08904', '08821']

	d = dict(zip(cities, zipcodes))
	print(d)

	print(d['PISCATAWAY'])
	```

**Dictionary comprehension**
- Instead of `zip` function, we can also use dictionary comprehension just like list comprehension.
	```python
	cities = ['PISCATAWAY', 'HIGHLAND PARK', 'FLAGTOWN']
	zipcodes = ['08854', '08904', '08821']

	d = {
		cities[i]: zipcodes[i] 
		for i in range(len(cities))
	}

	print(d['PISCATAWAY'])
	```
- It seems the result is the same as that by using `zip` function. But comprehension could be very useful in some scenarios. For example, in the following example, we have a list of student names and a list of ages of the corresponding students. We would like to get the dictionary for students older than 20 years old.
	```python
	names = ['Jack', 'Mark', 'Mary', 'Jenny']
	ages = [22, 18, 21, 17]

	d = {
		names[i]: ages[i] 
		for i in range(len(names)) 
		if ages[i]>20
	}
	print(d)
	```
- The output would be
	```python
	{'Jack': 22, 'Mary': 21}
	```

## 11. Practice questions 2: dictionary
1. Character counts. Given a string, try to obtain the counts of the characters in it (case insensitive). For example, given "Rutgers, RBS", the output should be the dictionary, {'T': 1, 'R': 3, 'B': 1, 'E': 1, ' ': 1, 'S': 2, 'U': 1, 'G': 1}.

2. Reverse lookup. The following dictionary shown the rosters of the three courses. We can easily check the student names each course has. Now we would like to do reverse lookup. That is, we would like to get a dictionary showing the courses that each student is taking. 
	```python
	roster = {
		'STATS_385': ['Jack', 'Anne', 'John', 'Peter'],
		'PROG_388': ['Tom', 'Mark', 'Jack', 'Jin'],
		'LARGESCALE_487': ['Anne', 'John', 'Jin', 'Jack']
	}
	```


