import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { environment } from '../../../../environments/environment.development';


const options = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
};


@Injectable({
  providedIn: 'root'
})


export class RestService
{
  bodyXML: string = "";

  constructor(private http: HttpClient) { }

  toArray(response: any[]): any[]
  {
    let result = [];

    if (response instanceof Array)
      result = response;
    else
      result.push(response);

    return result;
  }

  // ================ PETICIONES REST ================ //

  post(body: string, metodo: string, url:string =environment.endPoint): Observable<any>
  {
    return this.http.post(url + metodo, body, options).pipe(
      catchError(this.handleError)
    )
  }

  // Método para realizar una solicitud GET
  get(metodo: string, url: string = environment.endPoint): Observable<any> {
    return this.http.get(url + metodo, options).pipe(
      catchError(this.handleError)
    );
  }

  private handleError(error: Response)
  {
    console.log('Código: ' + error.status);
    console.log('Mensaje: ' + error.statusText + ' en ' + error.url);

    return throwError(() => error);
  }
}
