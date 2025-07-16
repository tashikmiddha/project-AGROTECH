function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const content=document.getElementById('content');
    sidebar.classList.toggle('collapsed');
    content.classList.toggle('collapsed');
}
 window.addEventListener("load", function () {
      const overlay = document.getElementById("loading-overlay");
      overlay.style.opacity = 0;
      setTimeout(() => {
        overlay.style.display = "none";
        document.body.classList.remove("loading");
      }, 600); // matches transition
    });
function toggleModels() {
    var list = document.getElementById('modelList');
    list.style.display = list.style.display === 'none' ? 'block' : 'none';
  }


