let menuOpen = false;  // This variable keeps track of whether the menu is open or closed

document.getElementById('menuButton').addEventListener('click', toggleMenu);

function loadView(viewName) {
    // Hide all sections first
    const sections = document.querySelectorAll('.content-section');
    sections.forEach(section => section.style.display = 'none');

    switch(viewName) {
        case 'home':
            document.getElementById('homeContent').style.display = 'block';
            break;
        case 'recipes':
            document.getElementById('recipesContent').style.display = 'block';
            // Optionally, you can call a function here to fetch and display recipes if they haven't been fetched yet.
            break;
        case 'pantry':
            document.getElementById('pantryContent').style.display = 'block';
            break;
    }
}


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

// ... existing JS ...
// ... existing JS ...

function fetchRecipeData() {
    return new Promise((resolve) => {
        // Simulating an async call with setTimeout.
        // Replace this with your actual fetch/axios call in the future.
        setTimeout(() => {
            resolve([
                {
                    name: "Spaghetti Carbonara",
                    description: "A classic Italian dish.",
                    ingredients: ["Spaghetti", "Eggs", "Pancetta", "Parmesan cheese"],
                    directions: ["Cook spaghetti.", "Mix eggs and cheese.", "Fry pancetta.", "Combine all ingredients."]
                },
                {
                    name: "Chicken Tikka Masala",
                    description: "A popular Indian dish.",
                    ingredients: ["Chicken", "Yogurt", "Tomatoes", "Spices"],
                    directions: ["Marinate chicken in yogurt and spices.", "Fry chicken.", "Make sauce with tomatoes.", "Combine chicken and sauce."]
                },
                {
                    name: "Caesar Salad",
                    description: "Healthy salad with romaine lettuce.",
                    ingredients: ["Romaine lettuce", "Croutons", "Parmesan cheese", "Caesar dressing"],
                    directions: ["Chop lettuce.", "Add croutons and cheese.", "Pour dressing."]
                },
                {
                    name: "Chocolate Cake",
                    description: "Decadent and moist chocolate dessert.",
                    ingredients: ["Flour", "Cocoa powder", "Eggs", "Sugar"],
                    directions: ["Mix dry ingredients.", "Add eggs.", "Bake in oven."]
                }
            ]);
        }, 1000); // 1 second delay to simulate server response time.
    });
}

function toggleRecipeDetails(clickedRecipeCard) {
    // First, close any recipe card that's already expanded
    const allRecipeCards = document.querySelectorAll('.recipe-card');
    allRecipeCards.forEach(card => {
        if (card !== clickedRecipeCard && card.classList.contains('expanded')) {
            card.classList.remove('expanded');
        }
    });

    // Now, toggle the expansion of the clicked recipe card
    clickedRecipeCard.classList.toggle('expanded');
}



function loadRecipePage() {
    const recipeContainer = document.getElementById('recipesContent');

    fetchRecipeData().then(recipes => {
        let recipeHtml = '';

        recipes.forEach(recipe => {
            recipeHtml += `
            <div class="recipe-card" onclick="toggleRecipeDetails(this)">
                <h3>${recipe.name}</h3>
                <p class="recipe-description">${recipe.description}</p>
                <div class="recipe-details">
                    <h4>Ingredients:</h4>
                    <ul class="recipe-ingredients">
                        ${recipe.ingredients.map(ing => `<li>${ing}</li>`).join('')}
                    </ul>
                    <h4>Directions:</h4>
                    <ul class="recipe-directions">
                        ${recipe.directions.map(dir => `<li>${dir}</li>`).join('')}
                    </ul>
                </div>
            </div>`;
        });

        recipeContainer.innerHTML = recipeHtml;
        loadView('recipes');
    });
}

// ... remaining JS ...

// ... remaining JS ...


function loadPantryPage() {
    // API call or DOM manipulation to load pantry page content
    // fetchPantryData();
}

// Example API call functions (to be fleshed out)
function fetchHomeData() {
    // API call to get home data
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



window.onload = function() {
    loadView('home');
}