import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Machine from './components/Machine'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Machine />
    </>
  )
}

export default App
