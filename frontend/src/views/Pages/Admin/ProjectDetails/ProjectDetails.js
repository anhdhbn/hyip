import React, { Component, lazy, Suspense } from 'react';
import {
  CardBody,
  Col,
  Row,
} from 'reactstrap';

import Form from "react-bootstrap/Form";
import { BatteryLoading } from 'react-loadingg';


import Project from "./Project"
import Chart from "./Chart"

const SearchDomain = lazy(() => import('../../../Components/SearchDomain'));

class ProjectDetails extends Component {
  constructor(props) {
    super(props);
    this.detailProject = this.detailProject.bind(this)
    this.state = {
      selectedOption:null,
    };
  }

  detailProject() {
    if (this.state.selectedOption){
      return (
        <Row>
          <Col xs={12} sm={12} md={12} lg={12} xl={12}>
            <Chart id={this.state.selectedOption.value}></Chart>
          </Col>
          <Col xs={12} sm={12} md={12} lg={12} xl={12}>
            <Project id={this.state.selectedOption.value}></Project>
          </Col>
        </Row>
      )
    } else {
      return null
    }
  }

  render() {

    return (
      <div className="animated fadeIn">
        <Row>
          <Suspense fallback={<BatteryLoading/>}>
            <CardBody>
              <Form>
                <Row>
                  <Col md="12">
                    <Form.Group>
                    <SearchDomain handleChange={selectedOption => this.setState({ selectedOption })}/>
                    </Form.Group>
                    
                  </Col>
                </Row>

                {this.detailProject()}
              </Form>
            </CardBody>
          </Suspense>
        </Row>
      </div>
    );
  }
}

export default ProjectDetails;
