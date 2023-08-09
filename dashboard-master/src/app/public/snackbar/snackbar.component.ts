import { Component, OnInit } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Mensaje, TipoMensaje } from 'src/app/core/models/Mensaje';
import { MensajesService } from 'src/app/core/services/mensajes/mensajes.service';

@Component({
  selector: 'app-snackbar',
  templateUrl: './snackbar.component.html',
  styleUrls: ['./snackbar.component.scss']
})
export class SnackbarComponent implements OnInit {

  // ================= Atributos ================= //

  mensaje: Mensaje ={texto:"", tipo:TipoMensaje.CORRECTO, duracion: 2000};




  // ================= Constructor ================= //

  constructor(private _snackBar: MatSnackBar, private mensajesService: MensajesService)
  {
    this.mensajesService.variableObservable.subscribe((mensaje) => {
      this.mensaje.texto = mensaje.texto;
      this.mensaje.tipo = mensaje.tipo;
      this.mensaje.duracion=mensaje.duracion;

      this.openSnackBar(this.mensaje.texto, "");
    });
  }
  ngOnInit(): void {
    throw new Error('Method not implemented.');
  }

  // ================= Métodos ================= //

  // Lanza un snackbar con una acción y un mensaje determinados
  openSnackBar(message: string, action: string)
  {
    let text : string= "";

    // Modifica el estilo del snackbar dependiendo del tipo de mensaje a enviar
    switch(this.mensaje.tipo)
    {
      case TipoMensaje.CORRECTO:
          this._snackBar.open(message, action, {
            panelClass: ['correcto-snackbar'], duration: this.mensaje.duracion
          });
        break;

      case TipoMensaje.INFO:
        this._snackBar.open(message, action, {
          panelClass: ['info-snackbar'], duration: this.mensaje.duracion
        });
        break;

      case TipoMensaje.WARNING:
        this._snackBar.open(message, action, {
          panelClass: ['warning-snackbar'], duration: this.mensaje.duracion
        });
        break;

      case TipoMensaje.ERROR:
        text = "\u{274C}   " + message ;
        this._snackBar.open(text, action, {
          panelClass: ['error-snackbar'], duration: this.mensaje.duracion
        });
        break;
    }
  }
}
