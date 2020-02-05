import React from "react";

const Dashboard = React.lazy(() => import("./views/Pages/Admin/Dashboard"));
const Create = React.lazy(() => import("./views/Pages/Admin/Create/Create"));


// https://github.com/ReactTraining/react-router/tree/master/packages/react-router-config
const routes = [
  { path: "/", exact: true, name: "Home" },
  { path: "/dashboard", name: "Dashboard", component: Dashboard },
  { path: "/create", name: "Create", component: Create },
];

export default routes;
