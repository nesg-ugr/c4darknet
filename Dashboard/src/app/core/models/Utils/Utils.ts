
import { ungzip,gzip } from 'pako';
import * as CryptoJS from 'crypto-js';
import { Router } from '@angular/router';

export class UtilsModule  {

  private static uint8ToString(arr:Uint8Array):string{
    return  Array(arr.length)
          .fill('')
          .map((_, i) => String.fromCharCode(arr[i]))
          .join('')

  }
  public static gzip(preguntaSOAP : string): string{

    var compress_gzip = gzip(preguntaSOAP);
    return window.btoa(this.uint8ToString(compress_gzip));
  }

  public static ungzip (preguntaSOAP: string): string{

    let gezipedData = window.atob(preguntaSOAP)
    let gzipedDataArray = Uint8Array.from(gezipedData, c => c.charCodeAt(0))
    let ungzipedData = ungzip(gzipedDataArray);


    return new TextDecoder().decode(ungzipedData);
  }

  public obtenerColorTexto()
  {
    return localStorage['tema'] === 'darkTheme' ? 'white' : 'black';
  }

  public static stringToBase64 (cadena: string): string{
    return window.btoa(cadena)
  }

  public static base64ToString (base64Data: string): string{
    return window.atob(base64Data)
  }

  // Elimina una subcadena en la última posicion encontrada en otra cadena
  public static eliminarFromString(searchValue: string, originalString: string)
  {
    let lastIndex = originalString.lastIndexOf(searchValue);

    if (lastIndex === -1)
      return originalString; // La subcadena no se encuentra en la cadena original

    return originalString.slice(0, lastIndex) + originalString.slice(lastIndex + searchValue.length);
  }

  public static async cifrarContrasena(contrasena: string)
  {
    const hash = CryptoJS.SHA512(contrasena).toString();
    return hash;
  }


  public static openNewTab(url_relative: string, router: Router){
    const baseUrl = window.location.href.replace(router.url,'');
    window.open(baseUrl + "/"+url_relative,'_blank');
  }

}
