# -*- coding: utf-8 -*-

"""
    :mod:`site_connectivity`
    ===========================================================================
    :synopsis: offline inter-site connectivity
    :author: Roberto Magán Carrión
    :contact: roberto.magan@uca.es, rmagan@ugr.es, robertomagan@gmail.com
    :organization: University of Cádiz, University of Granada
    :project: I2P Crawler
    :since: 0.0.1
"""

from pony.orm import sql_debug, db_session
from database import dbsettings
from database import dbutils


#sql_debug(True)


def set_connectivity():
    """
    Updates the connectivity summary tables.
    """
    with db_session:
        #finished_sites = dbutils.get_sites_by_processing_status(dbsettings.Status.DISCOVERING)
        sites = dbutils.get_sites()

        for site in sites:
            print(("ID {0} - {1}".format(site.id, site.name)))
            set_site_connectivity_summary(site.name, site.pages)

    print(("TOTAL sites found {0}".format(len(sites))))


def set_site_connectivity_summary(site, pages):
    with db_session:
        n_incoming_links = len(dbutils.get_incoming_links(site))
        n_outgoing_links = len(dbutils.get_outgoing_links(site))
        degree = n_incoming_links + n_outgoing_links
        print(("Adding connectivity summary to {0}, in_links: {1}, out_links: {2}, degree: {3}, out_pages_links: {4}".format(
            site, n_incoming_links, n_outgoing_links, degree, pages)))
        dbutils.set_connectivity_summary(s_url=site, n_incoming=n_incoming_links, n_outgoing=n_outgoing_links,
                                         n_degree=degree, n_pages=pages)


def export_links():
    """
    Export in CSV format the links (edges) among sites.
    """
    with db_session:
        links = dbutils.get_links()

        for link in links:
            print(("{0} - {1}".format(link.src_site.id, link.dst_site.id)))
            #print("{0}{1} --> {1}{2}".format(link.src_site.id, link.src_site.name, link.dst_site.id, link.dst_site.name))

    print(("TOTAL links found {0}".format(len(links))))


def delete_sites(site_id_list):
    with db_session:
        for id in site_id_list:
            print(("Deleting site ID={0}".format(id)))
            dbutils.delete_links_by_site_id(id)
            dbutils.delete_site_by_id(id)

def main():
    # 1) Deleting duplicated nodes which have same b32 and friendly url
    # This list should be computed outside
    duplicated = [3465,
 1771,
 844,
 1441,
 2476,
 712,
 3643,
 1393,
 2445,
 935,
 924,
 24821,
 874,
 1689,
 1045,
 5251,
 787,
 2979,
 1108,
 6622,
 1624,
 6124,
 1774,
 2534,
 1871,
 64,
 3493,
 3718,
 2965,
 501,
 1714,
 1770,
 860,
 1595,
 2665,
 2659,
 469,
 4629,
 1286,
 1517,
 1396,
 244,
 2515,
 237,
 401]
    delete_sites(duplicated)

    # 2) Update connectivity summary table
    set_connectivity()



if __name__ == '__main__':
    main()
