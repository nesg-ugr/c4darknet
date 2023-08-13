import { Component, OnInit } from '@angular/core';
import { throwError } from 'rxjs';
import { TipoMensaje } from 'src/app/core/models/Mensaje';
import { BooleanServices } from 'src/app/core/services/booleanService/booleanService.service';
import { MensajesService } from 'src/app/core/services/mensajes/mensajes.service';
import { RestService } from 'src/app/core/services/rest/rest.service';

@Component({
  selector: 'app-graficasEstaticas',
  templateUrl: './graficasEstaticas.component.html',
  styleUrls: ['./graficasEstaticas.component.scss']
})
export class GraficasEstaticasComponent implements OnInit {

  graficas : any
  cargado: boolean = false;

  constructor(protected mensajesService: MensajesService, protected restService: RestService, protected booleanServices: BooleanServices) { }

  ngOnInit() {

    this.mensajesService.sendMessage("Generando gráficas estáticas", TipoMensaje.INFO)
    this.booleanServices.updateProgressBar(true);

    this.restService.get('obtenerGraficasEstaticas').subscribe({
      next: (response) => {
        if (response && Array.isArray(response)) {
          this.graficas = response;
          this.booleanServices.updateProgressBar(false);
          this.cargado = true;

          this.mensajesService.sendMessage("Mostrando " + this.graficas.length + " gráficas", TipoMensaje.CORRECTO, 3500)
        }
      },
      error: (error) => {
        this.booleanServices.updateProgressBar(false);
        throwError(() => error);
      }
    });

  }

}
