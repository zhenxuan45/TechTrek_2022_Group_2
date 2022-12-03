import { useState } from 'react'

const AddTask = ({onAdd}) => {

    // This segment creates the states and the state methods
    const [text, setText] = useState("")
    const [day, setDay] = useState("")
    // Default for reminder is false
    const [reminder, setReminder] = useState(false)

    // this handles the submit button
    const onSubmit = (e) =>{

        // this prevents the default redirect action
        e.preventDefault()

        // Checks to see if task is added
        if(!text) {

            // If NO TASK ADDED, generates an alert and returns nothing, leaving the function
            alert('Please add a task')
            return
        }

        // calls the on Add Prop to pass information back up
        onAdd({text, day, reminder})

        // Resets the data fields
        setText('')
        setDay('')
        setReminder(false)
    }

    return (
        <form className='add-form' onSubmit={onSubmit}>
            <div className='form-control'>
                <label> Task </label>
                <input type='text'
                    placeholder='Add Task'
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                />
            </div>
            <div className='form-control'>
                <label> Day & Time </label>
                <input type='text' placeholder='Add Day and Time'
                value={day}
                onChange={(e) => setDay(e.target.value)}
                 />
            </div>
            <div className='form-control form-control-check'>
                <label>Set Reminder </label>
                <input type='checkbox' 
                value={reminder}
                checked = {reminder}
                onChange={(e) => setReminder(e.currentTarget.checked)}/>
            </div>

            <input type="submit" value="Save Task" className='btn btn-block' />
        </form>
    )
}

export default AddTask