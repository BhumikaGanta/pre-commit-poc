# Request and Response Handling in Node.js

In web development with Node.js and Express, handling requests and responses efficiently is crucial. This guide covers the basics of request and response objects, and provides examples and exercises to help you understand their usage better.

## Request Handler Function

A request handler function in Node.js and Express receives two arguments:

- `req`: Represents the incoming request.
  - Class [IncomingMessage](https://nodejs.org/api/http.html#http_class_http_incomingmessage) in Node.js.
  - Subclass [Request](http://expressjs.com/en/4x/api.html#req) in Express.
- `res`: Represents the response that will be sent.
  - Class [ServerResponse](https://nodejs.org/api/http.html#http_class_http_serverresponse) in Node.js.
  - Subclass [Response](http://expressjs.com/en/4x/api.html#res) in Express.

### Example

Create a Web App that Displays the Current Time

```js
import express from "express";

const app = express();

app.use((req, res) => {
  const timeString = new Date().toTimeString();
  res.send("<h1>Current time: " + timeString + "</h1>");
});

app.listen(3000, () => {
  console.log("Server is running on http://localhost:3000");
});
```

### The Request Object

The request object contains details about the incoming request. Here’s an example of a request object:

```json
{
  "url": "/",
  "method": "GET",
  "headers": {
    "user-agent": "Mozilla/5.0 (Windows ..."
  }
}
```

- Class in plain Node.js / Connect: IncomingMessage
- Class in Express: Request

### Example:

Create a Website with Different Responses Based on the Requested URL

```js
import express from "express";

const app = express();

app.get("/", (req, res) => {
  res.send("<h1>Welcome to the Home Page</h1>");
});

app.get("/about", (req, res) => {
  res.send("<h1>About Us</h1>");
});

app.get("/contact", (req, res) => {
  res.send("<h1>Contact Us</h1>");
});

app.listen(3000, () => {
  console.log("Server is running on http://localhost:3000");
});
```

## The Response Object

The response object is used to send data back to the client.

- Class in plain Node.js / Connect: ServerResponse
- Class in Express: Response

Methods in Express:

- `.send()`: Sends the response body.
- `.set()`: Sets the response’s HTTP headers.
- `.status()`: Sets the HTTP status for the response.

### Example: Sending a Plain Text Response

```js
app.get("/date", (req, res) => {
  res.set({ "Content-Type": "text/plain" });
  res.send("Date:\n" + new Date().toLocaleDateString());
});
```

### Example: Setting Status and Headers

```js
app.get("/not-found", (req, res) => {
  res.status(404);
  res.set({ "Content-Type": "text/plain" });
  res.send("Document not found.\n");
});
```

## Setting a Cookie

You can set cookies using `res.cookie()` or by explicitly setting the Set-Cookie header.

1. Using `res.cookie()`:

```js
app.get("/set-cookie", (req, res) => {
  res.cookie("a", "1");
  res.send("Cookie set");
});
```

2. Setting the Set-Cookie header explicitly:

```js
app.get("/set-cookie-explicit", (req, res) => {
  res.set({ "Set-Cookie": "a=1" });
  res.send("Cookie set explicitly");
});
```
