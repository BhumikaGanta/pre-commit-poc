# Routing in Express

Routing is a crucial part of web development, as it defines how your application responds to client requests for different endpoints. Express provides a simple and powerful way to handle routing.

## Basic Routing

You can define routes in Express using methods like `.get()`, `.post()`, `.put()`, `.delete()`, etc. Each method corresponds to an HTTP verb.

### Example

```js
import express from "express";

const app = express();
const PORT = process.env.PORT || 3000;

// Define routes
app.get("/", (req, res) => {
  res.send("<h1>Home</h1>\n");
});

app.get("/about", (req, res) => {
  res.send("<h1>About</h1>\n");
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

In this example, two routes are defined: `/` for the home page and `/about` for the about page.

## Other HTTP Methods

Express supports all HTTP methods, allowing you to handle various types of requests.

### Example

```js
app.post("/submit", (req, res) => {
  res.send("Form submitted");
});

app.put("/update", (req, res) => {
  res.send("Resource updated");
});

app.delete("/delete", (req, res) => {
  res.send("Resource deleted");
});
```

## Route Parameters

Route parameters are used to capture values specified at their position in the URL. These values can be accessed via `req.params`.

### Example

```js
app.get("/articles/:id", (req, res) => {
  const articleId = req.params.id;
  res.send(`Article ID: ${articleId}`);
});
```

In this example, visiting `/articles/123` will respond with Article ID: 123.

## Query Parameters

Query parameters are used to filter or sort data and can be accessed via req.query.

### Example

```js
app.get("/search", (req, res) => {
  const query = req.query.q;
  res.send(`Search query: ${query}`);
});
```

Visiting `/search?q=nodejs` will respond with Search query: nodejs.

## Handling Forms

To handle form submissions, you typically use the POST method.

### Example

```js
app.use(express.urlencoded({ extended: true }));

app.post("/submit-form", (req, res) => {
  const formData = req.body;
  res.send(`Form data received: ${JSON.stringify(formData)}`);
});
```

## Redirects

You can redirect requests to different routes using res.redirect().

### Example

```js
app.get("/home", (req, res) => {
  res.redirect("/");
});
```

In this example, visiting /home will redirect the client to the / route.

## Organizing Routes

For larger applications, it's common to organize routes using Express Router. This helps in keeping the code modular and manageable.

### Example

Create a separate router file routes/articles.js:

```js
import express from "express";
const router = express.Router();

router.get("/:id", (req, res) => {
  const articleId = req.params.id;
  res.send(`Article ID: ${articleId}`);
});

router.post("/", (req, res) => {
  res.send("Create a new article");
});

export default router;
```

In your main application file:

```js
import express from "express";
import articleRoutes from "./routes/articles.js";

const app = express();
const PORT = process.env.PORT || 3000;

app.use("/articles", articleRoutes);

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
