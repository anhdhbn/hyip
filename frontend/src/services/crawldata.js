import { requestServices } from './index';

const fetchDataCrawledProject = (id) => requestServices.customAxios.get(`crawldata/${id}`).then((res) => res.data);

export default {
  fetchDataCrawledProject
};