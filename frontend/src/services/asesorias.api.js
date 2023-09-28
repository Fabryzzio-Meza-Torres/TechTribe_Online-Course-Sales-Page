import axios from "axios";

const BASE_URL = "http://127.0.0.1:5001/productos/asesorias";

export const getAllAsesorias = async () => {
  const data = await axios.get(BASE_URL);

  return data;
};
