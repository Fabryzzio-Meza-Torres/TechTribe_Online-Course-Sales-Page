<template>
  <div>
    <div v-if="!paidFor">
      <h1 class="Title">Compra de este Curso - ${{ product.price }}</h1>
      <img
        :src="require(`@/assets/Tech.jpg`)"
        alt="Compra"
        class="imagen-compra"
      />
      <div id="paypal-button-container"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CompraPaypal",
  data: function () {
    return {
      loaded: false,
      paidFor: false,
      product: {
        price: 100.0,
        description: "Más que un curso, una experiencia que cambiará tu vida",
        img: "@/assets/Tech.jpg",
      },
    };
  },
  mounted: function () {
    const script = document.createElement("script");
    script.src =
      "ATljcOCG8lV7KWR_DoyMTbYIBWgy9e7SYry3N6mNYsM3CYm5TUo5YfDZ8kD-O8Hw9VelreIqhP1q_oeR";
    script.addEventListener("load", () => this.setLoaded());
    document.body.appendChild(script);
  },
  methods: {
    setLoaded: function () {
      this.loaded = true;
      window.paypal
        .Buttons({
          createOrder: (data, actions) => {
            return actions.order.create({
              purchase_units: [
                {
                  description: this.product.description,
                  amount: {
                    currency_code: "USD",
                    value: this.product.price,
                  },
                },
              ],
            });
          },
          onApprove: (data, actions) => {
            return actions.order.capture().then((details) => {
              this.paidFor = true;
              console.log(details);
            });
          },
        })
        .render("#paypal-button-container");
    },
  },
};
</script>

<style>
.imagen-compra {
  width: 500px;
  height: 400px;
}
.Title {
  text-align: center;
  font-size: 50px;
  font-family: "Roboto", sans-serif;
  color: white;
  margin-top: 50px;
  margin-bottom: 50px;
}
</style>
