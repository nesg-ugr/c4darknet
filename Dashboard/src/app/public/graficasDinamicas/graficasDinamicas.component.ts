import { Component, OnInit } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { TipoMensaje } from 'src/app/core/models/Mensaje';
import { BooleanServices } from 'src/app/core/services/booleanService/booleanService.service';
import { MensajesService } from 'src/app/core/services/mensajes/mensajes.service';
import { RestService } from 'src/app/core/services/rest/rest.service';

@Component({
  selector: 'app-graficasDinamicas',
  templateUrl: './graficasDinamicas.component.html',
  styleUrls: ['./graficasDinamicas.component.scss']
})
export class GraficasDinamicasComponent implements OnInit {

  graficas : any[] = [];
  cargado: boolean = false;

  metodos: string [] = [];
  cantidadRegistrosControls: FormControl[] = [];

  constructor(protected mensajesService: MensajesService, protected restService: RestService, protected booleanServices: BooleanServices) { }

  ngOnInit() {
    this.mensajesService.sendMessage("Generando gráficas dinámicas", TipoMensaje.INFO);
    this.booleanServices.updateProgressBar(true);

    this.restService.get('obtenerGraficasDinamicas').subscribe({
      next: (response) => {
        if (response.obtenerGraficasDinamicasResponse) {
          // this.graficas = response;

          // this.cargado = true;

          response.obtenerGraficasDinamicasResponse.forEach((element: any) => {

            // Obtener las claves excluyendo "titulo"
            let metodo = Object.keys(element).toString();

            const keysExcludingTitulo = Object.keys(element[metodo]).filter(key => key !== 'titulo');

            this.graficas.push(element[metodo]);



            this.cantidadRegistrosControls.push(new FormControl('', [Validators.pattern('^[0-9]*$')]));


            metodo = metodo.replace('Response', '');
            this.metodos.push(metodo);
          });

          this.cargado = true;
          this.booleanServices.updateProgressBar(false);
          this.mensajesService.sendMessage("Mostrando " + this.graficas.length + " gráficas", TipoMensaje.CORRECTO, 3500)
        }
      },
      error: (error) => {
        this.booleanServices.updateProgressBar(false);
        this.mensajesService.sendMessage(error.message, TipoMensaje.ERROR);
        // throwError(() => error);
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

          this.graficas[index]= response[this.metodos[index]+'Response'];

          this.booleanServices.updateProgressBar(false);
          this.cargado = true;

          this.mensajesService.sendMessage("Gráfica " + this.graficas[index].titulo + " actualizada", TipoMensaje.CORRECTO, 5000)
        }
      },
      error: (error) => {
        this.booleanServices.updateProgressBar(false);
        this.mensajesService.sendMessage(error.message, TipoMensaje.ERROR, 5000);
      }
    });
  }

}
