import Vue from 'vue'
import VueRouter from 'vue-router'
import Listar from '@/components/Listar'
import Editar from '@/components/Editar'
import Crear from '@/components/Crear'
 
Vue.use(VueRouter)
 
const routes = [  
  {
    path: '/resumenlibro/listar',
    name: 'listar',
    component: Listar
  },
  {
    path: '/resumenlibro/ingresar',
    name: 'Ingresar',
    component: Crear
  },
  {
    path: '/resumenlibro/editar/:id/:autor/:autorDelLibro/:libro/:resumen',
    name: 'Editar',
    component: Editar
  },
]
 
const router = new VueRouter({
  routes: routes,
  mode: 'history',
})
export default router