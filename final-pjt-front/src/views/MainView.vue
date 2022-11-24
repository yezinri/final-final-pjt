<template>
  <div>
    <div class="container mt-5">
      <h1 class="fw-bold text-center" style="color: #00ABB3;">whyisitreal</h1>
      <div class="d-flex justify-content-center py-3">
        <button @click="goSignup" class="btn btn-primary mb-2" style="background-color: #00ABB3; border: #00ABB3; box-shadow: 0 4px 4px -2px black;">join us</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MainView',
  methods: {
    goSignup() {
      this.$router.push({ name:'signup' })
    }
  }
}
</script>

<style>

</style>