# INBUILT METHODS

## Reduce()

this is a higher order function which is used to reduce elements in an array into one  value

it takes two arguments: `array(callback, initialValue)`

the callback function is called for each element in the array.

this calback function takes four arguments:

1. accumulator - the additions we have been making/accumulating
2. current value - current element being processed
3. current index - current index of the element being processed
4. array - original array being processed

syntax:

```javascript
array = [1, 2, 3, 4, 5]
array.reduce((acc, current)=> acc + current,0)
```
