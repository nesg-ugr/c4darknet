import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';
import { Mensaje, TipoMensaje } from '../../models/Mensaje';


@Injectable({
  providedIn: 'root'
})


export class MensajesService
{
  private mensajes: Mensaje[] = [];
  private enviarMensaje$: Subject<Mensaje> = new Subject<Mensaje>();
  public variableObservable = this.enviarMensaje$.asObservable();

  constructor() { }

  // public getMensaje(i:number): string
  // {
  //   return this.mensajes[i].texto;
  // }

  // public getMensajes(): Mensaje []
  // {
  //   return this.mensajes;
  // }

  // Para usar el servicio importarlo en el constructor, y llamar a este metodo con parametro (true o false)
  public sendMessage(newValue: string, _tipo : TipoMensaje, duracion:number = 2000)
  {
    this.mensajes.push({texto:newValue, tipo:_tipo, duracion: duracion});
    this.enviarMensaje$.next(this.mensajes[this.mensajes.length - 1]);
  }
}
