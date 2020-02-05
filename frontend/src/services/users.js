import { requestServices } from 'services';

const submitRegister = (param) => requestServices.customAxios.post('user/register', param).then((res) => res.data);
const submitLoginRequest = (param) => requestServices.customAxios.post('user/login', param).then((res) => res.data);
const submitLogoutRequest = () => requestServices.customAxios.post('user/logout').then((res) => res.data);

export default {
    submitRegister,
    submitLoginRequest,
    submitLogoutRequest
  };