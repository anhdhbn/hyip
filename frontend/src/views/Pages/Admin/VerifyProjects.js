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
      this.setState({projects: res.data.slice()}, ()=> {
        let {projects} = this.state
        let subProjects = []
        for (let i = 0 ; i < this.state.numTake; i++){
          subProjects.push(projects.shift())
        }
        this.setState({subProjects})
      })
      toast.success(`Fetched ${res.data.length} projects`)
    })
    .catch((reason) => {
      toast.error(`Fetched errors`)
    })
  }

  funcRemoveItem(id, index){
    let {projects, subProjects} = this.state
    let project = projects.shift()
    this.setState({projects})

    subProjects[index] = project
    this.setState({subProjects})
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