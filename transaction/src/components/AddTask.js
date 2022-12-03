import { useState } from 'react'

const AddTask = ({onAdd}) => {

    // This segment creates the states and the state methods
    const [accountID, setaccountID] = useState("")
    const [receiveAcc, setreceiveAcc] = useState("")
    const [date, setDate] = useState("")
    const [transAmount, settransAmount] = useState("")
    const [comment, setComment] = useState("")

    // this handles the submit button
    const onSubmit = (e) =>{

        // this prevents the default redirect action
        e.preventDefault()

        // Checks to see if task is added
        if(!transAmount) {

            // If NO TASK ADDED, generates an alert and returns nothing, leaving the function
            alert('Please add a transaction amount')
            return
        }

        // calls the on Add Prop to pass information back up
        onAdd({accountID,receiveAcc,date,transAmount,comment})

        // Resets the data fields
        setaccountID('')
        setreceiveAcc('')
        setDate('')
        settransAmount('')
        setComment('')
    }

    return (
        <form className='add-form' onSubmit={onSubmit}>
            <div className='form-control'>
                <label> Account ID </label>
                <input type='text'
                    placeholder='Account ID'
                    value={accountID}
                    onChange={(e) => setaccountID(e.target.value)}
                />
            </div>
            <div className='form-control'>
                <label> Receiving Account </label>
                <input type='text' placeholder='Receiving Account'
                value={receiveAcc}
                onChange={(e) => setreceiveAcc(e.target.value)}
                 />
            </div>
            <div className='form-control'>
                <label> Date </label>
                <input type='text' placeholder='Schedule Date'
                value={date}
                onChange={(e) => setDate(e.target.value)}
                 />
            </div>
            <div className='form-control'>
                <label> Transaction Amount </label>
                <input type='text' placeholder='Transaction Amount'
                value={transAmount}
                onChange={(e) => settransAmount(e.target.value)}
                 />
            </div>
            <div className='form-control'>
                <label> Comment </label>
                <input type='text' placeholder='Comment'
                value={comment}
                onChange={(e) => setComment(e.target.value)}
                 />
            </div>


            <input type="submit" value="Schedule Transaction" className='btn btn-block' />
        </form>
    )
}

export default AddTask