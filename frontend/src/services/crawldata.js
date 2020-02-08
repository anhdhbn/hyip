import { requestServices } from './index';

const fetchDataCrawledProject = (id, limit) => requestServices.customAxios.get(`crawldata/${id}?limit=${limit}`).then((res) => res.data);

export default {
  fetchDataCrawledProject
};