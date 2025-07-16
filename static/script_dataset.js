const datasets = [
  { name: "Watering Dataset", file: "datasets/data.csv" },
  { name: "Fertilizer Dataset", file: "datasets/data_core.csv" },
  { name: "Crop yield Dataset", file: "datasets/crop_yield.csv" },
  { name: "Crop Recommendation Dataset", file: "datasets/Crop_recommendation.csv" },
  { name: "Titanic Dataset", file: "datasets/Titanic-Dataset.csv" }
]

const container = document.getElementById('datasetContainer');
const searchBar = document.getElementById('searchBar');

function renderDatasets(filteredDatasets) {
  container.innerHTML = '';
  filteredDatasets.forEach(ds => {
    const card = document.createElement('div');
    card.className = 'dataset-card';
    card.innerHTML = `
      <h3>${ds.name}</h3>
      <a class="download-btn" href="/static/${ds.file}" download>Download</a>
    `;
    container.appendChild(card);
  });
}

searchBar.addEventListener('input', function () {
  const query = searchBar.value.toLowerCase();
  const filtered = datasets.filter(ds => ds.name.toLowerCase().includes(query));
  renderDatasets(filtered);
});

// Initial render
renderDatasets(datasets);
