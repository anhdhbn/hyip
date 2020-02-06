import React from 'react';
import {
  Col,
  Row,
} from "reactstrap";

import CreateProject from "./Create"
import EditProject from "./Edit"
import RemoveProject from "./Remove"
import ProjectWidget from "../../../Widgets/ProjectWidget"

export default class Account extends React.Component {
  render() {
    return (
      <div className="animated fadeIn">
        <Row>
          <Col xs={12} sm={12} md={6} lg={6} xl={6}>
            <CreateProject></CreateProject>
          </Col>
          <Col xs={12} sm={12} md={6} lg={6} xl={6}>
            <EditProject></EditProject>
          </Col>
          <Col xs={12} sm={12} md={6} lg={6} xl={6}>
            <RemoveProject></RemoveProject>
          </Col>

          <Col xs={12} sm={12} md={12} lg={12} xl={12}>
            <ProjectWidget id="01b1edce-91a2-4d5b-9641-e32a0f4e94d5"></ProjectWidget>
          </Col>
        </Row>
      </div>
    )
  }
}