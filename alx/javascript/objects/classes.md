# CLASSES IN JAVASCRIPT

classes are templates for creating objects. They encapsulate data with code to work on that data.

to declare classes you use: `class`

```javascript
class Multiverse {
    name;

    constructor(name) {
        this.name = name
    }
}
```

to create  a new instance of Multiverse:

```javascript
julien = new Multiverse('julien');
```

## inheritance

we can inherit another class into our class

```javascript
class miniverse extends Multiverse {
    teaches;

    constructor(name, teaches) {
        super(name)
        this.teaches = teaches
    }
}
```

to create a new instance of miniverse:

```javascript
minijulien = new miniverse('minijulien', 'lemur kingdom')
```

## Encapsulation

Private data properties must be declared in the class declaration, and their names start with `#.`

### Private methods

You can have private methods as well as private data properties. Just like private data properties, their names start with `#`, and they can only be called by the object's own methods.

```javascript
class Example {
  somePublicMethod() {
    this.#somePrivateMethod();
  }

  #somePrivateMethod() {
    console.log("You called me?");
  }
}

const myExample = new Example();

myExample.somePublicMethod(); // 'You called me?'

myExample.#somePrivateMethod(); // SyntaxError

```

## CLASS ELEMENTS

they can be characterized by three aspects:

1. kind - Getter, Setter, method, field
2. location - static, instance
3. visibility - public, private
