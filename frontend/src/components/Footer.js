// src/components/Footer.js
import React from 'react';
import './styles/Footer.css'; // Import CSS file for styling (optional)

const Footer = () => {
  return (
    <footer className="footer">
      <p>&copy; {new Date().getFullYear()} CooperDuper. All rights reserved.</p>
    </footer>
  );
};

export default Footer;
