import React, { useState } from "react";
import "./styles/Popup.css";

const Popup = () => {
  const [isVisible, setIsVisible] = useState(false);

  const togglePopup = () => {
    setIsVisible(!isVisible);
  };

  return (
    <div className="popup" onClick={togglePopup}>
      Click me to toggle the popup!
      <span className={`popuptext ${isVisible ? "show" : ""}`}>
        A Simple Popup!
      </span>
    </div>
  );
};

export default Popup;
