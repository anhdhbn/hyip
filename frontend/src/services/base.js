import { PROXY, BASE, POST, GET } from "./const";

export const post = (endpoint, body, onSuccess, onFailure) => {
  const url = `${PROXY}${BASE}${endpoint}`;
  console.log("Post data", url, "\nBody", body);
  fetch(url, {
    method: POST,
    headers: {
      Accept: "application/json, text/plain, */*",
      "Content-Type": "application/json"
      // Origin: "http://localhost"
    },
    body: JSON.stringify(body)
  })
    .then(res => res.json())
    .then(data => {
      if (data.error_code === 200) onSuccess(data, body);
      else onFailure(data);
    })
    .catch(onFailure);
};

export const get = (endpoint, onSuccess, onFailure) => {
  const url = `${PROXY}${BASE}${endpoint}`;
  console.log("Get url:", url);
  // fetch(url, {
  //   method: GET,
  //   headers: {
  //     Accept: "application/json",
  //     "Content-Type": "application/json",
  //     Origin: "http://localhost"
  //   }
  // })
  fetch(url)
    .then(res => res.json())
    .then(data => {
      console.log("Data get: ", data);
      if (data.code === 200) onSuccess(data.data);
      else onFailure(data);
    })
    .catch(onFailure);
};
