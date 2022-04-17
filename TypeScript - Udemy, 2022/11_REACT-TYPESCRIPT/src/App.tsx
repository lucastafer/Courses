import React, { createContext } from "react";

// 5 - importação de componentes
import FirstComponent from "./components/FirstComponent";
import SecondComponent from "./components/SecondComponent";

// 6 - destructuring
import Destructuring, { Category } from "./components/Destructuring";

// 7 -  useState
import State from "./components/State";
import Context from "./components/Context";

// 8 - type
type textOrNull = string | null;

// 9 - context
interface IAppContext {
  language: string;
  framework: string;
  projects: number;
}

export const AppContext = createContext<IAppContext | null>(null);

function App() {
  // 1 - variaveis
  const name: string = "Lucas";
  const age: number = 21;
  const isWorking: boolean = true;

  // 2 - funções
  const userGreeting = (name: string): string => {
    return `Hi, ${name}!`;
  };

  // 8 - type
  const myText: textOrNull = "Has some text here!";
  const mySecondText: textOrNull = null;

  // 9 - context
  const contextValue = {
    language: "JavaScript",
    framework: "Express",
    projects: 5,
  };

  return (
    <AppContext.Provider value={contextValue}>
      <div className="App">
        <h1>React w/ TS</h1>
        <h2>Name: {name}</h2>
        <p>Age: {age}</p>
        {isWorking && <p>Online now!</p>}
        {userGreeting(name)}
        <FirstComponent />
        <SecondComponent name="Teste" />
        <Destructuring
          title="First post"
          content="Nice post about TS"
          commentsQty={10}
          tags={["JavaScript", "TypeScript"]}
          category={Category.TS}
        />
        <State />
      </div>
      <Context />
    </AppContext.Provider>
  );
}

export default App;
