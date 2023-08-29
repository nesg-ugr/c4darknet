import { Component, OnInit } from '@angular/core';
import { TipoMensaje } from 'src/app/core/models/Mensaje';
import { BooleanServices } from 'src/app/core/services/booleanService/booleanService.service';
import { MensajesService } from 'src/app/core/services/mensajes/mensajes.service';
import { RestService } from 'src/app/core/services/rest/rest.service';

@Component({
  selector: 'app-temporizador',
  templateUrl: './temporizador.component.html',
  styleUrls: ['./temporizador.component.scss']
})
export class TemporizadorComponent implements OnInit {

  timer: number = 10 * 60; // Tiempo total en segundos
  countdown: number = this.timer;
  interval: any;

  constructor(protected mensajesService: MensajesService, protected restService: RestService, protected booleanServices: BooleanServices) { }

  ngOnInit(): void {
    this.startCountdown();
    this.restService.get('getTimer').subscribe({
      next: (response) => {
        if (response.getTimerResponse) {
          this.timer=response.getTimerResponse.timer;
          this.countdown = response.getTimerResponse.time_left;
        }
      },
      error: (error) => {
        this.mensajesService.sendMessage(error.message, TipoMensaje.ERROR);
      }
    });

  }

  formatTime(timeInSeconds: number): string {
    const minutes = Math.floor(timeInSeconds / 60);
    const seconds = timeInSeconds % 60;
    return `${this.padZero(minutes)}:${this.padZero(seconds)}`;
  }

  padZero(value: number): string {
    return value < 10 ? `0${value}` : `${value}`;
  }

  startCountdown(): void {
    this.interval = setInterval(() => {
      if (this.countdown > 0) {
        this.countdown--;
      } else {
        this.resetCountdown();
      }
    }, 1000);
  }

  resetCountdown(): void {
    clearInterval(this.interval);
    this.countdown = this.timer; // Reiniciar el tiempo
    this.startCountdown(); // Iniciar el temporizador nuevamente
    this.refrescarCache();
  }

  refrescarCache(){
    this.restService.get('actualizarCache').subscribe({
      next: (response) => {
        if (response.actualizarCacheResponse.status = 'correcto') {
          this.mensajesService.sendMessage("Cache actualizada", TipoMensaje.INFO, 2500)
        }
      },
      error: (error) => {
        this.mensajesService.sendMessage("No se pudo actualizar la cache", TipoMensaje.ERROR);
      }
    });
  }
}
