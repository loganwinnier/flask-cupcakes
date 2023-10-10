"use strict";

const BASE_CUPCAKE_URL = "/api/cupcakes";

let cupcakes;
const $cupcakeList = $('#cupcake-list');
const $cupcakeForm = $("#cupcake-form");

//TODO: put data in class and Ui into this file
/** Make fetch request to BASE_CUPCAKE_URL and  display cupcakes in DOM */
async function getAndShowCupcakes() {
    const response = await fetch(BASE_CUPCAKE_URL);
    const data = await response.json();
    cupcakes = data.cupcakes.map(cupcake => new Cupcake(cupcake));

    for (const cupcake of cupcakes) {
        cupcake.addToHtml();
    }
}

/** handleAddCupcakeForm: Handles submit of cupcake form. Adds new cupcake to database and local storage. Appends to DOM  */
async function handleAddCupcakeForm(evt) {
    evt.preventDefault();
    const flavor = $("#flavor").val();
    const size = $("#size").val();
    const rating = $("#rating").val();
    const image_url = $("#image-url").val();

    const response = await fetch(BASE_CUPCAKE_URL, {
        method: "POST",
        body: JSON.stringify(
            {
                "flavor": flavor, //Object Shorthand
                "size": size,
                "rating": rating,
                "image_url": image_url
            }),
        headers: { "content-type": "application/json" }
    });

    const data = await response.json();
    const cupcake = new Cupcake(data.cupcake);
    cupcakes.push(cupcake);

    cupcake.addToHtml();
    $cupcakeForm[0].reset();
}
$cupcakeForm.on("submit", handleAddCupcakeForm);

getAndShowCupcakes();