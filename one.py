app.js
import React from 'react';
import ParentComponent from './ParentComponent';

function App() {
  return (
    <div className="App">
      <h1>React Data Sharing Example</h1>
      <ParentComponent />
    </div>
  );
}

export default App;


childcomponent
import React from 'react';

function ChildComponent(props) {
  return (
    <div style={{ border: '2px solid green', padding: '10px', margin: '10px' }}>
      <h3>Child Component</h3>
      <p>Received from Parent: {props.data}</p>
    </div>
  );
}

export default ChildComponent;


parentcomponent
import React, { useState } from 'react';
import ChildComponent from './ChildComponent';

function ParentComponent() {
  const [message, setMessage] = useState('Hello from Parent!');

  const updateMessage = () => {
    setMessage('Message updated by Parent!');
  };

  return (
    <div style={{ border: '2px solid blue', padding: '10px', margin: '10px' }}>
      <h2>Parent Component</h2>
      <p>Message: {message}</p>
      <button onClick={updateMessage}>Change Message</button>
      
      {/* Passing data to child component */}
      <ChildComponent data={message} />
    </div>
  );
}

export default ParentComponent;




















app.js

import React from 'react';
import CounterClass from './CounterClass';
import CounterHook from './CounterHook';

function App() {
  return (
    <div className="App">
      <h1>Understanding the Importance of Hooks</h1>
      <CounterClass />
      <hr />
      <CounterHook />
    </div>
  );
}

export default App;


counterclass
import React, { Component } from 'react';

class CounterClass extends Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
  }

  increment = () => {
    this.setState({ count: this.state.count + 1 });
  };

  render() {
    return (
      <div>
        <h2>Class Counter: {this.state.count}</h2>
        <button onClick={this.increment}>Increment</button>
      </div>
    );
  }
}

export default CounterClass;



counterhook
import React, { useState } from 'react';

function CounterHook() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h2>Hook Counter: {count}</h2>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}

export default CounterHook;
