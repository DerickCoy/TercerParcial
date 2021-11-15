<template>
 
    <center>
    <div>
    <h1>Actualizar Resumen</h1>
    <br>
    <h2>ID: {{id=$route.params.id}} </h2>
    <form  action="" @submit.prevent="mounted()">
      <div class="col-sm-7">
         <div class="card-header">
        <h3>Autor</h3>
        <input v-model="autor" type="text" class="form-control">
        <h3>Autor del Libro</h3>
        <input v-model="autorDelLibro" type="text" class="form-control">
        <h3>Libro</h3>
        <input v-model="libro" type="text" class="form-control">
        <h3>Resumen</h3>
        <textarea class="form-control" rows="3" input v-model="resumen"></textarea>
        <br>
        <button type="submit" onclick="location.href='http://localhost:8080/resumenlibro/listar/';" class="btn btn-success" name="button">Actualizar</button>
        </div>
      </div>
    </form>
  </div>
  </center>
 
</template>
 
<script>
  import axios from 'axios'
  export default{
    autor: 'LibroData',
    data(){
      return {
        autor: this.$route.params.autor,
        autorDelLibro: this.$route.params.autorDelLibro,
        libro: this.$route.params.libro,
        resumen: this.$route.params.resumen,
        id: '',
        directory: []
      }
    },
    methods: {
    async mounted () {
  try {
        var result = await axios({
          method: 'POST',
          url: 'http://localhost:8000/graphql',
          data: {
            query: `
            mutation{
  updatePublicacion(input:{id:"`+this.id+`", autor:"`+this.autor+`",autorDelLibro:"`+this.autorDelLibro+`",libro:"`+this.libro+`"resumen:"`+this.resumen+`"}){
    Publicacion{
      id
      autor
      autorDelLibro
      libro
      resumen
    }
  }
}
 
            `
          }
        })
        this.directory = result.data.data.allCategories
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>
 
