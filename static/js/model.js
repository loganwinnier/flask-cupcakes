"use strict";

/** Cupcake:  a cupcake */
class Cupcake {

    constructor({ id, flavor, size, rating, image_url }) {
        this.id = id;
        this.flavor = flavor;
        this.size = size;
        this.rating = rating;
        this.image_url = image_url;
    }

    /** Create new DOM Li for cupcake. Append to Cupcake list */
    addToHtml() {
        let $cupcakeLi = $(
            `<li id='${this.id}'>
            <p><b>Flavor: ${this.flavor}</b></p>
            <p> Size: ${this.size} Rating: ${this.rating}</p>
            <img src=${this.image_url} height="200" width="200">
            <button id='delete-cupcake'>Delete</button>
            </li>`);
        $cupcakeList.append($cupcakeLi);
    }
}