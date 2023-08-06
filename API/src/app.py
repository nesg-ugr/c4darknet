import os
import sys
from flask import Flask, jsonify, request
from config import config

from pony.orm import db_session

from urllib.parse import unquote


# Obtenemos la ruta absoluta del directorio que contiene el archivo app.py
current_directory = os.path.abspath(os.path.dirname(__file__))

# Obtenemos la ruta del directorio que contiene el módulo dbutils.py
crawler_directory = os.path.join(current_directory, '..', '..', 'crawler')

# Obtenemos la ruta del directorio que contiene el módulo dbutils.py
api_directory = os.path.join(current_directory, '..')

# Agregamos el directorio del módulo al sys.path
sys.path.append(crawler_directory)
sys.path.append(api_directory)

import database.dbutils as dbutils # Importamos todo el módulo dbutils.py
import models.sites as sites# Importa el módulo sites desde la carpeta models

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World!</h1>"

@app.route('/get_sites', methods=['GET'])
def get_sites():
    # Llamamos a la función get_sites() desde el módulo dbutils.py
    sites_list = dbutils.get_sites()

    # Crear una lista de instancias de la clase SiteData con los datos de los sitios
    sites_data = [
        sites.SiteData(
            id=site.id,
            name=site.name,
            error_tries=site.error_tries,
            discovering_tries=site.discovering_tries,
            pages=site.pages,
            uuid=site.uuid,
            type=str(site.type),
            current_status=str(site.current_status),
            source=str(site.source),
            timestamp=site.timestamp,
            timestamp_s=site.timestamp_s
        ).to_dict() for site in sites_list
    ]

    # Devuelve los resultados como JSON
    return jsonify(sites_data)


from pony.flask import db_session

@app.route('/get_site_by_id/<int:s_id>', methods=['GET'])
def get_site_by_id(s_id):
    with db_session:
        # Llamamos a la función get_site_by_id() desde el módulo dbutils.py, pasando el valor de s_id como argumento
        site = dbutils.get_site_by_id(s_id)

        if site is not None:
            # Crear una instancia de la clase SiteData con los datos del sitio
            site_data = sites.SiteData(
                id=site.id,
                name=site.name,
                error_tries=site.error_tries,
                discovering_tries=site.discovering_tries,
                pages=site.pages,
                uuid=site.uuid,
                type=str(site.type),
                current_status=str(site.current_status),
                source=str(site.source),
                timestamp=site.timestamp,
                timestamp_s=site.timestamp_s
            )

            # Devolver los datos del sitio como JSON utilizando el método to_dict
            return jsonify(site_data.to_dict())
        else:
            # Si el sitio no fue encontrado, devuelve un mensaje de error
            return jsonify({"error": "Site not found"}), 404




@app.route('/get_links', methods=['GET'])
def get_links():
    with db_session:
        # Llamamos a la función get_links() desde el módulo dbutils.py
        links_list = dbutils.get_links()

        # Crear una lista de diccionarios con los datos de los enlaces
        links_data = []
        for link in links_list:
            # Convertir los objetos Multiset en listas
            dst_sites = list(link.dst_site)
            src_sites = list(link.src_site)
            
            # Crear diccionarios para los sitios de destino y origen
            dst_site_attributes = {
                "id": dst_sites[0].id if dst_sites else None,
                "name": dst_sites[0].name if dst_sites else None
            }
            src_site_attributes = {
                "id": src_sites[0].id if src_sites else None,
                "name": src_sites[0].name if src_sites else None
            }

            # Agregar los atributos a la lista de enlaces
            links_data.append({
                "id": link.id,
                "dst_site": dst_site_attributes,
                "src_site": src_site_attributes
            })

        # Devuelve los resultados como JSON
        return jsonify(links_data)



@app.route('/get_incoming_links_by_site_id/<int:ts_id>', methods=['GET'])
def get_incoming_links_by_site_id(ts_id):
    with db_session:
        # Llamamos a la función get_incoming_links_by_site_id() desde el módulo dbutils.py, pasando el valor de ts_id como argumento
        incoming_links = dbutils.get_incoming_links_by_site_id(ts_id)

        if incoming_links:
            # Crear una lista de diccionarios con los datos de los enlaces entrantes
            links_data = []
            for link in incoming_links:
                # Convertir los objetos Multiset en listas
                dst_sites = list(link.dst_site)
                src_sites = list(link.src_site)
                
                # Crear diccionarios para los sitios de destino y origen
                dst_site_attributes = {
                    "id": dst_sites[0].id if dst_sites else None,
                    "name": dst_sites[0].name if dst_sites else None
                }
                src_site_attributes = {
                    "id": src_sites[0].id if src_sites else None,
                    "name": src_sites[0].name if src_sites else None
                }

                # Agregar los atributos a la lista de enlaces
                links_data.append({
                    "id": link.id,
                    "dst_site": dst_site_attributes,
                    "src_site": src_site_attributes
                })

            # Devuelve los resultados como JSON
            return jsonify(links_data)
        else:
            # Si el sitio no fue encontrado, devuelve un mensaje de error
            return jsonify({"error": "Site not found"}), 404

@app.route('/get_incoming_links/<path:ts_url>', methods=['GET'], strict_slashes=False)
def get_incoming_links(ts_url):
    # Decodifica la URL para obtener la URL original
    ts_url = unquote(ts_url)

    with db_session:
        # Llamamos a la función get_incoming_links() desde el módulo dbutils.py, pasando la URL como argumento
        incoming_links = dbutils.get_incoming_links(ts_url)

        if incoming_links:
            #for attribute in dir(incoming_links[0]):
            #    print(f"{attribute}: {getattr(incoming_links[0], attribute)}")
                
            # Crear una lista de diccionarios con los datos de los enlaces entrantes
            links_data = []
            for link in incoming_links:
                # Convertir los objetos Multiset en listas
                dst_sites = list(link.dst_site)
                src_sites = list(link.src_site)
                
                # Crear diccionarios para los sitios de destino y origen
                dst_site_attributes = {
                    "id": dst_sites[0].id if dst_sites else None,
                    "name": dst_sites[0].name if dst_sites else None
                }
                src_site_attributes = {
                    "id": src_sites[0].id if src_sites else None,
                    "name": src_sites[0].name if src_sites else None
                }

                # Agregar los atributos a la lista de enlaces
                links_data.append({
                    "id": link.id,
                    "dst_site": dst_site_attributes,
                    "src_site": src_site_attributes
                })

            # Devuelve los resultados como JSON
            return jsonify(links_data)
        else:
            # Si el sitio no fue encontrado, devuelve un mensaje de error
            return jsonify({"error": "Site not found"}), 404
        




if __name__ == '__main__': 
    app.config.from_object(config['development'])
    app.run()

