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