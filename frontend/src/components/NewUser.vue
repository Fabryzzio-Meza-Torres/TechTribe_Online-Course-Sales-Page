<template>
    <div class="form_register">
      <form  @submit.prevent.stop="createUserEvent">
        <h4>Registrate sin costo</h4>
        <div class="form-group">
        <label>Nombre:</label>
        <input type="text" v-model="user.firstname" />
        </div>
        <div class="form-group">
        <label>Apellido:</label>
        <input type="text" v-model="user.lastname" />
        </div>
        <div class="form-group">
        <label>Correo Electronico:</label>
        <input type="email" v-model="user.email" />
        </div>
        <div class="form-group">
        <label>Constraseña:</label>
        <input type="password" v-model="user.contrasena" />
        </div>
        <small id="valueHelp" class="form-text text-muted">Debe de ser alfanumerico y más de 8 caracteress </small>
        <button class="submit-button" type="submit">Registrar</button>
        <p><router-link to="/sing-in">¿Ya tengo Cuenta?</router-link></p>
      </form>
        <div class="user-message-errors" v-if="errorLists.length > 0">
        <ul>
          <li v-for="error in errorLists" :key="error">
            {{ error }}
          </li>
        </ul>
      </div>
    <div v-else>
      <span class="user-message-success">User created Successfully!!</span>
    </div>
    </div>
</template>

<script>
import { signUp } from "@/services/users.api";
export default{
    name:"SignUp",
    data(){
        return{
            firstname:"",
            lastname:"",
            correo:"",
            
        }
    }

}
</script>
<style></style>