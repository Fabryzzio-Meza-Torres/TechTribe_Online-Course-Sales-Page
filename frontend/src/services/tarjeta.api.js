import axios from "axios";

const BASE_URL =
  "http://CP-Proyecto-1649315824.us-east-1.elb.amazonaws.com:5002/tarjeta";

export const createTarjeta = async (tarjeta) => {
  const data = await axios.post(BASE_URL, tarjeta);
  console.log(data);
  return data;
};
