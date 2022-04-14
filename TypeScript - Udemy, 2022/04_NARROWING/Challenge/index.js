"use strict";
const review = (stars) => {
    if (stars) {
        switch (stars) {
            case 1:
                console.log("1 Star: Terrible!");
                break;
            case 2:
                console.log("2 Stars: Bad.");
                break;
            case 3:
                console.log("3 Stars: Regular.");
                break;
            case 4:
                console.log("4 Stars: Good.");
                break;
            case 5:
                console.log("5 Stars: Great!");
                break;
            default:
                console.log("Please choose an option between 1 and 5.");
                break;
        }
    }
    else {
        console.log("Review not provided.");
    }
};
review(5);
review();
review(7);
function showUserReview(review) {
    if (!review) {
        console.log("Você não avaliou o produto!");
        return;
    }
    console.log(`A nota que você deu foi ${review}, obrigado!`);
}
showUserReview(false); //Estranho pois se colocar true ele retorna "Você deu a nota true!"
showUserReview(3);
showUserReview(4);
