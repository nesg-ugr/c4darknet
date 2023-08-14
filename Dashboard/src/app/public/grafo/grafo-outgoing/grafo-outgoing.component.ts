import { Component, HostListener, OnInit } from '@angular/core';
import { throwError } from 'rxjs';
import { BooleanServices } from 'src/app/core/services/booleanService/booleanService.service';
import { MensajesService } from 'src/app/core/services/mensajes/mensajes.service';
import { RestService } from 'src/app/core/services/rest/rest.service';
import { GrafoComponent } from '../grafo.component';
import { TipoMensaje } from 'src/app/core/models/Mensaje';

@Component({
  selector: 'app-grafo-outgoing',
  templateUrl: './grafo-outgoing.component.html',
  styleUrls: ['./grafo-outgoing.component.scss']
})
export class GrafoOutgoingComponent extends GrafoComponent implements OnInit {

  constructor(mensajesService: MensajesService, restService: RestService, booleanServices: BooleanServices) {

    super(mensajesService,restService,booleanServices);


  }

  ngOnInit() {

    this.booleanServices.updateProgressBar(true);

    this.restService.get('generarArchivosJSONGrafoTopOutgoing').subscribe({
      next: (response) => {
        if (response.generarArchivosJSONGrafoTopOutgoingResponse != undefined)
        {
          this.nodes = response.generarArchivosJSONGrafoTopOutgoingResponse.nodos;
          this.links = response.generarArchivosJSONGrafoTopOutgoingResponse.aristas;

          this.nodes = this.nodes.map(node => ({ ...node, color: this.randomColor() }));
        }
        this.booleanServices.updateProgressBar(false);
      },
      error: (error) => {
        this.booleanServices.updateProgressBar(false);
        this.mensajesService.sendMessage(error.message, TipoMensaje.ERROR);
      }
    });
  }

  @HostListener('window:resize', ['$event'])
  onResize(event: any) {
    this.updateMaxDimensions();
  }

}
