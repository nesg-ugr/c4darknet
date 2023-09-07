import { ActivatedRoute } from '@angular/router';
import packageJson from '../../package.json';


export const environment = {
  appVersion: packageJson.version,
  credenciales: {
    usuario: '',
    contrasena: ''
  },
  route: ActivatedRoute,
  production: true,
  endPoint: '',
  endPointAdmin: ''
};

/*
 * For easier debugging in development mode, you can import the following file
 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
 *
 * This import should be commented out in production mode because it will have a negative impact
 * on performance if an error is thrown.
 */
import 'zone.js/plugins/zone-error'; // Included with Angular CLI.import
