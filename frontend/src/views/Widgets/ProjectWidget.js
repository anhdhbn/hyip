import React, { Component } from 'react';
import PropTypes from 'prop-types';
import {
  Button,
  ButtonGroup,
  ButtonToolbar,
  Card,
  CardBody,
  CardFooter,
  CardTitle,
  Col,
  Row,
} from "reactstrap";
import { Line } from 'react-chartjs-2';
import { parse } from 'url';
import { CustomTooltips } from '@coreui/coreui-plugin-chartjs-custom-tooltips';
import { getStyle, hexToRgba } from '@coreui/coreui/dist/js/coreui-utilities'

import projectServices from '../../services/projects'
import crawldataServices from '../../services/crawldata'

const brandPrimary = getStyle('--primary')
const brandSuccess = getStyle('--success')
// const brandInfo = getStyle('--info')
const brandWarning = getStyle('--warning')
const brandDanger = getStyle('--danger')

const propTypes = {
  id: PropTypes.string,
};

const defaultProps = {
  id: null,
};

const options = {
  tooltips: {
    enabled: false,
    custom: CustomTooltips,
    intersect: true,
    mode: 'index',
    position: 'nearest',
    callbacks: {
      labelColor: function(tooltipItem, chart) {
        return { backgroundColor: chart.data.datasets[tooltipItem.datasetIndex].borderColor }
      }
    }
  },
  maintainAspectRatio: false,
  legend: {
    display: false,
  },
  elements: {
    point: {
      radius: 3,
      hitRadius: 10,
      hoverRadius: 4,
      hoverBorderWidth: 3,
    },
  },
}


class ProjectWidget extends Component {
  constructor(props){
    super(props);
    this.getPaidData = this.getPaidData.bind(this)
    this.getGrowthRateData = this.getGrowthRateData.bind(this)
    this.fetchData = this.fetchData.bind(this)
    this.state = {
      dataProject: {},
      crawldata: {},
      drawData: {
        labels: [],
        total_investment: [],
        total_paid_out: [],
        total_member: [],
        alexa_rank: [],
      }
    }
  }

  componentDidMount() {
    projectServices.fetchInfoProject(this.props.id).then(res => {
      if (res.success) {
        this.setState({...this.state, dataProject: res.data})
        let domain = parse(this.state.dataProject.url).hostname
        this.setState({dataProject: {...this.state.dataProject, domain: domain}})
      }
    })
    this.fetchData()
  }

  fetchData(days='all') {
    this.setState({days: days})
    crawldataServices.fetchDataCrawledProject(this.props.id, this.props.days).then(res => {
      this.setState({...this.state, crawldata: res.data})

      let data = this.state.crawldata
      let dates = data.map(e => new Date(e.created_date))
      let labels = dates.map(e => `${e.getDate()}/${e.getMonth()+1}`)
      let total_investment = data.map(e => e.total_investment)
      let total_paid_out = data.map(e => e.total_paid_out)
      let total_member = data.map(e => e.total_member)
      let alexa_rank = data.map(e => e.alexa_rank)

      this.setState({drawData: {...this.state.drawData, labels: labels}})
      this.setState({drawData: {...this.state.drawData, total_investment: total_investment}})
      this.setState({drawData: {...this.state.drawData, total_paid_out: total_paid_out}})
      this.setState({drawData: {...this.state.drawData, total_member: total_member}})
      this.setState({drawData: {...this.state.drawData, alexa_rank: alexa_rank}})
    })
  }

  createDataForChart(labelName, data, color) {
    return {
      label: labelName,
      backgroundColor: hexToRgba(color, 10),
      borderColor: color,
      pointHoverBackgroundColor: '#fff',
      borderWidth: 2,
      // fill: false,
      // lineTension: 0.1,
      // borderCapStyle: 'butt',
      // borderDash: [],
      // borderDashOffset: 0.0,
      // borderJoinStyle: 'miter',
      // pointBorderColor: color,
      // pointBackgroundColor: '#fff',
      // pointBorderWidth: 1,
      // pointHoverRadius: 10,
      // pointHoverBackgroundColor: color,
      // pointHoverBorderColor: 'rgba(220,220,220,1)',
      // pointHoverBorderWidth: 2,
      // pointRadius: 3,
      // pointHitRadius: 10,
      data: data,
    }
  }

  getPaidData() {
    let d1 = this.state.drawData.total_investment
    let d2 = this.state.drawData.total_paid_out
    let profit = []
    for(let i=0; i< d1.length; i++){
      profit.push(d1[i] - d2[i])
    }

    return {
      labels: this.state.drawData.labels,
      datasets: [
        this.createDataForChart('Total investment', this.state.drawData.total_investment, brandPrimary),
        this.createDataForChart('Total paid out', this.state.drawData.total_paid_out, brandWarning),
        this.createDataForChart('Profit', profit, brandSuccess),
      ]
    }
  }

  getGrowthRateData(){
    let d1 = this.state.drawData.total_investment
    let d2 = this.state.drawData.total_paid_out
    let profit = []
    for(let i=0; i< d1.length; i++){
      profit.push(d1[i] - d2[i])
    }

    let  igr = []
    for(let i=1; i< profit.length; i++){
      if (profit[i]  === 0) {
        igr.push(0)
      } else {
        let item = (profit[i] - profit[i-1])/profit[i]
        igr.push(item)
      }
    }
    return {
      labels: this.state.drawData.labels.reverse().slice(1).reverse(),
      datasets: [
        this.createDataForChart('Income Growth Rate', igr, brandDanger),
      ]
    }
  }

  returnMember() {
    if (this.state.drawData.total_member[0] === -1) return null;
    else {
      return (
          <Col sm={12} md className="mb-sm-2 mb-0">
            <div className="text-value">{this.state.drawData.total_member.slice(-1)[0]}</div>
            <div className="text-uppercase text-muted small">Members</div>
          </Col>
      )
    }
  }

  render() {
    if (this.state.crawldata.length > 1) {
      return (
        <Card>
          {/* <CardHeader> </CardHeader> */}
          <CardBody>
            <Row>
              <Col sm="5">
                <CardTitle className="mb-0">{this.state.dataProject.domain}</CardTitle>
              </Col>

              <Col sm="7" className="d-none d-sm-inline-block">
                <ButtonToolbar className="float-right" aria-label="Toolbar with button groups">
                  <ButtonGroup className="mr-3" aria-label="First group">
                    <Button color="outline-secondary" onClick={() => this.fetchData('7')} active={this.state.days === '7'}>Day</Button>
                    <Button color="outline-secondary" onClick={() => this.fetchData('30')} active={this.state.days === '30'}>Month</Button>
                    <Button color="outline-secondary" onClick={() => this.fetchData('all')} active={this.state.days === 'all'}>All</Button>
                  </ButtonGroup>
                </ButtonToolbar>
              </Col>
            </Row>

            <Row style={{ marginTop: 10 + 'px' }}>
              <Col xs={12} sm={12} md={12} lg={6} xl={6}  >
                <div className="chart-wrapper">
                  <Line data={this.getPaidData()} options={options} />
                </div>
              </Col>

              <Col  xs={12} sm={12} md={12} lg={6} xl={6}>
                <div className="chart-wrapper">
                  <Line data={this.getGrowthRateData()} options={options} />
                </div>
              </Col>
            </Row>
          </CardBody>
          <CardFooter>
            <Row className="text-center brand-card-body">
              <Col sm={12} md className="mb-sm-2 mb-0">
                <div className="text-value">{this.state.drawData.total_investment.slice(-1)[0]}</div>
                <div className="text-uppercase text-muted small">Total Investment</div>
              </Col>

              <Col sm={12} md className="mb-sm-2 mb-0">
                <div className="text-value">{this.state.drawData.total_paid_out.slice(-1)[0]}</div>
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
      );
    } else {
      return null;
    }
  }
}

ProjectWidget.propTypes = propTypes;
ProjectWidget.defaultProps = defaultProps;

export default ProjectWidget;
