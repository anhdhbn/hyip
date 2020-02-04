import { get, post } from "./base";

export const check_easy = (onSuccess, onFailure, url_is_checked) => {
  // http://14.188.197.152:5000/api/celery/check-easy?url=https://longinvest.biz/
  get(`celery/check-easy?url=${url_is_checked}`, onSuccess, onFailure);
};

export const create = (body, onSuccess, onFailure) => {
  post(`project/create`, body, onSuccess, onFailure);
};
