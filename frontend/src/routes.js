import React from "react";

const Dashboard = React.lazy(() => import("./views/Pages/Admin/Dashboard"));
const ProjectManager = React.lazy(() => import("./views/Pages/Admin/ProjectManager/ProjectManager"));


// https://github.com/ReactTraining/react-router/tree/master/packages/react-router-config
const routes = [
  { path: "/", exact: true, name: "Home" },
  { path: "/dashboard", name: "Dashboard", component: Dashboard },
  { path: "/project-manager", name: "Project manager", component: ProjectManager },
];

export default routes;
