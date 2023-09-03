import React from 'react'

function CrudOp() {
  return (
    <>
    <section class="text-gray-400 bg-gray-900 body-font">
  <div class="container pl-10 pr-10 pt-28 pb-20 mx-auto">
    <div class="flex flex-wrap -mx-4 -mb-10 text-center">
      <div class="sm:w-1/2 mb-10 px-4">
        <h2 class="title-font text-2xl font-medium text-white mt-6 mb-3">ADD A CUSTOMER</h2>
        <button class="flex mx-auto mt-6 text-white bg-violet-500 border-0 py-2 px-5 focus:outline-none hover:bg-violet-600 rounded">Button</button>
      </div>
      <div class="sm:w-1/2 mb-10 px-4">
        <h2 class="title-font text-2xl font-medium text-white mt-6 mb-6">VIEW A CUSTOMER</h2>
        <button class="flex mx-auto mt-6 text-white bg-violet-500 border-0 py-2 px-5 focus:outline-none hover:bg-violet-600 rounded">Button</button>
      </div>
    </div>
  </div>
</section>
<section class="text-gray-400 bg-gray-900 body-font ">
  <div class="container pr-10 pl-10 pt-20 pb-28 mx-auto">
    <div class="flex flex-wrap -mx-4 -mb-10 text-center">
      <div class="sm:w-1/2 mb-10 px-4">
        <h2 class="title-font text-2xl font-medium text-white mt-6 mb-6">UPDATE A CUSTOMER</h2>
        <button class="flex mx-auto mt-6 text-white bg-violet-500 border-0 py-2 px-5 focus:outline-none hover:bg-violet-600 rounded">Button</button>
      </div>
      <div class="sm:w-1/2 mb-10 px-4">
        <h2 class="title-font text-2xl font-medium text-white mt-6 mb-4">REMOVE A CUSTOMER</h2>
        <button class="flex mx-auto mt-6 text-white bg-violet-500 border-0 py-2 px-5 focus:outline-none hover:bg-violet-600 rounded">Button</button>
      </div>
    </div>
  </div>
</section>
    </>
  )
}

export default CrudOp


