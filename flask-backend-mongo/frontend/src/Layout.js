import Header from "./components/Header/Header";
import Sidenav from "./components/Sidenav/Sidenav";
import { useState } from "react";
import { Route } from "react-router-dom";

function Layout(props) {
  const [menuAbierto, setMenuAbierto] = useState(false);

  const toggleMenuLateral = () => {
    setMenuAbierto(!menuAbierto);
  };

  return (
    <>
      <Sidenav
        open={menuAbierto}
        menuClickedFunction={toggleMenuLateral}
      ></Sidenav>
      <Header menuClickedFunction={toggleMenuLateral}></Header>
      <main className="container pt-5">
        <Route {...props} />
      </main>
    </>
  );
}

export default Layout;
