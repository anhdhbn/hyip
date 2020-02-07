import React, { Component, lazy, Suspense, useState, useEffect  } from 'react';
import { Bar, Line } from 'react-chartjs-2';
import {
  Badge,
  Button,
  ButtonDropdown,
  ButtonGroup,
  ButtonToolbar,
  Card,
  CardBody,
  CardFooter,
  CardHeader,
  CardTitle,
  Col,
  Dropdown,
  DropdownItem,
  DropdownMenu,
  DropdownToggle,
  Progress,
  Row,
  Table,
} from 'reactstrap';
import { CustomTooltips } from '@coreui/coreui-plugin-chartjs-custom-tooltips';
import { getStyle, hexToRgba } from '@coreui/coreui/dist/js/coreui-utilities'
import { BatteryLoading } from 'react-loadingg';


const ProjectWidget = lazy(() => import('../../../Widgets/ProjectWidget'));



const DataComponent = ({ url, fallback, fallbackDelay }) => {
  const [data, setData] = useState(null);
  const [delayed, setDelayed] = useState(true);

  useEffect(() => {
    let unmounted = false;
    fetch(url)
      .then(res => res.json())
      .then(data => !unmounted && setData(data))
      .catch(console.error);
    return () => (unmounted = true);
  }, []);

  useEffect(() => {
    const timeout = setTimeout(() => setDelayed(false), fallbackDelay);
    return () => clearTimeout(timeout);
  }, []);

  return data ? <pre>JSON.stringify(data, null, 2)</pre> : !delayed && fallback
};

class Dashboard extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }
  render() {

    return (
      <div className="animated fadeIn">
        <Row>
          <Suspense fallback={<BatteryLoading/>}>
            <Col xs={12} sm={12} md={12} lg={12} xl={12}>
              <ProjectWidget id="01b1edce-91a2-4d5b-9641-e32a0f4e94d5"></ProjectWidget>
            </Col>
          </Suspense>


          <ClipLoader loading={true}></ClipLoader>
          <DataComponent url="http://domain/data" fallback={<p>Loading...</p>}></DataComponent>
          
        </Row>
      </div>
    );
  }
}

export default Dashboard;
