import {React, useState} from 'react';
import axios from 'axios';
import "./Form.css";

// save in state:

function Form(){
  const [file , setFile] = useState();
  const [gender, setGender] = useState();
  const [age, setAge] = useState();
  const [result, setResult] = useState("Nothing recieved yet");

  function handleFileChange (e){
    if (e.target.files)
      {  
        console.log(e.target.files);
        setFile(e.target.files[0]);
      }
  }

  async function handleUpload(endpoint)
  {
    // e.preventDefault();
    if (!file) return ;

    const formData = new FormData();
    formData.append("pdf", file);
    if (endpoint === "summarize_content")
    {
      formData.append("gender", gender);
      formData.append("age", age);
    }
    try
    {
      const response = await axios.post(`http://localhost:8000/${endpoint}`, formData, {
        headers :{
          'Content-Type' : 'multipart/form-data',
          'Authorization' : process.env.REACT_APP_REST_API_KEY
        },
      });
      console.log(response.data.result);
      setResult(response.data.result);
    } 
    catch (error){ console.log(error)};
  }

  return (
  <div className="upload-container">
      <input type="file" accept=".pdf" onChange={handleFileChange} className="file-input" />
      <p>
        <b>Age: </b>
          <input type="text" name="age" onChange={(e)=>setAge(e.target.value)}/>
      </p>
      <p>
        <b>Gender: </b>
          <input type="radio" name="gender" value="female" onChange={(e)=>setGender(e.target.value)}/>
          Female 
          <input type="radio" name="gender" value="male"  onChange={(e)=>setGender(e.target.value)}/>
          Male 
      </p>
      {file && (
        <>
        <button onClick={()=> handleUpload("get_content")} className="upload-button">
          Get Content
        </button>
        <button onClick={()=> handleUpload("summarize_content")} className="upload-button">
          Summerize Content
        </button>
        </>
      )}
      <p>
        {result}
      </p>
    </div>
  );
}

export default Form;

