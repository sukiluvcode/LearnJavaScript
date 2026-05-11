## JavaScript Fundamentals

### Variables — Declare and store data

- Use `let` for variables that can change, `const` for constants
- Avoid `var` (legacy, has scoping issues); modern JS uses `let`/`const`

```js
let age = 25;
const name = 'Alice';
```

### Alert / Prompt / Confirm — Interact with the user (browser only)

- `alert(msg)` — shows a message, no return value
- `prompt(msg)` — asks for text input, returns the string or `null` if cancelled
- `confirm(msg)` — asks OK/Cancel, returns `true` or `false`
- All three are **modal**: they pause script execution until dismissed
- The position and style of the dialog are controlled by the browser, not your code

```js
alert('Hello!');
let name = prompt('What is your name?');
let confirmed = confirm('Are you sure?');
```

### Operators — Perform operations on values

- **Unary `+`** — converts a value to a number
  ```js
  +'42'   // → 42 (number)
  ```
- **Binary `+`** — adds numbers, but concatenates if either side is a string
  ```js
  1 + '2'   // → '12' (string)
  1 + 2     // → 3 (number)
  ```
- **Assignment `=`** — assigns a value and also *returns* it (unlike Python)
  ```js
  let a = (b = 5); // b and a are both 5
  ```

### Comparisons — Compare values

- `==` — equality with **type conversion** (e.g. `'5' == 5` is `true`); special case: `null` and `undefined` only equal each other
- `===` — **strict** equality, no type conversion (`'5' === 5` is `false`)
- `>`, `<`, `>=`, `<=` — also do type conversion by default

```js
0 == false    // true  (type conversion)
0 === false   // false (strict)
null == undefined  // true
null === undefined // false
```

### If / Else — Conditional logic

- Use `if / else if / else` for multi-branch logic
- Use the ternary `?` operator for simple one-line conditions

```js
if (score >= 90) {
  console.log('A');
} else if (score >= 70) {
  console.log('B');
} else {
  console.log('F');
}

// Ternary shorthand
let result = (score >= 70) ? 'Pass' : 'Fail';
```

### Logical operators
- &&, ||, !
equivalent of python and, or, not

### Nullish coalescing operator
- ??
`a ?? b`
?? returns the first argument if it’s not null/undefined. Otherwise, the second one.

### Loops — Repeat code while a condition is true

- **`while`** — checks condition first, then runs the body
  ```js
  while (condition) { ... }
  ```
- **`do...while`** — runs the body first, then checks; always executes at least once
  ```js
  do { ... } while (condition);
  ```
- **`for`** — most common; has begin, condition, and step in one line
  ```js
  for (let i = 0; i < 5; i++) { ... }
  ```

### Loop Control — break and continue

- **`break`** — exits the loop immediately
- **`continue`** — skips the rest of the current iteration, moves to the next
  ```js
  for (let i = 0; i < 10; i++) {
    if (i % 2 === 0) continue; // skip even numbers
    if (i > 7) break;          // stop at 8
    console.log(i);            // prints 1, 3, 5, 7
  }
  ```
- Ternary `?` cannot replace `if` when `break`/`continue` is needed

### Labels — Break out of nested loops

- A label marks a loop so `break`/`continue` can target it specifically
- Labels do **not** let you jump to arbitrary places in code — only to the labelled loop

  ```js
  outer: for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      if (j === 1) break outer; // exits both loops
    }
  }
  ```

### switch

similar to python match case

```js
switch (arg) {
  case expression1:
    ...
    [break]
  case expression2:
    ...
    [break]
  default:
    ...
}
```
If the equality is found, switch starts to execute the code starting from the corresponding case, until the nearest break (or until the end of switch).

grouping of "case"

```js
...
case case1:
case case2:
  ...
  [break]
...
```
where case1 and case2 run the same codes

### Functions — Declare and call reusable code

- Use the `function` keyword (unlike Python's `def`)
- A missing argument becomes `undefined`, not an error

```js
function greet(name) {
  console.log('Hello, ' + name);
}
greet('Alice');
```

- **Default parameters** — same idea as Python, but the default expression re-evaluates every call
  ```js
  function showMessage(from, text = 'no text given') {
    console.log(from + ': ' + text);
  }
  ```

- **Return** — works like Python, but without a `return` the function returns `undefined` (not `None`)

- **Watch out — auto semicolon after `return`**: unlike Python, putting the value on the next line silently returns `undefined`
  ```js
  // Bug: returns undefined
  return
    someValue;

  // Correct: wrap in parentheses
  return (
    someValue
  );
  ```

- **Scope** — local variables are invisible outside the function, same as Python; outer variables are readable unless shadowed by a local one

- **Naming convention** — use action-verb prefixes to signal intent:
  - `get…` — returns a value
  - `create…` — creates something
  - `check…` — returns a boolean
  - `show…` — displays something

### Function Expressions — Functions as values

- In JS, functions are values — you can store, copy, and pass them around (like Python's first-class functions)
- A **function expression** assigns an anonymous function to a variable; note the `;` at the end (it's an assignment statement)
  ```js
  let greet = function() {
    console.log('Hello');
  };
  greet();
  ```

- **Hoisting** (key difference from Python): function *declarations* are available before their definition in the file; function *expressions* are not
  ```js
  sayHi(); // works — declaration is hoisted
  function sayHi() { console.log('Hi'); }

  greet(); // Error — expression not hoisted yet
  let greet = function() { console.log('Hi'); };
  ```

- **Callbacks** — pass a function as an argument to be called later (same concept as Python, just different syntax)
  ```js
  function ask(question, onYes, onNo) {
    if (confirm(question)) onYes();
    else onNo();
  }

  ask('Are you sure?', () => console.log('OK'), () => console.log('Cancelled'));
  ```

- **When to use which**: prefer function declarations (more readable, hoisted); use expressions when you need to conditionally define a function or assign it based on logic

### Arrow Functions — Concise function syntax

- Shorter alternative to function expressions, similar to Python lambdas but more powerful
- Single-line: the expression is **implicitly returned** (no `return` needed)
  ```js
  let sum = (a, b) => a + b;
  let double = n => n * 2;      // single param: no parentheses needed
  let greet = () => 'Hello!';   // no params: empty parentheses required
  ```

- Multi-line: use curly braces, but then `return` is **required** explicitly
  ```js
  let sum = (a, b) => {
    let result = a + b;
    return result;
  };
  ```

- Compared to Python lambdas: arrow functions can span multiple lines and contain full logic; Python lambdas are limited to a single expression
- Commonly used for short callbacks
  ```js
  [1, 2, 3].map(n => n * 2); // [2, 4, 6]
  ```

### Objects — Key-value data structure (like Python dicts)

- Create with `{}` literals (preferred) or `new Object()`
- Access with dot notation or square brackets; use square brackets for dynamic keys or multiword property names
  ```js
  let user = { name: 'Alice', age: 25 };
  user.name;         // 'Alice'
  user['age'];       // 25
  user.isAdmin = true;
  delete user.age;
  ```

- **Computed properties** — dynamic key names at creation time
  ```js
  let field = 'name';
  let user = { [field]: 'Alice' }; // { name: 'Alice' }
  ```

- **Property shorthand** — when variable name matches property name
  ```js
  let name = 'Alice', age = 25;
  let user = { name, age }; // same as { name: name, age: age }
  ```

- **`in` operator** — check if a property exists (more reliable than `=== undefined`)
  ```js
  'name' in user  // true
  'foo' in user   // false
  ```

- **`for...in` loop** — iterate over all properties (like Python's `for key in dict`)
  ```js
  for (let key in user) {
    console.log(key, user[key]);
  }
  ```
  - Integer-like keys are sorted numerically; all other keys appear in insertion order

### Object References & Copying — Objects are passed by reference

- Primitives (`number`, `string`, etc.) are copied by value; objects are copied **by reference** — same as Python
  ```js
  let a = { name: 'Alice' };
  let b = a;       // b points to the same object
  b.name = 'Bob';
  console.log(a.name); // 'Bob'
  ```

- **Comparing objects**: `==` and `===` check reference identity, not contents — two objects with identical properties are NOT equal
  ```js
  let x = {}, y = {};
  x === y; // false — different objects in memory
  ```

- **`const` objects are still mutable** — `const` only prevents reassigning the variable, not modifying its properties
  ```js
  const user = { name: 'Alice' };
  user.name = 'Bob'; // allowed
  user = {};         // Error
  ```

- **Shallow clone** — `Object.assign(target, source)` copies top-level properties only; nested objects are still shared by reference
  ```js
  let clone = Object.assign({}, user);
  ```

- **Deep clone** — `structuredClone(obj)` fully copies all nested objects; handles circular references but cannot clone functions
  ```js
  let deepClone = structuredClone(user);
  ```

### Object Methods & `this` — Functions inside objects

- A function stored as an object property is called a **method**
- **Method shorthand** — omit the `function` keyword (preferred)
  ```js
  let user = {
    name: 'Alice',
    greet() {             // shorthand
      console.log('Hi, I am ' + this.name);
    },
  };
  ```

- **`this` is bound at call time, not definition time** (key difference from Python's `self`)
  - `this` refers to the object *before the dot* at the moment of the call
  - The same function called through different objects gets a different `this`
  ```js
  function sayHi() { console.log(this.name); }

  let alice = { name: 'Alice', say: sayHi };
  let bob   = { name: 'Bob',   say: sayHi };

  alice.say(); // 'Alice'
  bob.say();   // 'Bob'
  ```

- Calling without an object context: `this` is `undefined` (strict mode) or the global object — a common source of bugs
  ```js
  let say = alice.say;
  say(); // undefined — no object before the dot
  ```

- **Arrow functions have no own `this`** — they inherit `this` from the surrounding scope, useful in callbacks
  ```js
  let user = {
    name: 'Alice',
    greet() {
      let inner = () => console.log(this.name); // this = user
      inner();
    }
  };
  user.greet(); // 'Alice'
  ```

### Constructor Functions & `new` — Create multiple similar objects

- A constructor is a regular function named with a **capital letter**, called with `new` (like a class in Python)
- `new` automatically: creates an empty object → assigns it to `this` → runs the function body → returns `this`
  ```js
  function User(name) {
    this.name = name;
    this.isAdmin = false;
  }

  let alice = new User('Alice');
  let bob   = new User('Bob');
  ```

### Optional Chaining — Safely access possibly-missing properties

Three forms, all return `undefined` instead of throwing if the left side is `null`/`undefined`:

- **`obj?.prop`** — safe property access
  ```js
  user?.address?.street  // undefined if user or address is missing
  ```
- **`obj?.[key]`** — safe bracket notation
  ```js
  user?.['firstName']
  ```
- **`obj.method?.()`** — safe method call
  ```js
  userGuest.admin?.()  // does nothing if admin method doesn't exist
  ```

### Symbols — Guaranteed unique identifiers

- Created with `Symbol(description)` — the description is just a label for debugging, not the value
- Every symbol is **always unique**, even if two have the same description
  ```js
  Symbol('id') === Symbol('id') // false
  ```
- Symbols don't auto-convert to strings — use `.toString()` or `.description` to display them
- Used as object property keys to avoid name collisions (e.g. when adding properties to third-party objects)
  ```js
  let id = Symbol('id');
  user[id] = 123; // hidden from other code using string keys
  ```
- **Symbols are skipped** by `for...in` and `Object.keys()` — they stay "hidden" from normal iteration
- **Global symbol registry** — `Symbol.for(key)` creates/reuses the same symbol across the whole app; `Symbol.keyFor(sym)` looks up its key
  ```js
  let s1 = Symbol.for('shared');
  let s2 = Symbol.for('shared');
  s1 === s2; // true
  ```
- **Well-known symbols** like `Symbol.iterator` and `Symbol.toPrimitive` let you customize built-in JS behaviors

### Object-to-Primitive Conversion — How objects become primitives

- JS uses a **hint** to decide how to convert an object:
  - `"string"` — when a string is expected (e.g. `alert(obj)`, using obj as a key)
  - `"number"` — for math operations and numeric comparisons
  - `"default"` — for ambiguous operators like binary `+` or `==`

- Conversion priority (JS checks in this order):
  1. `Symbol.toPrimitive(hint)` — if defined, handles all hints in one method
  2. `toString()` then `valueOf()` for `"string"` hint (reversed for `"number"`)
  ```js
  let user = {
    name: 'Alice',
    [Symbol.toPrimitive](hint) {
      return hint === 'string' ? this.name : 42;
    }
  };
  alert(user);  // 'Alice'  (string hint)
  +user;        // 42       (number hint)
  ```

- If only `toString()` is defined, it handles all conversion contexts
- Conversion methods must return a **primitive** — returning an object is ignored
- **Further conversions**: the returned primitive may be coerced again (e.g. a string returned from `+` might get converted to a number for a later `*`)

### Primitive Methods — How primitives can have methods

- Unlike Python (where everything is an object), JS primitives are lightweight values — but they still support methods
- When you call a method on a primitive, JS **temporarily wraps it** in an object, runs the method, then discards the wrapper immediately
  ```js
  'hello'.toUpperCase(); // 'HELLO' — a String wrapper is created and thrown away
  (1.5).toFixed(0);      // '2'    — a Number wrapper is created and thrown away
  ```
- Wrapper types: `String`, `Number`, `Boolean`, `Symbol`, `BigInt`
- `null` and `undefined` have no wrappers — accessing any property on them throws an error

- **Never use `new Number()` / `new String()`** — they create objects, not primitives, causing subtle bugs:
  ```js
  typeof new Number(0)  // 'object' (not 'number'!)
  if (new Number(0)) {} // always true — objects are truthy, even zero
  ```
- Use `Number()` / `String()` **without `new`** for type conversion — that returns a primitive

### Numbers — Working with numeric values

- Use `_` as a visual separator for readability: `1_000_000`
- `num.toString(base)` — converts a number to a string in the given base; calling directly on a literal needs two dots or parentheses
  ```js
  (255).toString(16); // 'ff'
  (255).toString(2);  // '11111111'
  123..toString(2);   // two dots needed when calling on a bare literal
  ```

- **Rounding methods**:
  ```js
  Math.floor(3.7);      // 3  — always rounds down
  Math.ceil(3.1);       // 4  — always rounds up
  Math.round(3.5);      // 4  — rounds to nearest
  Math.trunc(3.9);      // 3  — removes decimal part (no rounding)
  (3.141).toFixed(2);   // '3.14' — rounds to n decimal places, returns a string
  ```

- **Checking special values**:
  ```js
  isNaN('str');      // true  — converts to number first, then checks
  isFinite('15');    // true  — '15' converts to 15, which is finite
  isFinite(Infinity) // false
  ```

- **Parsing numbers from strings** — stops at the first non-numeric character (useful for CSS values):
  ```js
  parseInt('100px');   // 100
  parseFloat('12.3em'); // 12.3
  parseInt('a123');    // NaN — fails immediately if it starts with non-digit
  ```

### Strings — Working with text

- Use backticks `` ` `` for multiline strings and template literals; single/double quotes cannot span lines
- `.length` is a **property**, not a method (no parentheses)
- Access characters with `[pos]` or `.at(pos)`; use `.at(-1)` for the last character — `[-1]` returns `undefined`
  ```js
  let str = 'Hello';
  str[0];    // 'H'
  str.at(-1); // 'o'
  str[-1];   // undefined
  ```

- Iterate over characters with `for...of`
- Strings are **immutable** — you can't change individual characters, only create new strings

- **Case conversion**:
  ```js
  'hello'.toUpperCase(); // 'HELLO'
  'Interface'[0].toLowerCase(); // 'i'
  ```

- **Searching**:
  ```js
  let str = 'Widget with id';
  str.indexOf('Widget'); // 0  — returns index or -1 if not found
  str.includes('with');  // true — returns boolean
  ```

- **Slicing** — `str.slice(start, end)` extracts a substring; negative values count from the end
  ```js
  let str = 'stringify';
  str.slice(0, 5);  // 'strin'  — from 0 up to (not including) 5
  str.slice(2);     // 'ringify' — from index 2 to end
  str.slice(-4);    // 'gify'   — last 4 characters
  str.slice(-4, -1) // 'gif'    — negative start to negative end
  ```

### Arrays — Ordered list of values (like Python lists)

- Create with `[]`; elements can be mixed types
  ```js
  let arr = [1, 'hello', true];
  arr[0];      // 1
  arr.at(-1);  // true — last element; arr[-1] returns undefined
  ```

- **Queue / stack methods** (all mutate the original array):
  ```js
  arr.push('x');    // add to end     (like Python list.append)
  arr.pop();        // remove from end (like Python list.pop)
  arr.unshift('x'); // add to front   (like Python list.insert(0, x))
  arr.shift();      // remove from front
  ```

- **Iterating** — use `for...of` (not `for...in`; `for...in` is for objects and has unexpected behavior on arrays)
  ```js
  for (let item of arr) {
    console.log(item);
  }
  ```

- **`length`** — not the count of elements but the greatest numeric index plus one; can be set manually
  ```js
  arr.length = 0; // empties the array
  ```

- **`toString`** — converts to a comma-separated string
  ```js
  [1, 2, 3].toString(); // '1,2,3'
  ```

- **Never compare arrays with `==`** — arrays are objects, so `==` checks reference identity, not contents
  ```js
  [] == []  // false — two different objects
  ```

### Array Methods: Modify & Combine — splice, slice, concat

- **`splice(pos, deleteCount, ...items)`** — removes `deleteCount` elements at `pos`, optionally inserts `...items`; **mutates** the original, returns the removed elements
  ```js
  let arr = ['I', 'study', 'JavaScript'];
  arr.splice(1, 1);                 // removes 'study' → ['I', 'JavaScript']
  arr.splice(1, 0, 'also', 'love'); // inserts without removing
  arr.splice(-1, 1);                // negative index: counts from the end
  ```

- **`slice(start, end)`** — returns a **new** array with elements from `start` up to (not including) `end`; negative indices count from the end; does not mutate
  ```js
  let arr = ['t', 'e', 's', 't'];
  arr.slice(1, 3);  // ['e', 's']
  arr.slice(-2);    // ['s', 't']
  ```

- **`concat(...items)`** — returns a **new** array combining the current array with `...items`; array arguments are spread in, other values are appended as single items
  ```js
  [1, 2].concat([3, 4], 5); // [1, 2, 3, 4, 5]
  ```

### Array Methods: Search & Iterate — indexOf, find, filter, forEach

- **`indexOf(item, from)` / `lastIndexOf(item, from)`** — returns the first/last index of `item` using strict equality (`===`), or `-1` if not found
  ```js
  let arr = [1, 0, false, 1];
  arr.indexOf(1);      // 0
  arr.lastIndexOf(1);  // 3
  ```

- **`includes(value)`** — returns `true` if the array contains `value`; handles `NaN` correctly (unlike `indexOf`)
  ```js
  [NaN].includes(NaN); // true
  [NaN].indexOf(NaN);  // -1 (indexOf can't find NaN)
  ```

- **`find(func)` / `findIndex(func)`** — returns the **first** element (or its index) where `func` returns truthy; `undefined` / `-1` if nothing matches
  ```js
  let users = [{ id: 1, name: 'Alice' }, { id: 2, name: 'Bob' }];
  users.find(u => u.id === 2);      // { id: 2, name: 'Bob' }
  users.findIndex(u => u.id === 2); // 1
  ```

- **`filter(func)`** — returns a **new** array of all elements where `func` returns truthy (like Python's `filter`)
  ```js
  users.filter(u => u.id < 2); // [{ id: 1, name: 'Alice' }]
  ```

- **`forEach(func)`** — calls `func(item, index, array)` for every element; always returns `undefined` — use only for side effects
  ```js
  ['Bilbo', 'Gandalf'].forEach((name, i) => console.log(i, name));
  ```

### Array Methods: Transform — map, sort, reverse, split/join, reduce

- **`map(func)`** — returns a **new** array where each element is the result of `func(item)`; does not mutate (like Python list comprehensions)
  ```js
  ['Bilbo', 'Gandalf'].map(name => name.length); // [5, 7]
  ```

- **`sort(func)`** — sorts the array **in place** (mutates); without a comparator it converts elements to strings first — always pass a comparator for numbers
  ```js
  [1, 10, 2].sort();                 // [1, 10, 2] — wrong! (string sort)
  [1, 10, 2].sort((a, b) => a - b);  // [1, 2, 10] — correct numeric sort
  ```

- **`reverse()`** — reverses the array **in place** (mutates); also returns a reference to the same array
  ```js
  [1, 2, 3].reverse(); // [3, 2, 1]
  ```

- **`str.split(delim)` / `arr.join(glue)`** — `split` breaks a string into an array; `join` combines an array into a string
  ```js
  'Bilbo, Gandalf'.split(', ');       // ['Bilbo', 'Gandalf']
  ['Bilbo', 'Gandalf'].join(' and '); // 'Bilbo and Gandalf'
  'hi'.split('');                     // ['h', 'i'] — splits into characters
  ```

- **`reduce(func, initial)` / `reduceRight(func, initial)`** — accumulates all elements into a single value; `func` receives `(accumulator, item, index, array)`; `reduceRight` processes right-to-left
  ```js
  [1, 2, 3, 4, 5].reduce((sum, n) => sum + n, 0); // 15
  ```
  - Always provide the `initial` value — omitting it throws on empty arrays

### Array Methods: Other — isArray, some, every, flat, fill, copyWithin

- **`Array.isArray(value)`** — returns `true` if `value` is an array; necessary because `typeof []` returns `'object'`
  ```js
  Array.isArray([]);  // true
  Array.isArray({});  // false
  typeof [];          // 'object' — not useful for distinguishing arrays
  ```

- **`some(func)` / `every(func)`** — `some` returns `true` if *at least one* element passes; `every` returns `true` if *all* pass; both short-circuit on the first decisive result
  ```js
  [1, 2, 3].some(n => n > 2);  // true
  [1, 2, 3].every(n => n > 0); // true
  ```

- **`flat(depth)` / `flatMap(func)`** — `flat` flattens nested arrays up to `depth` levels (default 1); `flatMap` maps then flattens one level in one pass
  ```js
  [[1, 2], [3, 4]].flat();         // [1, 2, 3, 4]
  [1, 2].flatMap(n => [n, n * 2]); // [1, 2, 2, 4]
  ```

- **`fill(value, start, end)`** — fills elements from `start` to `end` with `value` **in place**
  ```js
  new Array(3).fill(0);        // [0, 0, 0]
  [1, 2, 3, 4].fill(0, 1, 3); // [1, 0, 0, 4]
  ```

- **`copyWithin(target, start, end)`** — copies a slice of the array to `target` position **in place**, overwriting existing elements; rarely used in everyday code
  ```js
  [1, 2, 3, 4, 5].copyWithin(0, 3); // [4, 5, 3, 4, 5]
  ```

### Iterables — Objects usable with for...of

- Any object can be made iterable by adding a **`Symbol.iterator`** method that returns an **iterator** — an object with a `next()` method
- `for...of` calls `Symbol.iterator` automatically; you can also call it manually for fine-grained control
- The iterator protocol: `next()` must return `{ value: any, done: boolean }` — `done: true` signals the end
  ```js
  let range = {
    from: 1,
    to: 5,
    [Symbol.iterator]() {
      this.current = this.from;
      return this; // the object itself is the iterator
    },
    next() {
      if (this.current <= this.to) {
        return { done: false, value: this.current++ };
      } else {
        return { done: true };
      }
    }
  };

  for (let num of range) console.log(num); // 1, 2, 3, 4, 5
  ```

- **Calling the iterator manually** — useful when you need to pause/resume iteration
  ```js
  let iterator = 'Hello'[Symbol.iterator]();
  iterator.next(); // { value: 'H', done: false }
  iterator.next(); // { value: 'e', done: false }
  // ...
  ```

- **Strings are iterable** and their iterator correctly handles surrogate pairs (emoji, rare Unicode chars); `str[index]` does not
  ```js
  for (let char of '𝒳😂') console.log(char); // '𝒳', '😂' — 2 items, not 4 bytes
  ```

- **Iterables vs array-likes** — two separate concepts that often overlap but are not the same:
  - **Iterable** — has `Symbol.iterator`; works with `for...of` (e.g. strings, arrays, `range` above)
  - **Array-like** — has numeric indexes and a `length` property; does *not* automatically work with `for...of`
  ```js
  let arrayLike = { 0: 'Hello', 1: 'World', length: 2 };
  for (let item of arrayLike) {} // TypeError — no Symbol.iterator
  ```
  - Arrays and strings are **both** iterable and array-like; many other objects are one or the other

### Array.from — Convert iterables and array-likes to real arrays

- **`Array.from(obj)`** — creates a real array from any iterable or array-like; unlocks all array methods on objects that don't have them
  ```js
  let arrayLike = { 0: 'Hello', 1: 'World', length: 2 };
  let arr = Array.from(arrayLike);
  arr.pop(); // 'World' — now a real array
  ```

- **`Array.from(obj, mapFn)`** — optional second argument maps each element during conversion (like combining `Array.from` + `map` in one step)
  ```js
  Array.from(range, n => n * n); // [1, 4, 9, 16, 25]
  ```

- **Correct Unicode splitting** — `Array.from` uses the string iterator, so it handles surrogate pairs properly; `str.split('')` does not
  ```js
  Array.from('𝒳😂'); // ['𝒳', '😂'] — 2 elements
  '𝒳😂'.split('');   // ['', '', '', ''] — 4 broken bytes
  ```

### Map — Key-value collection with any key type (like Python dict, but keys can be anything)

- Like a plain object, but **any value can be a key** — including objects, functions, and `NaN`; keys are never converted to strings
- **`new Map()`** — creates an empty map; or pass an array of `[key, value]` pairs to initialize
  ```js
  let map = new Map([['one', 1], ['two', 2]]);
  ```

- **Core methods**:
  - **`map.set(key, value)`** — stores a value; returns the map itself, so calls can be chained
  - **`map.get(key)`** — returns the value, or `undefined` if the key doesn't exist
  - **`map.has(key)`** — returns `true` / `false`
  - **`map.delete(key)`** — removes the entry; returns `true` if the key existed
  - **`map.clear()`** — removes all entries
  - **`map.size`** — number of entries (a property, not a method)
  ```js
  let map = new Map();
  map.set('name', 'Alice').set(1, 'one').set(true, 'yes'); // chaining
  map.get('name'); // 'Alice'
  map.get(1);      // 'one'
  map.size;        // 3
  ```

- **Object keys** — this is the key advantage over plain objects
  ```js
  let user = { id: 1 };
  map.set(user, 'profile data');
  map.get(user); // 'profile data'
  ```

- **Iteration** — always in insertion order (same as Python dicts since 3.7)
  - **`map.keys()`** — iterable of keys
  - **`map.values()`** — iterable of values
  - **`map.entries()`** — iterable of `[key, value]` pairs; this is the default for `for...of`
  - **`map.forEach((value, key) => {})`** — note: value comes first (opposite of what you might expect)
  ```js
  for (let [key, value] of map) console.log(key, value);
  map.forEach((value, key) => console.log(key, value));
  ```

- **Converting between Object and Map**:
  ```js
  let obj = { a: 1, b: 2 };
  let map = new Map(Object.entries(obj));  // Object → Map
  let back = Object.fromEntries(map);      // Map → Object
  ```

### Set — Collection of unique values (like Python set)

- Stores values with **no duplicates**; adding the same value twice is silently ignored
- Iteration is in **insertion order** (unlike Python sets)
- Faster uniqueness checks than an array — use a Set instead of an array when you need to track membership

- **`new Set()`** — creates an empty set; or pass any iterable to initialize
  ```js
  let set = new Set([1, 2, 3, 2, 1]); // {1, 2, 3} — duplicates dropped
  ```

- **Core methods**:
  - **`set.add(value)`** — adds a value; returns the set itself (chainable); no-op if value already exists
  - **`set.delete(value)`** — removes a value; returns `true` if it existed
  - **`set.has(value)`** — returns `true` / `false`
  - **`set.clear()`** — removes all entries
  - **`set.size`** — number of entries
  ```js
  let set = new Set();
  set.add('a').add('b').add('a'); // {'a', 'b'} — second 'a' ignored
  set.has('b'); // true
  set.size;     // 2
  ```

- **Iteration** — `for...of` and `forEach` both work; `set.keys()`, `set.values()`, and `set.entries()` exist for Map compatibility (keys/values are the same thing in a Set)
  ```js
  for (let value of set) console.log(value);
  ```

- **Common pattern — deduplicate an array**:
  ```js
  let arr = [1, 2, 2, 3, 3, 3];
  let unique = Array.from(new Set(arr)); // [1, 2, 3]
  // or: [...new Set(arr)]
  ```

### Destructuring Assignment — Unpack arrays and objects into variables

- **Array destructuring** — match by position; works with any iterable (array, string, Set, Map)
  ```js
  let [firstName, surname] = 'John Smith'.split(' ');
  let [a, , c] = [1, 2, 3];      // skip with extra comma → c = 3
  [guest, admin] = [admin, guest]; // swap variables, no temp needed
  ```

- **Object destructuring** — match by property name (order doesn't matter)
  ```js
  let { title, width, height } = options;
  let { width: w, height: h } = options; // rename: "what : goes where"
  ```

- **Gotcha** — without `let`/`const`, wrap in parentheses or `{...}` is treated as a code block
  ```js
  ({ title, width } = { title: 'Menu', width: 200 });
  ```

- **Default values** — `=` kicks in when the value is `undefined`; works for both arrays and objects
  ```js
  let [name = 'Guest'] = [];           // name = 'Guest'
  let { width: w = 100 } = {};         // w = 100 (rename + default combined)
  ```

- **Rest pattern `...`** — gather remaining items/properties; must be last
  ```js
  let [first, ...rest] = [1, 2, 3, 4];        // rest = [2, 3, 4]
  let { title, ...rest } = options;           // rest = remaining properties object
  ```

- **Nested destructuring** — match the shape on the left; intermediate objects (like `size`, `items`) are not created as variables
  ```js
  let { size: { width }, items: [first] } = options;
  ```

- **Smart function parameters** — destructure in the signature; `= {}` prevents error on missing argument
  ```js
  function show({ title = 'Menu', width = 100 } = {}) {}
  show();           // uses all defaults
  show({ title: 'A' }); // named arguments, any order
  ```

### JSON — Serialize and deserialize data (language-independent format)

- **`JSON.stringify(value, replacer?, space?)`** — converts a JS value to a JSON string; double quotes only
- Supported types: objects, arrays, strings, numbers, booleans, `null`
- **Skipped silently**: functions, symbol keys/values, `undefined` properties
- **Circular references** throw `"Converting circular structure to JSON"`
- `new Date(...)` is invalid — use bare values only; no comments allowed in JSON
- Single quotes and unquoted property names are invalid in JSON (JSON5 relaxes this but is a separate library)

```js
JSON.stringify(1);              // "1"
JSON.stringify('test');         // ""test"" — string values get double-quoted
JSON.stringify([1, 2, 3]);      // "[1,2,3]"

let meetup = { title: "Conference", room: { number: 23 } };
JSON.stringify(meetup);
// {"title":"Conference","room":{"number":23}}
```

- **Replacer (2nd arg)**: an array of keys to include, or a function `(key, value)` returning the replacement (return `undefined` to skip); first call wraps whole object as `{ "": value }`
  ```js
  JSON.stringify(obj, ['title', 'name']);  // array — only those keys
  JSON.stringify(obj, (key, val) => key == 'occupiedBy' ? undefined : val); // function
  ```

- **Space (3rd arg)**: number (indent spaces) or string for pretty-printing
  ```js
  JSON.stringify(obj, null, 2); // 2-space indent
  ```

- **Custom `toJSON()`** — if an object has this method, `JSON.stringify` calls it; `Date` has a built-in `toJSON` that produces an ISO string (e.g. `"2017-01-01T00:00:00.000Z"`)
  ```js
  let room = { number: 23, toJSON() { return this.number; } };
  JSON.stringify(room); // "23"
  ```

- **`JSON.parse(str, reviver?)`** — parses a JSON string back to a JS value
  ```js
  let user = JSON.parse('{ "name": "John", "age": 35 }');
  user.age; // 35
  ```

- **Reviver (2nd arg)** — function `(key, value)` to transform values during parse; commonly used to revive dates (JSON strings don't auto-convert to `Date`)
  ```js
  let str = '{"date":"2017-11-30T12:00:00.000Z"}';
  let obj = JSON.parse(str, (key, value) => key == 'date' ? new Date(value) : value);
  obj.date.getDate(); // works — now a real Date
  ```

### Rest Parameters & Spread Syntax — `...` in function definitions vs calls

- **Rest parameters `...`** — in a function **definition**, gathers remaining arguments into a real array; must be **last**
  ```js
  function sumAll(...args) {       // args = [1, 2, 3]
    return args.reduce((s, n) => s + n, 0);
  }
  sumAll(1, 2, 3); // 6

  function show(first, last, ...titles) {} // first two named, rest in titles array
  ```

- **Spread syntax `...`** — in a function **call** or array/object literal, expands an iterable into individual elements (the inverse of rest)
  ```js
  Math.max(...[3, 5, 1]);          // same as Math.max(3, 5, 1) → 5
  Math.max(1, ...arr1, 2, ...arr2); // can mix spread with normal values
  ```

- **Merge / copy arrays and objects** — spread creates shallow copies, preferred over `Object.assign`
  ```js
  let merged = [0, ...arr1, 2, ...arr2];
  let arrCopy = [...arr];
  let objCopy = { ...obj };
  ```

- **String to characters** — spread uses the string iterator, so it handles Unicode correctly
  ```js
  [...'Hello']; // ['H', 'e', 'l', 'l', 'o']
  ```

- **Spread vs `Array.from`** — spread works only with iterables; `Array.from` works with both array-likes and iterables (more universal)

- **The `arguments` variable** (legacy) — array-like, iterable, not a real array; arrow functions don't have it; rest parameters are preferred

### Block Scope with `{}` — Braces as scope, not just syntax

- In JavaScript, `{}` creates a **block** — a unit of scope. This happens inside `if`, `for`, `while`, and so on, but you can also use `{}` **standalone** to create a new scope without any control-flow statement. Python has no equivalent: indentation defines blocks there, and there's no way to create a standalone scope just with braces.

- Unlike Python:
  - Python uses **indentation** to define blocks; JS uses **braces** `{}`
  - Python does not have standalone block scoping — variables defined inside `if`/`for`/`while` are still accessible outside
  - JS with `let`/`const` confines variables to the nearest enclosing block `{}`; Python variables leak out of `if`/`for` bodies

  ```js
  // Standalone block — creates a separate scope
  {
    let message = 'Hello';
    console.log(message); // 'Hello'
  }
  console.log(message); // ReferenceError — message is not defined

  // In Python, this equivalent would still have message visible outside.
  ```

- **`let` / `const` are block-scoped** — they only exist inside the `{}` where they're declared:
  ```js
  if (true) {
    let x = 10;
    const y = 20;
  }
  console.log(x); // ReferenceError
  ```

- **`var` ignores block scope** — `var` is function-scoped only, not block-scoped. This is a key reason to avoid it:
  ```js
  if (true) {
    var x = 10;
  }
  console.log(x); // 10 — var leaks out of the block
  ```

- **Blocks in loops** — each iteration of a `for` loop with `let` gets its own fresh binding (not true for `var`):
  ```js
  for (let i = 0; i < 3; i++) {
    setTimeout(() => console.log(i), 0); // 0, 1, 2 — each callback sees its own i
  }
  for (var i = 0; i < 3; i++) {
    setTimeout(() => console.log(i), 0); // 3, 3, 3 — all share the same i
  }
  ```

### Lexical Environment — The mechanism behind scope and hoisting

- A **Lexical Environment** is an internal object that JS creates whenever a block, function, or script runs. It has two parts:
  1. **Environment Record** — stores all local variables, function parameters, and `this` binding
  2. **Outer reference** — a pointer to the outer Lexical Environment (the environment enclosing this one)

- This is why function **declarations** are instantly available (hoisted) but function **expressions** are not:

- **When a script starts**, JS creates the global Lexical Environment. During this initial setup, it scans for all `function` **declarations** and immediately initializes them — they are fully created and callable before any code executes.

  ```js
  // This works — declaration was initialized during environment setup
  sayHi(); // 'Hi'
  function sayHi() { console.log('Hi'); }
  ```

- **Function expressions** are just variable assignments. The variable exists (or goes through TDZ for `let`/`const`), but the function value isn't assigned until the line runs:

  ```js
  greet(); // Error — greet is in TDZ (let) or undefined (var)
  let greet = function() { console.log('Hello'); }; // assignment happens here
  ```

- **Step by step** what happens:
  1. Script starts → global Lexical Environment created
  2. All function declarations are scanned and initialized immediately → `sayHi` is a function
  3. All `let`/`const` variables are registered but **uninitialized** (TDZ — Temporal Dead Zone) → `greet` exists but can't be accessed
  4. `var` variables are registered and initialized to `undefined` → accessible but worthless until assignment
  5. Code executes line by line → `greet` gets its function value only when the assignment line runs

- **When a function is called**, a new Lexical Environment is created for that call's local variables, with its outer reference pointing to the environment where the function was **created** (not called). This outer reference chain is what makes closures work.

### Closures — Functions that remember their outer variables

- A **closure** is a function that remembers and can access variables from its outer scope, even after that outer scope has finished executing.

- In JavaScript, **all functions are closures** — every function has a hidden `[[Environment]]` internal property that points to the Lexical Environment where the function was **created** (not where it's called). This is set once at creation time and never changes.

- **How it works**:
  1. When a function is **created**, it stores `[[Environment]]` = the current Lexical Environment
  2. When the function is **called**, a new Lexical Environment is created for that call
  3. That new environment's outer reference is set to the function's `[[Environment]]`
  4. Variable lookup: search current environment → outer reference → outer's outer → ... → global
  5. If a variable is not found anywhere, it's an error (strict mode) or creates a global (non-strict)

- **Classic example — counter factory**:
  ```js
  function makeCounter() {
    let count = 0;                    // local to makeCounter
    return function() {               // inner function created here
      return ++count;                 // accesses count from outer scope
    };
  }

  let counter = makeCounter();        // makeCounter() returns, but count lives on
  console.log(counter()); // 1        // inner function still has access via closure
  console.log(counter()); // 2
  console.log(counter()); // 3
  ```

- **Why `count` survives**: after `makeCounter()` returns, its execution context is gone, but the Lexical Environment is kept alive because the inner function's `[[Environment]]` still references it. The garbage collector can't reclaim it as long as the inner function is reachable.

- **Each closure gets its own environment** — calling the outer function again creates a **new** Lexical Environment, so closures are independent:
  ```js
  let c1 = makeCounter();
  let c2 = makeCounter();
  c1(); // 1
  c1(); // 2
  c2(); // 1 — separate count
  ```

- **Closures capture the variable itself, not a snapshot** — if the variable changes later, the closure sees the current value:
  ```js
  let name = 'Alice';
  function getName() { return name; }
  name = 'Bob';
  getName(); // 'Bob' — not 'Alice', because it accesses the live variable
  ```

- **Closures in loops — the `var` trap**:
  ```js
  for (var i = 0; i < 3; i++) {
    setTimeout(() => console.log(i), 0);
  }
  // Prints: 3, 3, 3 — all closures share the same i (var is function-scoped)
  ```
  Fix: use `let` (block-scoped, each iteration gets its own binding):
  ```js
  for (let i = 0; i < 3; i++) {
    setTimeout(() => console.log(i), 0);
  }
  // Prints: 0, 1, 2 — each closure sees its own i
  ```

- **Immediately-Invoked Function Expression (IIFE)** — an older pattern that uses closures to create private scope before `let`/`const` existed (now largely replaced by blocks with `let`):
  ```js
  (function() {
    let privateVar = 'hidden';
    // privateVar is only visible here
  })();
  ```

- **Closures are used everywhere** in JS: event handlers, callbacks, module patterns, `setTimeout`, promises, and any time a function references variables outside its own body.

### Scheduling: setTimeout & setInterval — Run code later / repeatedly

**`setTimeout(func, delay?, ...args)`** — runs `func` once after `delay` ms.

```js
let timerId = setTimeout(() => alert('Hello'), 1000);
setTimeout(sayHi, 1000, "Hello", "John"); // args passed to func
```

- **Common mistake**: `setTimeout(sayHi(), 1000)` — calls `sayHi` immediately, passes its return value (not the function). Pass the reference: `setTimeout(sayHi, 1000)`.
- **`clearTimeout(timerId)`** — cancels a pending timeout. The identifier doesn't become null after canceling.

**`setInterval(func, delay?, ...args)`** — runs `func` repeatedly every `delay` ms. Stopped with **`clearInterval(timerId)`**.

**`setTimeout(func, 0)`** — schedules `func` to run as soon as possible, but **after the current script finishes**:
```js
setTimeout(() => alert("World"), 0);
alert("Hello");
// Output: Hello → World
```

- Browser limitation: after 5 nested timers, the delay is forced to **≥ 4ms** (HTML spec). Node.js does not have this limit; it also offers `setImmediate`.

**Nested `setTimeout` vs `setInterval`**:
- `setInterval`: next call is queued every `delay` ms regardless of how long the function takes. If the function runs longer than the interval, calls stack up and fire with zero pause between them.
- Nested `setTimeout`: each call schedules the next only after completing, guaranteeing a pause **between** executions (not between starts). Use this when:
  - You need dynamic delays (e.g., exponential backoff)
  - The function is CPU-heavy and you need guaranteed spacing
  - You want precision between end of one call and start of next

```js
// Nested setTimeout pattern
let timerId = setTimeout(function tick() {
  // do work
  timerId = setTimeout(tick, 2000);
}, 2000);
```

**No exact timing guarantee** — delays can increase due to CPU load, background tabs, or battery-saving mode (up to 300–1000ms in some cases).

**Garbage collection** — `setTimeout`/`setInterval` hold an internal reference to the function, keeping it and its outer lexical environment alive. Always `clearTimeout`/`clearInterval` when done.

**alert() and timers** — `alert`/`confirm`/`prompt` are modal but the internal timer keeps ticking. If you dismiss an alert after several seconds, the next interval fires immediately.

### Function Binding: bind — Fix `this` and partially apply arguments

**`func.bind(context, ...args)`** — returns a new function with `this` permanently set to `context` and optional leading arguments pre-filled.

```js
let boundFunc = func.bind(context);
let bound = func.bind(context, arg1, arg2);  // partial application
```

**Primary use: fixing `this` for callbacks.** When a method is passed somewhere (e.g., `setTimeout`), it loses its object context:

```js
let user = {
  firstName: "John",
  sayHi() { console.log(`Hello, ${this.firstName}!`); }
};
setTimeout(user.sayHi, 1000);        // Hello, undefined! — this is lost
setTimeout(user.sayHi.bind(user), 1000); // Hello, John! — this is fixed
```

A wrapper (`() => user.sayHi()`) works too, but is vulnerable if `user` changes before the callback fires. `bind` captures the object at binding time, making it safer.

**Partial application** — fix leading arguments without touching `this`. Pass `null` as context when `this` isn't needed:

```js
function mul(a, b) { return a * b; }
let double = mul.bind(null, 2);
double(3); // 6
double(4); // 8
let triple = mul.bind(null, 3);
triple(3); // 9
```

Useful for creating specialized functions from generic ones (e.g., `sendTo(to, text)` from `send(from, to, text)`).

**Custom `partial` without context** — native `bind` forces you to provide a context. For partial-only binding that preserves `this` dynamically:

```js
function partial(func, ...argsBound) {
  return function(...args) {
    return func.call(this, ...argsBound, ...args);
  };
}
// this is passed through from the call site, argsBound are fixed
```

**Key gotchas**:
- **Context is immutable** — once bound, `this` can never be changed, not even by re-binding or calling as a method on another object
- **First bind wins** — `f.bind(a).bind(b)` still uses `a`; re-binding has no effect
- **Own properties are lost** — `bind` creates a new object; custom properties on the original function are not carried over
- In non-strict mode, `null` context becomes the global object (usually irrelevant for partials)

### Arrow Functions Revisited — No `this`, no `arguments`, no `new`

Beyond shorter syntax (covered earlier), arrow functions differ from regular functions in key ways:

**No own `this`** — arrow functions take `this` from the enclosing scope (lexical `this`). This is why they shine as callbacks inside methods:

```js
let group = {
  title: "Our Group",
  students: ["John", "Pete", "Alice"],
  showList() {
    // arrow: this = group (from showList)
    this.students.forEach(student => console.log(this.title + ': ' + student));
  }
};
```

A regular function inside `forEach` would have `this = undefined` (strict mode). Arrow functions avoid this entirely — they don't create a binding, they just look up `this` like any other variable.

Contrast with `.bind(this)`: bind creates a wrapper with fixed context; arrow functions simply don't *have* `this` — lookup follows normal lexical scoping.

**No `arguments` object** — useful in decorators that forward both `this` and arguments:

```js
function defer(f, ms) {
  return function() {
    setTimeout(() => f.apply(this, arguments), ms); // arrow takes arguments from defer's wrapper
  };
}
```

Without an arrow, you'd need `let ctx = this; let args = arguments;` before `setTimeout`.

**Cannot be called with `new`** — arrow functions have no `this`, so they can't be constructors. `new` throws `TypeError`.

**No `super`** — `super` lookup falls through to the enclosing scope (or fails).

**Summary of differences vs regular functions:**

| Feature | Arrow | Regular |
|---|---|---|
| `this` | Lexical (from enclosing scope) | Dynamic (call site) |
| `arguments` | Not available | Available |
| `new` | Throws TypeError | Allowed |
| `super` | Not available | Available |

**Gotchas**:
- **Don't use arrow functions as object methods** — `this` won't point to the object but to the outer scope
- **`.call()` / `.apply()` / `.bind()` can't change `this`** on arrows — arguments still pass through but `this` is ignored
- **DOM event listeners** — arrow handlers don't get `this = element`; use `event.currentTarget` instead

### Classes — Basic syntax

**A class is a kind of function.** `class User {...}` does two things: creates a function named `User` (the constructor) and stores methods on `User.prototype`.

```js
class User {
  constructor(name) { this.name = name; }    // called by new
  sayHi() { console.log(this.name); }         // method on User.prototype
  // note: no commas between methods
}

typeof User;          // 'function'
User === User.prototype.constructor; // true
User.prototype.sayHi; // the function code
```

**Key differences from pure functions** — classes are NOT just syntactic sugar:
- **Must call with `new`** — `User()` throws `TypeError` (internal flag `[[IsClassConstructor]]: true`)
- **Methods are non-enumerable** — won't appear in `for...in`
- **All code inside** is automatically strict mode (`"use strict"`)

**Class expressions** — classes can be defined inline, passed around, returned:

```js
let User = class MyClass {
  sayHi() { console.log(MyClass); } // MyClass visible only inside
};
new User().sayHi(); // works
console.log(MyClass); // ReferenceError — not visible outside
```

Dynamic creation:
```js
function makeClass(phrase) {
  return class { sayHi() { console.log(phrase); } };
}
```

**Getters / setters** — defined on the prototype, same syntax as object literals:

```js
class User {
  constructor(name) { this.name = name; } // invokes setter
  get name() { return this._name; }
  set name(value) {
    if (value.length < 4) { console.log("Too short."); return; }
    this._name = value;
  }
}
```

**Computed method names** — bracket notation works:

```js
class User { ['say' + 'Hi']() { console.log("Hello"); } }
```

**Class fields** — set on each *instance*, not the prototype:

```js
class User {
  name = "John";                          // per-instance property
  sayHi() { console.log(this.name); }
}
let u = new User();
u.name;                   // 'John'
User.prototype.name;      // undefined — fields are on instances
```

Values can come from expressions: `name = prompt("Name?", "John");`

**Bound methods via arrow fields** — solves the losing-`this` problem for callbacks:

```js
class Button {
  constructor(value) { this.value = value; }
  click = () => { console.log(this.value); }; // arrow field = per-instance, this bound
}
let button = new Button("hello");
setTimeout(button.click, 1000); // 'hello' — works, unlike prototype methods
```

Tradeoff: each instance gets its own copy → more memory, but `this` is always correct.

**Complete example — Clock:**

```js
class Clock {
  constructor({ template }) { this.template = template; }
  render() {
    let date = new Date();
    let [h, m, s] = [date.getHours(), date.getMinutes(), date.getSeconds()]
      .map(v => String(v).padStart(2, '0'));
    console.log(this.template.replace('h', h).replace('m', m).replace('s', s));
  }
  start() { this.render(); this.timer = setInterval(() => this.render(), 1000); }
  stop() { clearInterval(this.timer); }
}
```

> Note: `static`, `extends`/`super`, `#private` fields — covered in separate chapters.