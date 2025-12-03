import React from 'react';
import './Checkout.css';

function Checkout() {
  return (
    <div className="checkout">
      <h1>Checkout</h1>
      <form>
        <label>Payment Method:</label>
        <select>
          <option>Credit Card</option>
          <option>PayPal</option>
        </select>
        <button>Pay Now</button>
      </form>
    </div>
  );
}

export default Checkout;