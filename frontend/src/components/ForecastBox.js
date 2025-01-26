import React from 'react';
import styles from './styles/ForecastBox.css';

const ForecastBox = ({forecast}) => {

  const today = new Date();
  const savedDate = new Date(forecast.datetime)

  let isToday = false;

  if(savedDate.getDate() == today.getDate()) {
    if(savedDate.getMonth() == today.getMonth()) {
      if(savedDate.getYear() == today.getYear()) {
        isToday = true
      }
    }
  }

  return (
    <div className="box">

      {isToday ? <h2>Today</h2> : <h2>{forecast.day}</h2>}
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
