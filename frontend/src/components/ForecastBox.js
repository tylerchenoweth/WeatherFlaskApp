import React from 'react';
import styles from './styles/ForecastBox.css';

const ForecastBox = ({forecast}) => {

  return (
    <div className="box">
      <h2>{forecast.day}</h2>
      <img src={forecast.weather.icon}></img>
      {/* <p><b>Temperature: </b>{forecast.temp} <span>&#8457;</span></p> */}
      <p>{forecast.min_temp} <span>&#8457;</span> --- {forecast.max_temp} <span>&#8457;</span></p>
      {/* <p><b>Feels Like: </b>{forecast.feels_like} <span>&#8457;</span></p> */}
      <p><b>Humidity: </b>{forecast.humidity}%</p>
      
      {/* <p>{forecast.weather.description}</p> */}
    </div>
  );
};

export default ForecastBox;
