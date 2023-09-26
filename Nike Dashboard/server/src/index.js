import express from "express";
import mongoose from 'mongoose';
import cors from 'cors';
import {userRouter} from './routes/userRoutes.js'
const app = express()

//midleware for the data transfer between frontend
app.use(express.json());
app.use(cors());
app.use("/auth", userRouter);


app.listen(3001, () => console.log("START")) //port for listen 