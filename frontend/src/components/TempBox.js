import React, {useState} from 'react';
import styles from './styles/TempBox.css';


const TempBox = ({forecast}) => {

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
        
        <p>{forecast.min_temp} <span>&#8457;</span> <span>&#126;</span> {forecast.max_temp} <span>&#8457;</span></p>
        
        <p><b>Humidity: </b>{forecast.humidity}%</p>

        

      </div>
    </div>


    {/* Below is the popup box */}
    {isOpen && (
      <div className="popup" onClick={() => setIsOpen(false)}>
         
        <div className="popup-content" onClick={(e) => e.stopPropagation()}>
            {/* <button className="close-btn" onClick="closePopup()">Close</button> */}

            {/* <div className="top-section">
                
                <div className="section center">
                    <div>
                        <div className="line">
                            <div className="title">Date: </div>
                            <div className="description">
                              {forecast.datetime.slice(8,11)}/
                              {forecast.datetime.slice(5,7)}/    
                              {forecast.datetime.slice(12,16)}
                            </div>
                        </div>
                        <div className="line">
                            <div className="title">Description: </div>
                            <div className="description">{forecast.weather.description}</div>
                        </div>
                        <div className="line">
                            <div className="title">Summary: </div>
                            <div className="description">{forecast.summary}</div>
                        </div>
                    </div>
                </div>
            </div> */}
            <h1>{forecast.day}</h1>
            <hr></hr>


            <div className='top-container'>
 

                
            <div className="top-section">
                        <div className="line">
                            <div className="title">Date: </div>
                            <div className="description">{forecast.datetime.slice(8,11)}/
                              {forecast.datetime.slice(5,7)}/    
                              {forecast.datetime.slice(12,16)}</div>
                        </div>
                        <div className="line">
                            <div className="title">Description: </div>
                            <div className="description">{forecast.weather.description} <span>&#8457;</span></div>
                        </div>
                        <div className="line">
                            <div className="title">Summary: </div>
                            <div className="description">{forecast.summary} </div>
                        </div>
                    </div>
                  </div>
                



            
            <hr></hr>
  






            <div className='container'>
 

                <div className="section-row">
                    <div className="section">
                        <div className="line">
                            <div className="title">Temperature: </div>
                            <div className="description">{forecast.temp} <span>&#8457;</span></div>
                        </div>
                        <div className="line">
                            <div className="title">Will Feel Like: </div>
                            <div className="description">{forecast.feels_like} <span>&#8457;</span></div>
                        </div>
                        <div className="line">
                            <div className="title">High: </div>
                            <div className="description">{forecast.max_temp} <span>&#8457;</span></div>
                        </div>
                        <div className="line">
                            <div className="title">Low: </div>
                            <div className="description">{forecast.min_temp} <span>&#8457;</span></div>
                        </div>
                    </div>

                    <div className="section">
                        <div className="line">
                            <div className="title">Wind Direction: </div>
                            <div className="description">{forecast.wind_direction} degrees</div>
                        </div>
                        <div className="line">
                            <div className="title">Wind Speed: </div>
                            <div className="description">{forecast.wind_speed} mph</div>
                        </div>
                        <div className="line">
                            <div className="title">Wind Gust: </div>
                            <div className="description">{forecast.wind_speed} mph</div>
                        </div>
                    </div>
                </div>

                <hr></hr>

                <div className="section-row">
                    <div className="section">
                        <div className="line">
                            <div className="title">Huidity: </div>
                            <div className="description">{forecast.humidity}</div>
                        </div>
                        <div className="line">
                            <div className="title">Dew Point: </div>
                            <div className="description">{forecast.dew_point}</div>
                        </div>
                    </div>

                    <div className="section">
                        <div className="line">
                            <div className="title">Sunrise: </div>
                            <div className="description">{forecast.sunrise}</div>
                        </div>
                        <div className="line">
                            <div className="title">Sunset: </div>
                            <div className="description">{forecast.sunset}</div>
                        </div>
                        <div className="line">
                            <div className="title">UVI Index: </div>
                            <div className="description">{forecast.uvi}</div>
                        </div>
                    </div>
                </div>
            </div>

        </div>
      </div>

    )}
  </>














  );
};

export default TempBox;
