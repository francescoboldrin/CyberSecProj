const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 3000; // Port to serve the site

const server = http.createServer((req, res) => {
    let filePath = './insa-login/index.html'; // Default to index.html for root path

    // Serve the requested files
    if (req.url !== '/') {
        filePath = `.${req.url}`;
    }

    const extname = path.extname(filePath);
    let contentType = 'text/html';

    // Determine the content type based on file extension
    switch (extname) {
        case '.js':
            contentType = 'application/javascript';
            break;
        case '.css':
            contentType = 'text/css';
            break;
        case '.png':
            contentType = 'image/png';
            break;
        case '.jpg':
        case '.jpeg':
            contentType = 'image/jpeg';
            break;
        case '.ico':
            contentType = 'image/x-icon';
            break;
        default:
            contentType = 'text/html';
    }

    // Read the requested file and send the response
    fs.readFile(filePath, (err, content) => {
        if (err) {
            if (err.code === 'ENOENT') {
                // File not found
                res.writeHead(404, { 'Content-Type': 'text/html' });
                res.end('<h1>404 Not Found</h1>', 'utf-8');
            } else {
                // Other server error
                res.writeHead(500);
                res.end(`Server Error: ${err.code}`);
            }
        } else {
            // Send the file content with the correct content type
            res.writeHead(200, { 'Content-Type': contentType });
            res.end(content, 'utf-8');
        }
    });
});

server.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
