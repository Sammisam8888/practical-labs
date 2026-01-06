window.globalChart = null;
window.updateChart = function(labels, data){
  if(window.globalChart){ window.globalChart.data.labels = labels; window.globalChart.data.datasets[0].data = data; window.globalChart.update(); return; }
  const ctx = document.getElementById('throughputChart') ? document.getElementById('throughputChart').getContext('2d') : null;
  if(!ctx) return;
  window.globalChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [{ label: 'Throughput (tx/s)', data: data, fill:false, tension:0.2 }]
    },
    options: { responsive:true, maintainAspectRatio:false, scales: { y: { beginAtZero:true } } }
  });
};

window.renderSingleChart = function(canvasId, labels, data){
  const el = document.getElementById(canvasId);
  if(!el) return null;
  const ctx = el.getContext('2d');
  return new Chart(ctx, {
    type: 'line',
    data: { labels: labels, datasets:[{ label:'Throughput', data: data, fill:false, tension:0.2 }] },
    options: { responsive:true, maintainAspectRatio:false, scales: { y:{ beginAtZero:true } } }
  });
};
