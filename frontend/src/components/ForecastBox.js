import React, {useState} from 'react';
import styles from './styles/ForecastBox.css';


const ForecastBox = ({forecast}) => {

  const today = new Date();
  const savedDate = new Date(forecast.datetime)
  const [isOpen, setIsOpen] = useState(false);

  let isToday = false;

  if(savedDate.getDate() == today.getDate()) {
    if(savedDate.getMonth() == today.getMonth()) {
      if(savedDate.getYear() == today.getYear()) {
        isToday = true
      }
    }
  }




  const [isVisible, setIsVisible] = useState(false);
  
    const togglePopup = () => {
      setIsVisible(!isVisible);
    };





  return (
    



  <>
    <div className="open-button" onClick={() => setIsOpen(true)}>
      {/* This is the forecast box */}
      <div className="box" >
        {isToday ? <h2>Today</h2> : <h2>{forecast.day}</h2>}
        <img src={forecast.weather.icon}></img>
        
        <p>{forecast.min_temp} <span>&#8457;</span> --- {forecast.max_temp} <span>&#8457;</span></p>
        
        <p><b>Humidity: </b>{forecast.humidity}%</p>

        

      </div>
    </div>


    {/* Below is the popup box */}
    {isOpen && (
      <div className="popup" onClick={() => setIsOpen(false)}>
          <div className="popup-content" onClick={(e) => e.stopPropagation()}>
              <h2>More details...</h2>
              <p><b>Description: </b>{forecast.datetime}</p>
              <p><b>Description: </b>{forecast.weather.description}</p>
              <p><b>Will Feel Like: </b>{forecast.feels_like} <span>&#8457;</span></p>
              <p><b>Temperature: </b>{forecast.temp} <span>&#8457;</span></p>
              <p><b>Wind Direction: </b>{forecast.wind_direction} mph</p>
              <p><b>Wind Speed: </b>{forecast.wind_speed} mph</p>
              <p><b>Wind Gust: </b>{forecast.wind_gust} mph</p>
              {/* <div className="close-button" onClick={() => setIsOpen(false)}>Close</div> */}
          </div>
      </div>
    )}
  </>














  );
};

export default ForecastBox;
