import React, { Component, lazy, Suspense } from 'react'
import {
  Row,
} from 'reactstrap';
import { BatteryLoading } from 'react-loadingg';
import projectService from '../../../../services/projects'
import trackingServices from '../../../../services/tracking'
import { toast } from 'react-toastify';
const ProjectWidget = lazy(() => import('../../../Components/Widgets/ProjectWidget'));


class Dashboard extends Component {
  constructor(props) {
    super(props);
    this.state = {
      projects: []
    };
  }

  componentWillMount(){
    let user_id = localStorage.user_id
    if (user_id === undefined){
      this.props.history.push('/login');
    }
  }

  componentDidMount(){
    let user_id = localStorage.user_id
    if (user_id !== undefined){
      trackingServices.fetchTrackingProject(user_id).then(res => {
        toast.success(`Fetched ${res.data.length} projects`)
        if (res.data.length > 0) {
          this.setState({...this.state, projects: res.data})
        }
      })
    }
  }

  render() {

    return (
      <div className="animated fadeIn">
        <Row>
          <Suspense fallback={<BatteryLoading/>}>
            {this.state.projects.slice(0, 10).map((item, key) =>  {
              return <ProjectWidget id={item.project_id} key={key}></ProjectWidget>
            })}
          </Suspense>
          
        </Row>
      </div>
    );
  }
}

export default Dashboard;
