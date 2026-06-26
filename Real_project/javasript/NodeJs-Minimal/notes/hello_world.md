## Hello World with Node.js

In this section, we'll explore how to create a simple "Hello World" server using Node.js, both with and without the Express framework. We'll also cover the complete setup, including package configuration and running the server.

### Hello World with Express

Express is a minimal and flexible Node.js web application framework that provides a robust set of features to develop web and mobile applications.

#### Example

Create a file named `server.js`:

```js
// server.js
import express from "express";

const app = express();

// Provide a function that handles a request to "/"
// and sends a response
app.get("/", (req, res) => {
  res.send("<h1>Hello World!</h1>\n");
});

// Listen on localhost:3000
app.listen(3000, () => {
  console.log("Server is running on http://localhost:3000");
});
```

#### Complete Setup with Express

1. Create a package.json file:

```json
{
  "type": "module",
  "eslintConfig": {
    "sourceType": "module"
  },
  "scripts": {
    "start": "node server.js"
  }
}
```

2. Install Express:

```bash

npm install express
```

3. Run the server:

```bash
npm run start
```

Open http://localhost:3000 in your browser to view the result.

### Hello World without Express

For a more fundamental approach, you can use the built-in http module to create a server.

#### Example

Create a file named server.js:

```js
// server.js
import http from "http";

const handler = (req, res) => {
  res.statusCode = 200;
  res.setHeader("Content-Type", "text/html; charset=UTF-8");
  res.end("<h1>Hello World!</h1>\n");
};

const server = http.createServer(handler);

server.listen(3000, () => {
  console.log("Server is running on http://localhost:3000");
});
```

#### Complete Setup without Express

1. Create a package.json file:

```json
{
  "type": "module",
  "eslintConfig": {
    "sourceType": "module"
  },
  "scripts": {
    "start": "node server.js"
  }
}
```

2. Run the server:

```bash
npm run start
```

Open http://localhost:3000 in your browser to view the result.
