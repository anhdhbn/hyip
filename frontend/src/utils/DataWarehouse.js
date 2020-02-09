import { CustomTooltips } from '@coreui/coreui-plugin-chartjs-custom-tooltips';
import { getStyle, hexToRgba } from '@coreui/coreui/dist/js/coreui-utilities'

import crawldataServices from '../services/crawldata'

const brandPrimary = getStyle('--primary')
const brandSuccess = getStyle('--success')
// const brandInfo = getStyle('--info')
const brandWarning = getStyle('--warning')
const brandDanger = getStyle('--danger')



const optionsChart = {
  tooltips: {
    enabled: false,
    custom: CustomTooltips,
    intersect: true,
    mode: 'index',
    position: 'nearest',
    callbacks: {
      labelColor: function(tooltipItem, chart) {
        return { backgroundColor: chart.data.datasets[tooltipItem.datasetIndex].borderColor }
      }
    }
  },
  maintainAspectRatio: false,
  // legend: {
  //   display: false,
  // },
  elements: {
    point: {
      radius: 3,
      hitRadius: 10,
      hoverRadius: 4,
      hoverBorderWidth: 3,
    },
  },
}

const createDataForChart = (labelName, data, color) => {
  return {
    label: labelName,
    backgroundColor: hexToRgba(color, 10),
    borderColor: color,
    pointHoverBackgroundColor: '#fff',
    borderWidth: 2,
    // fill: false,
    // lineTension: 0.1,
    // borderCapStyle: 'butt',
    // borderDash: [],
    // borderDashOffset: 0.0,
    // borderJoinStyle: 'miter',
    // pointBorderColor: color,
    // pointBackgroundColor: '#fff',
    // pointBorderWidth: 1,
    // pointHoverRadius: 10,
    // pointHoverBackgroundColor: color,
    // pointHoverBorderColor: 'rgba(220,220,220,1)',
    // pointHoverBorderWidth: 2,
    // pointRadius: 3,
    // pointHitRadius: 10,
    data: data,
  }
};

const calcProfit = (total_investments, total_paid_outs) => {
  let d1 = total_investments
  let d2 = total_paid_outs
  let profit = []
  for(let i=0; i< d1.length; i++){
    profit.push(d1[i] - d2[i])
  }
  return profit
}

const getProfitData = (total_investments, total_paid_outs, labels) => {
  let profit = calcProfit(total_investments, total_paid_outs)
  return {
    labels: labels,
    datasets: [
      createDataForChart('Total investment', total_investments, brandPrimary),
      createDataForChart('Total paid out', total_paid_outs, brandWarning),
      createDataForChart('Profit', profit, brandSuccess),
    ]
  }
}

const getGrowthRateData = (total_investments, total_paid_outs, labels) => {
  let profit = calcProfit(total_investments, total_paid_outs)

  let  igr = []
  for(let i=1; i< profit.length; i++){
    if (profit[i]  === 0) {
      igr.push(0)
    } else {
      let item = (profit[i] - profit[i-1])/profit[i]
      igr.push(item)
    }
  }
  return {
    labels: labels.reverse().slice(1).reverse(),
    datasets: [
      createDataForChart('Income Growth Rate', igr, brandDanger),
    ]
  }
}

const createSingleData = (labels, label, data) => {
  return {
    labels: labels,
    datasets: [
      createDataForChart(label, data, brandPrimary),
    ]
  }
}

const preprocessFetchData = (id, days='all') => {
  return new Promise((resolve, reject) => {
    crawldataServices.fetchDataCrawledProject(id, days).then(res => {
      res.drawData = {}
      let data = res.data
      let dates = data.map(e => new Date(e.created_date))
      let labels = dates.map(e => `${e.getDate()}/${e.getMonth()+1}`)
      let total_investments = data.map(e => e.total_investments)
      let total_paid_outs = data.map(e => e.total_paid_outs)
      let total_members = data.map(e => e.total_members)
      let alexa_rank = data.map(e => e.alexa_rank)
      
      res.drawData.labels = labels
      res.drawData.total_investments = total_investments
      res.drawData.total_paid_outs = total_paid_outs
      res.drawData.total_members = total_members
      res.drawData.alexa_rank = alexa_rank
      resolve(res)
    })
  })
}

export default {
  optionsChart,
  createDataForChart,
  calcProfit,
  getProfitData,
  createSingleData,
  getGrowthRateData,
  preprocessFetchData
}