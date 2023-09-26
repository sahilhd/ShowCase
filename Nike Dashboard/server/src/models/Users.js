import mongoose from "mongoose";

const Userschema = new mongoose.Schema({
    username: {type: String, required: true, unique: true},
    password: {type: String, required: true},
});

export const UserModel = mongoose.model("users", Userschema)