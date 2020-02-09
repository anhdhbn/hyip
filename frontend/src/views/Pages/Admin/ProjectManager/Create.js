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
class CreateProject extends Component {
  constructor(props) {
    super(props);
    this.handleBlurURL = this.handleBlurURL.bind(this);
    this.postForm = this.postForm.bind(this);
    this.state = {
      postData: {
        url: '',
        script_type: 0,
        investment_selector: '',
        paid_out_selector: '',
        member_selector: '',
        start_date: '',
        status_project: 0,
        plans: '',
      },
      checkData: {
        total_investment: 0,
        total_paid_out: 0,
        total_member: 0,
      }
    };
  }

  handleBlurURL(event) {
    let url = parse(this.state.postData.url);
    if (url.hostname != null) {
      celeryServices.checkEasy({url: this.state.postData.url}).then(checkData => {
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
      if (res.success) {
        toast.success(`${parse(this.state.postData.url).hostname} was create`)
      } else {
        toast.error(`${res}`)
      }
    })
  }

  render() {
    return (
      <CardBody>
        <Form>
          <Row>
            <Col xs="12" sm="8">
              <Form.Group controlId="form_url">
                <Form.Label>URL</Form.Label>
                <Form.Control
                  type="url"
                  name="url"
                  placeholder="Enter url"
                  onBlur={this.handleBlurURL}
                  onChange={e => this.setState({postData : {...this.state.postData, url: e.target.value}})}
                />
              </Form.Group>
            </Col>

            <Col xs="12" sm="4">
              <Form.Group controlId="form_script_type">
                <Form.Label>Script Type</Form.Label>
                <Form.Control as="select"
                  onChange={e => this.setState({postData : {...this.state.postData, script_type: e.target.value}})}
                  >
                  <option value="0">LICENSED</option>
                  <option value="1">UNKNOWN</option>
                  <option value="2">NOTLICENSED</option>
                </Form.Control>
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
              {this.showResultSelector("investment", this.state.checkData.total_investment)}
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
              {this.showResultSelector("paid out", this.state.checkData.total_paid_out)}
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
              {this.showResultSelector("member", this.state.checkData.total_member)}
              <br />
            </Col>

            <Col xs="12" sm="6">
              <Form.Group controlId="form_start_date">
                <Form.Label>Start date</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="yyyy-mm-dd"
                  onChange={e => this.setState({postData : {...this.state.postData, start_date: e.target.value}})}
                />
              </Form.Group>
            </Col>

            <Col xs="12" sm="6">
              <Form.Group controlId="form_status_project">
                <Form.Label>Status project</Form.Label>
                <Form.Control as="select"
                  onChange={e => this.setState({postData : {...this.state.postData, status_project: e.target.value}})}>
                  <option value="0">PAYING</option>
                  <option value="1">WAITING</option>
                  <option value="2">PROBLEM</option>
                  <option value="3">SCAM</option>
                </Form.Control>
              </Form.Group>
            </Col>

            <Col xs="12">
              <Form.Group controlId="form_plans">
                <Form.Label>Plans</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="1.0%-1.6% daily, 130%-240% after"
                  onChange={e => this.setState({postData : {...this.state.postData, plans: e.target.value}})}
                />
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