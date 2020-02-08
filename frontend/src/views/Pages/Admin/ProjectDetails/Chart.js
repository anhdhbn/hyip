import React, { Component } from 'react';
import PropTypes from 'prop-types';

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
    return (null)
  }
}


Chart.propTypes = propTypes;
Chart.defaultProps = defaultProps;

export default Chart;
