import React, { useEffect, useState } from 'react';
import axios from 'axios';

import Header from './components/Header';
import Footer from './components/Footer';
import CurrentWeatherBox from './components/CurrentWeatherBox';
import ForecastBox from './components/ForecastBox';

import './App.css';



// This isnt used
// Im just keeping it here for future reference or just in case
function ColorFontCombinations() {
  const combinations = [
    { textColor: "#800000", backgroundColor: "#f5f5f5", font: "Arial" }, // Maroon on Light Gray
    { textColor: "#800000", backgroundColor: "#a9a9a9", font: "Times New Roman" }, // Maroon on Dark Gray
    { textColor: "#ff0000", backgroundColor: "#dcdcdc", font: "Helvetica" }, // Red on Light Gray
    { textColor: "#ff6600", backgroundColor: "#696969", font: "Georgia" }, // Orange on Dark Gray
    { textColor: "#800000", backgroundColor: "#dcdcdc", font: "Courier New" }, // Maroon on Light Gray
    { textColor: "#ff6600", backgroundColor: "#808080", font: "Tahoma" }, // Orange on Dark Gray
    { textColor: "#ff0000", backgroundColor: "#a9a9a9", font: "Verdana" }, // Red on Dark Gray
    { textColor: "#800000", backgroundColor: "#e8e8e8", font: "Lucida Console" }, // Maroon on Light Gray
    { textColor: "#ff6600", backgroundColor: "#b0b0b0", font: "Palatino Linotype" }, // Orange on Dark Gray
    { textColor: "#ff0000", backgroundColor: "#808080", font: "Trebuchet MS" }, // Red on Dark Gray
  ];

  // Repeat combinations to make up to 50 boxes
  while (combinations.length < 50) {
    combinations.push(...combinations.slice(0, 10));
  }
  combinations.length = 50; // Ensure it is exactly 50

  return (
    <div className="color-grid">
      {combinations.map((combo, index) => (
        <div
          key={index}
          className="color-box"
          style={{
            backgroundColor: combo.backgroundColor,
            color: combo.textColor,
            fontFamily: combo.font,
          }}
        >
          <p className="font-title">{combo.font}</p>
          <p className="color-code">Text: {combo.textColor}</p>
          <p className="color-code">Background: {combo.backgroundColor}</p>
        </div>
      ))}
    </div>
  );
}







function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000') // Flask backend URL
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
