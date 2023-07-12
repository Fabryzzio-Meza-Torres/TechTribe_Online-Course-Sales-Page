import axios from "axios";

const BASE_URL = "http://127.0.0.1:5002/tarjeta";

export const createTarjeta = async (tarjeta) => {
  const data = await axios.post(BASE_URL, tarjeta);
  console.log(data);
  return data;
};
