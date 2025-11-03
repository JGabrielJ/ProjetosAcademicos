let image = document.getElementById("image");
let userName = document.getElementById("userName");
let showhide = document.getElementById("showHide");
let profile = document.getElementById("profile");

let shown = false;
function showHide(username, ID) {
    if (!shown) {
        shown = true;
        showhide.src = "./images/hide.png";
        userName.value = `${username}@${ID}`;
    } else {
        shown = false;
        showhide.src = "./images/show.png";
        userName.value = username;
    }
};

profile.addEventListener("change", (e) => {
    let file = e.target.files[0];

    if (file) {
        let reader = new FileReader();

        reader.onload = (e) => {
            image.src = e.target.result;
        };

        reader.readAsDataURL(file);
    }
});
