let uploadedFile = null;

function simulateFileUpload(files) {
  setTimeout(() => {
    const fileName = files[0].name;
    const fileSize = files[0].size;
    const fileList = document.getElementById('fileList');
    const fileNameElement = document.createElement('div');
    fileNameElement.classList.add('fileName');
    fileNameElement.textContent = fileName;
    fileList.appendChild(fileNameElement);

    uploadedFile = fileName;
    document.getElementById('deleteButton').style.display = 'block';

    const fileSizeElement = document.getElementById('fileSize');
    fileSizeElement.textContent = `Taille du fichier: ${formatFileSize(fileSize)}`;
  }, 5000);

  const progressBar = document.getElementById('progressBar');
  progressBar.style.width = '100%';

  // Réinitialiser la barre de progression après 5 secondes
  setTimeout(() => {
    progressBar.style.width = '0';
  }, 5000);
}

function uploadFileFromInput(files) {
  simulateFileUpload(files);
}

function formatFileSize(bytes) {
  if (bytes === 0) return '0 octets';
  const k = 1024;
  const sizes = ['octets', 'Ko', 'Mo', 'Go', 'To'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

const dropArea = document.getElementById('dropArea');

dropArea.addEventListener('dragover', function(event) {
  event.preventDefault();
  this.classList.add('dragover');
});

dropArea.addEventListener('dragleave', function(event) {
  event.preventDefault();
  this.classList.remove('dragover');
});

dropArea.addEventListener('drop', function(event) {
  event.preventDefault();
  this.classList.remove('dragover');
  const files = event.dataTransfer.files;
  simulateFileUpload(files);
});

document.getElementById('uploadButton').addEventListener('click', function() {
  document.getElementById('fileInput').click();
});

document.getElementById('fileInput').addEventListener('change', function() {
  const files = this.files;
  uploadFileFromInput(files);
});

document.getElementById('urlInput').addEventListener('change', function() {
  const url = this.value.trim();
  if (url !== '') {
    simulateFileUpload([{ name: 'article.html', size: 123456 }]);
    this.value = '';
  }
});

document.getElementById('deleteButton').addEventListener('click', function() {
  if (uploadedFile !== null) {
    const fileList = document.getElementById('fileList');
    fileList.innerHTML = '';
    uploadedFile = null;
    this.style.display = 'none';

    const fileSizeElement = document.getElementById('fileSize');
    fileSizeElement.textContent = '';
  }
});
