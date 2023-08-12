import { Component } from '@angular/core';
import { Node, Edge } from '@swimlane/ngx-graph'; // Importa los datos del grafo desde tu archivo JSON
import { BooleanServices } from 'src/app/core/services/booleanService/booleanService.service';
import { MensajesService } from 'src/app/core/services/mensajes/mensajes.service';
import { RestService } from 'src/app/core/services/rest/rest.service';

export abstract class GrafoComponent {

  view: [number, number] = [1900, 910]; // Tamaño de la vista del gráfico
  nodes: Node[] = [];

  links: Edge[] = [];


  layoutOptions = {
    orientation: 'LR'
  };

  constructor(protected mensajesService: MensajesService, protected restService: RestService, protected booleanServices: BooleanServices) {


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
