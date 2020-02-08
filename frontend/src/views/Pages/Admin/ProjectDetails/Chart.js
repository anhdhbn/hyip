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

class Chart extends Component{
  constructor(props){
    super(props);
    this.state = {
    }
  }

  render(){
    return (
      <Card>
        <CardHeader>Verify</CardHeader>
      </Card>
    )
  }
}


Chart.propTypes = propTypes;
Chart.defaultProps = defaultProps;

export default Chart;
