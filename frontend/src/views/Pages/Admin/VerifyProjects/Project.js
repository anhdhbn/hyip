import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { parse } from 'url';
import {
  Card,
  CardBody,
  CardHeader,
  Col,
  Button,
} from 'reactstrap';

import { AppSwitch } from '@coreui/react'
import Form from "react-bootstrap/Form";
import { toast } from 'react-toastify';
import projectService from "../../../../services/projects"
import celeryServices from "../../../../services/celery"

const propTypes = {
  id: PropTypes.string,
};

const defaultProps = {
  id: null,
};

class Project extends Component{
  constructor(props){
    super(props);
    this.handleUpdate = this.handleUpdate.bind(this)
    this.handleVerify = this.handleVerify.bind(this)
    this.checkSelenium = this.checkSelenium.bind(this)
    this.callApiFetchData = this.callApiFetchData.bind(this)
    this.state = {}
  }

  //   Object.keys(obj).forEach(k =>
  //     (obj[k] && typeof obj[k] === 'object') && removeEmptyOrNull(obj[k]) ||
  //     (!obj[k] && obj[k] !== undefined) && delete obj[k]
  //   );
  //   return obj;
  // };

  componentDidUpdate(prevProps, prevState){
    if (prevProps.id !== this.props.id){
      this.callApiFetchData(this.props.id)
    }
  }

  removeNulls(obj){
    var isArray = obj instanceof Array;
    for (var k in obj){
      if (obj[k]===null) isArray ? obj.splice(k,1) : delete obj[k];
      else if (typeof obj[k]=="object") this.removeNulls(obj[k]);
    }
  }

  componentDidMount(){
    this.callApiFetchData(this.props.id)
  }

  callApiFetchData(id){
    projectService.fetchInfoProject(id).then(res  =>  {
      this.removeNulls(res.data)
      this.setState({...res.data})

      let url = parse(res.data.url);
      this.setState({domain: url.hostname})
      if (url.hostname !== undefined) {
        celeryServices.checkEasy({url: res.data.url}).then(checkData => {
          this.setState({...checkData.data})
        })
      }
    })
  }

  handleUpdate(){
    projectService.updateSelectorProject(this.props.id, this.state).then(res => {
      if (res.success) {
        toast.success(`${this.state.domain} was updated`)
        this.props.funcRemoveItem(this.props.id)
      } else {
        toast.error(`${this.state.domain} have not updated`)
      }
    })
  }

  handleVerify(){
    projectService.makeProjectVerified(this.props.id, {}).then(res => {
      if (res.success) {
        toast.success(`${this.state.domain} was verified`)
        this.props.funcRemoveItem(this.props.id)
      } else {
        toast.error(`${this.state.domain} have not verified`)
      }
    })
  }

  checkSelenium(){
    const params = {
      url: this.state.url,
      investment_selector: this.state.investment_selector,
      paid_out_selector: this.state.paid_out_selector,
      member_selector: this.state.member_selector,
    }
    celeryServices.checkSelenium(params).then(res => {
      if (!res.success) {
        toast.error(`${this.state.domain} check selenium failed`)
        this.setState({...res.data})
      }
    })
  }

  showResultSelector(name, value) {
    if (value !== 0){
      return (
        <>
          <Form.Text className="text-muted">
            Test {name} selector: <span style={{color: "red"}}>{value}</span>
          </Form.Text>
          <br/>
        </>
      )
    }
  }


  render(){
    if(this.state.url){
      return (
        <Card>
          <CardHeader><a target="_blank" rel="noopener noreferrer" href={this.state.url}>{this.state.url}</a></CardHeader>
          <CardBody>
            <Col xs="12">
              <Form.Group controlId={`form_investment_selector_update_${this.props.index}`}>
                <Form.Label>Investment selector</Form.Label>
                <Form.Control
                  type="text"
                  value={this.state.investment_selector}
                  onChange={e => this.setState({investment_selector: e.target.value})}
                />
              </Form.Group>
              {this.showResultSelector("investment", this.state.total_investment)}
            </Col>
  
            <Col xs="12">
              <Form.Group controlId={`form_paid_out_selector_update_${this.props.index}`}>
                <Form.Label>Paid out selector</Form.Label>
                <Form.Control
                  type="text"
                  placeholder=""
                  value={this.state.paid_out_selector}
                  onChange={e => this.setState({paid_out_selector: e.target.value})}
                />
              </Form.Group>
              {this.showResultSelector("paid out", this.state.total_paid_out)}
            </Col>
  
            <Col xs="12">
              <Form.Group controlId={`form_member_selector_update_${this.props.index}`}>
                <Form.Label>Member selector</Form.Label>
                <Form.Control
                  type="text"
                  placeholder=""
                  value={this.state.member_selector}
                  onChange={e => this.setState({member_selector: e.target.value})}
                />
              </Form.Group>
              {this.showResultSelector("member", this.state.total_member)}
            </Col>
  
            <Col xs="12">
              <Form.Group controlId={`form_plans_update_${this.props.index}`}>
                <Form.Label>Plans</Form.Label>
                <Form.Control
                  type="text"
                  value={this.state.plans}
                  onChange={e => this.setState({plans: e.target.value})}
                />
              </Form.Group>
            </Col>
  
            <Col>
              <Form.Group controlId={`form_easy_update_${this.props.index}`}>
                <Form.Label>Is easy</Form.Label>
                <br/>
                <AppSwitch 
                  className={'mx-1'} 
                  variant={'3d'} 
                  color={'primary'} 
                  checked={this.state.easy_crawl || false}
                  onChange={e => this.setState({easy_crawl: e.target.value})}
                  />
              </Form.Group>
            </Col>
            
            <CardBody className="text-center">
              <Button color="warning" active tabIndex={-1} onClick={this.handleUpdate} className="mr-3" >Update</Button>
              <Button color="success" active tabIndex={-1} onClick={this.handleVerify} className="mr-3">Verify</Button>
              <Button color="primary" active tabIndex={-1} onClick={this.checkSelenium}>Check selenium</Button>
            </CardBody>
          </CardBody>
        </Card>
      )
    } else {
      return null
    }
    
  }
}


Project.propTypes = propTypes;
Project.defaultProps = defaultProps;

export default Project;
