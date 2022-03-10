/* globals Chart:false, feather:false */

(function () {
  'use strict'
   // 1. Создаём новый объект XMLHttpRequest
   var xhr = new XMLHttpRequest();

   // 2. Конфигурируем его: GET-запрос на URL 'phones.json'
   xhr.open('GET', '/dashboard/result?id=1', false);

   // 3. Отсылаем запрос
   xhr.send();

   var array = JSON.parse(xhr.responseText)
   var rps = array.load_result.rps
   var ts = array.load_result.ts

  // Graphs
  var ctx = document.getElementById('myChart')
  // eslint-disable-next-line no-unused-vars
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: ts,
      datasets: [{
        data: rps,
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