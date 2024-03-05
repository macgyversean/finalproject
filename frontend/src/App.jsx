import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Layout from "./pages/Layout";
import Home from "./routes/Home";
import ErrorPage from "./pages/ErrorPage";
import About from "./routes/About";
// import SingleCeo, { loader as SingleCeoLoader } from "./routes/SingleCeo";
// import AddCeo, { action as addCeoAction } from "./routes/AddCeo";

const router = createBrowserRouter([
  {
    element: <Layout />,
    errorElement: <ErrorPage />,
    children: [
      {
        path: "/",
        element: <Home />,
      },
      {
        path: "/about",
        element: <About />,
      },
    ],
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;
