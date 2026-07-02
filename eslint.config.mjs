export default [
  {
    files: ["Real_project/javasript/**/*.js"],
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "commonjs",
      globals: {
        console: "readonly",
        require: "readonly",
        module: "readonly",
        process: "readonly",
        __dirname: "readonly",
        __filename: "readonly",
      },
    },
    rules: {
      "no-undef": "error",
    },
  },
  {
    files: ["Real_project/python/**/vue-client/**/*.js"],
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "module",
      globals: {
        console: "readonly",
        localStorage: "readonly",
        FormData: "readonly",
        window: "readonly",
        document: "readonly",
      },
    },
    rules: {
      "no-undef": "error",
    },
  },
];
