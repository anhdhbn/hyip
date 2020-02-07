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
import AsyncSelect from 'react-select/async';

import domainService from '../../../../services/domains'

class EditProject extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  searchDomain(input){
    return new Promise((resolve, reject) => {
      if(!input) return reject("Empty")
      domainService.searchDomain(input).then(res => {
        if (!res.success) return reject(res)
        resolve(res.data)
      })
    })
  }

  render() {
    return (
      <CardBody>
        <Row>
          <Col md="12">
            <AsyncSelect cacheOptions defaultOptions loadOptions={this.searchDomain} />
          </Col>
        </Row>
      </CardBody>
    )
  }
}

export default EditProject;