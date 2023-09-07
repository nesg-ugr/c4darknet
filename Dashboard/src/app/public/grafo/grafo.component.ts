import { Node, Edge } from '@swimlane/ngx-graph'; // Importa los datos del grafo desde tu archivo JSON
import { BooleanServices } from 'src/app/core/services/booleanService/booleanService.service';
import { MensajesService } from 'src/app/core/services/mensajes/mensajes.service';
import { RestService } from 'src/app/core/services/rest/rest.service';

export abstract class GrafoComponent {

  view: [number, number] = [1900, 910]; // Tamaño de la vista del gráfico
  nodes: Node[] = [];

  links: Edge[] = [];

  maxWidth: number = 0;
  maxHeight: number= 0;


  layoutOptions = {
    orientation: 'LR'
  };

  constructor(protected mensajesService: MensajesService, protected restService: RestService, protected booleanServices: BooleanServices) {
    this.updateMaxDimensions();
  }



  updateMaxDimensions() {
    this.maxWidth = window.innerWidth;
    this.maxHeight = window.innerHeight;
    this.view = [this.maxWidth, this.maxHeight - 80]
  }

  randomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

}
