# OBJECT

this is a collection of objects of related data and functionalities

in javascript, creating an object begins with defining and initializing a variable `const person = {}`

that is an empty object, to fill it with data:

```javascript
const Multiverse = {
    name: ['king', 'julien'],
    kingdom: 'Madagascar',
    age: 30,
    bio: function(){
        console.log(`king: ${this.name}`
    }
}
```

## Dot Notation

you can access the object properties and methods using dot notation.

`person.age, person.bio, person.kingdom`

## Bracket notation

you can also use bracket notation to access the object properties

`multiverse['name']`

## Nesting Objects inside Objects

an object can be nested inside another object

```javascript
const Multiverse = {
    miniverse: {
            kingdom: 'penguins',
            leader: 'skipper'
    }
}
```

to access this inner object: `Multiverse.miniverse.kingdom`

## updating Objects

you can use both dot notation and bracket notation to update the object properties

```javascript
person.age = 45;
person["name"]["last"] = "Cratchit";
```

you can also create new members of the object using this way

## constructors

when you call a constructor, it creates a new object, bind `this` to the new object, run the code in the constructor and return the new object

syntax:

```javascript
function Person(name) {
  this.name = name;
  this.introduceSelf = function () {
    console.log(`Hi! I'm ${this.name}.`);
  };
}

```

to call this constructor:

```javascript
const salva = new Person("Salva");
salva.name;
salva.introduceSelf();
// "Hi! I'm Salva."

const frankie = new Person("Frankie");
frankie.name;
frankie.introduceSelf();
// "Hi! I'm Frankie."

```
