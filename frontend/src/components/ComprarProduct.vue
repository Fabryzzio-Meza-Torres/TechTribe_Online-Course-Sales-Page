<template>
<div class="tarjeta-form">
    <form @submit.prevent.stop="CreateTarjetaEvent">
    <div class="form-group">
    <label>Numero de Tarjeta: </label>
    <input type="text" v-model="credit_card.creditcard_number" placeholder="Numero de Tarjeta" required>
    </div>
    <div class="form-group">
    <label>Fecha de Vencimiento: </label>
    <input type="text" v-model="credit_card.expiration_date" placeholder="Fecha de Vencimiento" required>
    </div>
    <div class="form-group">
    <label>Codigo de Seguridad: </label>
    <input type="text" v-model="credit_card.password" placeholder="Contraseña requerida" required>
    </div>
    </form>

</div>
</template>
<script></script>