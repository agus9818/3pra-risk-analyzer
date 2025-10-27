# Simulación del invetario de activos con su Criticidad
CRITICIDAD_ACTIVOS = {
    'API_Pagos': 'Alta',  # Componente financiero crítico
    'Portal_Clientes': 'Media',  # Interfaz de usuario importante
    'Servicio_Logistica': 'Baja', # Servicio de apoyo
}

def obtener_criticidad_activo(activo_nombre: str) -> str:
    """Busca la criticidad predefinida de un activo, o devuelve 'Media' por defecto."""

    return CRITICIDAD_ACTIVOS.get(activo_nombre, 'Media')

def calcular_prioridad_ticket(severidad_scanner: str, activo_nombre: str) -> tuple[str, str]:
    """Aplica la lógia de negocio para calcular la Prioridad de Ticket (P0-P3).
       RETORNA: (prioridad_ticket, criticidad_activo)"""
       
    criticidad = obtener_criticidad_activo(activo_nombre)
    prioridad_ticket = "P3-Baja" # Prioridad base

    # Lógica de Priorización: Combinar Severidad (Escáner) y Criticidad
    if severidad_scanner == 'Crítico':
        prioridad = 'P0 - Bloqueador'
    elif severidad_scanner == 'Alto':
        if criticidad == 'Alto':
            prioridad = 'P1 - Urgente'
        else:
            prioridad = 'P2 - Importante'
    
    elif severidad_scanner == 'Medio':
        if criticidad == 'Alto':
            prioridad = 'P2 - Importante'
        else: 
            prioridad = 'P3 - Bajo'
    
    # Si la severidad es 'Bajo', la prioridad se mantiene en 'P3 - Bajo'

    return prioridad, criticidad