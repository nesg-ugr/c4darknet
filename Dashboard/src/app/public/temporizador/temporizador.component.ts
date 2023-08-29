import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-temporizador',
  templateUrl: './temporizador.component.html',
  styleUrls: ['./temporizador.component.scss']
})
export class TemporizadorComponent implements OnInit {

  countdown: number = 10; // Tiempo inicial en segundos
  interval: any;

  constructor() { }

  ngOnInit(): void {
    this.startCountdown();
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
    this.countdown = 10; // Reiniciar el tiempo
    this.startCountdown(); // Iniciar el temporizador nuevamente
  }
}
