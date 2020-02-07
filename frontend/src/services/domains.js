import { requestServices } from './index';

const searchDomain = (input) => requestServices.customAxios.get(`domain?input=${input}`).then((res) => res.data);

export default {
  searchDomain
};