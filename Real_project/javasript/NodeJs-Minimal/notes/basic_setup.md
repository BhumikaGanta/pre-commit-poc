# Node.js Express App Setup

This guide will help you set up a basic Node.js application using Express, with environment configuration, a rendering engine, and routing.

## Steps

1. Create `package.json`
2. Install packages
3. Add `.gitignore` file
4. Load configuration from `.env` file
5. Configure the rendering engine and routes
6. Add views

## 1. Create `package.json`

Create a `package.json` file to manage your project's dependencies and scripts.

### Example `package.json`

```json
{
  "name": "my-express-app",
  "version": "1.0.0",
  "description": "A simple Express application",
  "main": "server.js",
  "type": "module",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^4.17.1",
    "dotenv": "^10.0.0",
    "express-react-views": "^0.11.0",
    "react": "^17.0.2",
    "react-dom": "^17.0.2"
  },
  "eslintConfig": {
    "sourceType": "module"
  },
  "author": "",
  "license": "ISC"
}
```

## 2. Install Packages

Install the required packages using npm:

```sh
npm install express dotenv express-react-views react react-dom
```

## 3. Add .gitignore File

Create a .gitignore file to exclude unnecessary files from being tracked by git.
Example .gitignore

```txt
.env
node_modules/
```

## 4. Load Configuration from .env File

Create a .env file to store your environment variables.

### Example .env

```txt
PORT=3000
```

Load the configuration in your application:

```js
import dotenv from "dotenv";

dotenv.config();

const PORT = process.env.PORT || 3000;
```

## 5. Configure the Rendering Engine and Routes

Set up the Express application, configure the rendering engine, and define your routes.

### server.js

```js
import express from "express";
import expressReactViews from "express-react-views";
import dotenv from "dotenv";

// Load environment variables
dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

// Set up the rendering engine
app.engine("jsx", expressReactViews.createEngine());
app.set("view engine", "jsx");

// Define routes
app.get("/", (req, res) => {
  res.render("index", { name: "world" });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

## 6. Add Views

Create a views directory and add your view files.

### views/index.jsx

Create a file named index.jsx in the views directory:

```jsx
// views/index.jsx
import React from "react";

const Index = ({ name }) => (
  <html>
    <head>
      <title>Hello, {name}!</title>
    </head>
    <body>
      <h1>Hello, {name}!</h1>
    </body>
  </html>
);

export default Index;
```
