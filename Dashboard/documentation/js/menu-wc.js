'use strict';

customElements.define('compodoc-menu', class extends HTMLElement {
    constructor() {
        super();
        this.isNormalMode = this.getAttribute('mode') === 'normal';
    }

    connectedCallback() {
        this.render(this.isNormalMode);
    }

    render(isNormalMode) {
        let tp = lithtml.html(`
        <nav>
            <ul class="list">
                <li class="title">
                    <a href="index.html" data-type="index-link">dashboard documentation</a>
                </li>

                <li class="divider"></li>
                ${ isNormalMode ? `<div id="book-search-input" role="search"><input type="text" placeholder="Type to search"></div>` : '' }
                <li class="chapter">
                    <a data-type="chapter-link" href="index.html"><span class="icon ion-ios-home"></span>Getting started</a>
                    <ul class="links">
                        <li class="link">
                            <a href="overview.html" data-type="chapter-link">
                                <span class="icon ion-ios-keypad"></span>Overview
                            </a>
                        </li>
                        <li class="link">
                            <a href="index.html" data-type="chapter-link">
                                <span class="icon ion-ios-paper"></span>README
                            </a>
                        </li>
                                <li class="link">
                                    <a href="dependencies.html" data-type="chapter-link">
                                        <span class="icon ion-ios-list"></span>Dependencies
                                    </a>
                                </li>
                                <li class="link">
                                    <a href="properties.html" data-type="chapter-link">
                                        <span class="icon ion-ios-apps"></span>Properties
                                    </a>
                                </li>
                    </ul>
                </li>
                    <li class="chapter modules">
                        <a data-type="chapter-link" href="modules.html">
                            <div class="menu-toggler linked" data-bs-toggle="collapse" ${ isNormalMode ?
                                'data-bs-target="#modules-links"' : 'data-bs-target="#xs-modules-links"' }>
                                <span class="icon ion-ios-archive"></span>
                                <span class="link-name">Modules</span>
                                <span class="icon ion-ios-arrow-down"></span>
                            </div>
                        </a>
                        <ul class="links collapse " ${ isNormalMode ? 'id="modules-links"' : 'id="xs-modules-links"' }>
                            <li class="link">
                                <a href="modules/AppModule.html" data-type="entity-link" >AppModule</a>
                                    <li class="chapter inner">
                                        <div class="simple menu-toggler" data-bs-toggle="collapse" ${ isNormalMode ?
                                            'data-bs-target="#components-links-module-AppModule-1e39b885592866f8cf3d9e38c3feca844131a7e988ec4e3daaf153cf4b8bcf0d2761078216b9dd08b1e9cc1aa7c1f2695a4dc95d98fcb6201888f8bcd5d85ad5"' : 'data-bs-target="#xs-components-links-module-AppModule-1e39b885592866f8cf3d9e38c3feca844131a7e988ec4e3daaf153cf4b8bcf0d2761078216b9dd08b1e9cc1aa7c1f2695a4dc95d98fcb6201888f8bcd5d85ad5"' }>
                                            <span class="icon ion-md-cog"></span>
                                            <span>Components</span>
                                            <span class="icon ion-ios-arrow-down"></span>
                                        </div>
                                        <ul class="links collapse" ${ isNormalMode ? 'id="components-links-module-AppModule-1e39b885592866f8cf3d9e38c3feca844131a7e988ec4e3daaf153cf4b8bcf0d2761078216b9dd08b1e9cc1aa7c1f2695a4dc95d98fcb6201888f8bcd5d85ad5"' :
                                            'id="xs-components-links-module-AppModule-1e39b885592866f8cf3d9e38c3feca844131a7e988ec4e3daaf153cf4b8bcf0d2761078216b9dd08b1e9cc1aa7c1f2695a4dc95d98fcb6201888f8bcd5d85ad5"' }>
                                            <li class="link">
                                                <a href="components/AppComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >AppComponent</a>
                                            </li>
                                        </ul>
                                    </li>
                            </li>
                            <li class="link">
                                <a href="modules/AppRoutingModule.html" data-type="entity-link" >AppRoutingModule</a>
                            </li>
                            <li class="link">
                                <a href="modules/CoreModule.html" data-type="entity-link" >CoreModule</a>
                            </li>
                            <li class="link">
                                <a href="modules/MaterialModule.html" data-type="entity-link" >MaterialModule</a>
                            </li>
                            <li class="link">
                                <a href="modules/PublicModule.html" data-type="entity-link" >PublicModule</a>
                                    <li class="chapter inner">
                                        <div class="simple menu-toggler" data-bs-toggle="collapse" ${ isNormalMode ?
                                            'data-bs-target="#components-links-module-PublicModule-7af31ca73256c94a7f4d67fdc8f33095438cc576636bc84271c267f8311914ec684b8f52344dced01509d2655e60e6e80336b3399488cae1872bde5176fa4bd6"' : 'data-bs-target="#xs-components-links-module-PublicModule-7af31ca73256c94a7f4d67fdc8f33095438cc576636bc84271c267f8311914ec684b8f52344dced01509d2655e60e6e80336b3399488cae1872bde5176fa4bd6"' }>
                                            <span class="icon ion-md-cog"></span>
                                            <span>Components</span>
                                            <span class="icon ion-ios-arrow-down"></span>
                                        </div>
                                        <ul class="links collapse" ${ isNormalMode ? 'id="components-links-module-PublicModule-7af31ca73256c94a7f4d67fdc8f33095438cc576636bc84271c267f8311914ec684b8f52344dced01509d2655e60e6e80336b3399488cae1872bde5176fa4bd6"' :
                                            'id="xs-components-links-module-PublicModule-7af31ca73256c94a7f4d67fdc8f33095438cc576636bc84271c267f8311914ec684b8f52344dced01509d2655e60e6e80336b3399488cae1872bde5176fa4bd6"' }>
                                            <li class="link">
                                                <a href="components/GraficasDinamicasComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >GraficasDinamicasComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/GraficasEstaticasComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >GraficasEstaticasComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/GrafoCompletoComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >GrafoCompletoComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/GrafoIncomingComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >GrafoIncomingComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/GrafoOutgoingComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >GrafoOutgoingComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/HeaderNavComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >HeaderNavComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/HomeComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >HomeComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/ModalInfo.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >ModalInfo</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/PublicComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >PublicComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/TablasAnalisisComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >TablasAnalisisComponent</a>
                                            </li>
                                            <li class="link">
                                                <a href="components/TemporizadorComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >TemporizadorComponent</a>
                                            </li>
                                        </ul>
                                    </li>
                                <li class="chapter inner">
                                    <div class="simple menu-toggler" data-bs-toggle="collapse" ${ isNormalMode ?
                                        'data-bs-target="#injectables-links-module-PublicModule-7af31ca73256c94a7f4d67fdc8f33095438cc576636bc84271c267f8311914ec684b8f52344dced01509d2655e60e6e80336b3399488cae1872bde5176fa4bd6"' : 'data-bs-target="#xs-injectables-links-module-PublicModule-7af31ca73256c94a7f4d67fdc8f33095438cc576636bc84271c267f8311914ec684b8f52344dced01509d2655e60e6e80336b3399488cae1872bde5176fa4bd6"' }>
                                        <span class="icon ion-md-arrow-round-down"></span>
                                        <span>Injectables</span>
                                        <span class="icon ion-ios-arrow-down"></span>
                                    </div>
                                    <ul class="links collapse" ${ isNormalMode ? 'id="injectables-links-module-PublicModule-7af31ca73256c94a7f4d67fdc8f33095438cc576636bc84271c267f8311914ec684b8f52344dced01509d2655e60e6e80336b3399488cae1872bde5176fa4bd6"' :
                                        'id="xs-injectables-links-module-PublicModule-7af31ca73256c94a7f4d67fdc8f33095438cc576636bc84271c267f8311914ec684b8f52344dced01509d2655e60e6e80336b3399488cae1872bde5176fa4bd6"' }>
                                        <li class="link">
                                            <a href="injectables/BooleanServices.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >BooleanServices</a>
                                        </li>
                                        <li class="link">
                                            <a href="injectables/MensajesService.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >MensajesService</a>
                                        </li>
                                        <li class="link">
                                            <a href="injectables/RestService.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >RestService</a>
                                        </li>
                                        <li class="link">
                                            <a href="injectables/TemaService.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >TemaService</a>
                                        </li>
                                    </ul>
                                </li>
                            </li>
                            <li class="link">
                                <a href="modules/PublicRoutingModule.html" data-type="entity-link" >PublicRoutingModule</a>
                            </li>
                            <li class="link">
                                <a href="modules/SharedModule.html" data-type="entity-link" >SharedModule</a>
                                    <li class="chapter inner">
                                        <div class="simple menu-toggler" data-bs-toggle="collapse" ${ isNormalMode ?
                                            'data-bs-target="#components-links-module-SharedModule-ba282537496428b91cc4cf59869e406c7a6f26ecb4d3ab7db2bca0160736d892dcd66a7472dd8daf628b8ada85c35f44e9249d8170b46592d84d7689ddbae03f"' : 'data-bs-target="#xs-components-links-module-SharedModule-ba282537496428b91cc4cf59869e406c7a6f26ecb4d3ab7db2bca0160736d892dcd66a7472dd8daf628b8ada85c35f44e9249d8170b46592d84d7689ddbae03f"' }>
                                            <span class="icon ion-md-cog"></span>
                                            <span>Components</span>
                                            <span class="icon ion-ios-arrow-down"></span>
                                        </div>
                                        <ul class="links collapse" ${ isNormalMode ? 'id="components-links-module-SharedModule-ba282537496428b91cc4cf59869e406c7a6f26ecb4d3ab7db2bca0160736d892dcd66a7472dd8daf628b8ada85c35f44e9249d8170b46592d84d7689ddbae03f"' :
                                            'id="xs-components-links-module-SharedModule-ba282537496428b91cc4cf59869e406c7a6f26ecb4d3ab7db2bca0160736d892dcd66a7472dd8daf628b8ada85c35f44e9249d8170b46592d84d7689ddbae03f"' }>
                                            <li class="link">
                                                <a href="components/NotFoundComponent.html" data-type="entity-link" data-context="sub-entity" data-context-id="modules" >NotFoundComponent</a>
                                            </li>
                                        </ul>
                                    </li>
                            </li>
                </ul>
                </li>
                    <li class="chapter">
                        <div class="simple menu-toggler" data-bs-toggle="collapse" ${ isNormalMode ? 'data-bs-target="#components-links"' :
                            'data-bs-target="#xs-components-links"' }>
                            <span class="icon ion-md-cog"></span>
                            <span>Components</span>
                            <span class="icon ion-ios-arrow-down"></span>
                        </div>
                        <ul class="links collapse " ${ isNormalMode ? 'id="components-links"' : 'id="xs-components-links"' }>
                            <li class="link">
                                <a href="components/SnackbarComponent.html" data-type="entity-link" >SnackbarComponent</a>
                            </li>
                        </ul>
                    </li>
                    <li class="chapter">
                        <div class="simple menu-toggler" data-bs-toggle="collapse" ${ isNormalMode ? 'data-bs-target="#classes-links"' :
                            'data-bs-target="#xs-classes-links"' }>
                            <span class="icon ion-ios-paper"></span>
                            <span>Classes</span>
                            <span class="icon ion-ios-arrow-down"></span>
                        </div>
                        <ul class="links collapse " ${ isNormalMode ? 'id="classes-links"' : 'id="xs-classes-links"' }>
                            <li class="link">
                                <a href="classes/GrafoComponent.html" data-type="entity-link" >GrafoComponent</a>
                            </li>
                            <li class="link">
                                <a href="classes/UtilsModule.html" data-type="entity-link" >UtilsModule</a>
                            </li>
                        </ul>
                    </li>
                        <li class="chapter">
                            <div class="simple menu-toggler" data-bs-toggle="collapse" ${ isNormalMode ? 'data-bs-target="#injectables-links"' :
                                'data-bs-target="#xs-injectables-links"' }>
                                <span class="icon ion-md-arrow-round-down"></span>
                                <span>Injectables</span>
                                <span class="icon ion-ios-arrow-down"></span>
                            </div>
                            <ul class="links collapse " ${ isNormalMode ? 'id="injectables-links"' : 'id="xs-injectables-links"' }>
                                <li class="link">
                                    <a href="injectables/BooleanServices.html" data-type="entity-link" >BooleanServices</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/MensajesService.html" data-type="entity-link" >MensajesService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/RestService.html" data-type="entity-link" >RestService</a>
                                </li>
                                <li class="link">
                                    <a href="injectables/TemaService.html" data-type="entity-link" >TemaService</a>
                                </li>
                            </ul>
                        </li>
                    <li class="chapter">
                        <div class="simple menu-toggler" data-bs-toggle="collapse" ${ isNormalMode ? 'data-bs-target="#interfaces-links"' :
                            'data-bs-target="#xs-interfaces-links"' }>
                            <span class="icon ion-md-information-circle-outline"></span>
                            <span>Interfaces</span>
                            <span class="icon ion-ios-arrow-down"></span>
                        </div>
                        <ul class="links collapse " ${ isNormalMode ? ' id="interfaces-links"' : 'id="xs-interfaces-links"' }>
                            <li class="link">
                                <a href="interfaces/CustomLink.html" data-type="entity-link" >CustomLink</a>
                            </li>
                            <li class="link">
                                <a href="interfaces/CustomNode.html" data-type="entity-link" >CustomNode</a>
                            </li>
                            <li class="link">
                                <a href="interfaces/Mensaje.html" data-type="entity-link" >Mensaje</a>
                            </li>
                        </ul>
                    </li>
                    <li class="chapter">
                        <div class="simple menu-toggler" data-bs-toggle="collapse" ${ isNormalMode ? 'data-bs-target="#miscellaneous-links"'
                            : 'data-bs-target="#xs-miscellaneous-links"' }>
                            <span class="icon ion-ios-cube"></span>
                            <span>Miscellaneous</span>
                            <span class="icon ion-ios-arrow-down"></span>
                        </div>
                        <ul class="links collapse " ${ isNormalMode ? 'id="miscellaneous-links"' : 'id="xs-miscellaneous-links"' }>
                            <li class="link">
                                <a href="miscellaneous/enumerations.html" data-type="entity-link">Enums</a>
                            </li>
                            <li class="link">
                                <a href="miscellaneous/variables.html" data-type="entity-link">Variables</a>
                            </li>
                        </ul>
                    </li>
                        <li class="chapter">
                            <a data-type="chapter-link" href="routes.html"><span class="icon ion-ios-git-branch"></span>Routes</a>
                        </li>
                    <li class="chapter">
                        <a data-type="chapter-link" href="coverage.html"><span class="icon ion-ios-stats"></span>Documentation coverage</a>
                    </li>
                    <li class="divider"></li>
                    <li class="copyright">
                        Documentation generated using <a href="https://compodoc.app/" target="_blank" rel="noopener noreferrer">
                            <img data-src="images/compodoc-vectorise.png" class="img-responsive" data-type="compodoc-logo">
                        </a>
                    </li>
            </ul>
        </nav>
        `);
        this.innerHTML = tp.strings;
    }
});