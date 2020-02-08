import React, { Component, lazy, Suspense } from 'react';
import { Bar, Line } from 'react-chartjs-2';
import {
  CardBody,
  CardFooter,
  CardHeader,
  CardTitle,
  Col,
  Row,
} from 'reactstrap';

import Form from "react-bootstrap/Form";
import { BatteryLoading } from 'react-loadingg';

import SearchDomain from '../../../Base/SearchDomain'
import Project from "./Project"

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
          <Col xs={12} sm={12} md={12} lg={12} xl={6}>
           Bieu do
          </Col>
          <Col xs={12} sm={12} md={12} lg={12} xl={6}>
            {/* day la Project
            gom hosting, is_verified, create_date, start_date, script_type(script)  */}
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
