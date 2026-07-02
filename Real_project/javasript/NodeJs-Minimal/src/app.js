// src/app.js
const express = require("express");
const app = express();
const sampleRoute = require("./routes/sampleRoute");

app.use(express.json());
app.use("/api", sampleRoute);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
