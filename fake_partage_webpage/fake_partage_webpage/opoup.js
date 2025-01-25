document.getElementById('backupButton').addEventListener('click', function() {
  chrome.runtime.sendMessage({ action: "backupCookies" }, function(response) {
    alert(response.message);
  });
});
