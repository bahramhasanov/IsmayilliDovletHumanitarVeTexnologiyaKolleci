function Hello() {
    var copyText = document.getElementById('copy')
    copyText.select();
    document.execCommand('copy')
    console.log('Copied Text')
  }