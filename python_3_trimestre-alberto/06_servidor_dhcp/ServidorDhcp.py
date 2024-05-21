from Equipo import Equipo
from ProtocoloIp import DireccionIp, DireccionMac


class ServidorDhcp(Equipo):
    
    def __init__(self, direccion_mac: DireccionMac, nombre: str) -> None:
        super().__init__(direccion_mac, nombre)
        self.direccion_ip_inicio: DireccionIp = None
        self.direccion_ip_fin: DireccionIp = None
        self.direcciones_asignadas: dict[DireccionMac, DireccionIp] = {}
        self.direcciones_reservadas: dict[DireccionMac,DireccionIp] = {}

    def establecer_parametros_dhcp(self, 
        direccion_ip_inicio: DireccionIp,
        direccion_ip_fin: DireccionIp,
    ):
        """
        La máscara de red será la que ya tiene establecida.
        La puerda de enlace será la que ya tiene establecida.
        El servidor DNS será el que ya tiene establecido.
        """
        self.direccion_ip_inicio = direccion_ip_inicio
        self.direccion_ip_fin = direccion_ip_fin

    def reservar_direccion_ip_a_equipo(self,direccion_mac: DireccionMac,direccion_ip: DireccionIp):
        
        if (direccion_ip not in self.direcciones_asignadas.values() and direccion_ip not in self.direcciones_reservadas.values()):
            self.direcciones_reservadas[direccion_mac] = direccion_ip
        else:
            print('Error, la dirección ip ya está asignada.')
            

    def asignar_direccion_ip_a_equipo(self, direccion_mac: DireccionMac) -> DireccionIp:
        numero_inicio = int(self.direccion_ip_inicio.split('.')[3])
        numero_fin = int(self.direccion_ip_fin.split('.')[3])
        prefijo =self.direccion_ip_inicio.split('.')[0]+self.direccion_ip_inicio.split('.')[1]+self.direccion_ip_inicio.split('.')[2]
        
        if (direccion_mac in self.direcciones_reservadas.keys()):
            self.direc
            for i in range (numero_inicio,numero_fin + 1 ):
                direccion_ip = f'{prefijo}.{i}'
                if (direccion_ip not in self.direcciones_asignadas.values() and direccion_ip not in self.direcciones_reservadas.values()):
                    self.direcciones_asignadas[direccion_mac] = direccion_ip
                    break
                else:
                    continue



if __name__ == '__main__':
    servidor = ServidorDhcp('AA:AA:AA:AA:AA:AA','servidor-dhcp-daw')
    servidor.establecer_parametros_red_estaticos('192.168.101','192.168.254','192.168.1.1','8.8.8.8')    
    servidor.establecer_parametros_dhcp('192.168.1.101','192.168.1.254')
    ip1 = servidor.asignar_direccion_ip_a_equipo('EE:EE:EE:EE:EE:01')
    ip2 = servidor.asignar_direccion_ip_a_equipo('EE:EE:EE:EE:EE:02')
    ip3 = servidor.asignar_direccion_ip_a_equipo('EE:EE:EE:EE:EE:03')
    ip4 = servidor.reservar_direccion_ip_a_equipo('EE:EE:EE:EE:EE:04','192.168.1.104')
    ip5 = servidor.reservar_direccion_ip_a_equipo('EE:EE:EE:EE:EE:05','192.168.1.101')
    ip6 = servidor.asignar_direccion_ip_a_equipo('EE:EE:EE:EE:EE:02')
    print('yes')
    
    