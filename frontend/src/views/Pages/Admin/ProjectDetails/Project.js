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

const propTypes = {
  id: PropTypes.string,
};

const defaultProps = {
  id: null,
};

const greenText = {
  color: 'green',
  textAlign: 'center',
  fontWeight: 'bold'
};

const redText = {
  color: 'red',
  textAlign: 'center',
  fontWeight: 'bold'
};

const boldText = {
  fontWeight: 'bold'
}

class Project extends Component{
  constructor(props){
    super(props);
    this.state = {}
  }

  render(){
    return (
      <Card>
        <CardHeader>Info project</CardHeader>
        <CardBody>

          <Row>
            <Col xs={12} sm={4} md={4} lg={4} xl={4}>Plans</Col>
            <Col xs={12} sm={8} md={8} lg={8} xl={8}>1.00% - 1.50% daily for 10 days | 1.50% - 2.00% daily for 20 days | 2.00% - 2.50% daily for 30 days | 2.50% - 3.00% daily for 40 days | 3.00% - 4.00% daily for 180 days ahihi</Col>
          </Row>

          <Row>
            <Col xs={12} sm={4} md={4} lg={4} xl={4}><span style={greenText}>Domain</span></Col>
            <Col xs={12} sm={8} md={8} lg={8} xl={8}>From <span style={boldText}>{"01-01-1999"}</span> To <span style={boldText}>{"01-06-1999"}</span> <span style={greenText}>{356} days</span></Col>
          </Row>

          <Row>
            <Col xs={12} sm={4} md={4} lg={4} xl={4}><span style={greenText}>Ip address</span></Col>
            <Col xs={12} sm={8} md={8} lg={8} xl={8}>{30} host</Col>
          </Row>

          <Row>
            <Col xs={12} sm={4} md={4} lg={4} xl={4}><span style={greenText}>SSL</span></Col>
            <Col xs={12} sm={8} md={8} lg={8} xl={8}>From <span style={boldText}>{"01-01-1999"}</span> To <span style={boldText}>{"01-06-1999"}</span> {356} days</Col>
          </Row>

          <Row>
            <Col xs={12} sm={4} md={4} lg={4} xl={4}><span  style={greenText}>Script</span></Col>
            <Col xs={12} sm={8} md={8} lg={8} xl={8}> {'Gold Coders'} - <span style={greenText}>{'licensed'}</span></Col>
          </Row>
        </CardBody>
      </Card>
    )
  }
}


Project.propTypes = propTypes;
Project.defaultProps = defaultProps;

export default Project;
