# ASYNCHRONOUS CODE

Since JavaScript is the language of the web, there are some functions that by necessity are going to take a decent amount of time to complete, such as fetching data from a server to display on your site.

For this reason, JavaScript includes support for asynchronous functions, or to put it another way, functions that can happen in the background while the rest of your code executes.

## CALLBACKS

these a functions that are passed into other functions.

they are passed as parameters.

## PROMISES

a promise is an object that might produce a value at some point in the future

## ASYNC/ AWAIT

### async

this lets the javascript engine know that you are executing /declaring an asynchronous function

When a function is declared with async, it automatically returns a promise

### await

await is pretty simple: it tells JavaScript to wait for an asynchronous action to finish before continuing the function. It’s like a ‘pause until done’ keyword. The await keyword is used to get a value from a function

### Error Handling

Handling errors in async functions is very easy. Promises have the .catch() method for handling rejected promises, and since async functions just return a promise, you can simply call the function, and append a .catch() method to the end.
