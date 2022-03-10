/* globals Chart:false, feather:false */

(function () {
  'use strict'

  feather.replace({ 'aria-hidden': 'true' })

  // Graphs
  var ctx = document.getElementById('myChart')
  // eslint-disable-next-line no-unused-vars
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59],
      datasets: [{
        data: [1424, 1784, 1039, 1010, 1352, 1127, 1723, 1908, 1203, 1946, 1515, 1301, 1398, 1433, 1639, 1726, 1343, 1794, 1039, 1456, 1750, 1105, 2000, 1057, 1723, 1395, 1074, 1636, 1261, 1685, 1405, 1444, 1294, 1440, 1240, 1874, 1240, 1857, 1394, 1096, 1520, 1189, 1302, 1406, 1558, 1189, 1408, 1320, 1754, 1144, 1644, 1896, 1784, 1490, 1562, 1853, 1589, 1472, 1294, 1482],
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#F04D5E',
        borderWidth: 1,
        pointBackgroundColor: '#F04D5E'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      }
    }
  })
})()