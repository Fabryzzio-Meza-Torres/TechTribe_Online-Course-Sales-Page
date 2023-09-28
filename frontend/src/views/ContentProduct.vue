<template>
  <div class="tarjeta-form">
    <form @submit.prevent.stop="CreateTarjetaEvent">
      <div class="form-group">
        <label>Numero de Tarjeta: </label>
        <input
          type="text"
          v-model="credit_card.creditcard_number"
          placeholder="Numero de Tarjeta"
          required
        />
      </div>
      <div class="form-group">
        <label>Fecha de Vencimiento: </label>
        <input
          type="text"
          v-model="credit_card.expiration_date"
          placeholder="Fecha de Vencimiento"
          required
        />
      </div>
      <div class="form-group">
        <label>Codigo de Seguridad: </label>
        <input
          type="text"
          v-model="credit_card.password"
          placeholder="Contraseña requerida"
          required
        />
      </div>
      <!-- botton -->
      <button type="submit" class="btn-submit">Pagar!</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "ContentProduct",
  components: {},
  mounted() {},
  data() {
    return {
      id: this.$route.params,
      credit_card: {
        creditcard_number: "",
        expiration_date: "",
        password: "",
      },
    };
  },
  created() {},
  methods: {
    CreateTarjetaEvent() {
      console.log(this.id);
    },
  },
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: sans-serif;
}

body {
  height: 100vh;
  background-color: #000;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.formulario {
  width: 400px;
  background-color: #192d3e;
  border: 5px solid #17133f;
  border-radius: 10px;
  padding: 30px 60px;
  text-align: center;
  margin-top: 20px;
}

.formulario h2 {
  margin-bottom: 20px;
  color: #fff;
}

.input-label {
  font-weight: bold;
  color: #fff;
}

input {
  height: 40px;
  border: 2px solid #17133f;
  border-radius: 10px;
  padding: 0 8px;
  color: #000;
  background-color: #fff;
}

.btn-submit {
  margin-top: 20px;
  cursor: pointer;
  border: none;
  height: 40px;
  background-color: #192d3e;
  box-shadow: 1px 1px 2px #000;
  color: #fff;
}

.btn-submit:hover {
  background-color: #0f1c26;
}

.message {
  color: #fff;
  font-size: 14px;
  font-weight: bold;
  margin-top: 10px;
}

.success {
  color: #4caf50;
}

.error {
  color: #f44336;
}

.tarjeta-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.tarjeta-form form {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.tarjeta-form form .form-group {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.tarjeta-form form .form-group label {
  color: #fff;
  font-size: 20px;
  font-weight: bold;
}

.tarjeta-form form .form-group input {
  margin-top: 10px;
  width: 300px;
  height: 40px;
  border: 2px solid #17133f;
  border-radius: 10px;
  padding: 0 8px;
  color: #000;
  background-color: #fff;
}

.tarjeta-form form .form-group input:focus {
  outline: none;
}

.tarjeta-form form .form-group input::placeholder {
  color: #000;
}

.tarjeta-form form .form-group input[type="submit"] {
  margin-top: 20px;
  cursor: pointer;
  border: none;
  height: 40px;
  background-color: #192d3e;
  box-shadow: 1px 1px 2px #000;
  color: #fff;
}

.tarjeta-form form .form-group input[type="submit"]:hover {
  background-color: #0f1c26;
}

.tarjeta-form form .form-group .message {
  color: #fff;
  font-size: 14px;
  font-weight: bold;
  margin-top: 10px;
}

.tarjeta-form form .form-group .success {
  color: #4caf50;
}

.tarjeta-form form .form-group .error {
  color: #f44336;
}

.tarjeta-form form .form-group .btn-submit {
  margin-top: 20px;
  padding: 10px;
  cursor: pointer;
  border: none;
  height: 40px;
  background-color: #192d3e;
  box-shadow: 1px 1px 2px #000;
  color: #fff;
  border-radius: 10px;
}
</style>
