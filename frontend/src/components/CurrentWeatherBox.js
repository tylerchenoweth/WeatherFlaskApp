// src/components/Header.js
import React from 'react';
import styles from './styles/CurrentWeatherBox.css';

const CurrentWeatherBox = ({geo, now}) => {
  return (
    <div className="currentWeatherMain">
      <h2>{geo.city}, {geo.state} {geo.country}A!, USA!</h2>
      <h3><b>Temperature: </b>{now.temp} <span>&#8457;</span></h3>
      <h3><b>Feels Like: </b>{now.feels_like} <span>&#8457;</span></h3>
    </div>
  );
};

export default CurrentWeatherBox;
