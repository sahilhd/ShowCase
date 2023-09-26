import express from "express";
import jwt from 'jsonwebtoken'
import bcrypt from 'bcrypt'
import {UserModel} from "../models/Users.js"

const router = express.Router();
router.post("/register", async(req, res) => {
    const {username, password} = req.body;
    const user = await UserModel.findOne({username});

    if (user) {return res.json({message : 'already exists'});}
    const securePass = await bcrypt.hash(password, 10)
    const newUser = new UserModel({username, password : securePass});
    await newUser.save();
    res.json({message: 'sucess'});
});

router.post("login", async(req, res) => {
    const {username, password} = req.body;
    const user = await UserModel.findOne({username});
    if (!user){
        return res.json({message: "user does not exist"});
    }
    const isValidPass = await bcrypt.compare(password, user.password);
    if (!isValidPass){return res.json({message: "incorrect"});}

    const token = jwt.sign({id:user._id}, "secret");
    res.json({token, userID: user._id});
});
export {router as userRouter};