import React, { Component } from 'react';

import {
  Button,
  CardBody,
  Col,
  Row,
} from "reactstrap";

import Form from "react-bootstrap/Form";
import { toast } from 'react-toastify';
import { AppSwitch } from '@coreui/react'

import SearchDomain from '../../../Components/SearchDomain'
import projectService from "../../../../services/projects"

class EditProject extends Component {
  constructor(props) {
    super(props);
    this.handleUpdate = this.handleUpdate.bind(this)
    this.handleVerify = this.handleVerify.bind(this)
    this.state = {
      selectedOption: {},
      postData: {}
    };
  }

  handleUpdate(){
    if (this.state.selectedOption && this.state.selectedOption.value){
      projectService.updateSelectorProject(this.state.selectedOption.value, this.state.postData).then(res => {
        if (res.success) {
          toast.success(`${this.state.selectedOption.label} was updated`)
          this.setState({selectedOption: {}})
        } else {
          toast.error(`${this.state.selectedOption.label} have not updated`)
        }
      })
    }
  }

  handleVerify(){
    if (this.state.selectedOption && this.state.selectedOption.value){
      projectService.makeProjectVerified(this.state.selectedOption.value, {}).then(res => {
        if (res.success) {
          toast.success(`${this.state.selectedOption.label} was verified`)
          this.setState({selectedOption: {}})
        } else {
          toast.error(`${this.state.selectedOption.label} have not verified`)
        }
      })
    }
  }

  handleChange = (selectedOption) => {
    if (selectedOption && selectedOption.value){
      this.setState({ selectedOption });
      projectService.fetchInfoProject(selectedOption.value).then(res  =>  {
        this.setState({postData: res.data})
      })
    } else {
      this.setState({ postData:  {} });
    }
  }

  form(){
    if (this.state.postData  && this.state.postData.plans){
      return (
        <>
        <Col xs="12">
          <Form.Group controlId="form_investment_selector_update">
            <Form.Label>Investment selector</Form.Label>
            <Form.Control
              type="text"
              placeholder=""
              value={this.state.investment_selector}
              onChange={e => this.setState({postData : {...this.state.postData, investment_selector: e.target.value}})}
            />
          </Form.Group>
        </Col>

        <Col xs="12">
          <Form.Group controlId="form_paid_out_selector_update">
            <Form.Label>Paid out selector</Form.Label>
            <Form.Control
              type="text"
              placeholder=""
              value={this.state.paid_out_selector}
              onChange={e => this.setState({postData : {...this.state.postData, paid_out_selector: e.target.value}})}
            />
          </Form.Group>
        </Col>

        <Col xs="12">
          <Form.Group controlId="form_member_selector_update">
            <Form.Label>Member selector</Form.Label>
            <Form.Control
              type="text"
              placeholder=""
              value={this.state.member_selector}
              onChange={e => this.setState({postData : {...this.state.postData, member_selector: e.target.value}})}
            />
          </Form.Group>
        </Col>

        <Col xs="12">
          <Form.Group controlId="form_plans_update">
            <Form.Label>Plans</Form.Label>
            <Form.Control
              type="text"
              value={this.state.postData.plans}
              onChange={e => this.setState({postData : {...this.state.postData, plans: e.target.value}})}
            />
          </Form.Group>
        </Col>

        <Col>
          <Form.Group controlId="form_easy_update">
            <Form.Label>Is easy</Form.Label>
            <br/>
            <AppSwitch 
              className={'mx-1'} 
              variant={'3d'} 
              color={'primary'} 
              checked={this.state.postData.easy_crawl || false}
              onChange={e => this.setState({postData : {...this.state.postData, easy_crawl: !this.state.postData.easy_crawl}})}
              />
          </Form.Group>

          <Form.Group controlId="form_crawlable_update">
            <Form.Label>Crawlable</Form.Label>
            <br/>
            <AppSwitch 
              className={'mx-1'} 
              variant={'3d'} 
              color={'primary'} 
              checked={this.state.postData.crawlable || false}
              onChange={e => this.setState({postData : {...this.state.postData, crawlable: !this.state.postData.crawlable}})}
              />
          </Form.Group>
        </Col>
        
        <Row>
          <CardBody className="text-center">
            <Button color="warning" active tabIndex={-1} onClick={this.handleUpdate} className="mr-3" >Update</Button>
            <Button color="success" active tabIndex={-1} onClick={this.handleVerify}>Verify</Button>
          </CardBody>
        </Row>
      </>
      )
    } else {
      return null
    }
  }

  render() {
    return(
      <CardBody>
        <Form>
          <Row>
            <Col md="12">
              <Form.Group>
              <SearchDomain handleChange={this.handleChange}/>

              {/* className="text-muted" */}
              <br/>
              <Form.Text >
                <a target="_blank" rel="noopener noreferrer" href={this.state.postData.url}>{this.state.postData.url}</a>
              </Form.Text>

              </Form.Group>
              
            </Col>
          </Row>

          {this.form()}
        </Form>
      </CardBody>
    )
  }
}

export default EditProject;