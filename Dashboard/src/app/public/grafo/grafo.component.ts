import { Component, OnInit } from '@angular/core';
import { nodes, links } from './data.json'; // Importa los datos del grafo desde tu archivo JSON

interface CustomNode {
  id: string; // Cambiar el tipo a string
  label: string;
}

interface CustomLink {
  id: string;
  source: string;
  target: string;
  label?: string;
}


@Component({
  selector: 'app-grafo',
  templateUrl: './grafo.component.html',
  styleUrls: ['./grafo.component.scss']
})
export class GrafoComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  view: [number, number] = [1900, 910]; // Tamaño de la vista del gráfico
  nodes: CustomNode[] = [
    { id: '11', label: 'YAFI' },
    { id: '2351', label: 'TUI' },
    { id: '5753', label: 'unfiltered' },
    { id: '721', label: 'Search-Freenet' },
    { id: '5', label: 'index' },
    { id: '862', label: 'Search-Freenet' },
    { id: '6', label: 'linkageddon' },
    { id: '706', label: 'nerdageddon' },
    { id: '4', label: 'Index' },
    { id: '2025', label: 'TestIndex' }
  ];

  links: CustomLink[] = [
    { id: '6333', source: '5', target: '11' },
    { id: '32339', source: '706', target: '11' },
    { id: '11231', source: '11', target: '5753' },
    { id: '17688', source: '2351', target: '5753' },
    { id: '12243', source: '11', target: '5' },
    { id: '20810', source: '2351', target: '5' },
    { id: '31012', source: '5753', target: '5' },
    { id: '23709', source: '721', target: '5' },
    { id: '12292', source: '11', target: '6' },
    { id: '20813', source: '2351', target: '6' },
    { id: '31015', source: '5753', target: '6' },
    { id: '24608', source: '721', target: '6' },
    { id: '6345', source: '5', target: '6' },
    { id: '12299', source: '11', target: '2025' },
    { id: '20663', source: '2351', target: '2025' },
    { id: '30865', source: '5753', target: '2025' },
    { id: '25284', source: '721', target: '2025' },
    { id: '7541', source: '5', target: '2025' }
  ];


  layoutOptions = 'dagre';

}
