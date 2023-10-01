import axios from "axios";

const BASE_URL =
  "http://CP-Proyecto-1649315824.us-east-1.elb.amazonaws.com:5000/register";

export const signUp = async (user) => {
  try {
    const response = await axios.post(BASE_URL, user);
    console.log("data: ", response.data);
    return response.data;
  } catch (error) {
    console.log("error here: ", error);
  }
};
