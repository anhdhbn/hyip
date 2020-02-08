import React, { Component } from 'react';

import AsyncSelect from 'react-select/async';

import domainService from '../../services/domains'

class SearchDomain extends Component {
  searchDomain(input){
    return new Promise((resolve, reject) => {
      if(!input) return reject("Empty")
      domainService.searchDomain(input).then(res => {
        if (!res.success) return reject(res)
        resolve(res.data)
      })
    })
  }

  render() {
    const {handleChange} = this.props
    return (
      <AsyncSelect 
        autoFocus 
        onChange={handleChange} 
        isClearable 
        isSearchable 
        cacheOptions={this.props.cached || true}
        defaultOptions 
        loadOptions={this.searchDomain} />
    )
  }
}

export default SearchDomain;