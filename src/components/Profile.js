import React from 'react'
import { useNavigate } from 'react-router-dom'

const Profile = (props) => {
    let profile = props.profile.profile
    const navigate=useNavigate()
    const handleBack = ()=>{
        props.setIsLoading(true)
        navigate("/")
    }
    return (
        <div>
            <button onClick={handleBack} className='p-2 bg-blue-900 text-white rounded-md ml-7 w-24 mb-5 font-bold'> <span className='text-lg'>{"< "}</span>Back</button>
            <h3 className='h-9 pl-7 bg-blue-900 text-white text-2xl font-bold italic'>Profile</h3>
            <div className='flex justify-center ml-7 m-5 bg-gray-200 p-5'>
                <div className='min-w-[400px] min-h-[260px]'>
                    <table>
                        <tr>
                            <td className='border-4 border-gray-200 bg-blue-900 text-white p-1'><b>Name</b></td>
                            <td className='bg-blue-200 border-4 pl-5 pr-10'>{profile[5]}</td>
                        </tr>
                        <tr>
                        <td className='border-4 border-gray-200 bg-blue-900 text-white p-1'><b>Father's Name</b></td>
                            <td className='bg-blue-200 border-4 pl-5 pr-10'>{profile[3]}</td>
                        </tr>
                        <tr>
                        <td className='border-4 border-gray-200 bg-blue-900 text-white p-1'><b>Mother's Name</b></td>
                            <td className='bg-blue-200 border-4 pl-5 pr-10'>{profile[4]}</td>
                        </tr>
                        <tr>
                        <td className='border-4 border-gray-200 bg-blue-900 text-white p-1'><b>Roll Number</b></td>
                            <td className='bg-blue-200 border-4 pl-5 pr-10'>{profile[0]}</td>
                        </tr>
                        <tr>
                        <td className='border-4 border-gray-200 bg-blue-900 text-white p-1'><b>Enrollment Number</b></td>
                            <td className='bg-blue-200 border-4 pl-5 pr-10'>{profile[2]}</td>
                        </tr>
                        <tr>
                        <td className='border-4 border-gray-200 bg-blue-900 text-white p-1'><b>Addmission Session</b></td>
                            <td className='bg-blue-200 border-4 pl-5 pr-10'>{profile[1]}</td>
                        </tr>
                        <tr>
                        <td className='border-4 border-gray-200 bg-blue-900 text-white p-1'><b>Course</b></td>
                            <td className='bg-blue-200 border-4 pl-5 pr-10'>{profile[7]}</td>
                        </tr>
                    </table>
                </div>
                <div className=''>
                    <img className='min-w-[200px] min-h-[260px]' src={profile[6]} alt="profile_photo" />
                </div>
            </div>
        </div>
    )
}

export default Profile
