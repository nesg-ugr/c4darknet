import { Component, HostListener, OnInit } from '@angular/core';
import { GrafoComponent } from '../grafo.component';
import { throwError } from 'rxjs';
import { BooleanServices } from 'src/app/core/services/booleanService/booleanService.service';
import { MensajesService } from 'src/app/core/services/mensajes/mensajes.service';
import { RestService } from 'src/app/core/services/rest/rest.service';
import { TipoMensaje } from 'src/app/core/models/Mensaje';

@Component({
  selector: 'app-grafo-incoming',
  templateUrl: './grafo-incoming.component.html',
  styleUrls: ['./grafo-incoming.component.scss']
})
export class GrafoIncomingComponent extends GrafoComponent implements OnInit {

  constructor(mensajesService: MensajesService, restService: RestService, booleanServices: BooleanServices) {

    super(mensajesService,restService,booleanServices);


  }

  ngOnInit() {

    this.booleanServices.updateProgressBar(true);

    this.restService.get('generarArchivosJSONGrafoTopIncoming').subscribe({
      next: (response) => {
        if (response.generarArchivosJSONGrafoTopIncomingResponse != undefined) {
          this.nodes = response.generarArchivosJSONGrafoTopIncomingResponse.nodos;
          this.links = response.generarArchivosJSONGrafoTopIncomingResponse.aristas;

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
