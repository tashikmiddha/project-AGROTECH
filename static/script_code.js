// List of notebooks: [title, GitHub raw link]
const notebooks = [
  {
    title: "Crop Prediction",
    url: "https://nbviewer.org/github/tashikmiddha/intern_project/blob/main/crop.ipynb"
  },
  {
    title: "Watering or not",
    url: "https://nbviewer.org/github/tashikmiddha/intern_project/blob/main/watering.ipynb"
  },
  {
    title: "Fertilizer prediction",
    url: "https://nbviewer.org/github/tashikmiddha/intern_project/blob/main/fertilizer.ipynb"
  }
];

const container = document.getElementById("notebookContainer");
const viewer = document.getElementById("notebookViewer");

notebooks.forEach(notebook => {
  const card = document.createElement("div");
  card.className = "notebook-card";
  card.textContent = notebook.title;

  card.addEventListener("click", () => {
    viewer.src = notebook.url;
    viewer.scrollIntoView({ behavior: "smooth" });
  });

  container.appendChild(card);
});
