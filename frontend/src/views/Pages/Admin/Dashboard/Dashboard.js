import React, { Component, lazy, Suspense, useState, useEffect  } from 'react';
import { Bar, Line } from 'react-chartjs-2';
import {
  Badge,
  Button,
  ButtonDropdown,
  ButtonGroup,
  ButtonToolbar,
  Card,
  CardBody,
  CardFooter,
  CardHeader,
  CardTitle,
  Col,
  Dropdown,
  DropdownItem,
  DropdownMenu,
  DropdownToggle,
  Progress,
  Row,
  Table,
} from 'reactstrap';
import { BatteryLoading } from 'react-loadingg';
import projectService from '../../../../services/projects'
import Loader from 'react-loader-spinner'

const ProjectWidget = lazy(() => import('../../../Widgets/ProjectWidget'));


class Dashboard extends Component {
  constructor(props) {
    super(props);
    this.state = {
      projects: []
    };
  }

  componentDidMount(){
    projectService.fetchEasyProjects().then(res => {
      if (res.success && res.data.length > 0) {
        this.setState({...this.state, projects: res.data})
        console.log(this.state.projects[0].id)
      }
    })
  }

  render() {

    return (
      <div className="animated fadeIn">
        <Row>
          <Suspense fallback={<BatteryLoading/>}>
            {this.state.projects.slice(0, 10).map((item, key) =>  {
              return <Col xs={12} sm={12} md={12} lg={12} xl={6} key={key}><ProjectWidget id={item.id}></ProjectWidget></Col>
            })}
          </Suspense>
          
        </Row>
      </div>
    );
  }
}

export default Dashboard;
