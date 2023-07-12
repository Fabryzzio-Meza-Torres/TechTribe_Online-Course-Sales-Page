import axios from "axios";

const BASE_URL = "http://127.0.0.1:5002/profesores";

export const getAllProfesores = async () => {
  const data = await axios.get(BASE_URL);
  console.log(data);
  return data;
};
