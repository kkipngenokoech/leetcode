async function populate() {
  const requestUrl =
    "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json";
  const request = new Request(requestUrl);
  const response = await fetch(request);
  return JSON.parse(response);
}

function getTodoList() {
  console.log("--------------------------------");
  //   console.log(populate());
  console.log("--------------------------------");
  console.log(JSON.parse(fetch("https://jsonplaceholder.typicode.com/todos")));
}
getTodoList();
