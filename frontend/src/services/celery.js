import { requestServices } from 'services';

// const params = {
// 	articleNumber: this.articleNumber,
// 	mode: 'bestseller',
// };

const checkEasy = (params) => requestServices.customAxios.get(`celery/check-easy`, { params }).then((res) => res.data);

export default {
    checkEasy
  };