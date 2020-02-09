import { requestServices } from './index';

const checkEasy = (params) => requestServices.customAxios.get(`celery/check-easy`, { params }).then((res) => res.data);
const checkSelenium = (params) => requestServices.customAxios.get(`celery/check-diff`, { params }).then((res) => res.data);

export default {
  checkEasy,
  checkSelenium
};