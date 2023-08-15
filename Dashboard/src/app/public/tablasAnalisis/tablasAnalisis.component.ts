import { LiveAnnouncer } from '@angular/cdk/a11y';
import { AfterViewInit, Component, OnInit, QueryList, ViewChild, ViewChildren } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort, Sort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { TipoMensaje } from 'src/app/core/models/Mensaje';
import { BooleanServices } from 'src/app/core/services/booleanService/booleanService.service';
import { MensajesService } from 'src/app/core/services/mensajes/mensajes.service';
import { RestService } from 'src/app/core/services/rest/rest.service';


@Component({
  selector: 'app-tablasAnalisis',
  templateUrl: './tablasAnalisis.component.html',
  styleUrls: ['./tablasAnalisis.component.scss']
})

export class TablasAnalisisComponent implements OnInit, AfterViewInit {
  displayedColumns: string[][] = [];

  dataSources: MatTableDataSource<any>[] = []; // Array de dataSources
  cargado: boolean = false;
  titulos: string[] = [];

  metodos: string [] = [];

  constructor(private _liveAnnouncer: LiveAnnouncer, protected mensajesService: MensajesService, protected restService: RestService, protected booleanServices: BooleanServices) {}

  @ViewChild(MatSort) sort: MatSort;

  ngAfterViewInit() {
  }

  ngOnInit() {
    this.mensajesService.sendMessage("Generando tablas", TipoMensaje.INFO);
    this.booleanServices.updateProgressBar(true);

    this.restService.get('obtenerTablas').subscribe({
      next: (response) => {
        if (response ) {

          response.obtenerTablasResponse.forEach((element: any) => {

            // Obtener las claves excluyendo "titulo"
            let metodo = Object.keys(element).toString();
            this.titulos.push(element[metodo].titulo);

            const keysExcludingTitulo = Object.keys(element[metodo]).filter(key => key !== 'titulo');

            let columns = ['position'];
            columns.push(...Object.keys(element[metodo][keysExcludingTitulo[0]][0]))
            this.displayedColumns.push(columns);

            this.dataSources.push(new MatTableDataSource(element[metodo][keysExcludingTitulo[0]]));

            metodo = metodo.replace('Response', '');
            this.metodos.push(metodo);

          });

          this.booleanServices.updateProgressBar(false);
          this.cargado = true;

          this.dataSources.forEach((dataSource) => {
            dataSource.sort = this.sort;
          });

          this.mensajesService.sendMessage("Mostrando " + this.dataSources.length + " tablas", TipoMensaje.CORRECTO, 3500)
        }
      },
      error: (error) => {
        this.booleanServices.updateProgressBar(false);
        this.mensajesService.sendMessage(error.message, TipoMensaje.ERROR);
      }
    });
  }

  pedirDatos(index: number){
    this.mensajesService.sendMessage("Actualizando tabla", TipoMensaje.INFO);
    this.booleanServices.updateProgressBar(true);

    const inputField = document.getElementById('inputField'+index) as HTMLInputElement;
    const valor = inputField.value;

    this.restService.get(this.metodos[index]+'/'+valor).subscribe({
      next: (response) => {
        if (response ) {

          const keysExcludingTitulo = Object.keys(response[this.metodos[index]+'Response']).filter(key => key !== 'titulo');

          this.dataSources[index]= new MatTableDataSource(response[this.metodos[index]+'Response'][keysExcludingTitulo[0]]);

          this.booleanServices.updateProgressBar(false);
          this.cargado = true;

          this.dataSources.forEach((dataSource) => {
            dataSource.sort = this.sort;
          });

          this.mensajesService.sendMessage("Tabla " + this.titulos[index] + " actualizada", TipoMensaje.CORRECTO, 5000)
        }
      },
      error: (error) => {
        this.booleanServices.updateProgressBar(false);
        this.mensajesService.sendMessage(error.message, TipoMensaje.ERROR);
      }
    });
  }

  announceSortChange(sortState: Sort) {
    if (sortState.direction) {
      this._liveAnnouncer.announce(`Sorted ${sortState.direction}ending`);
    } else {
      this._liveAnnouncer.announce('Sorting cleared');
    }
  }
}
