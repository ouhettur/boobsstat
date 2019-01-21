function styleSwitcher() {
    $("body").toggleClass('light');
    $(".container > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(1n)").toggleClass('light');
}

function clickTimer() {
    styleSwitcher();
    if (localStorage.getItem('state') === "light") {
        localStorage.setItem("state", "dark")
    } else {
        localStorage.setItem("state", "light")
    }
}

function stateChanger(state) {
    if (state === null) {
        localStorage.setItem("state", "dark")
    } else if (state === "light") {
        localStorage.setItem("state", "light");
        styleSwitcher()
    }

}

$(document).ready(function () {
    $(".timer").click(function () {
        clickTimer()
    });
    let state = localStorage.getItem('state');
    stateChanger(state)

});
