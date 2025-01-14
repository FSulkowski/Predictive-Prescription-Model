import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

const API_URL = 'http://localhost:5000';

function App() {
  const [userData, setUserData] = useState({
    gluc: '',
    cholesterol: '',
    BMI: '',
    smoke: '',
    alco: '',
    cardio: '',
    weight: '',
    height: ''
  });
  const [result, setResult] = useState('');
  const [error, setError] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    console.log(name, value);
    setUserData(prevData => ({
      ...prevData,
      [name]: value
    }));
    setError(''); // Clear any previous errors
  };

  const validateInputs = (data) => {
    const requiredFields = ['gluc', 'cholesterol', 'BMI', 'weight', 'height'];
    const missingFields = requiredFields.filter(field => !data[field]);
    
    if (missingFields.length > 0) {
      throw new Error(`Please fill out these required fields: ${missingFields.join(', ')}`);
    }

    // Validate numerical fields
    const numericFields = ['gluc', 'cholesterol', 'BMI', 'weight', 'height'];
    numericFields.forEach(field => {
      const value = Number(data[field]);
      if (isNaN(value) || value < 0) {
        throw new Error(`${field} must be a valid positive number`);
      }
    });
  };

// useEffect(() => {
//   // Fetch initial user data from the server
//   axios.get(`/dummy`, {
//     withCredentials: true
//   })
//    .then(response => {
//       // setUserData(response.data);
//       console.log('User data fetched:', response.data);
//     })
//    .catch(error => {
//       console.error('Error fetching user data:', error);
//     });
// })

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setResult('');

    try {
      validateInputs(userData);

      const dataToSend = {
        ...userData,
        gluc: Number(userData.gluc),
        cholesterol: Number(userData.cholesterol),
        BMI: Number(userData.BMI),
        weight: Number(userData.weight),
        height: Number(userData.height),
        smoke: userData.smoke === '' ? null : Number(userData.smoke),
        alco: userData.alco === '' ? null : Number(userData.alco),
        cardio: userData.cardio === '' ? null : Number(userData.cardio)
      };

      // const response = await axios.post(`${API_URL}/predict`, dataToSend, {
      //   headers: {
      //     'Content-Type': 'application/json',
      //   },
      //   withCredentials: true
      // });

      // setResult(response.data.result);
      fetch('/predict', {
        method: 'POST', // Specify the request method
        headers: {
          'Content-Type': 'application/json' // Set the content type to JSON
        },
        body: JSON.stringify({ // Convert the body to a JSON string
         dataToSend
        })
      })
        .then(response => {
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
          return response.json(); // Parse the response as JSON
        })
        .then(data => {
          console.log('Success:', data); // Handle the response data
        })
        .catch(error => {
          console.error('Error:', error); // Handle any errors
        });
    } catch (error) {
      const errorMessage = error.response?.data?.error || error.message || 'An error occurred';
      setError(errorMessage);
      console.error('Error:', error);
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Ozempic Qualification Check</h1>
      
      {error && <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">{error}</div>}
      
      <form onSubmit={handleSubmit} className="space-y-4">
        {Object.entries(userData).map(([field, value]) => (
          <div key={field} className="flex flex-col">
            <label className="mb-1 capitalize">
              {field}:
              <input
                type="text"
                name={field}
                value={value}
                onChange={handleChange}
                className="border rounded px-2 py-1 w-full"
              />
            </label>
          </div>
        ))}
        
        <button 
          type="submit"
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          Check Qualification
        </button>
      </form>

      {result && (
        <div className="mt-4 p-4 bg-green-100 border border-green-400 text-green-700 rounded">
          <h3 className="font-bold">{result}</h3>
        </div>
      )}
    </div>
  );
}

export default App;