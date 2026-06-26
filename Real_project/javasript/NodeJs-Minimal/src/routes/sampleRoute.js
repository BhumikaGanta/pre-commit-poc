// src/routes/sampleRoute.js
const express = require("express");
const router = express.Router();
const { getAllSamples } = require("../controllers/sampleController");

router.get("/samples", getAllSamples);

module.exports = router;
