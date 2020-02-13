import React, { Component } from 'react';

import {
  Col,
  Row,
} from 'reactstrap';

import { toast } from 'react-toastify';

import projectService from "../../../services/projects"
import Project from "../../Components/Project"


class VerifyProjects extends Component{
  constructor(props){
    super(props);
    this.funcRemoveItem = this.funcRemoveItem.bind(this)
    this.state = {
      projects: [],
      subProjects: [],
      numTake: 3
    }
  }

  componentDidMount(){
    projectService.fetchUnVerifiedProjects().then(res => {
      this.setState({projects: res.data}, ()=> {
        this.setState({subProjects: this.state.projects.slice(0, this.state.numTake)})
      })
      toast.success(`Fetched ${res.data.length} projects`)
    })
    .catch((reason) => {
      toast.error(`Fetched errors`)
    })
  }

  funcRemoveItem(id){
    let pos = this.state.projects.map(item => item.id).indexOf(id);
    if (pos !== -1){
      this.state.projects.splice(pos, 1)
      this.setState({subProjects: this.state.projects.slice(0, this.state.numTake)});
    }
  }

  render(){
    return (
      <Row>
        {this.state.subProjects.map((project, index) =>
          <Col xs={12} sm={12} md={12} lg={6} xl={4} key={index}>
            <Project id={project.id} index={index} funcRemoveItem={this.funcRemoveItem} skip/>
          </Col>
        )}
      </Row>
    )
  }
}

export default VerifyProjects;