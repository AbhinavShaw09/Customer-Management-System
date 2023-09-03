import React from 'react'
import Navbar from '../Utils/Navbar'
import CrudOp  from '../Utils/CrudOp'
import Footer from '../Utils/Footer'

function Home() {
  return (<>
    <Navbar />
    <CrudOp/>
    <Footer/>
  </>
  )
}

export default Home