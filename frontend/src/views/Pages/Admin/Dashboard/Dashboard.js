import React, { Component, lazy, Suspense } from 'react'
import {
  Col,
  Row,
} from 'reactstrap';
import { BatteryLoading } from 'react-loadingg';
import projectService from '../../../../services/projects'

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
