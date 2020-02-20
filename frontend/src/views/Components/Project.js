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
import projectService from "../../services/projects"
import celeryServices from "../../services/celery"

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

  componentDidUpdate(prevProps, prevState){
    if (prevProps.id !== this.props.id){
      this.setState({total_investments: -2, total_paid_outs: -2, total_members: -2})
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
      toast.success(`${this.state.domain} was updated`)
      if (this.props.funcRemoveItem){
        this.props.funcRemoveItem(this.props.id, this.props.index)
      }
    }).catch((reason)=>{
      toast.error(`${this.state.domain} have not updated ${reason}`)
    })
  }

  handleVerify(){
    projectService.makeProjectVerified(this.props.id, {}).then(res => {
      toast.success(`${this.state.domain} was verified`)
      if (this.props.funcRemoveItem){
        this.props.funcRemoveItem(this.props.id, this.props.index)
      }
    }).catch((reason)=>{
      toast.error(`${this.state.domain} have not verified`)
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
      this.setState({...res.data})
      toast.success(`${this.state.domain} check selenium successful`)
    }).catch((reason)=> {
      toast.error(`${this.state.domain} check selenium failed: ${reason}`)
    })
  }

  showResultSelector(name, value) {
    if (value !== -2){
      return (
        <Form.Text className="text-muted mb-4">
          Test {name} selector: <span style={{color: "red"}}>{value}</span>
        </Form.Text>
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
              <Form.Group controlId={`form_investment_selector_${this.props.index}`}>
                <Form.Label>Investment selector</Form.Label>
                <Form.Control
                  type="text"
                  value={this.state.investment_selector}
                  onChange={e => this.setState({investment_selector: e.target.value})}
                />
                {this.showResultSelector("investment", this.state.total_investments)}
              </Form.Group>
              
            </Col>
  
            <Col xs="12">
              <Form.Group controlId={`form_paid_out_selector_${this.props.index}`}>
                <Form.Label>Paid out selector</Form.Label>
                <Form.Control
                  type="text"
                  placeholder=""
                  value={this.state.paid_out_selector}
                  onChange={e => this.setState({paid_out_selector: e.target.value})}
                />
              {this.showResultSelector("paid out", this.state.total_paid_outs)}
              </Form.Group>
            </Col>
  
            <Col xs="12">
              <Form.Group controlId={`form_member_selector_${this.props.index}`}>
                <Form.Label>Member selector</Form.Label>
                <Form.Control
                  type="text"
                  placeholder=""
                  value={this.state.member_selector}
                  onChange={e => this.setState({member_selector: e.target.value})}
                />
                {this.showResultSelector("member", this.state.total_members)}
              </Form.Group>
              
            </Col>
  
            <Col xs="12">
              <Form.Group controlId={`form_plans_${this.props.index}`}>
                <Form.Label>Plans</Form.Label>
                <Form.Control
                  type="text"
                  value={this.state.plans}
                  onChange={e => this.setState({plans: e.target.value})}
                />
              </Form.Group>
            </Col>
  
            <Col>
              <Form.Group controlId={`form_easy_${this.props.index}`}>
                <Form.Label>Is easy</Form.Label>
                <br/>
                <AppSwitch 
                  className={'mx-1'} 
                  variant={'3d'} 
                  color={'primary'} 
                  checked={this.state.easy_crawl || false}
                  onChange={e => this.setState({easy_crawl: !this.state.easy_crawl})}
                  />
              </Form.Group>
            </Col>

            <Col>
              <Form.Group controlId={`form_crawlable_${this.props.index}`}>
                <Form.Label>Crawlable</Form.Label>
                <br/>
                <AppSwitch 
                  className={'mx-1'} 
                  variant={'3d'} 
                  color={'primary'} 
                  checked={this.state.crawlable || false}
                  onChange={e => this.setState({crawlable: !this.state.crawlable})}
                  />
              </Form.Group>
            </Col>

            <Col>
              <Form.Group controlId={`form_currency_${this.props.index}`}>
                <Form.Label>Currency</Form.Label>
                <Form.Control as="select"
                  onChange={e => this.setState({type_currency: e.target.value})}
                  value={this.state.type_currency}>
                  <option value="">None</option>
                  <option value="USD">USD</option>
                  <option value="BTC">BTC</option>
                  <option value="RUP">RUP</option>
                </Form.Control>
              </Form.Group>
            </Col>
            
            <CardBody className="text-center">
              <Button color="warning" active tabIndex={-1} onClick={this.handleUpdate} className="mr-3" >Update</Button>
              <Button color="success" active tabIndex={-1} onClick={this.handleVerify} className="mr-3">Verify</Button>
              <Button color="primary" active tabIndex={-1} onClick={this.checkSelenium} className="mr-3">Check selenium</Button>
              {this.props.skip ? (<Button color="danger" active tabIndex={-1} onClick={e=> this.props.funcRemoveItem(this.props.id, this.props.index)}>Skip</Button>): null}
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