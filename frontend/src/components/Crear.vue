<template>
 
  <center>
    <div>
    <h1>Ingresar nueva Resumen de Libro</h1>
    <br>
    <form  action="" @submit.prevent="mounted()">
      <div class="col-sm-7">
         <div class="card-header">
        <h3>Autor</h3>
        <input v-model="autor" autor="" type="text" class="form-control">
        <h3>Autor del Libro</h3>
        <input v-model="autorDelLibro" autorDelLibro="" type="text" class="form-control">
        <h3>Libro</h3>
        <input v-model="libro" libro="" type="text" class="form-control">
        <h3>Resumen</h3>
        
        <textarea resumen="" type="text" class="form-control" rows="3" input v-model="resumen" ></textarea>
        <br>
        <button type="submit" onclick="location.href='http://localhost:8080/resumenlibro/listar/';" class="btn btn-warning" name="button">Ingresar</button>
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
        autor: '',
        autorDelLibro: '',
        libro: '',
        resumen: '',
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
  createPublicacion(input:{autor:"`+this.autor+`",autorDelLibro:"`+this.autorDelLibro+`",libro:"`+this.libro+`",resumen:"`+this.resumen+`"}){
    Publicacion{
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
        this.directory = result.data.data.allPublicaciones
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>
