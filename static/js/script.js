/* Example JavaScript for the cycling e-commerce shop */
// Function to highlight the search input on focus
const searchInput = document.querySelector('#query');
searchInput.addEventListener('focus', function() {
  this.style.borderColor = '#337ab7';
});

// Function to remove highlight from search input on blur
searchInput.addEventListener('blur', function() {
  this.style.borderColor = '';
});

// Function to display a confirmation message when adding a product to the cart
const addToCartBtns = document.querySelectorAll('.add-to-cart-btn');
addToCartBtns.forEach(btn => {
  btn.addEventListener('click', function() {
    const productName = this.dataset.productName;
    const confirmMsg = `Added ${productName} to your cart.`;
    alert(confirmMsg);
  });
});



