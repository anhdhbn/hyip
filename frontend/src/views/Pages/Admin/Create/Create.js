import React, { Component, lazy, Suspense } from "react";

import {
  Button,
  CardBody,
  CardHeader,
  Col,
  Row,
} from "reactstrap";

import * as createServices from "../../../../services/create";
import Form from "react-bootstrap/Form";
import Card from "react-bootstrap/Card";

class Create extends Component {
  constructor(props) {
    super(props);
    this.checkURL = this.checkURL.bind(this);
    this.handleChangeURL = this.handleChangeURL.bind(this);
    this.handleCheckURLSuccess = this.handleCheckURLSuccess.bind(this);
    this.handleChangeScriptType = this.handleChangeScriptType.bind(this);
    this.handleChangeInvestmentSelector = this.handleChangeInvestmentSelector.bind(
      this
    );
    this.handleChangePaidOutSelector = this.handleChangePaidOutSelector.bind(
      this
    );
    this.handleChangMememberSelector = this.handleChangMememberSelector.bind(
      this
    );
    this.handleChangeStartDate = this.handleChangeStartDate.bind(this);
    this.handleChangePlans = this.handleChangePlans.bind(this);
    this.handleChangeStatusProject = this.handleChangeStatusProject.bind(this);
    this.postForm = this.postForm.bind(this);
    this.handPostFormSuccess = this.handPostFormSuccess.bind(this);
    this.handPostFormFalure = this.handPostFormFalure.bind(this);
    this.clearResponseMessage = this.clearResponseMessage.bind(this);

    this.state = {
      //Request
      url: undefined,
      script_type: undefined,
      investment_selector:
        "#statistic > div > div > div:nth-child(2) > div > div.item.item3.aos-init.aos-animate > div.number > span",
      paid_out_selector:
        "#statistic > div > div > div:nth-child(2) > div > div.item.item4.aos-init.aos-animate > div.number > span",
      member_selector:
        "#statistic > div > div > div:nth-child(2) > div > div.item.item2.aos-init.aos-animate > div.number > span",
      total_investment: null,
      total_paid_out: null,
      total_member: null,
      start_date: undefined,
      plans: undefined,
      easy_crawl: false,
      status_project: undefined,
      //Validation
      //Responses
      response_errors: undefined,
      response_message: "Please click commit!"
    };
  }

  checkURL(url_is_checked) {
    createServices.check_easy(
      this.handleCheckURLSuccess,
      this.handleCheckURLFailure,
      url_is_checked
    );
  }

  handleCheckURLSuccess(res) {
    if ((res.total_investment !== null) & (res.total_paid_out !== null)) {
      this.setState({ easy_crawl: true });
    }
    this.setState({
      total_investment: res.total_investment,
      total_member: res.total_member,
      total_paid_out: res.total_paid_out
    });
  }

  handleCheckURLFailure(res) {
    console.log("Checked URL false");
  }

  handleChangeURL(event) {
    var url_is_checked = event.target.value;
    this.setState({ url: url_is_checked });
    this.checkURL(url_is_checked);
    this.clearResponseMessage();
  }

  handleChangeScriptType(event) {
    this.setState({ script_type: event.target.value });
    this.clearResponseMessage();
  }

  handleChangeInvestmentSelector(event) {
    this.setState({
      investment_selector: event.target.value
    });
    this.clearResponseMessage();
  }

  handleChangePaidOutSelector(event) {
    this.setState({ paid_out_selector: event.target.value });
    this.clearResponseMessage();
  }

  handleChangMememberSelector(event) {
    this.setState({ member_selector: event.target.value });
    this.clearResponseMessage();
  }

  handleChangeStartDate(event) {
    this.setState({ start_date: event.target.value });
    this.clearResponseMessage();
  }

  handleChangePlans(event) {
    this.setState({ plans: event.target.value });
    this.clearResponseMessage();
  }

  handleChangeStatusProject(event) {
    this.setState({ status_project: event.target.value });
    this.clearResponseMessage();
  }

  clearResponseMessage() {
    this.setState({ response_message: "Please click commit!" });
  }

  postForm() {
    var body = {
      url: this.state.url,
      investment_selector: this.state.investment_selector,
      paid_out_selector: this.state.paid_out_selector,
      member_selector: this.state.member_selector,
      start_date: this.state.start_date,
      plans: this.state.plans,
      easy_crawl: this.state.easy_crawl
    };
    createServices.create(
      body,
      this.handPostFormSuccess,
      this.handPostFormFalure
    );
  }

  handPostFormSuccess(res, body) {
    //   {
    //     "code": 200,
    //     "custom_code": "",
    //     "success": true,
    //     "message": "",
    //     "data": {
    //         "id": "751cbb1e-5f42-46b5-9793-e48bd9943d50"
    //     }
    //  }
    this.setState({ response_message: res.data.id });
  }

  handPostFormFalure(res) {
    console.log("Post form failure!!!", res);
    if (res.custom_code === "registed_before")
      this.setState({
        response_message: "Domain was exists"
      });
  }

  render() {
    return (
      <div>
        <Row>
          <Col>
            <Card>
              <CardHeader>Parameters</CardHeader>
              <CardBody>
                <Form>
                  <Form.Group controlId="form_url">
                    <Form.Label>URL</Form.Label>
                    <Form.Control
                      type="text"
                      name="url"
                      placeholder="Enter url"
                      onChange={this.handleChangeURL}
                    />
                    <Form.Text className="text-muted">
                      We'll never share your email with anyone else.
                    </Form.Text>
                  </Form.Group>

                  <Form.Group controlId="form_script_type">
                    <Form.Label>Script type</Form.Label>
                    <Form.Control
                      type="text"
                      placeholder="interger"
                      onChange={this.handleChangeScriptType}
                    />
                  </Form.Group>

                  <Form.Group controlId="form_investment_selector">
                    <Form.Label>Investment selector</Form.Label>
                    <Form.Control
                      type="text"
                      placeholder=""
                      value={this.state.investment_selector}
                      onChange={this.handleChangeInvestmentSelector}
                    />
                  </Form.Group>

                  <Form.Group controlId="form_paid_out_selector">
                    <Form.Label>Paid out selector</Form.Label>
                    <Form.Control
                      type="text"
                      placeholder=""
                      value={this.state.paid_out_selector}
                      onChange={this.handleChangePaidOutSelector}
                    />
                  </Form.Group>

                  <Form.Group controlId="form_member_selector">
                    <Form.Label>Member selector</Form.Label>
                    <Form.Control
                      type="text"
                      placeholder=""
                      value={this.state.member_selector}
                      onChange={this.handleChangMememberSelector}
                    />
                  </Form.Group>

                  <Form.Group controlId="form_start_date">
                    <Form.Label>Start date</Form.Label>
                    <Form.Control
                      type="text"
                      placeholder="2018-07-12"
                      onChange={this.handleChangeStartDate}
                    />
                  </Form.Group>

                  <Form.Group controlId="form_plans">
                    <Form.Label>Form plans</Form.Label>
                    <Form.Control
                      type="text"
                      placeholder="1.0%-1.6% daily, 130%-240% after"
                      onChange={this.handleChangePlans}
                    />
                  </Form.Group>

                  <Form.Group controlId="form_status_project">
                    <Form.Label>Form status project</Form.Label>
                    <Form.Control
                      type="text"
                      placeholder="interger"
                      onChange={this.handleChangeStatusProject}
                    />
                  </Form.Group>

                  <Button
                    variant="primary"
                    type="button"
                    className="btn btn-primary"
                    onClick={this.postForm}
                  >
                    Submit
                  </Button>
                </Form>
              </CardBody>
            </Card>
          </Col>
        </Row>

        <Card>
          <Card.Header>Responses</Card.Header>
          <Card.Body>{this.state.response_message}</Card.Body>
        </Card>
      </div>
    );
  }
}

export default Create;
