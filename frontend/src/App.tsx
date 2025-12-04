//import { useState } from 'react'
import './App.css'

//@ts-expect-error
import { Button } from "react-bootstrap";
import NavbarSCM from './components/Navbar/Navbar';

function App() {
  return (
    <>
      <header>
        <title>SCM</title>
      </header>
      <NavbarSCM />
      <div style={{ padding: "2rem" }}>
        <Button variant="primary">Hello Bootstrap</Button>
      </div>
    </>
  )
}

export default App
