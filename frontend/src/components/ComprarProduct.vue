<template>
  <div class="formulario-compra">
    <h2>Formulario de Compra</h2>
    <form @submit.prevent="submitCompra">
      <div>
        <label for="creditcard_number">Número de Tarjeta:</label>
        <input type="text" v-model="numeroTarjeta" required />
      </div>
      <div>
        <label for="expiration_date">Fecha de Expiración:</label>
        <input type="text" v-model="expiracion" required />
      </div>
      <div>
        <label for="password">Código de Seguridad (CVV):</label>
        <input type="text" v-model="password" required />
      </div>
      <button type="submit">Realizar Compra</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      numeroTarjeta: "",
      expiracion: "",
      password: "",
      monto: "100",
    };
  },
  methods: {
    async submitCompra() {
      const compra = {
        creditcard_number: this.numeroTarjeta,
        expiration_date: this.expiracion,
        password: this.password,
      };

      try {
        const response = await axios.post(
          "http://CP-Proyecto-1649315824.us-east-1.elb.amazonaws.com:5002/transactions",
          compra
        );

        if (response && response.data.success) {
          console.log("Compra realizada con éxito", response.data);

          setTimeout(() => {
            alert("Gracias por tu compra");
            this.$router.push({ name: "home" });
          }, 2000);
        } else {
          console.error("Error al realizar la compra", response.data.message);
        }
      } catch (error) {
        console.error("Error al realizar la compra", error);
      }
    },
  },
};
</script>

<style scoped>
.formulario-compra {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 400px;
  background-color: #192d3e;
  border: 5px solid #17133f;
  border-radius: 10px;
  padding: 30px 60px;
  text-align: center;
  margin-top: 20px;
}

.formulario-compra h2 {
  font-size: 24px;
  margin-bottom: 20px;
  text-align: center;
}

.formulario-compra label {
  display: block;
  margin-bottom: 5px;
}

.formulario-compra input {
  width: 100%;
  background: #24303c;
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 16px;
  border: 1px solid #1f53c5;
  font-family: "calibri";
  font-size: 18px;
  color: white;
}

.formulario-compra button {
  width: 320px;
  background: #1f53c5;
  border: none;
  padding: 12px;
  color: white;
  margin: 16px 0;
  font-size: 16px;
}

.formulario-compra button:hover {
  background-color: #0f1c26;
}
</style>
