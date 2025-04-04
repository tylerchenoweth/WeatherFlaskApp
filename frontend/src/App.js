import React, { useEffect, useState } from 'react';
import axios from 'axios';

import Header from './components/Header';
import Footer from './components/Footer';
import CurrentWeatherBox from './components/CurrentWeatherBox';
import ForecastBox from './components/ForecastBox';

import './App.css';


function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    axios.get('http://127.0.0.1:5001') // Flask backend URL
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the data!', error);
      });
  }, []);

  
  // This needs to be here because if the elements get rendered before
  // the data is fetched you will just get a blank screen
  if (data === null) {
    console.log("Data is null. Loading...");
    return <div>Loading...</div>; // Render a loading state
  }

 

  // main return
  return (
    <div>
      <Header />
      <CurrentWeatherBox geo={data.geo} now={data.now}/>

      <div className="forecastBoxes">
        {Object.entries(data.forecast).map(([key, value]) => (
          <ForecastBox key={key} forecast={value} />
        ))}
      </div>

      <br></br><br></br><br></br><br></br><br></br>
      <Footer />
    </div>
  );

}


export default App;
