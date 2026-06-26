## Configuration via Environment Variables

Credentials and configuration should be supplied via environment variables to enhance security and flexibility. This approach ensures sensitive information is not hardcoded into the application's source code and can be easily changed without modifying the codebase.

### Important Points

- **Security**: Environment variables keep sensitive data out of your source code, reducing the risk of exposing credentials.
- **Flexibility**: Easily change configurations for different environments (development, staging, production) without altering the code.

## .env File

A common way to supply configuration and credentials is by storing them in a file named _.env_ and loading them as environment variables using the _dotenv_ library.

### Best Practices

- Ensure the _.env_ file is not under version control by adding it to your _.gitignore_ file.
- Keep the _.env_ file secure and limit access to it.

### Example _.env_ File

```bash
PORT=3000
NODE_ENV=production
DB_URL=mongodb+srv://user:password@cluster0.mongodb.net/mydatabase  #pragma: allowlist secret
AUTH0_DOMAIN=dev-xxxxxx.eu.auth0.com
AUTH0_CLIENT_ID=your-client-id
AUTH0_CLIENT_SECRET=your-client-secret
```

### Loading Environment Variables in JavaScript

Use the dotenv library to load the variables from the .env file into process.env.

```js
import dotenv from "dotenv";

dotenv.config();

const PORT = process.env.PORT;
const DB_URL = process.env.DB_URL;
const AUTH0_DOMAIN = process.env.AUTH0_DOMAIN;
const AUTH0_CLIENT_ID = process.env.AUTH0_CLIENT_ID;
const AUTH0_CLIENT_SECRET = process.env.AUTH0_CLIENT_SECRET;

console.log(`Server running on port: ${PORT}`);
console.log(`Connected to database at: ${DB_URL}`);
```

### Adding .env to .gitignore

Ensure the .env file is not included in version control by adding it to your .gitignore file.

```plaintext
# .gitignore
.env
```

### NODE_ENV

The NODE_ENV environment variable is crucial for defining the environment in which an application is running. This variable can significantly impact the behavior and performance of your application.
Example:

- Development: NODE_ENV=development
- Production: NODE_ENV=production

#### Importance of NODE_ENV

In production environments, NODE_ENV=production should always be set to avoid exposing sensitive information and to optimize performance.

```bash
NODE_ENV=production
```

#### Usage in Express

In an Express application, setting NODE_ENV to production ensures that error messages and stack traces are not exposed to the end users, enhancing security.

```js
import express from "express";
import dotenv from "dotenv";

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

if (process.env.NODE_ENV === "production") {
  // Production-specific settings
  app.use((err, req, res, next) => {
    res.status(500).send("Something went wrong!");
  });
} else {
  // Development-specific settings
  app.use((err, req, res, next) => {
    res.status(500).send(err.stack);
  });
}

app.listen(PORT, () => {
  console.log(`Server running in ${process.env.NODE_ENV} mode on port ${PORT}`);
});
```
