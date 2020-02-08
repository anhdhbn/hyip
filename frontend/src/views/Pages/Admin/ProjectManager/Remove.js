import React, { Component } from 'react';

import {
  Button,
  CardBody,
  Col,
  Row,
} from "reactstrap";

import Form from "react-bootstrap/Form";
import { toast } from 'react-toastify';

import projectServices from '../../../../services/projects'

import SearchDomain from '../../../Base/SearchDomain'

class RemoveProject extends Component {
  constructor(props) {
    super(props);
    this.handleRemove = this.handleRemove.bind(this)
    this.state = {
      selectedOption:null,
    };
  }


  handleRemove() {
    if (this.state.selectedOption.value){
      projectServices.removeProject(this.state.selectedOption.value, {}).then(res => {
        if (res.success) {
          toast.success(`${this.state.selectedOption.label} was removed`)
          this.setState({selectedOption: null})
        } else {
          toast.error(`${this.state.selectedOption.label} have not removed`)
        }
      })
    }
  }

  removeButton(){
    if (this.state.selectedOption){
      return(
        <Row>
          <CardBody className="text-center">
            <Button color="danger" active tabIndex={-1} onClick={this.handleRemove}>Remove</Button>
          </CardBody>
        </Row>
      )
    } else {
      return null
    }
  }

  render() {
    return (
      <CardBody>
        <Form>
          <Row>
            <Col md="12">
              <Form.Group>
              <SearchDomain handleChange={selectedOption => this.setState({ selectedOption })}/>
              </Form.Group>
              
            </Col>
          </Row>
          {this.removeButton()}
        </Form>
      </CardBody>
    )
  }
}

export default RemoveProject;