// src/components/Header.js
import React from 'react';
import './styles/ForecastBox.css'; // Import CSS file for styling (optional)

const CurrentWeatherBox = ({forecast}) => {

  





  return (
    <div className="box">
      <h2>{forecast.day}</h2>
      <p><b>Temperature: </b>{forecast.temp} <span>&#8457;</span></p>
      <p><b>Feels Like: </b>{forecast.feels_like} <span>&#8457;</span></p>
      <p><b>Humidity: </b>{forecast.humidity}</p>
    </div>
  );
};

export default CurrentWeatherBox;
