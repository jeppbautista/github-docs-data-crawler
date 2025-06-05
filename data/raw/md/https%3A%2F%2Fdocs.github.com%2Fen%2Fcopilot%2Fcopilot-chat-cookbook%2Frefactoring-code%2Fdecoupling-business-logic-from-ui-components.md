  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Copilot Chat Cookbook](https://docs.github.com/en/copilot/copilot-chat-cookbook "Copilot Chat Cookbook")/
  * [Refactoring code](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code "Refactoring code")/
  * [Decoupling business logic](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/decoupling-business-logic-from-ui-components "Decoupling business logic")


# Decoupling business logic from UI components
Copilot Chat can help you separate your business logic from your user interface code, making it easier to maintain and scale your application.
## In this article
  * [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/decoupling-business-logic-from-ui-components#example-scenario)
  * [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/decoupling-business-logic-from-ui-components#example-prompt)
  * [Example response](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/decoupling-business-logic-from-ui-components#example-response)
  * [Further reading](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/decoupling-business-logic-from-ui-components#further-reading)


In many front-end frameworks, business logic can become embedded within user interface (UI) components, making the code hard to maintain or extend, especially as the application grows.
Copilot Chat can help you refactor your code to extract business logic into separate services or state management solutions. This allows the business logic to be reused across different UI components. It also makes the code easier to scale by separating concerns and reducing interdependencies, and it simplifies unit testing by allowing business logic to be tested independently from UI components.
## [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/decoupling-business-logic-from-ui-components#example-scenario)
In this JavaScript code, the `Counter` component configures the business logic for the component and also defines UI code for using the component in a web page.
```
import React, { useState } from 'react';

const Counter = (const [count, setCount] = useState(0);

  const increment = (if (count >= 10) {
      alert('Count cannot exceed 10');
      return;
    }
    setCount(count + 1);
  };

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>Increment</button>
    </div>
  );
};

export default Counter;

```

## [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/decoupling-business-logic-from-ui-components#example-prompt)
`Use Redux to separate the UI code from the Counter component in this code.`
## [Example response](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/decoupling-business-logic-from-ui-components#example-response)
Copilot provides step-by-step instructions for refactoring the code.
The suggested changes refactor the `Counter` component to use Redux for state management. This includes setting up a Redux store with an initial state and a reducer, defining an increment action, and modifying the `Counter` component to connect to the Redux store. Finally, the application is wrapped with a `Provider` component to make the Redux store available to the `Counter` component. This separates the UI logic from state management.
The proposed changes separate the code into five separate files.
Copilot Chat responses are non-deterministic, so you may get a different response from the one described here.
### [actions.js](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/decoupling-business-logic-from-ui-components#actionsjs)
```
export const increment = (type: 'INCREMENT'
});

```

### [reducer.js](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/decoupling-business-logic-from-ui-components#reducerjs)
```
const initialState = {
  count: 0
};

const counterReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'INCREMENT':
      if (state.count >= 10) {
        alert('Count cannot exceed 10');
        return state;
      }
      return {
        ...state,
        count: state.count + 1
      };
    default:
      return state;
  }
};

export default counterReducer;

```

### [store.js](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/decoupling-business-logic-from-ui-components#storejs)
```
import { createStore } from 'redux';
import counterReducer from './reducer';

const store = createStore(counterReducer);

export default store;

```

### [counter.js](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/decoupling-business-logic-from-ui-components#counterjs)
```
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { increment } from './actions';

const Counter = (const count = useSelector(state => state.count);
  const dispatch = useDispatch();

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => dispatch(increment())}>Increment</button>
    </div>
  );
};

export default Counter;

```

### [index.js](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/decoupling-business-logic-from-ui-components#indexjs)
```
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import store from './store';
import Counter from './counter';

ReactDOM.render(
  <Provider store={store}>
    <Counter />
  </Provider>,
  document.getElementById('root')
);

```

## [Further reading](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/decoupling-business-logic-from-ui-components#further-reading)
  * [Prompt engineering for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
  * [Best practices for using GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)


