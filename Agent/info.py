import psutil
from pyspectator.memory import VirtualMemory, NonvolatileMemory
from pyspectator.network import NetworkInterface

from pyspectator.processor import Cpu
import json


class Info() :
    sendInfo = {}


    def __init__(self):
        self.sendInfo = {}
        self.userInfo()
        self.connectionInfo()
        self.cpuInfo()
        self.ramInfo()
        self.debitInfo()
        self.diskInfo()
        #self.getInfo()

    def bytes2human(n):
        symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
        prefix = {}
        for i, s in enumerate(symbols):
            prefix[s] = 1 << (i + 1) * 10
        for s in reversed(symbols):
            if n >= prefix[s]:
                value = float(n) / prefix[s]
                return '%.1f%s' % (value, s)
        return "%sB" % n

    def cpuInfo(self):
        c = Cpu(monitoring_latency=1)
        print(c.count)
        print(c.load)
        print(c.load_stats)
        self.sendInfo['cpuNumber'] = psutil.cpu_count(logical=False)
        self.sendInfo['cpuFreqCurrent'] = psutil.cpu_freq().current
        self.sendInfo['cpuFreqMin'] = psutil.cpu_freq().min
        self.sendInfo['cpuFreqMax'] = psutil.cpu_freq().max

    def ramInfo(self):
        d = VirtualMemory(monitoring_latency=1)
        self.sendInfo['ramTotal'] = d.total  # psutil.virtual_memory().total
        self.sendInfo['ramAvailable'] = d.available  # psutil.virtual_memory().available
        self.sendInfo['ramPercent'] = d.used_percent  # psutil.virtual_memory().percent
        self.sendInfo['ramFree'] = d.total - d.used  # psutil.virtual_memory().free
        self.sendInfo['ramUsed'] = d.used  # psutil.virtual_memory().used

    def debitInfo(self):
        debit = NetworkInterface(monitoring_latency=1)
        self.sendInfo['byte_send'] = debit.bytes_sent
        self.sendInfo['byte_recv'] = debit.bytes_recv

    def userInfo(self):
        c = psutil.users().pop(0).name
        self.sendInfo['name'] = c

    def connectionInfo(self):
        liste = psutil.net_if_addrs()
        t = NetworkInterface(monitoring_latency=1)
        key = list(liste.keys())
        self.sendInfo['ip'] = t.ip_address  # liste.get(key.__getitem__(1))[0].address
        self.sendInfo['mac'] = liste.get(key.__getitem__(1))[2].address

    def diskInfo(self):
        disks = psutil.disk_partitions()
        dev = ""
        for disk in disks:
            path = disk.device

            if "sda" in path:
                dev = path
            break
        mem = NonvolatileMemory(monitoring_latency=1, device=dev)
        self.sendInfo['total_size'] = mem.total
        self.sendInfo['size_used'] = mem.used
        self.sendInfo['size_free'] = mem.total - mem.used


    def getInfo(self):
        top =self.sendInfo
        return top
