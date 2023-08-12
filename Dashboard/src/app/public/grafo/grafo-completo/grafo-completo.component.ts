import { Component, OnInit } from '@angular/core';
import { throwError } from 'rxjs';
import { BooleanServices } from 'src/app/core/services/booleanService/booleanService.service';
import { MensajesService } from 'src/app/core/services/mensajes/mensajes.service';
import { RestService } from 'src/app/core/services/rest/rest.service';
import { GrafoComponent } from '../grafo.component';
import { UtilsModule } from 'src/app/core/models/Utils/Utils';

@Component({
  selector: 'app-grafo-completo',
  templateUrl: './grafo-completo.component.html',
  styleUrls: ['./grafo-completo.component.scss']
})
export class GrafoCompletoComponent extends GrafoComponent implements OnInit {

  constructor(mensajesService: MensajesService, restService: RestService, booleanServices: BooleanServices) {

    super(mensajesService,restService,booleanServices);

  }

  ngOnInit() {
    this.restService.get('getCompressedCSVs').subscribe({
      next: (response) => {
        const zipBase64: string = response.archivos_zip;

        if (zipBase64) {
          // Decodificar el contenido Base64 a un arreglo de bytes
          const zipBytes = this.base64ToArrayBuffer(zipBase64);

          // Crear un Blob con los bytes del archivo ZIP
          const blob = new Blob([zipBytes], { type: 'application/zip' });

          // Crear una URL descargable para el Blob
          const url = URL.createObjectURL(blob);

          // Crear un enlace de descarga y hacer clic en él
          const a = document.createElement('a');
          a.href = url;
          a.download = 'grafo.zip';
          a.click();

          // Liberar la URL creada
          URL.revokeObjectURL(url);
        }

        this.booleanServices.updateProgressBar(false);
      },
      error: (error) => {
        this.booleanServices.updateProgressBar(false);
        throwError(() => error);
      }
    });
  }

  // Función para decodificar Base64 a un arreglo de bytes
  private base64ToArrayBuffer(base64: string): ArrayBuffer {
    const binaryString = atob(base64);
    const length = binaryString.length;
    const bytes = new Uint8Array(length);
    for (let i = 0; i < length; i++) {
      bytes[i] = binaryString.charCodeAt(i);
    }
    return bytes.buffer;
  }


}
