# -*- coding: utf-8 -*-

"""
    :mod:`monitor`
    ===========================================================================
    :synopsis: For monitoring process status
    :author: Roberto Magán Carrión
    :contact: roberto.magan@uca.es, rmagan@ugr.es, robertomagan@gmail.com
    :organization: University of Cádiz, University of Granada
    :project: I2P Crawler
    :since: 0.0.1
"""

import psutil as ps
import datetime
import time
import argparse


def monitoring(pid, interval):

    """

    System and process monitoring. It is monitors process with the desired pid.

    :param pid: int, PID of the process to monitor
    :param interval: int, sample interval in seconds.
    """

    process = ps.Process(pid=pid)

    ts = datetime.datetime.now()

    SEP = ","

    head = "ts,pid," \
           "p_status," \
           "p_cpu_percent," \
           "p_mem_percent," \
           "p_mem_rss," \
           "p_mem_vms," \
           "p_mem_shared," \
           "p_mem_uss," \
           "p_mem_pss," \
           "p_mem_swap," \
           "s_mem_total," \
           "s_mem_available," \
           "s_mem_used," \
           "s_mem_free," \
           "s_swap_total," \
           "s_swap_used," \
           "s_swap_free," \
           "s_swap_percent," \
           "s_cpu_percent" + "\n"

    with open(str(pid) + "_output.csv", "w") as f:

        f.writelines(head)
        f.flush()

        while 1:

            ts = ts + datetime.timedelta(seconds=interval)

            p_info = process.as_dict()
            p_mem_info = p_info['memory_full_info']
            s_mem_info = ps.virtual_memory()
            s_swap_info = ps.swap_memory()

            to_write = str(ts) + SEP
            to_write += str(p_info['pid']) + SEP
            to_write += p_info['status'] + SEP
            to_write += str(p_info['cpu_percent']) + SEP
            to_write += str(p_info['memory_percent']) + SEP
            to_write += str(p_mem_info.rss) + SEP
            to_write += str(p_mem_info.vms) + SEP
            to_write += str(p_mem_info.shared) + SEP
            to_write += str(p_mem_info.uss) + SEP
            to_write += str(p_mem_info.pss) + SEP
            to_write += str(p_mem_info.swap) + SEP
            to_write += str(s_mem_info.total) + SEP
            to_write += str(s_mem_info.available) + SEP
            to_write += str(s_mem_info.used) + SEP
            to_write += str(s_mem_info.free) + SEP
            to_write += str(s_swap_info.total) + SEP
            to_write += str(s_swap_info.used) + SEP
            to_write += str(s_swap_info.free) + SEP
            to_write += str(s_swap_info.percent) + SEP
            to_write += str(ps.cpu_percent()) + "\n"

            f.writelines(to_write)
            f.flush()

            time.sleep(interval)

            to_write = ""


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument(
        'pid', type=int, help='PID to monitor')
    parser.add_argument(
        'interval', type=int, help='Sample time to monitor in seconds.'
    )

    args = parser.parse_args()

    monitoring(args.pid, args.interval)
