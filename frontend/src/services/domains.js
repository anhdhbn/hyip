import { requestServices } from './index';

const searchDomain = (input) => requestServices.customAxios.get(`domain/search?input=${input}`).then((res) => res.data);

export default {
  searchDomain
};