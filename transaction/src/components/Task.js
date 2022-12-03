import React from 'react'
import { FaTimes } from 'react-icons/fa'

const Task = ({ task, onDelete, onToggle }) => {
    return (
        <div
            // IF task.reminder is true, output reminder, else nothing
            // className={`task ${task.reminder ? 'reminder' : ''}`}
            // onDoubleClick={() => onToggle(task.id)}
        >
            <h3>
                {task.date} <FaTimes
                    style={{ color: 'red', cursor: 'pointer' }}

                    // using this empty function allows us to send the task.id back
                    onClick={() => onDelete(task.id)}
                />
            </h3>
            <p>
                {task.accountID}
            </p>
            <p>
                {task.receiveAcc}
            </p>
            <p>
                {task.transAmount}
            </p>
            <p>
                {task.comment}
            </p>
        </div>
    )
}


export default Task

/*
 How to change something in the main App.js from a component? 
 Send a prop down from the main app 
 State gets passed down, actions get passed up
*/