import Task from "./Task"

const Tasks = ({tasks, onDelete, onToggle}) => {
//     // tasks is part of the state, to change any component, need to use the defined function setTasks
//     // state is immutate, you can only create and add new
//     const [tasks, setTasks] = useState([
//         {
//             id: 1,
//             text: "Doctor's Appointment",
//             day: "Feb 5th at 2:30pm",
//             reminder: true,
//         },
//         {
//             id: 2,
//             text: "Meeting at School",
//             day: "Feb 6th at 1:30pm",
//             reminder: true,
//         },
//         {
//             id: 3,
//             text: "Food Shopping",
//             day: "Feb 5th at 2:30pm",
//             reminder: false,
//         }
//     ])

    return (
        <>
            {
                //Creates a new array with the results of calling a callback on every element in the array
                // sends a task from the array task into the function
                tasks.map((task) => (<Task 
                    key={task.id} 
                    task = {task} 
                    onDelete = {onDelete}
                    onToggle = {onToggle}
                />))
            }
        </>
    )
}

export default Tasks