import React, { useEffect, useState } from 'react';
import axios from 'axios';


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
          <h1>Sammy The Weather Swami</h1>
          <p>{data ? data.geo.city : 'Loading...'}</p>
          <p>{data ? data.geo.state : 'Loading...'}</p>
          <p>{data ? data.geo.country : 'Loading...'}</p>
        </div>
    );
}

export default App;
