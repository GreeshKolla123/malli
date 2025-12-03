import React from 'react';
import './Header.css';

function Header() {
  return (
    <div className="header">
      <h1>Malli</h1>
      <nav>
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="/cart">Cart</a></li>
          <li><a href="/orders">Orders</a></li>
        </ul>
      </nav>
    </div>
  );
}

export default Header;