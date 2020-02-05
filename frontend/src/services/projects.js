import { requestServices } from 'services';

const fetchEasyProjects = () => requestServices.customAxios.get('project?type=easy').then((res) => res.data);
const fetchAllProjects = () => requestServices.customAxios.get('project?type=all').then((res) => res.data);
const fetchNotScamProjects = () => requestServices.customAxios.get('project?type=notscam').then((res) => res.data);
const fetchVerifiedProjects = () => requestServices.customAxios.get('project?type=verified').then((res) => res.data);
const fetchUnVerifiedProjects = () => requestServices.customAxios.get('project?type=unverified').then((res) => res.data);
const fetchInfoProject = (id) => requestServices.customAxios.get(`project/${id}`).then((res) => res.data);


const createProject = (param) => requestServices.customAxios.post('projects/create', param).then((res) => res.data);
const removeProject = (id, param) => requestServices.customAxios.post(`projects/remove/${id}`, param).then((res) => res.data);
const makeProjectVerified = (id, param) => requestServices.customAxios.post(`projects/verified/${id}`, param).then((res) => res.data);

export default {
    fetchEasyProjects,
    fetchAllProjects,
    fetchNotScamProjects,
    fetchVerifiedProjects,
    fetchUnVerifiedProjects,
    fetchInfoProject,
    createProject,
    removeProject,
    makeProjectVerified
  };