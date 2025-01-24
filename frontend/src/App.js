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
    axios.get('http://127.0.0.1:5000') // Flask backend URL
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the data!', error);
      });
  }, []);

  
  // This needs to be here because if the elements get rendered before
  // the data is fetched youll just get a blank screen
  if (data === null) {
    console.log("Data is null. Loading...");
    return <div>Loading...</div>; // Render a loading state
  }

  
  //   const fonts = [
  //     { name: "Arial", style: "Arial, sans-serif" },
  //     { name: "Helvetica", style: "Helvetica, sans-serif" },
  //     { name: "Times New Roman", style: "'Times New Roman', serif" },
  //     { name: "Georgia", style: "Georgia, serif" },
  //     { name: "Courier New", style: "'Courier New', monospace" },
  //     { name: "Verdana", style: "Verdana, sans-serif" },
  //     { name: "Trebuchet MS", style: "'Trebuchet MS', sans-serif" },
  //     { name: "Garamond", style: "Garamond, serif" },
  //     { name: "Palatino Linotype", style: "'Palatino Linotype', 'Book Antiqua', Palatino, serif" },
  //     { name: "Lucida Console", style: "'Lucida Console', Monaco, monospace" },
  //     { name: "Tahoma", style: "Tahoma, sans-serif" },
  //     { name: "Impact", style: "Impact, sans-serif" },
  //     { name: "Segoe UI", style: "'Segoe UI', Tahoma, Geneva, sans-serif" },
  //     { name: "Roboto", style: "'Roboto', sans-serif" },
  //     { name: "Open Sans", style: "'Open Sans', sans-serif" },
  //     { name: "Lato", style: "'Lato', sans-serif" },
  //     { name: "Oswald", style: "'Oswald', sans-serif" },
  //     { name: "Montserrat", style: "'Montserrat', sans-serif" },
  //     { name: "PT Serif", style: "'PT Serif', serif" },
  //     { name: "Merriweather", style: "'Merriweather', serif" },
  //   ];








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
      
      {/* {fonts.map((font, index) => (
        <h2 key={index} style={{ fontFamily: font.style }}>
          {index + 1}. {font.name}
        </h2>
      ))} */}

      <br></br><br></br><br></br><br></br><br></br>
      <Footer />
    </div>
  );






  // const styles = [
  //   // Inspired by #800000, #CCCCCC, and Georgia
  //   { background: "#CCCCCC", color: "#800000", fontFamily: "Georgia, serif", name: "Georgia" },
  //   { background: "#B3B3B3", color: "#730000", fontFamily: "Garamond, serif", name: "Garamond" },
  //   { background: "#E0E0E0", color: "#990000", fontFamily: "'Palatino Linotype', serif", name: "Palatino Linotype" },
  //   { background: "#D6D6D6", color: "#7D0000", fontFamily: "'Times New Roman', serif", name: "Times New Roman" },
  //   { background: "#C2C2C2", color: "#880000", fontFamily: "'PT Serif', serif", name: "PT Serif" },
  //   { background: "#D9D9D9", color: "#760000", fontFamily: "Arial, sans-serif", name: "Arial" },
  //   { background: "#E6E6E6", color: "#8B0000", fontFamily: "Verdana, sans-serif", name: "Verdana" },
  //   { background: "#BFBFBF", color: "#740000", fontFamily: "Helvetica, sans-serif", name: "Helvetica" },
  //   { background: "#D0D0D0", color: "#7F0000", fontFamily: "'Open Sans', sans-serif", name: "Open Sans" },
  //   { background: "#C9C9C9", color: "#860000", fontFamily: "'Montserrat', sans-serif", name: "Montserrat" },

  //   // Additional variations
  //   { background: "#DCDCDC", color: "#850000", fontFamily: "'Lora', serif", name: "Lora" },
  //   { background: "#E3E3E3", color: "#890000", fontFamily: "'Merriweather', serif", name: "Merriweather" },
  //   { background: "#CBCBCB", color: "#7A0000", fontFamily: "'Roboto Slab', serif", name: "Roboto Slab" },
  //   { background: "#B8B8B8", color: "#820000", fontFamily: "'Playfair Display', serif", name: "Playfair Display" },
  //   { background: "#C4C4C4", color: "#780000", fontFamily: "'Noto Serif', serif", name: "Noto Serif" },
  //   { background: "#C7C7C7", color: "#8D0000", fontFamily: "'Libre Baskerville', serif", name: "Libre Baskerville" },
  //   { background: "#CFCFCF", color: "#8A0000", fontFamily: "'Crimson Text', serif", name: "Crimson Text" },
  //   { background: "#CECECE", color: "#830000", fontFamily: "'Raleway', sans-serif", name: "Raleway" },
  //   { background: "#C5C5C5", color: "#8C0000", fontFamily: "'Bitter', serif", name: "Bitter" },
  //   { background: "#D4D4D4", color: "#790000", fontFamily: "'Zilla Slab', serif", name: "Zilla Slab" },
  // ];

  // return (
  //   <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: "20px", padding: "20px" }}>
  //     {styles.map((style, index) => (
  //       <div
  //         key={index}
  //         style={{
  //           backgroundColor: style.background,
  //           fontFamily: style.fontFamily,
  //           color: style.color,
  //           padding: "20px",
  //           borderRadius: "8px",
  //           textAlign: "center",
  //           boxShadow: "0 2px 4px rgba(0, 0, 0, 0.1)",
  //         }}
  //       >
  //         <p style={{ margin: 0 }}>{style.name}</p>
  //         <p style={{ fontSize: "14px", marginTop: "8px" }}>Text: {style.color}</p>
  //         <p style={{ fontSize: "14px" }}>Background: {style.background}</p>
  //       </div>
  //     ))}
  //   </div>
  // );








  // const styles = [
  //   { background: "#F2F2F2", fontFamily: "Arial, sans-serif", name: "Arial" },
  //   { background: "#E6E6E6", fontFamily: "Helvetica, sans-serif", name: "Helvetica" },
  //   { background: "#D9D9D9", fontFamily: "'Times New Roman', serif", name: "Times New Roman" },
  //   { background: "#CCCCCC", fontFamily: "Georgia, serif", name: "Georgia" },
  //   { background: "#B3B3B3", fontFamily: "'Courier New', monospace", name: "Courier New" },
  //   { background: "#A6A6A6", fontFamily: "Verdana, sans-serif", name: "Verdana" },
  //   { background: "#999999", fontFamily: "'Trebuchet MS', sans-serif", name: "Trebuchet MS" },
  //   { background: "#8C8C8C", fontFamily: "Garamond, serif", name: "Garamond" },
  //   { background: "#808080", fontFamily: "'Palatino Linotype', serif", name: "Palatino Linotype" },
  //   { background: "#737373", fontFamily: "'Lucida Console', monospace", name: "Lucida Console" },
  //   { background: "#666666", fontFamily: "Tahoma, sans-serif", name: "Tahoma" },
  //   { background: "#595959", fontFamily: "Impact, sans-serif", name: "Impact" },
  //   { background: "#4D4D4D", fontFamily: "'Segoe UI', sans-serif", name: "Segoe UI" },
  //   { background: "#404040", fontFamily: "'Roboto', sans-serif", name: "Roboto" },
  //   { background: "#333333", fontFamily: "'Open Sans', sans-serif", name: "Open Sans" },
  //   { background: "#262626", fontFamily: "'Lato', sans-serif", name: "Lato" },
  //   { background: "#1A1A1A", fontFamily: "'Oswald', sans-serif", name: "Oswald" },
  //   { background: "#0D0D0D", fontFamily: "'Montserrat', sans-serif", name: "Montserrat" },
  //   { background: "#E0E0E0", fontFamily: "'PT Serif', serif", name: "PT Serif" },
  //   { background: "#F5F5F5", fontFamily: "'Merriweather', serif", name: "Merriweather" },
  // ];

  // return (
  //   <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: "20px", padding: "20px" }}>
  //     {styles.map((style, index) => (
  //       <div
  //         key={index}
  //         style={{
  //           backgroundColor: style.background,
  //           fontFamily: style.fontFamily,
  //           color: "#800000",
  //           padding: "20px",
  //           borderRadius: "8px",
  //           textAlign: "center",
  //           boxShadow: "0 2px 4px rgba(0, 0, 0, 0.1)",
  //         }}
  //       >
  //         <p style={{ margin: 0 }}>{style.name}</p>
  //         <p style={{ fontSize: "14px", marginTop: "8px" }}>Background: {style.background}</p>
  //       </div>
  //     ))}
  //   </div>
  // );













  // const styles = [
  //   // First set (original light gray backgrounds and darker maroon text)
  //   { background: "#F2F2F2", fontFamily: "Arial, sans-serif", name: "Arial", color: "#800000" },
  //   { background: "#E6E6E6", fontFamily: "Helvetica, sans-serif", name: "Helvetica", color: "#800000" },
  //   { background: "#D9D9D9", fontFamily: "'Times New Roman', serif", name: "Times New Roman", color: "#800000" },
  //   { background: "#CCCCCC", fontFamily: "Georgia, serif", name: "Georgia", color: "#800000" },
  //   { background: "#B3B3B3", fontFamily: "'Courier New', monospace", name: "Courier New", color: "#800000" },
  //   { background: "#A6A6A6", fontFamily: "Verdana, sans-serif", name: "Verdana", color: "#800000" },
  //   { background: "#999999", fontFamily: "'Trebuchet MS', sans-serif", name: "Trebuchet MS", color: "#800000" },
  //   { background: "#8C8C8C", fontFamily: "Garamond, serif", name: "Garamond", color: "#800000" },
  //   { background: "#808080", fontFamily: "'Palatino Linotype', serif", name: "Palatino Linotype", color: "#800000" },
  //   { background: "#737373", fontFamily: "'Lucida Console', monospace", name: "Lucida Console", color: "#800000" },
  //   { background: "#666666", fontFamily: "Tahoma, sans-serif", name: "Tahoma", color: "#800000" },
  //   { background: "#595959", fontFamily: "Impact, sans-serif", name: "Impact", color: "#800000" },
  //   { background: "#4D4D4D", fontFamily: "'Segoe UI', sans-serif", name: "Segoe UI", color: "#800000" },
  //   { background: "#404040", fontFamily: "'Roboto', sans-serif", name: "Roboto", color: "#800000" },
  //   { background: "#333333", fontFamily: "'Open Sans', sans-serif", name: "Open Sans", color: "#800000" },
  //   { background: "#262626", fontFamily: "'Lato', sans-serif", name: "Lato", color: "#800000" },
  //   { background: "#1A1A1A", fontFamily: "'Oswald', sans-serif", name: "Oswald", color: "#800000" },
  //   { background: "#0D0D0D", fontFamily: "'Montserrat', sans-serif", name: "Montserrat", color: "#800000" },
  //   { background: "#E0E0E0", fontFamily: "'PT Serif', serif", name: "PT Serif", color: "#800000" },
  //   { background: "#F5F5F5", fontFamily: "'Merriweather', serif", name: "Merriweather", color: "#800000" },

  //   // Second set (darker gray backgrounds and lighter maroon text)
  //   { background: "#4A4A4A", fontFamily: "Arial, sans-serif", name: "Arial", color: "#A05252" },
  //   { background: "#3F3F3F", fontFamily: "Helvetica, sans-serif", name: "Helvetica", color: "#A05252" },
  //   { background: "#363636", fontFamily: "'Times New Roman', serif", name: "Times New Roman", color: "#A05252" },
  //   { background: "#2C2C2C", fontFamily: "Georgia, serif", name: "Georgia", color: "#A05252" },
  //   { background: "#242424", fontFamily: "'Courier New', monospace", name: "Courier New", color: "#A05252" },
  //   { background: "#1F1F1F", fontFamily: "Verdana, sans-serif", name: "Verdana", color: "#A05252" },
  //   { background: "#191919", fontFamily: "'Trebuchet MS', sans-serif", name: "Trebuchet MS", color: "#A05252" },
  //   { background: "#141414", fontFamily: "Garamond, serif", name: "Garamond", color: "#A05252" },
  //   { background: "#0F0F0F", fontFamily: "'Palatino Linotype', serif", name: "Palatino Linotype", color: "#A05252" },
  //   { background: "#0A0A0A", fontFamily: "'Lucida Console', monospace", name: "Lucida Console", color: "#A05252" },
  //   { background: "#333333", fontFamily: "Tahoma, sans-serif", name: "Tahoma", color: "#A05252" },
  //   { background: "#292929", fontFamily: "Impact, sans-serif", name: "Impact", color: "#A05252" },
  //   { background: "#232323", fontFamily: "'Segoe UI', sans-serif", name: "Segoe UI", color: "#A05252" },
  //   { background: "#1A1A1A", fontFamily: "'Roboto', sans-serif", name: "Roboto", color: "#A05252" },
  //   { background: "#151515", fontFamily: "'Open Sans', sans-serif", name: "Open Sans", color: "#A05252" },
  //   { background: "#0D0D0D", fontFamily: "'Lato', sans-serif", name: "Lato", color: "#A05252" },
  //   { background: "#050505", fontFamily: "'Oswald', sans-serif", name: "Oswald", color: "#A05252" },
  //   { background: "#2E2E2E", fontFamily: "'Montserrat', sans-serif", name: "Montserrat", color: "#A05252" },
  //   { background: "#383838", fontFamily: "'PT Serif', serif", name: "PT Serif", color: "#A05252" },
  //   { background: "#404040", fontFamily: "'Merriweather', serif", name: "Merriweather", color: "#A05252" },
  // ];

  // return (
  //   <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: "20px", padding: "20px" }}>
  //     {styles.map((style, index) => (
  //       <div
  //         key={index}
  //         style={{
  //           backgroundColor: style.background,
  //           fontFamily: style.fontFamily,
  //           color: style.color,
  //           padding: "20px",
  //           borderRadius: "8px",
  //           textAlign: "center",
  //           boxShadow: "0 2px 4px rgba(0, 0, 0, 0.1)",
  //         }}
  //       >
  //         <p style={{ margin: 0 }}>{style.name}</p>
  //         <p style={{ fontSize: "14px", marginTop: "8px" }}>Background: {style.background}</p>
  //       </div>
  //     ))}
  //   </div>
  // );

}


export default App;
