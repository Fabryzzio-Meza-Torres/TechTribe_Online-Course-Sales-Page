import axios from "axios";

const BASE_URL =
  "http://CP-Proyecto-1649315824.us-east-1.elb.amazonaws.com:5001/profesores";

export const getAllProfesores = async () => {
  const data = await axios.get(BASE_URL);
  console.log(data);
  return data;
};
