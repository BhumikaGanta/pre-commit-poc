# Request Parameters in Node.js

When dealing with web applications, understanding how to handle request parameters is crucial. These parameters can be sent via URLs or in the request body, depending on the HTTP method used.

## Request Parameters Format

By default, browsers send form contents in URL-encoded format, such as:

```txt
foo=1&bar=2&baz=3
```

## In GET Requests

In GET requests, parameters are appended to the URL:

```txt
https://example.com/search?foo=1&bar=2&baz=3
```

## In POST Requests

In POST requests, parameters are included in the request body.

## Getting Request Parameters

### Handling GET Request Parameters

To read parameters from a GET request, you can use req.query in Express:

```js
app.get("/search", (req, res) => {
  const foo = req.query.foo;
  const bar = req.query.bar;
  const baz = req.query.baz;
  res.send(`Received parameters - foo: ${foo}, bar: ${bar}, baz: ${baz}`);
});
```

### Handling POST Request Parameters

To handle parameters in a POST request, you need to use the express.urlencoded middleware to parse the URL-encoded data in the request body:

1. Setup the middleware:

```js
app.use(express.urlencoded({ extended: true }));
```

2. Read parameters from req.body:

```js
app.post("/submit", (req, res) => {
  const foo = req.body.foo;
  const bar = req.body.bar;
  const baz = req.body.baz;
  res.send(`Received parameters - foo: ${foo}, bar: ${bar}, baz: ${baz}`);
});
```

### Example: Complete Setup

Here is a complete example of an Express server handling both GET and POST requests with parameters:

```js
import express from "express";

const app = express();

// Middleware to parse URL-encoded data
app.use(express.urlencoded({ extended: true }));

// Handling GET request parameters
app.get("/search", (req, res) => {
  const foo = req.query.foo;
  const bar = req.query.bar;
  const baz = req.query.baz;
  res.send(
    `Received parameters in GET - foo: ${foo}, bar: ${bar}, baz: ${baz}`,
  );
});

// Handling POST request parameters
app.post("/submit", (req, res) => {
  const foo = req.body.foo;
  const bar = req.body.bar;
  const baz = req.body.baz;
  res.send(
    `Received parameters in POST - foo: ${foo}, bar: ${bar}, baz: ${baz}`,
  );
});

// Start the server
app.listen(3000, () => {
  console.log("Server is running on http://localhost:3000");
});
```
