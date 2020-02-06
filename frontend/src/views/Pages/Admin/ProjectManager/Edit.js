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

class EditProject extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <Card>
        <CardHeader>Edit project</CardHeader>
        <CardBody>

        </CardBody>
      </Card>
    )
  }
}

export default EditProject;