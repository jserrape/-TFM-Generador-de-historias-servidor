class Historia:

    def __init__(self, nombre_historia=None, latitud_historia=None, longitud_historia=None, zoom=None, descripcion_historia=None, dict=None):
        if dict is None:
            self.nombre_historia = nombre_historia
            self.latitud_historia  = float( latitud_historia )
            self.longitud_historia = float( longitud_historia )
            self.zoom = int( zoom )
            self.descripcion_historia = descripcion_historia
        else:
            self.nombre_historia = dict['nombre_historia']
            self.latitud_historia  = float( dict['latitud_historia'] )
            self.longitud_historia = float( dict['longitud_historia'] )
            self.zoom = int( dict['zoom'] )
            self.descripcion_historia = dict['descripcion_historia']

    def toJSON(self):
        return {'nombre_historia':self.nombre_historia,'latitud_historia':self.latitud_historia,'longitud_historia':self.longitud_historia,'zoom':self.zoom,'descripcion_historia':self.descripcion_historia}

    def toXML(self):
        xml_msg = '<historia>'
        xml_msg += '<nombre_historia>{}</nombre_historia>'.format( self.nombre_historia )
        xml_msg += '<latitud_historia>{}</latitud_historia>'.format( self.latitud_historia )
        xml_msg += '<longitud_historia>{}</longitud_historia>'.format( self.longitud_historia )
        xml_msg += '<zoom>{}</zoom>'.format( self.zoom )
        xml_msg += '<descripcion_historia>{}</descripcion_historia>'.format( self.descripcion_historia )
        xml_msg += '</historia>'

        return xml_msg