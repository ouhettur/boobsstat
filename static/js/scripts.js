function change() {
    $("body").toggleClass('light');
    $(".container > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(1n)").toggleClass('light');
}

$(document).ready(function () {
    $(".timer").click(function () {
        change();
        if (localStorage.getItem('state') === "light") {
            localStorage.setItem("state", "dark")
        } else {
            localStorage.setItem("state", "light")
        }
    });
    let state = localStorage.getItem('state');
    if (state === null) {
        localStorage.setItem("state", "dark")
    } else if (state === "light") {
        localStorage.setItem("state", "light");
        change()
    }
});
