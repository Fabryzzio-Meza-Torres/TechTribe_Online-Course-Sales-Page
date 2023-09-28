<template>
  <div class="login">
    <div class="formulario">
      <h2 class="form-title">INICIAR SESIÓN</h2>

      <!-- Formulario de inicio de sesión -->
      <form @submit.prevent="loginEvent" class="form-container">
        <div class="form-group">
          <label for="email" class="input-label">Correo Electrónico</label>
          <input
            type="email"
            id="email"
            v-model="email"
            placeholder="Ingrese su correo electrónico"
            required
          />
        </div>

        <div class="form-group">
          <label for="password" class="input-label">Contraseña</label>
          <input
            type="password"
            id="password"
            v-model="password"
            placeholder="Ingrese su contraseña"
            required
          />
        </div>

        <button type="submit" class="btn-submit">Iniciar Sesión</button>
      </form>

      <!-- Mensaje de éxito o error -->
      <div
        v-if="message"
        :class="{ success: success, error: !success }"
        class="message"
      >
        {{ message }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SignIn",
  data() {
    return {
      email: "",
      password: "",
      message: "",
      success: false,
    };
  },
  methods: {
    async loginEvent() {
      let user = {
        email: this.email,
        password: this.password,
      };
      fetch("http://127.0.0.1:5000" + "/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(user),
      })
        .then((res) => {
          return res.json();
        })
        .then((data) => {
          if (data && data.success) {
            this.success = true;
            this.message = "Inicio de sesión exitoso!";
            //imprimir cookie de flask session
            console.log(data);
            //guardar la cookie en cookie
            document.cookie = "session=" + data.cookie;
            setTimeout(() => {
              window.location.href = "/";
            }, 1000);
          } else {
            this.message = "Credenciales incorrectas!";
            this.success = false;
          }
          return data;
        })
        .catch((err) => console.log(err));
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
</style>
