# Rendering HTML in Node.js with Express

Rendering HTML is a core task for web applications. You can render HTML either manually (which can be unsafe) or by using a template engine, which is more secure and manageable.

## Manual HTML Rendering (Not Recommended)

Rendering HTML manually can expose your application to security risks like cross-site scripting (XSS). However, here’s a basic example:

```js
app.get("/", (req, res) => {
  const name = "world";
  res.send(`
    <!DOCTYPE html>
    <html>
      <head><title>Hello ${name}</title></head>
      <body>Hello ${name}</body>
    </html>
  `);
});
```

# Rendering HTML via Template Engines

Template engines allow you to separate your HTML from your server-side code, making your application more maintainable and secure. Here are some popular template engines and their integrations with Express:

### 1. EJS (Embedded JavaScript)

- **Website**: [EJS](https://ejs.co/)
- **Express Integration**: [Using EJS with Express](https://github.com/mde/ejs/wiki/Using-EJS-with-Express)

### 2. Handlebars (or Mustache)

- **Website**: [Handlebars](https://handlebarsjs.com/)
- **Express Integration**: [Express Handlebars](https://github.com/pillarjs/hbs)

### 3. Pug (formerly Jade)

- **Website**: [Pug](https://pugjs.org)
- **Express Integration**: [Using Template Engines with Express](https://expressjs.com/en/guide/using-template-engines.html)

### 4. React

- **Website**: [React](https://reactjs.org/)
- **Express Integration**: [Express React Views](https://github.com/reactjs/express-react-views)

### 5. Marko

- **Website**: [Marko](https://markojs.com/)
- **Express Integration**: [Marko with Express](https://markojs.com/docs/express/)

For a comprehensive list of template engines, refer to the [Express Template Engines](https://expressjs.com/en/resources/template-engines.html) resource.

## General Procedure for Using a Template Engine

Here is a general procedure to use a template engine with Express:

```js
import express from "express";
import myengine from "myengine";

const app = express();

app.engine("myengine", myengine());
app.set("view engine", "myengine");

app.get("/", (req, res) => {
  const name = "world";
  // renders 'views/index.myengine'
  res.render("index", { name: name });
});

app.listen(3000, () => {
  console.log("Server is running on port 3000");
});
```

### Registering Various Template Engines

You can register multiple template engines in your application. Here is how you can set up EJS, Handlebars, and React as your template engines:

```js
import express from "express";
import ejs from "ejs";
import expressHandlebars from "express-handlebars";
import expressReactViews from "express-react-views";

const app = express();

app.engine("ejs", ejs.renderFile);
app.engine("handlebars", expressHandlebars());
app.engine("jsx", expressReactViews.createEngine());

app.set("view engine", "ejs"); // Default template engine
```

### Rendering HTML via express-react-views

To render HTML using React components, you need to install the necessary npm packages:

```sh
npm install express express-react-views react react-dom
```

### Example React View

Create a views directory and add an index.jsx file:

```jsx
// views/index.jsx
import React from "react";

const Index = ({ name }) => {
  return (
    <html>
      <head>
        <title>Hello, {name}!</title>
      </head>
      <body>
        <h1>Hello, {name}!</h1>
      </body>
    </html>
  );
};

export default Index;
```

### Setting Up Express to Use React Views

Here is how you set up your Express application to use express-react-views:

```js
import express from "express";
import expressReactViews from "express-react-views";
import dotenv from "dotenv";

// Load environment variables
dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

app.engine("jsx", expressReactViews.createEngine());
app.set("view engine", "jsx");

app.get("/", (req, res) => {
  const name = "world";
  res.render("index", { name });
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
