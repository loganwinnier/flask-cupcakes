"use strict";

const BASE_CUPCAKE_URL = "http://127.0.0.1:5001//api/cupcakes";
let cupcakes;


const $cupcakeList = $('#cupcake-list');
const $cupcakeForm = $("#cupcake-form");

async function getAndShowCupcakes() {
    const response = await fetch(BASE_CUPCAKE_URL);
    const data = await response.json();
    cupcakes = data.cupcakes.map(cupcake => new Cupcake(cupcake));

    for (const cupcake of cupcakes) {
        console.log(cupcake);
        let $cupcakeLi = $(
            `<li id='${cupcake.id}'>
            <p><b>Flavor: ${cupcake.flavor}</b></p>
            <p> Size: ${cupcake.size} Rating: ${cupcake.rating}</p>
            <img src=${cupcake.image_url} height="200" width="200">
            </li>`);
        $cupcakeList.append($cupcakeLi);
    }

}

async function addCupcake(evt) {
    evt.preventDefault();
    const flavor = $("#flavor").val();
    const size = $("#size").val();
    const rating = $("#rating").val();
    const image_url = $("#image-url").val();

    const response = await fetch(BASE_CUPCAKE_URL, {
        method: "POST",
        body: JSON.stringify(
            {"cupcake":
            {
                "flavor": flavor,
                "size": size,
                "rating": rating,
                "image_url": image_url
            }
        }),
        headers: { "content-type": "application/json" }
    });
    const data = await response.json();

    //const cupcake = new Cupcake(data.cupcake);

    await getAndShowCupcakes();
}

$cupcakeForm.on("submit", addCupcake);



getAndShowCupcakes();