import React, { useEffect, useState } from 'react';
import axios from 'axios';

import Header from './components/Header';
import Footer from './components/Footer';


function App() {
    const [data, setData] = useState(null);

    useEffect(() => {
      axios.get('http://127.0.0.1:5000') // Adjusted to Flask's actual port
    .then(response => {
        setData(response.data);
    })
    .catch(error => {
        console.error('There was an error fetching the data!', error);
    });

    }, []);

    return (
      <div>
        <Header/>

        <h2>{data.geo.city}, {data.geo.state}</h2>
        <h2>{data.geo.country}</h2>
        <h2><b>Temperature: </b>{data.now.temp} <span>&#8457;</span></h2>
        <h2><b>Feels Like: </b>{data.now.feels_like} <span>&#8457;</span></h2>

        <div>
          <h1>Fruits:</h1>
          <ul>
            {data.forecast.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
        </div>

        <Footer/>
      </div>
    );
}

export default App;
