## Identity Provider

An _identity provider_ is a service that verifies the identity of users by authenticating them. This process ensures that users are who they claim to be, allowing secure access to various applications and services.

### Examples:

- The current end user is logged in as user "john_doe" on this domain.
- The current user is authenticated as user "alice123" by _Google_ or as user "bob456" by _Facebook_.

### Mechanism for the User:

When a user clicks on _login_, they are redirected to a login page provided by the identity provider. Once logged in, they are sent back to the original site. In the background, the user receives an _identity token_, which is a piece of data proving their identity with the identity provider. This token is usually stored as a cookie (e.g., `appSession`).

#### Example:

- User clicks "Login" on `myapp.com`.
- They are redirected to a login page at `authprovider.com/login`.
- After entering credentials, they are redirected back to `myapp.com/callback` with an identity token.
- The identity token is stored as a cookie, allowing `myapp.com` to recognize the user.

### Standards:

- **Authorization**: OAuth2
- **Authentication**: OpenID Connect

## Auth0

**Auth0** (pronounced _auth-zero_) is a widely-used identity provider that supports authentication via "internal" accounts or external identity providers such as _Google_, _Apple_, _Facebook_, and others.

### Auth0: Registration and Setup

1. **Register for an Auth0 account** at [Auth0](https://auth0.com).
2. **In the sidebar**, select "Applications".
3. **Select the default application** or create a new "Regular Web Application". The chosen name will be shown to users during authentication.

#### Registration Details:

- Select region: EU / US / AU
- Select account type: personal / company

### Application Settings:

- **Allowed Callback URLs**: URLs where users are redirected after login completion.
- **Allowed Logout URLs**: URLs where users are redirected after logout.

#### Callback URLs Example:

```txt
http://localhost:3000/callback,
https://mydomain.com/callback
```

#### Logout URLs Example:

```txt
http://localhost:3000,
https://mydomain.com
```

### Configuration

Example .env Configuration for Local Development:

```bash
ISSUER_BASE_URL=https://dev-xxxxxxxx.eu.auth0.com
CLIENT_ID=jA0EAwMCxamDRMfOGV5gyZPnyX1BBPOQ
SECRET=7qHciKUpXk7pCXqG45bweRBQxBTMpztB
BASE_URL=http://localhost:3000
PORT=3000
```

Under Settings:

- Each Auth0 registrant has at least one domain (e.g., dev-xxxxxxxx.eu.auth0.com).
- Each app has a specific client ID (e.g., jA0EAwMCxamDRMfOGV5gyZPnyX1BBPOQ).
- Secret: Generate a long, random string yourself (recommendation: at least 32 characters).

## Express and Auth0

### Guides:

- **Most Recent Library**: [express-openid-connect](https://auth0.com/docs/quickstart/webapp/express)
- **Older Libraries**: [Auth0 Express Quickstart](https://auth0.com/docs/quickstart/webapp/express)

### npm Package: `express-openid-connect`

This middleware is used for authentication and automatically adds the following URLs: _/login_, _/logout_, _/callback_.

```js
const { auth } = require("express-openid-connect");
const express = require("express");
const app = express();

app.use(
  auth({
    authRequired: false,
    auth0Logout: true,
    baseURL: process.env.BASE_URL,
    clientID: process.env.CLIENT_ID,
    issuerBaseURL: process.env.ISSUER_BASE_URL,
    secret: process.env.SECRET,
  }),
);

// Home route displaying authentication status
app.get("/", (req, res) => {
  if (req.oidc.isAuthenticated()) {
    res.send(
      `<p>Logged in as ${req.oidc.user.name} <a href="/logout">Log out</a></p>
       <pre>${JSON.stringify(req.oidc.user, null, 2)}</pre>`,
    );
  } else {
    res.send('<div>Not logged in <a href="/login">Log in</a></div>');
  }
});

// Start the server
app.listen(process.env.PORT, () => {
  console.log(`App listening on port ${process.env.PORT}`);
});
```
