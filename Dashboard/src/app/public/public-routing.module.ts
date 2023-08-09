import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { PublicComponent } from './public.component';


const routes: Routes = [
  {
    path: '', component: PublicComponent, children:
    [
      { path: '', redirectTo: 'home', pathMatch: 'full' },
      // { path: 'login',component: LoginComponent,  canActivate: [canActivate], data: { url:"login" }},
      { path: 'home', component: HomeComponent },
      // { path: 'admin', component: AdminComponent, canActivate: [canActivate] },
    ]
  },

];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})


export class PublicRoutingModule { }
