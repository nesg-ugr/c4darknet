import { MediaMatcher } from '@angular/cdk/layout';
import { OverlayContainer } from '@angular/cdk/overlay';
import { ChangeDetectorRef, Component, EventEmitter, HostBinding, OnInit, Output, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatSidenav } from '@angular/material/sidenav';
import { Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { TipoMensaje } from 'src/app/core/models/Mensaje';
import { MensajesService } from 'src/app/core/services/mensajes/mensajes.service';
import { TemaService } from 'src/app/core/services/tema/tema.service';
import { SnackbarComponent } from '../snackbar/snackbar.component';
import { BooleanServices } from 'src/app/core/services/booleanService/booleanService.service';
import { UtilsModule } from 'src/app/core/models/Utils/Utils';
import { environment } from 'src/environments/environment.development';

@Component({
  selector: 'app-header-nav',
  templateUrl: './header-nav.component.html',
  styleUrls: ['./header-nav.component.scss']
})
export class HeaderNavComponent implements OnInit {

  // ================= Atributos ================= //

  events: string[] = [];
  suscriberToDelete : Subscription[] = [];
  @ViewChild('snav') sidenav: MatSidenav | undefined;

  @Output() updateTema: EventEmitter<string> = new EventEmitter<string>();
  @HostBinding('class') componentCssClass: any;

  mostrarProgressBar: boolean = false;
  hayLogoCof: boolean = false;

  fillerNav: Array <{
    nombre: string;
    url: string;
    icon: string;
    selected: boolean
  }> = [];

  mensaje: string = "";

  iconoTema: string = '';
  textoTema: string = '';

  tema = localStorage["tema"] == 'lightTheme' ? 'light' : 'dark';

  mobileQuery: MediaQueryList;
  private _mobileQueryListener: () => void;


  // ================= Constructor ================= //

  constructor(changeDetectorRef: ChangeDetectorRef, media: MediaMatcher, public overlayContainer: OverlayContainer,
              private router: Router, private temaService: TemaService, private mensajesService: MensajesService,
              private snackBar: SnackbarComponent, public dialog: MatDialog,
              private booleanServices: BooleanServices)
  {
    this.mobileQuery = media.matchMedia('(max-width: 600px)');
    this._mobileQueryListener = () => changeDetectorRef.detectChanges();
    this.mobileQuery.addEventListener('change', this._mobileQueryListener);

    this.suscriberToDelete.push(this.mensajesService.variableObservable.subscribe((mensaje) => {
      if(mensaje.tipo == TipoMensaje.ERROR || mensaje.tipo == TipoMensaje.WARNING)
        this.mensaje = mensaje.texto;
      else
        this.snackBar.openSnackBar(mensaje.texto, "");
    }));

    this.suscriberToDelete.push(this.temaService.variableObservable.subscribe(tema => {
      this.tema = tema == 'lightTheme' ? 'light' : 'dark';
    }));

    this.fillerNav = [{nombre: 'Gráficas estáticas', url: 'graficas-estaticas', icon: 'show_chart', selected: false},{nombre: 'Gráficas dinámicas', url: 'graficas-dinamicas', icon: 'query_stats', selected: false},
                      {nombre: 'Descargar CSV grafo completo', url: 'grafo-completo', icon: 'download', selected: false},{nombre: 'Grafo outgoing', url: 'grafo-outgoing', icon: 'account_tree', selected: false},
                      {nombre: 'Grafo incoming', url: 'grafo-incoming', icon: 'account_tree', selected: false}, {nombre: 'Tablas', url: 'tablas', icon: 'table_view', selected: false}
                    ]
  }

  ngOnInit()
  {

    // Establecemos el modo oscuro por defecto
    if (localStorage['tema'] === undefined)
      localStorage['tema'] = "darkTheme";

    if (localStorage['color'] === undefined)
      localStorage['color'] = "Cyan";

    this.onSetTheme(true);
  }

  ngOnDestroy():void{
    this.mobileQuery.removeEventListener('change', this._mobileQueryListener);
    for(let subscribe of this.suscriberToDelete){
      if (subscribe) {
        subscribe.unsubscribe();
      }
    }

    this.suscriberToDelete = [];
  }

  ngAfterViewInit()
  {
    this.suscriberToDelete.push(this.booleanServices.variableObservableProgressBar.subscribe((valor: boolean) => {
      this.mostrarProgressBar = valor;
    }));
  }

  // ================= Métodos ================= //

  // Redirecciona al usuario al login o al home dependiendo de si ha iniciado o no sesión
  redireccionar()
  {
    this.router.navigate(["/home"]);
  }

  // Redirecciona al usuario a un enlace a en una pestaña nueva
  redireccionarEnNuevaPestana(event: MouseEvent)
  {
    this.redireccionarPestanaNueva();
  }

  redireccionarPestanaNueva() {
    UtilsModule.openNewTab('home',this.router);
  }

  // Abre un modal con información acerca del sitio web
  abrirInfo()
  {
    const dialogRef = this.dialog.open(ModalInfo, {
      width: '40vw',
      maxHeight: '80vh',
    });
  }

  // Cierra la sesión de un usuario
  cerrarSesion()
  {
    sessionStorage.clear();
    this.router.navigate(["/login"]);
    this.mensajesService.sendMessage("Desconectado", TipoMensaje.INFO);
  }

  // Establece el tema de la aplicación
  public onSetTheme(reset :boolean = false)
  {
    if(!reset){
      localStorage['tema'] = localStorage['tema'] === 'lightTheme' ? 'darkTheme' : 'lightTheme';
    }
    const container = this.overlayContainer.getContainerElement();
    container.classList.remove('lightTheme' + localStorage['color'], 'darkTheme' + localStorage['color']);
    container.classList.add(localStorage['tema'] + localStorage['color']);

    this.componentCssClass = localStorage['tema'] + localStorage['color'];
    this.iconoTema = localStorage['tema'] === 'lightTheme' ? 'brightness_4' : 'brightness_5';
    this.textoTema = localStorage['tema'] === 'lightTheme' ? 'Modo oscuro' : 'Modo claro';

    const themeButton = document.getElementById('themeButton');

    if (themeButton)
    {
      if (this.textoTema === 'Modo oscuro')
        themeButton.classList.add('rotateR');

      if (this.textoTema === 'Modo claro')
        themeButton.classList.add('rotateL');

      themeButton.addEventListener('animationend', () => {
        this.iconoTema = localStorage['tema'] === 'lightTheme' ? 'brightness_4' : 'brightness_5';
        this.textoTema = localStorage['tema'] === 'lightTheme' ? 'Modo oscuro' : 'Modo claro';
        themeButton.classList.remove('rotateL');
        themeButton.classList.remove('rotateR');
      }, { once: true });
    }

    this.temaService.updateTema(localStorage['tema']);

  }

  // Establece el color primario de la aplicación
  public onSetColor(color: string)
  {
    const container = this.overlayContainer.getContainerElement();
    container.classList.remove('lightTheme' + localStorage['color'], 'darkTheme' + localStorage['color']);

    localStorage['color'] = color;
    this.componentCssClass = localStorage['tema'] + localStorage['color'];
    localStorage['classCSS'] = this.componentCssClass;

    container.classList.add(localStorage['classCSS'] );
  }
}






// Modal para mostrar la info
@Component({
  selector: 'info',
  templateUrl: './info.html',
  styleUrls: ['./header-nav.component.scss']
})


export class ModalInfo
{
  titulo: string = 'Dashboard';
  version: string = environment.appVersion;
  copyright: string = '\u00A9 2023 Juan Miguel Hernández Gómez';
  descripcion: string = 'Son muchos los trabajos que han estudiado la Deep Web, en concreto las Darknets. Sin embargo, la mayoría de ellos se centran en el contenido y la información de los sitios ocultos y no en como se relacionan entre ellos. Aquí se abordará dicha cuestión haciendo uso de la herramienta C4Darknet para cual se diseñará un dashboard que permita la visualización en tiempo real del grafo completo de conectividad entre sitios en las Darknet.';
  usuario: string = 'Juan Miguel Hernández Gómez';

  constructor() { }

  obtenerColorTexto()
  {
    return localStorage['tema'] === 'darkTheme' ? 'white' : 'black';
  }
}
