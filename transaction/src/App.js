
import { useState, useEffect } from 'react'
import axios from 'axios';
import BankAccountType from './components/BankAccountType';
import BankBalance from './components/BankBalance';
import ScheduledTransactions from './components/ScheduledTransactions'
import BasicTabs from './components/Tabs';


function App() {

  return (
    <div className="container">
      <BasicTabs/>
    </div>
  );
}

export default App;
