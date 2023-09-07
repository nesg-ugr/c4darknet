import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';


@Injectable({
  providedIn: 'root'
})


export class TemaService
{
  private tema: string = localStorage['tema'];
  private updateTema$: Subject<string> = new Subject<string>();
  public variableObservable = this.updateTema$.asObservable();

  constructor() { }

  public updateTema(newValue: string)
  {
    this.tema = newValue;
    this.updateTema$.next(this.tema);
  }
}
