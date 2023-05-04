import DetailForm from './components/DetailForm';
import Navbar from './components/Navbar';
import Marquee from "react-fast-marquee";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import { useState } from 'react';
import ResultPage from './components/ResultPage';


function App() {
  const [json,setJson]=useState({})
  const [isLoading, setIsLoading] = useState(true)
  const fetchResults=async(data)=>{
    setIsLoading(true)
      let url="http://localhost:5000/results"
      let x = await fetch(url,{
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin':'*',
          'Access-Control-Allow-Methods':'POST,PATCH,OPTIONS'
          },
        body: JSON.stringify({
          "year":data["year"],
          "roll":data["roll"],
          "current_sem":Number(data["current_sem"]),
          "branch": data["branch"]
        })
      });
      let y = await x.json();
    console.log(y)
    setJson(y)
    setIsLoading(false)
  }
  return (
    <Router>
      <div className='bg-blue-200 min-h-screen min-w-[800px] pb-5'>
        <Navbar />
        <Marquee pauseOnHover={true} direction="left" className="text-red-500" behavior=""><b>Note: </b> Do not press submit button multiple time. Your result will be fetched soon. Pressing multiple time submit button will cause meaning less request to University server.</Marquee>
        <div className='flex justify-center font-extrabold text-5xl italic text-blue-900 m-5'>Result Analyser</div>
        <Routes>
          <Route exact path="/" element={<DetailForm setIsLoading={setIsLoading} fetchResults={fetchResults} />}></Route>
          <Route exact path="/results" element={<ResultPage setIsLoading={setIsLoading} json={json} loading={isLoading} />}></Route>
        </Routes>
      </div>
    </Router>
  );
}

export default App;
