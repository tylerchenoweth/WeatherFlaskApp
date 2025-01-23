// src/components/Header.js
import React from 'react';
import './styles/Header.css'; // Import CSS file for styling (optional)

const Header = () => {
  return (
    <header className="header">
      <h1>Sammy the Weather Swami</h1>
      <nav>
        <ul className="nav-links">
          <li><a href="/">Home</a></li>
          <li><a href="/about">About</a></li>
          <li><a href="/contact">Contact</a></li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
