import React from 'react';
import {
  Col,
  Row,
  Nav, 
  NavItem, 
  NavLink,
  TabContent, 
  TabPane
} from "reactstrap";

import CreateProject from "./Create"
import EditProject from "./Edit"
import RemoveProject from "./Remove"

export default class Account extends React.Component {
  constructor(props) {
    super(props);
    this.toggle = this.toggle.bind(this);
    this.state = {
      activeTab: new Array(4).fill('1'),
    };
  }

  toggle(tabPane, tab) {
    const newArray = this.state.activeTab.slice()
    newArray[tabPane] = tab
    this.setState({
      activeTab: newArray,
    });
  }

  tabPane() {
    return (
      <>
        <TabPane tabId="1">
          <CreateProject></CreateProject>
        </TabPane>
        <TabPane tabId="2">
          <EditProject></EditProject>
        </TabPane>
        <TabPane tabId="3">
          <RemoveProject></RemoveProject>
        </TabPane>
      </>
    );
  }
  render() {
    return (
      <div className="animated fadeIn">
        <Row>
        <Col xs={12} sm={12} md={12} lg={12} xl={12} className="mb-4">
            <Nav tabs>
              <NavItem>
                <NavLink
                  active={this.state.activeTab[0] === '1'}
                  onClick={() => { this.toggle(0, '1'); }}
                >
                  Create Project
                </NavLink>
              </NavItem>
              <NavItem>
                <NavLink
                  active={this.state.activeTab[0] === '2'}
                  onClick={() => { this.toggle(0, '2'); }}
                >
                  Edit Project
                </NavLink>
              </NavItem>
              <NavItem>
                <NavLink
                  active={this.state.activeTab[0] === '3'}
                  onClick={() => { this.toggle(0, '3'); }}
                >
                  Remove Project
                </NavLink>
              </NavItem>
            </Nav>
            <TabContent activeTab={this.state.activeTab[0]}>
              {this.tabPane()}
            </TabContent>
          </Col>

          {/* <Col xs={12} sm={12} md={6} lg={6} xl={6}>
            <CreateProject></CreateProject>
          </Col>
          <Col xs={12} sm={12} md={6} lg={6} xl={6}>
            <EditProject></EditProject>
          </Col>
          <Col xs={12} sm={12} md={6} lg={6} xl={6}>
            <RemoveProject></RemoveProject>
          </Col> */}
        </Row>
      </div>
    )
  }
}