## Libraries Overview

Node.js is a powerful JavaScript runtime built on Chrome's V8 engine, designed for building scalable and efficient server-side applications. One of the key strengths of Node.js is its rich ecosystem of libraries and frameworks that extend its functionality, making it easier to develop complex applications.

### 1. Node.js Core Modules

Node.js comes with a set of core modules that provide essential functionalities without the need for external libraries. Some of the most commonly used core modules include:

- **http**: Provides the ability to create HTTP servers and clients.
- **fs**: Enables interacting with the file system.
- **path**: Utilities for working with file and directory paths.
- **os**: Provides operating system-related utility methods and properties.

### Example of Using Core Modules

```js
const http = require("http");
const fs = require("fs");
const path = require("path");

const server = http.createServer((req, res) => {
  if (req.url === "/") {
    fs.readFile(path.join(__dirname, "index.html"), (err, data) => {
      if (err) throw err;
      res.writeHead(200, { "Content-Type": "text/html" });
      res.end(data);
    });
  }
});

const PORT = 3000;
server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

## 2. Connect

connect is a minimal framework that provides middleware support.

### Example

```js
const connect = require("connect");
const http = require("http");

const app = connect();

app.use((req, res, next) => {
  res.setHeader("Content-Type", "text/plain");
  res.end("Hello World\n");
});

const PORT = process.env.PORT || 3000;
http.createServer(app).listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}/`);
});
```

## 3. Express

express is a comprehensive framework that includes middleware, routing, view rendering, and more.

Most projects will use express due to its ease of use and extensive feature set.

### Example

```js
import express from "express";
import dotenv from "dotenv";

// Load environment variables
dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware example
app.use(express.json());

// Routing example
app.get("/", (req, res) => {
  res.send("Hello World");
});

app.post("/data", (req, res) => {
  res.json(req.body);
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
