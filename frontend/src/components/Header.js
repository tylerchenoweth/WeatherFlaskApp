// src/components/Header.js
import React from 'react';
import './styles/Header.css'; // Import CSS file for styling (optional)




const CrystalBallSvg = () => {
  return (
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100" height="100">
  <g>
    <title>Layer 1</title>
    <ellipse strokeWidth="10" ry="137.5" rx="137.5" id="svg_1" cy="250" cx="250" stroke="#000" fill="none"/>
    <line stroke="#000" strokeWidth="10" strokeLinecap="undefined" strokeLinejoin="undefined" id="svg_9" y2="436" x2="90" y1="357" x1="162" fill="none"/>
    <line strokeWidth="10" strokeLinecap="undefined" strokeLinejoin="undefined" id="svg_10" y2="436" x2="410" y1="357" x1="338" stroke="#000" fill="none"/>
    <line strokeLinecap="undefined" strokeLinejoin="undefined" id="svg_11" y2="505" x2="458" y1="514" x1="106" stroke="#000" strokeWidth="10" fill="none"/>
    <line stroke="#000" strokeWidth="10" strokeLinecap="undefined" strokeLinejoin="undefined" id="svg_12" y2="436" x2="90" y1="357" x1="162" fill="none"/>
    <line stroke="#000" strokeWidth="10" strokeLinecap="undefined" strokeLinejoin="undefined" id="svg_13" y2="436" x2="90" y1="357" x1="162" fill="none"/>
    <line strokeLinecap="undefined" strokeLinejoin="undefined" id="svg_15" y2="436" x2="413" y1="436" x1="88" strokeWidth="10" stroke="#000" fill="none"/>
    <ellipse transform="rotate(-44.2589 184 179)" ry="22" rx="46" id="svg_16" cy="179" cx="184" strokeWidth="10" stroke="#000" fill="none"/>
    <line stroke="#000" id="svg_17" y2="9" x2="234" y1="91" x1="235" strokeWidth="10" fill="none"/>
    <line id="svg_18" y2="254" x2="497" y1="256" x1="403" strokeWidth="10" stroke="#000" fill="none"/>
    <line transform="rotate(7.44514 434.5 117.5)" id="svg_19" y2="68" x2="477" y1="167" x1="392" strokeWidth="10" stroke="#000" fill="none"/>
    <line transform="rotate(8.91493 337 62)" stroke="#000" id="svg_20" y2="18" x2="351" y1="106" x1="323" strokeWidth="10" fill="none"/>
    <line transform="rotate(9.48642 110 82.5)" id="svg_21" y2="50" x2="64" y1="115" x1="156" strokeWidth="10" stroke="#000" fill="none"/>
    <line id="svg_22" y2="255" x2="8" y1="257" x1="99" strokeWidth="10" stroke="#000" fill="none"/>
    <line id="svg_23" y2="354" x2="32" y1="318" x1="113" strokeWidth="10" stroke="#000" fill="none"/>
    <line id="svg_24" y2="141" x2="29" y1="185" x1="117" strokeWidth="10" stroke="#000" fill="none"/>
    <line id="svg_25" y2="381" x2="468" y1="332" x1="391" strokeWidth="10" stroke="#000" fill="none"/>
  </g>
</svg>


  )
}


const Header = () => {
  return (
    <header className="header">
      <h1>Sammy the Weather Swami</h1>


      <CrystalBallSvg />


    </header>
  );
};

export default Header;
