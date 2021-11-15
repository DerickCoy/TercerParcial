<template>
<center>
  <a :href="`/resumenlibro/ingresar/`" class="btn btn-info">Crear</a>
  <div class="col-sm-7">
    <div class="card text-center" v-for="input in directory.edges" :key="input.id">
      <div class="card-header">
        <h1 class="card-title">{{ input.node.autor }}</h1>
      </div>
      <div class="card-body">
        <h5>Autor de Libro</h5>
        <p class="card-text">{{ input.node.autorDelLibro }}</p>
      </div>
      <div class="card-body">
        <h5>Libro</h5>
        <p class="card-text">{{ input.node.libro }}</p>
      </div>
      <div class="card-body">
        <h5>Resumen</h5>
        <p class="card-text">{{ input.node.resumen }}</p>
      </div>
      
      <div class="card-footer text-muted">
        <td type="button" class="btn btn-warning"><a :href="`/resumenlibro/editar/${input.node.id}/${input.node.autor}/${input.node.autorDelLibro}/${input.node.libro}/${input.node.resumen}`">Editar</a></td>
      </div>
      <br><br><br>
    </div>
  </div>
</center>
 
</template>
 
<script>
  import axios from 'axios'
  export default{
name: 'LibroData',
    data(){
      return {
    directory: []
      }
    },
    async mounted () {
    try {
  var result = await axios({
    method: 'POST',
    url: 'http://localhost:8000/graphql',
    data: {
      query: `
      {
          allPublicaciones {
                    edges {
                    node {
                        id
                        autor
                        autorDelLibro
                        libro
                        resumen
                    }
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
</script>
