console.log("JavaScript loaded!");
let menuOpen = false;  // This variable keeps track of whether the menu is open or closed

document.getElementById('menuButton').addEventListener('click', toggleMenu);

function toggleMenuIcon(element) {
    element.classList.toggle('close');
}


function toggleMenu() {
    console.log("Workin")
    let menu = document.getElementById('menu');
    let overlay = document.getElementById('overlay');
    if (!menu || !overlay) {
        console.error('Menu or overlay not found!');
        return;
    }
    if (!menuOpen) {
        // If the menu is currently closed, open it
        menu.style.left = '0';
        overlay.style.display = 'block';  // Show the overlay when menu is open
    } else {
        // If the menu is currently open, close it
        menu.style.left = '-80vw';
        overlay.style.display = 'none';   // Hide the overlay when menu is closed
    }

    menuOpen = !menuOpen;  // Toggle the state of menuOpen for the next time the function runs
}

function loadHomePage() {
    // API call or DOM manipulation to load home page content
    // fetchHomeData();
}

function loadRecipePage() {
    // API call or DOM manipulation to load recipe page content
    // fetchRecipeData();
}

function loadPantryPage() {
    // API call or DOM manipulation to load pantry page content
    // fetchPantryData();
}

// Example API call functions (to be fleshed out)
function fetchHomeData() {
    // API call to get home data
}

function fetchRecipeData() {
    // API call to get recipe data
}

function fetchPantryData() {
    // API call to get pantry data
}

function sendMessage() {
    const chatContainer = document.getElementById('chatContainer');
    const userMessageInput = document.getElementById('userMessage');

    // Display user's message
    const userMsgDiv = document.createElement('div');
    userMsgDiv.className = 'message user';
    userMsgDiv.textContent = userMessageInput.value;
    chatContainer.appendChild(userMsgDiv);

    // Simulating server's response after user's message
    setTimeout(() => {
        const serverMsgDiv = document.createElement('div');
        serverMsgDiv.className = 'message bot';
        serverMsgDiv.textContent = 'Message received';
        chatContainer.appendChild(serverMsgDiv);
    }, 1000);

    // Clear the input field
    userMessageInput.value = '';
}
