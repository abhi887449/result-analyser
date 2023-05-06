import React, { useState } from 'react'
import { useNavigate } from "react-router-dom"

// this component is used to take data from user and request to backend for results
const DetailForm = (props) => {
    const { setIsLoading, fetchResults } = props
    const [data, setData] = useState({
        "year": "",
        "roll": "",
        "current_sem": 6,
        "branch": ""
    })
    const navigate = useNavigate()
    const handelSubmit = () => {
        setIsLoading(true)
        fetchResults(data)
        navigate("/results")
    }
    const onChange = (e)=>{
        setData({...data,[e.target.name]:e.target.value})
      }
    return (
        <>
            <form className='flex flex-col m-auto w-fit p-10 border mt-10 border-blue-900 rounded-xl shadow-lg bg-blue-200 shadow-blue-900' onSubmit={handelSubmit}>
                <div className='flex flex-col md:flex-row m-auto mt-7 mb-7'>
                    <div className='mb-7 md:mr-10'>
                        <label className=' h-10 w pl-4 p-2 pr-2 rounded-tl-md rounded-bl-md text-lg text-white bg-blue-900' htmlFor="year">Admission</label>
                        <select onChange={onChange} required className='pl-2 h-10 w-48 rounded-tr-md rounded-br-md border focus:border-blue-900 hover:border-blue-900' name="year" id="year">
                            <option className='p-3' value="">Select Admi. Session</option>
                            <option className='p-3' value="2021-22">2021-22</option>
                            <option className='p-3' value="2020-21">2020-21</option>
                            <option className='p-3' value="2019-20">2019-20</option>
                            <option className='p-3' value="2018-19">2018-19</option>
                        </select>
                    </div>
                    <div className='md:ml-10'>
                        <label className=' h-10 pl-4 p-2 pr-4 rounded-tl-md rounded-bl-md text-lg text-white bg-blue-900' htmlFor="current_sem">Semester</label>
                        <select onChange={onChange} required className='pl-2 h-10 w-48 rounded-tr-md rounded-br-md border focus:border-blue-900 hover:border-blue-900' name="current_sem" id="current_sem">
                            <option className='p-3' value="">Select Semester</option>
                            <option className='p-3' value={1}>First Semester</option>
                            <option className='p-3' value={2}>Second Semester</option>
                            <option className='p-3' value={3}>Third Semester</option>
                            <option className='p-3' value={4}>Fourth Semester</option>
                            <option className='p-3' value={5}>Fifth Semester</option>
                            <option className='p-3' value={6}>Sixth Semester</option>
                            <option className='p-3' value={7}>Seventh Semester</option>
                            <option className='p-3' value={8}>Eighth Semester</option>
                            <option className='p-3' value={8}>Pass Out</option>
                        </select>
                    </div>
                </div>
                <div className='m-auto flex flex-col md:flex-row'>
                    <div className='md:mr-10'>
                        <label className=' h-10 pl-4 p-2 pr-7 rounded-tl-md rounded-bl-md text-lg text-white bg-blue-900' htmlFor="roll">Roll No.</label>
                        <input onChange={onChange} required placeholder='Write Roll Number' className='pl-2 mb-7 h-10 w-48 border rounded-tr-md rounded-br-md focus:border-blue-900 hover:border-blue-900' type="text" name="roll" id="roll" />
                    </div>
                    <div className='md:ml-10'>
                        <label className='h-10 pl-4 p-2 pr-9 rounded-tl-md rounded-bl-md text-lg text-white bg-blue-900' htmlFor="branch">Branch</label>
                        <select onChange={onChange} required className=' pl-2 h-10 w-48 rounded-tr-md rounded-br-md border focus:border-blue-900 hover:border-blue-900' name="branch" id="branch">
                            <option className='p-3' value="">Select Branch</option>
                            <option className='p-3' value="B.Tech CSE">B.Tech CSE</option>
                        </select>
                    </div>
                </div>
                <button className='mt-7 hover:bg-green-600 w-28 m-auto rounded-md p-2 bg-blue-900 text-white' type="submit">Submit</button>
            </form>
        </>
    )
}

export default DetailForm
