let getAllDrinks = async() => {
     // requête http GET vers mon api de lecture de boissons
    let data = await fetch('http://127.0.0.1:5000/getAllDrinks');
    // transformation de la réponse en json
    let count = await data.json();
    // pour chaque élément, récupération de tous les paramètres transmis
    await count.forEach( element => {
      let title = element.title;
      let price = (element.price/100);
      let description = element.description;
      let imageUrl = element.imageUrl;
      let idTitle = title.replace(/ /g, "_");

      //récupération dans la liste de div vide de la div qui contiendra la boisson
      let newDiv = document.querySelector(" body div");
      // création des id et attribute de cette div
      newDiv.className = "drink";
      newDiv.id = idTitle;
      // création de la div img
      let image = document.createElement("img");
      image.className = idTitle;
      //récupération de l'url de l'image dans l'attribut src de img
      image.setAttribute("src", imageUrl);
      newDiv.appendChild(image);
      otherDiv = document.createElement("div");
      otherDiv.className = 'Content';
      newDiv.appendChild(otherDiv);
      let firstp = document.createElement("p");
      firstp.innerText = title;
      otherDiv.appendChild(firstp);
      let secondp = document.createElement("p");
      secondp.innerText = price;
      otherDiv.appendChild(secondp);
      let thirstp = document.createElement("p");
      thirstp.innerText = description;
      otherDiv.appendChild(thirstp);
    
      document.body.appendChild(newDiv);

    });
}
getAllDrinks();



document.querySelectorAll(" body > div").forEach(item => {
  item.addEventListener('click', event => {
    let attribute = item.getAttribute("id");
    console.log(attribute);

    document.querySelectorAll(" body > div").forEach(item => {
      item.remove(" body > div > img");
      item.remove(" body > div > div ");
      
    });
    let getOneDrink = async() => {
      let env = String('http://127.0.0.1:5000/getOneDrink/'+attribute)
      let data = await fetch(env);
      let element = await data.json();
      console.log(element);
      let title = element[0].title;
      let price = (element[0].price/100);
      let description = element[0].description;
      let imageUrl = element[0].imageUrl;
      let idTitle = title.replace(/ /g, "_");

      let newDiv = document.createElement("div");
      newDiv.className = "onedrink";
      newDiv.id = idTitle;
      let image = document.createElement("img");
      image.className = idTitle;
      image.className = "oneimg";
      image.setAttribute("src", imageUrl);
      newDiv.appendChild(image);
      otherDiv = document.createElement("div");
      otherDiv.className = 'Content';
      newDiv.appendChild(otherDiv);
      let firstp = document.createElement("p");
      firstp.innerText = title;
      otherDiv.appendChild(firstp);
      let secondp = document.createElement("p");
      secondp.innerText = price;
      otherDiv.appendChild(secondp);
      let thirstp = document.createElement("p");
      thirstp.innerText = description;
      otherDiv.appendChild(thirstp);
      document.body.appendChild(newDiv);

    }
    getOneDrink();
    
  })
})
