import { requestServices } from './index';

const fetchEasyProjects = () => requestServices.customAxios.get('projects?type=easy').then((res) => res.data);
const fetchAllProjects = () => requestServices.customAxios.get('projects?type=all').then((res) => res.data);
const fetchNotScamProjects = () => requestServices.customAxios.get('projects?type=notscam').then((res) => res.data);
const fetchVerifiedProjects = () => requestServices.customAxios.get('projects?type=verified').then((res) => res.data);
const fetchUnVerifiedProjects = () => requestServices.customAxios.get('projects?type=unverified').then((res) => res.data);
const fetchInfoProject = (id) => requestServices.customAxios.get(`projects/${id}`).then((res) => res.data);


const createProject = (param) => requestServices.customAxios.post('projects', param).then((res) => res.data);
const removeProject = (id, param) => requestServices.customAxios.delete(`projects/${id}`, param).then((res) => res.data);
const makeProjectVerified = (id, param) => requestServices.customAxios.patch(`projects/${id}`, param).then((res) => res.data);
const updateSelectorProject = (id, param) => requestServices.customAxios.put(`projects/${id}`, param).then((res) => res.data);

export default {
  fetchEasyProjects,
  fetchAllProjects,
  fetchNotScamProjects,
  fetchVerifiedProjects,
  fetchUnVerifiedProjects,
  fetchInfoProject,
  createProject,
  removeProject,
  makeProjectVerified,
  updateSelectorProject
};