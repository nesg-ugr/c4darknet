import { NgModule } from '@angular/core';
import { CommonModule, registerLocaleData } from '@angular/common';
import localeEs from '@angular/common/locales/es';

registerLocaleData(localeEs, 'es');


@NgModule({
  declarations: [],
  imports: [
    CommonModule,
  ]
})


export class CoreModule { }
