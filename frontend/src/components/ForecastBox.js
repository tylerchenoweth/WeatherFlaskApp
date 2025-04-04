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
    {/* TODAY INFO */}
    <div className="open-button" onClick={() => setIsOpen(true)}>
      {/* This is the forecast box */}
      <div className="box" >
        {isToday ? <h2>Today</h2> : <h2>{forecast.day}</h2>}
        <img src={forecast.weather.icon}></img>
        
        <p>{forecast.min_temp} <span>&#8457;</span> <span>&#126;</span> {forecast.max_temp} <span>&#8457;</span></p>
        
        <p><b>Humidity: </b>{forecast.humidity}%</p>

      </div>
    </div>


    {/* POPUP BOX */}
    {isOpen && (
      <div className="popup" onClick={() => setIsOpen(false)}>
          <div className="popup-content" onClick={(e) => e.stopPropagation()}>
            <h1>{forecast.day}</h1>
            <hr></hr>

            <table>
              <tbody>
                <tr>
                  <td><b>Date: </b></td>
                  <td>
                    {forecast.datetime.slice(8,11)}/
                    {forecast.datetime.slice(5,7)}/    
                    {forecast.datetime.slice(12,16)}
                  </td>
                </tr>
                <tr className="divider">
                  <td><b>Description: </b></td>
                  <td>{forecast.weather.description}</td>
                </tr>
                <tr>
                  <td><b>Summary: </b></td>
                  <td>{forecast.summary}</td>
                </tr>

                <tr>
                  <td><hr></hr></td>
                  <td><hr></hr></td>
                  <td><hr></hr></td>
                  <td><hr></hr></td>
                </tr>
                

                <tr>
                  <td><b>Will Feel Like: </b></td>
                  <td>{forecast.feels_like} <span>&#8457;</span></td>
                  <td><b>Wind Direction: </b></td>
                  <td>{forecast.wind_direction} degrees</td>
                </tr>
                <tr>
                  <td><b>Temperature: </b></td>
                  <td>{forecast.temp} <span>&#8457;</span></td>
                  <td><b>Wind Speed: </b></td>
                  <td>{forecast.wind_speed} mph</td>
                </tr>
                <tr>
                  <td><b>High: </b></td>
                  <td>{forecast.max_temp} <span>&#8457;</span></td>
                  <td><b>Wind Gust: </b></td>
                  <td>{forecast.wind_gust} mph</td>
                </tr>
                <tr>
                  <td><b>Low: </b></td>
                  <td>{forecast.min_temp} <span>&#8457;</span></td>
                </tr>
                
                <tr>
                  <td><hr></hr></td>
                  <td><hr></hr></td>
                  <td><hr></hr></td>
                  <td><hr></hr></td>
                </tr>
                
                <tr>
                  <td><b>Humidity: </b></td>
                  <td>{forecast.humidity}%</td>
                  <td><b>Sunrise: </b></td>
                  <td>{forecast.sunrise}</td>
                </tr>
                <tr>
                  <td><b>Dew Point: </b></td>
                  <td>{forecast.dew_point}%</td>
                  <td><b>Sunset: </b></td>
                  <td>{forecast.sunset}</td>
                </tr>
                <tr>
                  <td></td><td></td>
                  <td><b>UVI Index: </b></td>
                  <td>{forecast.uvi}</td>
                </tr>

                {/* <tr>
                  <td><hr></hr></td>
                  <td><hr></hr></td>
                  <td><hr></hr></td>
                  <td><hr></hr></td>
                </tr> */}
                {/* <tr>
                  <td><b>Sunrise: </b></td>
                  <td>{forecast.sunrise}</td>
                </tr>
                <tr>
                  <td><b>Sunset: </b></td>
                  <td>{forecast.sunset}</td>
                </tr>
                <tr>
                  <td><b>UVI Index: </b></td>
                  <td>{forecast.uvi}</td>
                </tr> */}
                {/* <tr>
                  <td><b>Wind Direction: </b></td>
                  <td>{forecast.wind_direction} mph</td>
                </tr>
                <tr>
                  <td><b>Wind Speed: </b></td>
                  <td>{forecast.wind_speed} mph</td>
                </tr>
                <tr>
                  <td><b>Wind Gust: </b></td>
                  <td>{forecast.wind_gust} mph</td>
                </tr> */}
              </tbody>
            </table>
              
          </div>
      </div>
    )}
  </>
  );
};

export default ForecastBox;
