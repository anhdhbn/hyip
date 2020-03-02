import React, { Component } from 'react';
import { HashRouter, Route, Switch } from 'react-router-dom';
import { Redirect } from 'react-router';
// import { renderRoutes } from 'react-router-config';
import { BatteryLoading } from 'react-loadingg'
import './App.scss';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
// Containers
const DefaultLayout = React.lazy(() => import('./containers/DefaultLayout'));

// Pages
const Login = React.lazy(() => import('./views/Pages/Login'));
const Register = React.lazy(() => import('./views/Pages/Register'));
const Page404 = React.lazy(() => import('./views/Pages/Page404'));
const Page500 = React.lazy(() => import('./views/Pages/Page500'));

class App extends Component {

  render() {
    return (
      <HashRouter>
          <React.Suspense fallback={<BatteryLoading />}>
            <Switch>
              <Route exact path="/" render={() => (<Redirect to="/admin/dashboard"/>)}/>
              <Route exact path="/login" name="Login Page" render={props => <Login {...props}/>} />
              <Route exact path="/register" name="Register Page" render={props => <Register {...props}/>} />
              <Route exact path="/404" name="Page 404" render={props => <Page404 {...props}/>} />
              <Route exact path="/500" name="Page 500" render={props => <Page500 {...props}/>} />
              <Route path="/admin" name="Home" render={props => <DefaultLayout {...props}/>} />
              <Redirect from='*' to='/404' />
            </Switch>
            <ToastContainer/>
          </React.Suspense>
      </HashRouter>
    );
  }
}

export default App;
