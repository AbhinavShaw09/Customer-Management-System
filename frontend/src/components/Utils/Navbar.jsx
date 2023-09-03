import React from 'react'

function Navbar() {
  return (
    <>
    <header class="text-gray-600 body-font bg-violet-500">
        <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
          <a class="hover:text-violet-900 flex title-font font-medium items-center text-white mb-4 md:mb-0">
            <span class="ml-3 text-xl font-bold">CUSTOMER MANAGEMENT SYSTEM</span>
          </a>
          <nav class="md:ml-auto flex flex-wrap items-center text-base justify-center">
          <a class="mr-5 hover:text-violet-900 font-bold text-white">HOME</a>
          <a class="mr-5 hover:text-violet-900 font-bold text-white">DASHBOARD</a>
            <button class="rounded-full bg-violet-300/50 font-bold resize p-1.5 hover:bg-violet-900 text-white  ring ring-white">LOG IN</button>
          </nav>
        
        </div>
      </header>

    </>
  )
}

export default Navbar