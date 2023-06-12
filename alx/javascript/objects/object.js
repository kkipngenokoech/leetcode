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
};

console.log(multiverseKing);
multiverseKing.bio();
