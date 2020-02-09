import React, { Component } from 'react';
import PropTypes from 'prop-types';
import {
  Card,
  CardBody,
  CardHeader,
  CardTitle,
  Col,
  Row,
  Button,
  ButtonGroup,
  ButtonToolbar,
} from 'reactstrap';
import { Line } from 'react-chartjs-2';
import { parse } from 'url';
import projectServices from '../../../../services/projects'
import dataWarehouse from "../../../../utils/DataWarehouse"

const propTypes = {
  id: PropTypes.string,
};

const defaultProps = {
  id: null,
};

class Chart extends Component{
  constructor(props){
    super(props);
    this.init = this.init.bind(this)
    this.state = {
      days: 'all',
      dataProject: {},
    }
  }
  
  componentDidMount(){
    this.init()
  }

  componentDidUpdate(prevProps, prevState){
    if (prevProps.id !== this.props.id){
      this.init()
    }
  }

  init(){
    projectServices.fetchInfoProject(this.props.id).then(res => {
      if (res.success) {
        this.setState({...this.state, dataProject: res.data})
        let domain = parse(this.state.dataProject.url).hostname
        this.setState({dataProject: {...this.state.dataProject, domain: domain}})
      }
    })

    this.fetchData(this.props.id, this.state.days)
  }

  fetchData(id, days='all') {
    this.setState({days: days})
    dataWarehouse.preprocessFetchData(id, this.state.days).then(res=>{
      this.setState({drawData: res.drawData})
    })
  }

  render(){
    if (this.state.drawData && this.state.drawData.total_investments && this.state.drawData.total_investments.length > 1){
      return (
        <Card>
          <CardHeader>Charts</CardHeader>
          <CardBody>
            {/* <InvestChartWidget id={this.props.id}/> */}
            <Row>
              <Col sm="5">
                <CardTitle className="mb-0"><a target="_blank" rel="noopener noreferrer" href={this.state.dataProject.url}>{this.state.dataProject.url}</a></CardTitle>
              </Col>
  
              <Col sm="7" className="d-none d-sm-inline-block">
                <ButtonToolbar className="float-right" aria-label="Toolbar with button groups">
                  <ButtonGroup className="mr-3" aria-label="First group">
                    <Button color="outline-secondary" onClick={() => this.fetchData(this.props.id, '7')} active={this.state.days === '7'}>Week</Button>
                    <Button color="outline-secondary" onClick={() => this.fetchData(this.props.id, '30')} active={this.state.days === '30'}>Month</Button>
                    <Button color="outline-secondary" onClick={() => this.fetchData(this.props.id, 'all')} active={this.state.days === 'all'}>All</Button>
                  </ButtonGroup>
                </ButtonToolbar>
              </Col>
            </Row>
  
            <Row style={{ marginTop: 10 + 'px' }}>
              <Col xs={12} sm={12} md={12} lg={6} xl={6}  >
                <div className="chart-wrapper">
                  <Line data={dataWarehouse.getProfitData(this.state.drawData.total_investments,
                    this.state.drawData.total_paid_outs, this.state.drawData.labels)} options={dataWarehouse.optionsChart} />
                </div>
              </Col>
  
              <Col  xs={12} sm={12} md={12} lg={6} xl={6}>
                <div className="chart-wrapper">
                  <Line data={dataWarehouse.getGrowthRateData(this.state.drawData.total_investments,
                    this.state.drawData.total_paid_outs, this.state.drawData.labels)} options={dataWarehouse.optionsChart} />
                </div>
              </Col>

              {this.state.drawData.total_members[0] === -1 ? null : (
                <Col  xs={12} sm={12} md={12} lg={6} xl={6}>
                  <div className="chart-wrapper">
                    <Line data={dataWarehouse.createSingleData(this.state.drawData.labels, "Members",
                    this.state.drawData.total_members)} options={dataWarehouse.optionsChart} />
                  </div>
                </Col>
              )}

                <Col  xs={12} sm={12} md={12} lg={6} xl={6}>
                  <div className="chart-wrapper">
                    <Line data={dataWarehouse.createSingleData(this.state.drawData.labels, "Alexa rank",
                    this.state.drawData.alexa_rank)} options={dataWarehouse.optionsChart} />
                  </div>
                </Col>

            </Row>
          </CardBody>
        </Card>
      )
    } else {
      return null
    }
    
  }
}


Chart.propTypes = propTypes;
Chart.defaultProps = defaultProps;

export default Chart;
