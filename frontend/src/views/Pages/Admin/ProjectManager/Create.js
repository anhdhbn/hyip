import React, { Component } from 'react';
import { parse } from 'url';
// import {createSession} from "net-ping";

import {
  Button,
  CardBody,
  Col,
  Row,
} from "reactstrap";

import Form from "react-bootstrap/Form";

import projectServices from '../../../../services/projects'
import celeryServices from '../../../../services/celery'
import { toast } from 'react-toastify';
import { AppSwitch } from '@coreui/react'

class CreateProject extends Component {
  constructor(props) {
    super(props);
    this.handleBlurURL = this.handleBlurURL.bind(this);
    this.postForm = this.postForm.bind(this);
    this.state = {
      postData: {
        url_crawl: '',
        investment_selector: '',
        paid_out_selector: '',
        member_selector: '',
        easy_crawl: false,
        crawlable: false,
        tracked: false,
        type_currency: '',
      },
      checkData: {
        total_investments: 0,
        total_paid_outs: 0,
        total_members: 0,
      }
    };
  }

  handleBlurURL(event) {
    let url = parse(this.state.postData.url_crawl);
    if (url.hostname != null) {
      celeryServices.checkEasy({url: this.state.postData.url_crawl}).then(checkData => {
        this.setState({checkData: checkData.data})
      })
    }
  }

  showResultSelector(name, value) {
    if (value !== 0){
      return (
        <Form.Text className="text-muted">
          Test {name} selector: <span style={{color: "red"}}>{value}</span>
        </Form.Text>
      )
    }
  }

  postForm() {
    const {postData} = this.state
    projectServices.createProject(postData).then((res) => {
      toast.success(`${parse(this.state.postData.url_crawl).hostname} was created`)
    })
  }

  render() {
    return (
      <CardBody>
        <Form>
          <Row>
            <Col xs="12" >
              <Form.Group controlId="form_url">
                <Form.Label>URL</Form.Label>
                <Form.Control
                  type="url"
                  name="url"
                  placeholder="Enter url"
                  onBlur={this.handleBlurURL}
                  onChange={e => this.setState({postData : {...this.state.postData, url_crawl: e.target.value}})}
                />
              </Form.Group>
            </Col>

            <Col xs="12">
              <Form.Group controlId="form_investment_selector">
                <Form.Label>Investment selector</Form.Label>
                <Form.Control
                  type="text"
                  placeholder=""
                  value={this.state.investment_selector}
                  onChange={e => this.setState({postData : {...this.state.postData, investment_selector: e.target.value}})}
                />
              </Form.Group>
              {this.showResultSelector("investment", this.state.checkData.total_investments)}
              <br />
            </Col>

            <Col xs="12">
              <Form.Group controlId="form_paid_out_selector">
                <Form.Label>Paid out selector</Form.Label>
                <Form.Control
                  type="text"
                  placeholder=""
                  value={this.state.paid_out_selector}
                  onChange={e => this.setState({postData : {...this.state.postData, paid_out_selector: e.target.value}})}
                />
              </Form.Group>
              {this.showResultSelector("paid out", this.state.checkData.total_paid_outs)}
              <br />
            </Col>

            <Col xs="12">
              <Form.Group controlId="form_member_selector">
                <Form.Label>Member selector</Form.Label>
                <Form.Control
                  type="text"
                  placeholder=""
                  value={this.state.member_selector}
                  onChange={e => this.setState({postData : {...this.state.postData, member_selector: e.target.value}})}
                />
              </Form.Group>
              {this.showResultSelector("member", this.state.checkData.total_members)}
              <br />
            </Col>

            <Col>
              <Form.Group controlId={`form_easy`}>
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
            </Col>

            <Col>
              <Form.Group controlId={`form_crawlable`}>
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

            <Col>
              <Form.Group controlId={`form_currency`}>
                <Form.Label>Currency</Form.Label>
                <Form.Control as="select"
                  onChange={e => this.setState({postData : {...this.state.postData, type_currency: e.target.value}})}
                  value={this.state.postData.type_currency}>
                  <option value="">None</option>
                  <option value="USD">USD</option>
                  <option value="BTC">BTC</option>
                  <option value="RUP">RUP</option>
                </Form.Control>
              </Form.Group>
            </Col>

          </Row>
          <Button 
            block 
            color="primary"
            onClick={this.postForm}
          >Submit</Button>
        </Form>
      </CardBody>
    )
  }
}

export default CreateProject;