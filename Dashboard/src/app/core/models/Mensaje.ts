export enum TipoMensaje {
  CORRECTO,
  ERROR,
  WARNING,
  INFO,
}

export interface Mensaje {
  texto: string
  tipo: TipoMensaje
  duracion: number
}
