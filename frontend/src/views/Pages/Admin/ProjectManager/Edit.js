import React, { Component } from 'react';

import {
  CardBody,
  Col,
  Row,
} from "reactstrap";

import Form from "react-bootstrap/Form";

import SearchDomain from '../../../Components/SearchDomain'
import Project from "../../../Components/Project"
class EditProject extends Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedOption: {}
    };
  }

  handleChange = (selectedOption) => {
    if (selectedOption && selectedOption.value){
      this.setState({ selectedOption });
    }
  }

  render() {
    return(
      <CardBody>
        <Form>
          <Row>
            <Col md="12">
              <Form.Group>
              <SearchDomain handleChange={this.handleChange}/>
              </Form.Group>      
            </Col>
          </Row>
          {this.state.selectedOption.value ? (<Project id={this.state.selectedOption.value}></Project>): null}
        </Form>
      </CardBody>
    )
  }
}

export default EditProject;