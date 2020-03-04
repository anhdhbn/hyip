import React, { Component } from 'react';
import PropTypes from 'prop-types';
import {
  Card,
  CardBody,
  CardFooter,
  CardTitle,
  Col,
  Row,
  Button,
  ButtonGroup,
  ButtonToolbar,
} from "reactstrap";
import { Line } from 'react-chartjs-2';
import { parse } from 'url';
import dataWarehouse from "../../../utils/DataWarehouse"
import projectServices from '../../../services/projects'
import trackingService from "../../../services/tracking"
import { toast } from 'react-toastify';

const propTypes = {
  id: PropTypes.string,
};

const defaultProps = {
  id: null,
};

class ProjectWidget extends Component {
  constructor(props){
    super(props);
    this.fetchData = this.fetchData.bind(this)
    this.removeTracking = this.removeTracking.bind(this)
    this.state = {
      crawldata: {},
      drawData: {
        labels: [],
        total_investments: [],
        total_paid_outs: [],
        total_members: [],
        alexa_rank: [],
      },
      normalize: {
        labels: [],
        total_investments: [],
        total_paid_outs: [],
        total_members: [],
        alexa_rank: [],
      },
      normalizeData: false,
      dataProject: {},
      days: "all",
      tracked: true
    }
  }

  componentDidMount() {
    projectServices.fetchInfoProject(this.props.id).then(res => {
      if (res.success) {
        this.setState({...this.state, dataProject: res.data})
        let domain = parse(this.state.dataProject.url_crawl).hostname
        this.setState({dataProject: {...this.state.dataProject, domain: domain}})
      }
    })

    
    this.fetchData(this.props.id)
  }

  fetchData(id, days='all') {
    this.setState({days: days})
    dataWarehouse.preprocessFetchData(id, days).then(res=>{
      this.setState({drawData: res.drawData, crawldata: res.data, normalize: res.normalize})
    })
  }

  returnMember() {
    if (this.state.drawData.total_members[0] === -1) return null;
    else {
      return (
          <Col sm={12} md className="mb-sm-2 mb-0">
            <div className="text-value">{this.state.drawData.total_members.slice(-1)[0]}</div>
            <div className="text-uppercase text-muted small">Members</div>
          </Col>
      )
    }
  }

  removeTracking(){
    let project_id = this.props.id
    trackingService.deleteProjectTracked({project_id}).then(res => {
      toast.success(`${this.state.dataProject.domain} was untracked` )
      this.setState({tracked: false})
    })
  }

  render() {
    if (this.state.crawldata.length > 1 && this.state.tracked) {
      return (
        <Col xs={12} sm={12} md={12} lg={12} xl={6} >
          <Card>
            <CardBody>
              <Row>
                <Col sm="5">
                  <CardTitle className="mb-0">{this.state.dataProject.domain}</CardTitle>
                </Col>

                <Col sm="7" className="d-none d-sm-inline-block">
                  <ButtonToolbar className="float-right" aria-label="Toolbar with button groups">
                    <ButtonGroup className="mr-3" aria-label="First group">
                      <Button color="info"
                        className="mr-1"
                        onClick={e=> this.setState({normalizeData: !this.state.normalizeData})}
                      >{this.state.normalizeData ? "Unnormalize" : "Normalize"}</Button>
                      <Button 
                      color="danger"
                      onClick={this.removeTracking}>Remove tracking</Button>
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
                    {this.state.normalizeData ? 
                    (<Line data={dataWarehouse.getProfitData(this.state.normalize.total_investments,
                      this.state.normalize.total_paid_outs, this.state.normalize.labels)} options={dataWarehouse.optionsChart} />)
                       : (<Line data={dataWarehouse.getProfitData(this.state.drawData.total_investments,
                      this.state.drawData.total_paid_outs, this.state.drawData.labels)} options={dataWarehouse.optionsChart} />)}
                    
                  </div>
                </Col>

                <Col  xs={12} sm={12} md={12} lg={6} xl={6}>
                  <div className="chart-wrapper">
                    <Line data={dataWarehouse.getGrowthRateData(this.state.drawData.total_investments,
                      this.state.drawData.total_paid_outs, this.state.drawData.labels)} options={dataWarehouse.optionsChart} />
                  </div>
                </Col>
              </Row>
            </CardBody>
            <CardFooter>
              <Row className="text-center brand-card-body">
                <Col sm={12} md className="mb-sm-2 mb-0">
                  <div className="text-value">{this.state.drawData.total_investments.slice(-1)[0]}</div>
                  <div className="text-uppercase text-muted small">Total Investment</div>
                </Col>

                <Col sm={12} md className="mb-sm-2 mb-0">
                  <div className="text-value">{this.state.drawData.total_paid_outs.slice(-1)[0]}</div>
                  <div className="text-uppercase text-muted small">Total Paid Out</div>
                </Col>

                {this.returnMember()}

                <Col sm={12} md className="mb-sm-2 mb-0">
                  <div className="text-value">{this.state.drawData.alexa_rank.slice(-1)[0]}</div>
                  <div className="text-uppercase text-muted small">Alaxa rank</div>
                </Col>
              </Row>
            </CardFooter>
          </Card>
        </Col>
      );
    } else {
      return null;
    }
  }
}

ProjectWidget.propTypes = propTypes;
ProjectWidget.defaultProps = defaultProps;

export default ProjectWidget;