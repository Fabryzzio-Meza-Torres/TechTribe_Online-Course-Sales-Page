import axios from "axios";

const API_URL =
  "http://CP-Proyecto-1649315824.us-east-1.elb.amazonaws.com:5002/transactions";

export default {
  async createTransaccion(pago, id_tarjeta) {
    try {
      const response = await axios.post(`${API_URL}/transactions`, {
        pago,
        id_tarjeta,
      });

      return response.data;
    } catch (error) {
      throw error.response.data;
    }
  },
};
