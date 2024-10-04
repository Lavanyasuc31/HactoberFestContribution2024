import React from 'react'
import { FaGithub } from 'react-icons/fa'
import { MdMenu } from 'react-icons/md'

const Navbar = ({setIsOpen}) => {
  return (
   <header className='bg-white h-[10vh] flex items-center justify-center'>
    <nav className='max-w-7xl mx-auto w-full px-2 flex items-center justify-between'>
        <div className='flex items-center gap-2'>
            <img src="/logo.png" alt="logo" className='w-10 rounded-full' />
            <h2 className='text-lg'>Music Player</h2>
        </div>
        <button onClick={()=>setIsOpen(true)} className='lg:hidden visible'>
            <MdMenu size={25}/>
        </button>
        <a href='https://github.com/ankitjhagithub21/'  target='_blank' className='hidden cursor-pointer hover:scale-105 lg:inline-block'>
            <FaGithub size={35}/>
        </a>
    </nav>
   </header>
  )
}

export default Navbar
