"use strict"

const BASE_CUPCAKE_URL = "http://127.0.0.1:5000//api/cupcakes";
let cupcakes;


const $cupcakeList = $('#cupcake-list')

async function getAndShowCupcakes() {
    const response = await fetch(BASE_CUPCAKE_URL);
    const data = await response.json();
    cupcakes = data.cupcakes.map(cupcake => new Cupcake(cupcake));

    for (const cupcake of cupcakes) {
        console.log(cupcake)
        let $cupcakeLi = $(`<li id='${cupcake.id}'>${cupcake.flavor}</li>`);
        $cupcakeList.append($cupcakeLi);
    }

}

getAndShowCupcakes()