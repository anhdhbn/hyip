
// @flow
import axios from 'axios';

export const BASE_API_URL = `${ 'http://backend/api/' || 'https://hyip-anhdh.herokuapp.com/api/'}`;

const customAxios = axios.create({
  baseURL: BASE_API_URL,
  withCredentials: true,
});

customAxios.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response) {
      const { data } = error.response;
      const serverMessage = data.message;
      const customCode = data.custom_code;
      console.log(serverMessage, customCode)
    }
    return Promise.reject(error);
  },
);

export default { customAxios };