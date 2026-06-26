## Comprehensive Guide to npm and Package Management

In this guide, we will explore the essential aspects of working with npm, the Node Package Manager, and its associated tools. We'll cover everything from understanding the npm registry to managing dependencies and scripts for your projects. This comprehensive overview is designed to help both beginners and experienced developers streamline their workflow and ensure they make the most of npm and its features.

### npm Registry

The npm registry is an online registry primarily consisting of open-source JavaScript packages. It is by far the largest software registry with [over 1 million packages](http://www.modulecounts.com/).

Examples: [Most depended upon packages](https://www.npmjs.com/browse/depended)

### Package Managers

Two major package managers for the npm registry are:

- **npm**: Node Package Manager, comes bundled with Node.js.
- **yarn**: An alternative package manager that needs to be installed separately.

### Package Configuration

Both public packages and private projects are managed via a configuration file named `package.json`.

#### Creating a Package Configuration

Start with an empty `package.json` configuration:

```json
{}
```

Alternatively, create a package.json with some content using npm init (or npm init -y for default options).

#### Adding Dependencies

Add dependencies using the following command:

```bash
npm install lodash bootstrap
```

#### Development Dependencies

When developing a reusable library to be published on the npm package registry, install dependencies that are only needed for development as dev-dependencies:

```bash
npm install eslint --save-dev
```

### Effects of Adding Dependencies

When you install dependencies, the following changes occur:

- **`package.json`**: Lists the minimum versions of the packages installed.
- **`node_modules`**: Folder that contains all installed packages.
- **`package-lock.json`**: Lists the exact versions of all packages in `node_modules`.

#### Dependencies in `package.json`

The `package.json` file lists dependencies with a version specifier using semantic versioning: `major.minor.patch`.

Possible configurations:

- `"express": "4.17.1"` - Exactly this version.
- `"express": "~4.17.1"` - Patch version updates allowed, for example, to `4.17.2`.
- `"express": "^4.17.1"` - Minor version updates allowed, for example, to `4.18.0`.

#### Dependencies in `package-lock.json`

The `package-lock.json` file lists the exact versions for all dependencies and their recursive dependencies.

#### `node_modules` Folder

This folder contains the actual packages and should not be put under version control. It can be recreated from `package.json` by running `npm install` (without any arguments).

### npm Scripts

npm can be used to execute scripts/commands that are needed for development. For example:

- `npm run lint` - Runs the linter.
- `npm run build` - Creates a build.
- `npm run dev` - Starts the application in development mode.
- `npm run deploy` - Deploys the application.

Some npm scripts have shorthands, notably `npm test` and `npm start`.

#### Configuring npm Scripts

Npm scripts are configured in `package.json`:

```json
{
  "scripts": {
    "lint": "eslint .",
    "build": "webpack --config webpack.config.js",
    "dev": "nodemon app.js",
    "deploy": "npm run build && scp -r ./dist user@server:/path/to/deploy"
  }
}
```

### Global Installs and npx

Node packages can be installed globally on a computer or executed directly from the npm registry.

#### Direct Execution

Execute a package directly without installation using npx:

```bash
npx json-server --watch db.json
```

#### Global Installation

Install a package globally:

```bash
npm install -g json-server

json-server --watch db.json
```
