// src/components/Header.js
import React from 'react';
import './styles/Header.css'; // Import CSS file for styling (optional)

const CurrentWeatherBox = ({geo, now}) => {
  return (
    <div>
      <h2>{geo.city}, {geo.state}</h2>
      <h2>{geo.country}</h2>
      <h2><b>Temperature: </b>{now.temp} <span>&#8457;</span></h2>
      <h2><b>Feels Like: </b>{now.feels_like} <span>&#8457;</span></h2>
    </div>
  );
};

export default CurrentWeatherBox;
