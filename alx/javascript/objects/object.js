// empty object
const multiverse = {};
console.log(multiverse);

// fill the empty object with data

const multiverseKing = {
  name: "king Julien",
  age: 30,
  kingdom: "madagascar",
  bio: function () {
    console.log(`${this.name} age: ${this.age} kingdom: ${this.kingdom} `);
  },
  giveName() {
    console.log(`${this.name}`);
  },
};

console.log(multiverseKing);
multiverseKing.bio();
multiverseKing.giveName();
multiverse.age = 30;
console.log(multiverse);
multiverse.kingdom = function () {
    multiverse.name = 'king Julien'
    console.log(`${this.name}`)
}

console.log(multiverse)
console.log(multiverse.kingdom());
