import React from 'react'
import Semester from './Semester'

const Results = (props) => {
    const { results } = props
    let data = []
    let count = 0
    let cgpa_total = 0
    let mark_total = 0
    let min_total = 0
    let max_total = 0
    Object.keys(results).forEach(function (key) {
        data.push(results[key])
    });
    return (
        <div>
            <h3 className='h-9 pl-7 bg-blue-900 text-white text-2xl font-bold italic'>Results</h3>
            {
                data.map((item, index) => {
                    return (
                        <Semester key={index} index={index} result={item} />
                    )
                })
            }
            <h3 className='h-9 mt-10 pl-7 bg-blue-900 text-white text-2xl font-bold italic'>Average of all semester</h3>
            <div className='flex justify-center ml-7 mt-5 bg-gray-200 p-5'>
                <div className='min-w-[400px] min-h-[260px]'>
                    <table>
                        <tr>
                            <td className='border-4 border-gray-200 bg-blue-900 text-white p-1'>Semester</td>
                            <td className='border-4 border-gray-200 bg-blue-900 text-white p-1'>Maximum Mark</td>
                            <td className='border-4 border-gray-200 bg-blue-900 text-white p-1'>Minimum Mark</td>
                            <td className='border-4 border-gray-200 bg-blue-900 text-white p-1'>Mark Obtained</td>
                            <td className='border-4 border-gray-200 bg-blue-900 text-white p-1'>CGPA Obtained</td>

                        </tr>

                        {
                            // this function will return average of all semester
                            data.map((item, index) => {
                                count += 1;
                                max_total += Number(item.total[0][0])
                                min_total += Number(item.total[0][1])
                                mark_total += Number(item.total[0][2])
                                cgpa_total += Number(/[\d.]+/.exec(item.total[0][3]))
                                return (
                                    <>
                                        <tr key={index}>
                                            <td className='border-4 border-gray-200 bg-blue-900 text-white p-1'>Semester {index + 1}</td>
                                            <td className='bg-blue-200 border-4 pl-5 pr-10'>{item.total[0][0]}</td>
                                            <td className='bg-blue-200 border-4 pl-5 pr-10'>{item.total[0][1]}</td>
                                            <td className='bg-blue-200 border-4 pl-5 pr-10'>{item.total[0][2]}</td>
                                            <td className='bg-blue-200 border-4 pl-5 pr-10'>{/[\d.]+/.exec(item.total[0][3])}</td>
                                        </tr>
                                    </>
                                )
                            })
                        }
                        <tr>
                            <td className='border-4 border-gray-200 bg-blue-900 text-white p-1'>Total</td>
                            <td className='bg-blue-200 border-4 pl-5 pr-10'>{max_total}</td>
                            <td className='bg-blue-200 border-4 pl-5 pr-10'>{min_total}</td>
                            <td className='bg-blue-200 border-4 pl-5 pr-10'>{mark_total}</td>
                            <td className='bg-blue-200 border-4 pl-5 pr-10'>{cgpa_total}</td>
                        </tr>
                        <tr>
                            <td className='border-4 border-gray-200 bg-blue-900 text-white p-1'>Average</td>
                            <td className='bg-blue-200 border-4 pl-5 pr-10'></td>
                            <td className='bg-blue-200 border-4 pl-5 pr-10'></td>
                            <td className='bg-blue-200 border-4 pl-5 pr-10'>{mark_total / count}</td>
                            <td className='bg-blue-200 border-4 pl-5 pr-10'>{cgpa_total / count}</td>
                        </tr>
                    </table>
                </div>
            </div>
        </div>
    )
}

export default Results
