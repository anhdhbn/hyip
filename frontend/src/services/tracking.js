import { requestServices } from './index';

const fetchTrackingProject = (user_id) => requestServices.customAxios.get(`tracking/${user_id}`).then((res) => res.data);

const postProjectTracked = (params) => requestServices.customAxios.post(`tracking`, params).then((res) => res.data);
const deleteProjectTracked = (params) => requestServices.customAxios.post(`tracking`, params).then((res) => res.data);

export default {
    fetchTrackingProject,
    postProjectTracked,
    deleteProjectTracked
};