document.getElementById('order-form').addEventListener('submit', async (e) => {
  e.preventDefault();

  const submitBtn = document.getElementById('submit-btn');
  const statusDiv = document.getElementById('status-message');

  submitBtn.disabled = true;
  submitBtn.innerText = 'Processing Order...';

  // Construct payload for single-piece direct home delivery
  const orderDetails = {
    item: {
      id: "VARIANT_12345",
      quantity: 1
    },
    shippingAddress: {
      name: document.getElementById('name').value,
      address1: document.getElementById('address').value,
      city: document.getElementById('city').value,
      zip: document.getElementById('zip').value,
      country: document.getElementById('country').value
    }
  };

  // Simulate API transmission to supplier endpoint
  setTimeout(() => {
    submitBtn.disabled = false;
    submitBtn.innerText = 'Place Single-Piece Order';
    
    statusDiv.className = 'success';
    statusDiv.style.display = 'block';
    statusDiv.innerHTML = `
      <strong>Order Submitted Successfully!</strong><br>
      Tracking ID: <code>TRK-${Math.floor(Math.random() * 899999 + 100000)}</code><br>
      Shipping 1 unit to: ${orderDetails.shippingAddress.address1}, ${orderDetails.shippingAddress.city}
    `;
    
    document.getElementById('order-form').reset();
  }, 1500);
});
