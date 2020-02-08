import React, { Component } from 'react';
import PropTypes from 'prop-types';

import {
  Card,
  CardBody,
  CardFooter,
  CardHeader,
  CardTitle,
  Col,
  Row,
} from 'reactstrap';

import { toast } from 'react-toastify';
import projectService from "../../../../services/projects"

import Project from "./Project"

const propTypes = {
  id: PropTypes.string,
};

const defaultProps = {
  id: null,
};

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
      if(res.success){
        this.setState({projects: res.data}, ()=> {
          this.setState({subProjects: this.state.projects.slice(0, this.state.numTake)})
        })
        toast.success(`Fetched ${res.data.length} projects`)
      }else {
        toast.error(`Fetched errors`)
      }
    })
  }

  funcRemoveItem(id){
    let pos = this.state.projects.map(item => item.id).indexOf(id);
    if (pos != -1){
      this.state.projects.splice(pos, 1)
      this.setState({subProjects: this.state.projects.slice(0, this.state.numTake)});
    }
  }

  render(){
    return (
      <Row>
        {this.state.subProjects.map((project, index) =>
          <Col xs={12} sm={12} md={12} lg={6} xl={4} key={index}>
            <Project id={project.id} funcRemoveItem={this.funcRemoveItem}/>
          </Col>
        )}
      </Row>
    )
  }
}


VerifyProjects.propTypes = propTypes;
VerifyProjects.defaultProps = defaultProps;

export default VerifyProjects;