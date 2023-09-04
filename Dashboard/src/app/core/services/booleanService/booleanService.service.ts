import { Injectable } from '@angular/core';
import { Observable, Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class BooleanServices {
  constructor() { }

  // SideNav
  private updateSideNav$: Subject<boolean> = new Subject<boolean>();
  private variableObservableSideNav = this.updateSideNav$.asObservable();

  public update()
  {
    this.updateSideNav$.next(true);
  }

  public getUpdateVariable(): Observable<boolean>
  {
    return this.variableObservableSideNav;
  }

  // Barra de progreso
  private showProgressBar: boolean = false;
  private updateShowProgressBar$: Subject<boolean> = new Subject<boolean>();
  public variableObservableProgressBar = this.updateShowProgressBar$.asObservable();


  public getShowProgressBar(): boolean
  {
    return this.showProgressBar;
  }

  public updateProgressBar(newValue: boolean)
  {
    this.showProgressBar = newValue;
    this.updateShowProgressBar$.next(this.showProgressBar);
  }

}
