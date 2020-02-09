import React, { Component } from 'react';
import PropTypes from 'prop-types';
import {
  Card,
  CardBody,
  CardHeader,
  Col,
  Row,
  Button,
  ButtonToolbar,
  ButtonGroup
} from 'reactstrap';

import { toast } from 'react-toastify';

import projectService from "../../../../services/projects"
import trackingService from "../../../../services/tracking"

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

class SpanBold extends Component{
  constructor(props){
    super(props);
  }

  render(){
    return(<span style={this.props.red ? redText: this.props.green ? greenText : boldText}>{this.props.spaced ? " " : ""}{this.props.data}{this.props.spacedb ? " " : ""}</span>)
  }
}

class Project extends Component{
  constructor(props){
    super(props);
    this.callApiGetData = this.callApiGetData.bind(this)
    this.trackThisProject = this.trackThisProject.bind(this)
    this.state = {
      domain: {},
      ssl: {},
      ip: {},
      easy_crawl: false,
      tracked: false
    }
  }

  callApiGetData(id){
    projectService.fetchDetailsProject(id).then(res => {
      if (res.success) {
        // this.setState({data: res.data})
        let {hosting, plans, created_at, start_date, easy_crawl, domain, ssl, ip} = res.data
        this.setState({hosting, plans, created_at, start_date, easy_crawl})
        if (domain.from_date && domain.to_date){
          domain.from_date = new Date(domain.from_date.replace("-", "/"))
          domain.to_date = new Date(domain.to_date.replace("-", "/"))
          domain.days = (domain.to_date - domain.from_date)/(24*60*60*1000)
          domain.from_date = domain.from_date.toISOString().slice(0,10)
          domain.to_date = domain.to_date.toISOString().slice(0,10)
        }

        if(ip.domains_of_this_ip){
          ip.length = ip.domains_of_this_ip.split(",").length
          ip.is_green = (ip.length === 1) && !ip.domains_of_this_ip.includes("API count exceeded")
        }

        if (ssl.from_date && ssl.to_date){
          ssl.from_date = new Date(ssl.from_date.replace("-", "/"))
          ssl.to_date = new Date(ssl.to_date.replace("-", "/"))
          ssl.days = (ssl.to_date - ssl.from_date)/(24*60*60*1000)
          ssl.from_date = ssl.from_date.toISOString().slice(0,10)
          ssl.to_date = ssl.to_date.toISOString().slice(0,10)
        }
        this.setState({domain, ip, ssl})
      }
    })

    let user_id = localStorage.user_id
    let project_id = this.props.id
    trackingService.postCheckTracked({user_id, project_id}).then(res =>{
      this.setState({tracked: res.data.tracked})
    })
  }

  componentDidMount(){
    this.callApiGetData(this.props.id)
  }

  componentDidUpdate(prevProps, prevState){
    if (prevProps.id !== this.props.id){
      this.callApiGetData(this.props.id)
    }
  }

  trackThisProject(){
    let user_id = localStorage.user_id
    let project_id = this.props.id
    if(this.state.tracked === false){
      trackingService.postProjectTracked({user_id, project_id}).then(res => {
        toast.success(`${this.state.domain.address} was tracked` )
      })
    } else {
      trackingService.deleteProjectTracked({user_id, project_id}).then(res => {
        toast.success(`${this.state.domain.address} was removed tracked` )
      })
    }
  }

  render(){
    if (this.state.domain){
      return(
        <Card>
          
          <CardHeader>
            <Row>
              <Col sm="5">Info project</Col>
              <Col sm="7" className="d-none d-sm-inline-block">
                <ButtonToolbar className="float-right" aria-label="Toolbar with button groups">
                  <ButtonGroup className="mr-3" aria-label="First group">
                    <Button 
                      color={this.state.tracked ? "success" : "danger"} 
                      onClick={this.trackThisProject}>{this.state.tracked ? "Track this project" : "Remove tracking"}</Button>
                  </ButtonGroup>
                </ButtonToolbar>
              </Col>
            </Row>
          </CardHeader>
          <CardBody>

            <Row>
              <Col xs={12} sm={3} md={3} lg={3} xl={3}>Plans</Col>
              <Col xs={12} sm={9} md={9} lg={9} xl={9}>{this.state.plans}</Col>
            </Row>

            <Row>
              <Col xs={12} sm={3} md={3} lg={3} xl={3}><SpanBold data={"Domain"} green={this.state.domain.days > 365}/></Col>
              <Col xs={12} sm={9} md={9} lg={9} xl={9}>From
                <SpanBold spaced data={this.state.domain.from_date}/> To
                <SpanBold spaced data={this.state.domain.to_date}/> 
                <SpanBold spaced spacedb green={this.state.domain.days > 365} data={this.state.domain.days}/>days
                {this.state.domain.days > 365 ? (<SpanBold spaced green data={`${Math.floor(this.state.domain.days/365)} years`}/>): null}
                </Col>
            </Row>

            <Row>
              <Col xs={12} sm={3} md={3} lg={3} xl={3}>
                <SpanBold green={this.state.ip.is_green} data={"Ip address"}/>
              </Col>
              <Col xs={12} sm={9} md={9} lg={9} xl={9}>{this.state.ip.address} hosted <span style={boldText}>{this.state.ip.length}</span> domain</Col>
            </Row>

            <Row>
              <Col xs={12} sm={3} md={3} lg={3} xl={3}>
                  <SpanBold data={"SSL"} green={this.state.ssl.ev}/>
                </Col>
              <Col xs={12} sm={9} md={9} lg={9} xl={9}>From
                <SpanBold spaced data={this.state.ssl.from_date}/> To
                <SpanBold spaced data={this.state.ssl.to_date}/> 
                <SpanBold spaced spacedb green={this.state.ssl.days > 365} data={this.state.ssl.days}/>days</Col>
            </Row>
            {this.state.start_date ? (<Row>
              <Col xs={12} sm={3} md={3} lg={3} xl={3}><SpanBold data={"Start date"}/></Col>
              <Col xs={12} sm={9} md={9} lg={9} xl={9}>{this.state.start_date}</Col>
            </Row>): null}
            <Row>
              <Col xs={12} sm={3} md={3} lg={3} xl={3}><SpanBold data={"Hosting"}/></Col>
              <Col xs={12} sm={9} md={9} lg={9} xl={9}>{this.state.hosting}</Col>
            </Row>
            <Row>
              <Col xs={12} sm={3} md={3} lg={3} xl={3}><SpanBold data={"Easy crawl"}/></Col>
              <Col xs={12} sm={9} md={9} lg={9} xl={9}><SpanBold green={this.state.easy_crawl} red={!this.state.easy_crawl} data={this.state.easy_crawl.toString()}/></Col>
            </Row>
            {/* <Row>
              <Col xs={12} sm={3} md={3} lg={3} xl={3}><span  style={greenText}>Script</span></Col>
              <Col xs={12} sm={9} md={9} lg={9} xl={9}> </Col>
            </Row> */}
          </CardBody>
        </Card>
      )
    }
    else {
      return null
    }
  }
}


Project.propTypes = propTypes;
Project.defaultProps = defaultProps;

export default Project;
