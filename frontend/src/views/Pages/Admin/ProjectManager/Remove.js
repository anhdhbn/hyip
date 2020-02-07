import React, { Component } from 'react';

import {
  Button,
  CardBody,
  CardHeader,
  Col,
  Row,
} from "reactstrap";

import Form from "react-bootstrap/Form";
import Card from "react-bootstrap/Card";

import projectServices from '../../../../services/projects'

import SearchDomain from '../../../Base/SearchDomain'

class RemoveProject extends Component {
  constructor(props) {
    super(props);
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

export default RemoveProject;