import React from 'react'
import logo from '../logo.svg'

const Navbar = () => {
  return (
    <div className='flex h-16 bg-blue-900'>
      <img className='mt-2 h-12 animate-spin' src={logo} alt="logo" />
      <h4 className='mt-4 italic text-white text-xl'>Result_Analyser</h4>
    </div>
  )
}

export default Navbar
