import { NgxGraphModule } from '@swimlane/ngx-graph';
import { SharedModule } from './../core/shared/shared.module';
import { PublicRoutingModule } from './public-routing.module';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PublicComponent } from './public.component';
import { HomeComponent } from './home/home.component';
import { HeaderNavComponent, ModalInfo } from './header-nav/header-nav.component';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatChipsModule } from '@angular/material/chips';
import { MatAutocompleteModule } from '@angular/material/autocomplete';
import { ReactiveFormsModule } from '@angular/forms';
import { MatIconModule } from '@angular/material/icon';
import { MatTooltipModule } from '@angular/material/tooltip';
import { DragDropModule} from '@angular/cdk/drag-drop';
import { MatMenuModule } from '@angular/material/menu';
import { BooleanServices } from '../core/services/booleanService/booleanService.service';
import { MensajesService } from '../core/services/mensajes/mensajes.service';
import { RestService } from '../core/services/rest/rest.service';
import { TemaService } from '../core/services/tema/tema.service';
import { SnackbarComponent } from './snackbar/snackbar.component';
import { GrafoIncomingComponent } from './grafo/grafo-incoming/grafo-incoming.component';
import { GrafoOutgoingComponent } from './grafo/grafo-outgoing/grafo-outgoing.component';
import { GrafoCompletoComponent } from './grafo/grafo-completo/grafo-completo.component';
import { GraficasEstaticasComponent } from './graficasEstaticas/graficasEstaticas.component';
import { GraficasDinamicasComponent } from './graficasDinamicas/graficasDinamicas.component';
import { TablasAnalisisComponent } from './tablasAnalisis/tablasAnalisis.component';

@NgModule({
  declarations: [
    PublicComponent,
    HomeComponent,
    HeaderNavComponent,
    ModalInfo,
    GrafoIncomingComponent,
    GrafoOutgoingComponent,
    GrafoCompletoComponent,
    GraficasEstaticasComponent,
    GraficasDinamicasComponent,
    TablasAnalisisComponent
  ],
  imports: [
    CommonModule,
    PublicRoutingModule,
    SharedModule,
    MatPaginatorModule,
    MatChipsModule,
    MatAutocompleteModule,
    ReactiveFormsModule,
    MatIconModule,
    // MonacoEditorModule.forRoot(),
    MatTooltipModule,
    DragDropModule,
    MatMenuModule,
    NgxGraphModule,
  ],
  providers: [
    RestService,
    MensajesService,
    BooleanServices,
    SnackbarComponent,
    // PeticionRespuestaService,
    TemaService,
    // TitleService,
    Location
  ]
})


export class PublicModule { }
