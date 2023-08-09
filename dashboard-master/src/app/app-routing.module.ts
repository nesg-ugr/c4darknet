import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

//Eso hace que Angular use rutas sin hash como /home en lugar de #/home.
import { LocationStrategy, PathLocationStrategy } from '@angular/common';

import { NotFoundComponent } from '../app/core/components/not-found/not-found.component';


const routes: Routes = [
  { path: '', loadChildren: () => import('./public/public.module').then(m => m.PublicModule) },
  { path: '**', component: NotFoundComponent },
];


@NgModule({
  imports: [RouterModule.forRoot(routes, {useHash: true})],
  exports: [RouterModule],
  providers: [
    {provide: LocationStrategy, useClass: PathLocationStrategy}
  ]
})


export class AppRoutingModule { }
