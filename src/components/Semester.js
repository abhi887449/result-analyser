import React from 'react'

// this component is for displaying semester result

const Semester = (props) => {
    const { result,index } = props
    return (
        <div>
            <h3 className='mt-10 h-9 pl-7 bg-blue-900 text-white text-2xl font-bold italic'>Semester {index+1}</h3>
            <div className='flex justify-center ml-7 mt-5 bg-gray-200 p-5'>
                <div className='min-w-[400px] min-h-[260px]'>
                    <table>
                        <tr>
                            <th className='border-4 border-gray-200 bg-blue-900 text-white p-1'><b>Subject Name</b></th>
                            <th className='border-4 border-gray-200 bg-blue-900 text-white p-1'><b>Max/Min Marks</b></th>
                            <th className='border-4 border-gray-200 bg-blue-900 text-white p-1'><b>Mark Obtained</b></th>
                            <th className='border-4 border-gray-200 bg-blue-900 text-white p-1'><b>CGPA Obtained</b></th>

                        </tr>
                        {result.subjects.map((item,index) => {
                            let min_max=item[1].split(" ")
                            return (
                                <tr key={index}>
                                    <td className='bg-blue-200 border-4 pl-5 pr-10'>{item[0]}</td>
                                    <td className='bg-blue-200 border-4 pl-5 pr-10'>{min_max[0]+"/"+min_max[1]}</td>
                                    <td className='bg-blue-200 border-4 pl-5 pr-10'>{item[2]}</td>
                                    <td className='bg-blue-200 border-4 pl-5 pr-10'>{/[\d.]+/.exec(item[3])}</td>
                                </tr>
                            )
                        })}
                                <tr>
                                    <td className='border-4 border-gray-200 bg-blue-900 text-white p-1'>Maximum Mark</td>
                                    <td className='bg-blue-200 border-4 pl-5 pr-10'>{result.total[0][0]}</td>
                                </tr>
                                <tr>
                                    <td className='border-4 border-gray-200 bg-blue-900 text-white p-1'>Minimum Mark</td>
                                    <td className='bg-blue-200 border-4 pl-5 pr-10'>{result.total[0][1]}</td>
                                </tr>
                                <tr>
                                    <td className='border-4 border-gray-200 bg-blue-900 text-white p-1'>Mark Obtained</td>
                                    <td className='bg-blue-200 border-4 pl-5 pr-10'>{result.total[0][2]}</td>
                                </tr>
                                <tr>
                                    <td className='border-4 border-gray-200 bg-blue-900 text-white p-1'>CGPA Obtained</td>
                                    <td className='bg-blue-200 border-4 pl-5 pr-10'>{/[\d.]+/.exec(result.total[0][3])}</td>
                                </tr>

                    </table>
                </div>
            </div>
        </div>
    )
}

export default Semester
