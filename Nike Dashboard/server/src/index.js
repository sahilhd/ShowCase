//const express = require("express")
import express from 'express';
import mongoose from 'mongoose';
import cors from 'cors';
import { userRouter} from './routes/users.js'
//remove password
const app = express()

app.use(express.json()); // sending data from the front end 
app.use(cors());
app.use("/auth", userRouter);

mongoose.connect("mongodb+srv://sahilhandauni:MERNpassword2003@shoes.mfn7pp7.mongodb.net/shoes?retryWrites=true&w=majority")
app.listen(3001, () => console.log("START")); // start api on port 3001

