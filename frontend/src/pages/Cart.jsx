import React from 'react';
import './Cart.css';

function Cart() {
  return (
    <div className="cart">
      <h1>Cart</h1>
      <ul>
        <li>Product 1</li>
        <li>Product 2</li>
        <li>Product 3</li>
      </ul>
      <button>Checkout</button>
    </div>
  );
}

export default Cart;