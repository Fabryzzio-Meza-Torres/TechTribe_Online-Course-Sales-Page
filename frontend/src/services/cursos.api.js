import axios from "axios";

const BASE_URL =
  "http://CP-Proyecto-1649315824.us-east-1.elb.amazonaws.com:5001/productos/cursos";

export const getAllCursos = async () => {
  const data = await axios.get(BASE_URL);
  console.log(data);
  return data;
};
