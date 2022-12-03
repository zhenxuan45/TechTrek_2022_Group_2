
import { useState, useEffect } from 'react'
import AddTask from './components/AddTask';
import Header from "./components/Header";
import Tasks from "./components/Tasks";
import axios from 'axios';


function App() {

  // tasks is part of the state, to change any component, need to use the defined function setTasks
  // state is immutate, you can only create and add new
  // state values should be kept in the top level components so that lower tiered components can be able to use them
  // test server npm i json-server
  // in the package.json set "server": "json-server -- watch db.json --port 5000" in scripts
  const [showAddTask, setShowAddTask] = useState(false)

  const [tasks, setTasks] = useState([])

  // useEffect is used to get something to happen the moment the page loads
  useEffect(() => {
    const getTasks = async () => {
      const tasksFromServer = await fetchTasks()
      setTasks(tasksFromServer)
    }

    getTasks()
  }, [])

  // Fetch Tasks
  const fetchTasks = async () => {

    //axios is used here to avoid double promise
    const res = await axios.get(`http://localhost:5000/tasks`)

    return res.data
  }

  //Used to update  Reminder status
  // Fetch Task
  const fetchTask = async (id) => {

    //axios is used here to avoid double promise
    const res = await axios.get(`http://localhost:5000/tasks/${id}`)

    return res.data
  }

  //Add Task
  const addTask = async (task) => {
    const res = await fetch('http://localhost:5000/tasks/', {
      method: 'POST',
      // Specifies the content type to be JSON
      headers: {
        'Content-type': 'application/json'
      },
      // Converts content to be JSON
      body: JSON.stringify(task)
    })

    const data = await res.json()
    setTasks([...tasks, data])

    // // Generates a random ID
    // const id = Math.floor (Math.random()*1000000 + 1 )
    // //Appends the id to task
    // const newTask = {id, ...task}
    // // Add the task to existing task list
    // setTasks([...tasks, newTask])
  }

  // Delete Task
  const deleteTask = async (id) => {

    //sends request to server to delete item
    await fetch(`http://localhost:5000/tasks/${id}`, {
      method: 'DELETE'
    })

    // Filter creates a new array with all elements that pass the test
    // in this case, filters out task with id  == id
    setTasks(tasks.filter((task) => task.id !== id))
  }

  //Toggle Reminder
  const toggleReminder = async (id) => {
    const taskToToggle = await fetchTask(id)
    const updTask = {
      ...taskToToggle, reminder: !taskToToggle.reminder
    }

    const res = await fetch(`http://localhost:5000/tasks/${id}`, {
      method: 'PUT',
      headers: {
        'Content-type': 'application/json'
      },
      // Converts content to be JSON
      body: JSON.stringify(updTask)
    }
    )
    
    const data = await res.json()

    // Runs the setTasks command
    setTasks(tasks.map((task) =>
      // Runs throught the array and checks if the id returned is the same as the task.id
      task.id === id ?

        // IF SAME, spread the rest of the task but set reminder to opposite of the reminder
        { ...task, reminder: data.reminder }

        // IF NOT SAME, Do nothing
        : task))
  }


  return (
    <div className="container">
      {/*  */}
      <Header
        title='Task Tracker'
        onAdd={() => setShowAddTask(!showAddTask)}
        showAdd={showAddTask}
      />

      {/* sends the prop down to the component */}
      {showAddTask && <AddTask onAdd={addTask} />}

      {/* Check if task.length > 0 */}
      {tasks.length > 0 ?
        // IF TRUE, RUN THIS
        <Tasks tasks={tasks} onDelete={deleteTask} onToggle={toggleReminder} /> :
        // RUN THIS
        "No Tasks to Show"
      }
    </div>
  );
}

export default App;
