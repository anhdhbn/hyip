import React, { Component } from 'react';

import {
  Button,
  CardBody,
  CardHeader,
  Col,
  Row,
  Input
} from "reactstrap";

import Form from "react-bootstrap/Form";
import SearchDomain from '../../../Base/SearchDomain'

class EditProject extends Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this)
    this.state = {
      selectedOption: null,
    };
  }

  handleChange = (selectedOption) => {
    this.setState({ selectedOption });
    console.log(selectedOption)
  }

  render() {
    return (
      <CardBody>
        <Row>
          <Col md="12">
            <SearchDomain handleChange={this.handleChange}/>
          </Col>
        </Row>
      </CardBody>
    )
  }
}

export default EditProject;