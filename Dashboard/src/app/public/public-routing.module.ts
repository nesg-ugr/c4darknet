import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { PublicComponent } from './public.component';
import { GrafoOutgoingComponent } from './grafo/grafo-outgoing/grafo-outgoing.component';
import { GrafoIncomingComponent } from './grafo/grafo-incoming/grafo-incoming.component';
import { GrafoCompletoComponent } from './grafo/grafo-completo/grafo-completo.component';
import { GraficasEstaticasComponent } from './graficasEstaticas/graficasEstaticas.component';
import { GraficasDinamicasComponent } from './graficasDinamicas/graficasDinamicas.component';
import { TablasAnalisisComponent } from './tablasAnalisis/tablasAnalisis.component';


const routes: Routes = [
  {
    path: '', component: PublicComponent, children:
    [
      { path: '', redirectTo: 'tablas', pathMatch: 'full' },
      // { path: 'login',component: LoginComponent,  canActivate: [canActivate], data: { url:"login" }},
      // { path: 'home', component: HomeComponent },
      { path: 'graficas-estaticas', component: GraficasEstaticasComponent },
      { path: 'graficas-dinamicas', component: GraficasDinamicasComponent },
      { path: 'grafo-completo', component: GrafoCompletoComponent },
      { path: 'grafo-outgoing', component: GrafoOutgoingComponent },
      { path: 'grafo-incoming', component: GrafoIncomingComponent },
      { path: 'tablas', component: TablasAnalisisComponent },
      // { path: 'admin', component: AdminComponent, canActivate: [canActivate] },
    ]
  },

];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})


export class PublicRoutingModule { }
