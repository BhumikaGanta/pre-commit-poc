# Middleware in Node.js

Middleware functions are essential components in web applications built with Node.js, especially when using libraries like `connect` and `express`. Middleware can handle requests, modify request and response objects, and manage the application's control flow.

## What is Middleware?

Middleware functions are functions that have access to the request object (`req`), the response object (`res`), and the next middleware function in the application's request-response cycle. Middleware can perform various tasks, including:

- Logging requests
- Parsing request bodies
- Managing sessions
- Serving static files
- Handling errors

## Using Middleware in `express`

Middleware in `express` is added using the `.use()` method. Each middleware function can end the request-response cycle by sending a response, or pass control to the next middleware function using `next()`.

### Example Setup with Middleware

```js
import express from "express";
import compression from "compression";
import morgan from "morgan";

const app = express();

// Log all incoming requests
app.use(morgan("common"));

// Serve static files from the "public" directory
app.use(express.static("public"));

// Compress all responses
app.use(compression());
```

In this example, three middleware functions are used:

- `morgan`: Logs all incoming requests.
- `express.static`: Serves static files from the public directory.
- `compression`: Compresses all responses.

## Common Middleware Examples

### 1. express.json() and express.urlencoded()

These middleware functions parse incoming request bodies and make the parsed data available under `req.body`.

```js
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
```

### 2. cookie-parser

Parses cookies attached to the client request object and makes them available under `req.cookies`.

```js
import cookieParser from "cookie-parser";

app.use(cookieParser());
```

### 3. compression

Compresses response bodies for all requests that traverse through the middleware.

```js
app.use(compression());
```

### 4. express.static

Serves static files such as HTML, CSS, and JavaScript from a specified directory.

```js
app.use(express.static("public"));
```

### 5. express-session

Stores session data on the server side and makes it available under `req.session`.

```js
import session from "express-session";

app.use(
  session({
    secret: "your-secret-key", #pragma: allowlist secret
    resave: false,
    saveUninitialized: true,
  }),
);
```

### 6. express-openid-connect or passport

These middleware functions handle user authentication.

```js
import { auth } from "express-openid-connect";
import passport from "passport";

// Example using express-openid-connect
app.use(
  auth({
    issuerBaseURL: "https://YOUR_DOMAIN",
    clientID: "YOUR_CLIENT_ID",
    baseURL: "http://localhost:3000",
    secret: "a long, randomly-generated string stored in env", #pragma: allowlist secret
  }),
);

// Example using passport
app.use(passport.initialize());
app.use(passport.session());
```

### 7. morgan

Logs request details to the console.

```js
import morgan from "morgan";

app.use(morgan("common"));
```
